#!/usr/bin/env python3
"""Market scan: find Solana meme coins from many sources, pre-rank them for free, then spend Helius credits only on the
best candidates. Info/risk only, never a buy signal. A low risk score means fewer red flags found, not "safe".

  python3 fast_scan.py [--top 6] [--survivors 3] [--movers 6] [--score-movers 0] [--min-liq 50000] [--max-mcap 300e6]
                       [--workers 8] [--reuse-min 30] [--no-smart] [--out DIR] [--learn] [--json] [--no-log]
  python3 fast_scan.py --mints <MINT> [<MINT> ...]     # score given mints in parallel

Sources (deduped): DEX Screener boosts (top/latest), latest profiles, community takeovers; GeckoTerminal trending pools
(1h, 6h), new pools, top PumpSwap pools by 24h volume, top Solana pools by 24h tx count; the realtime daemon's recent
pump.fun graduations and rug/burst-wallet buys (recent_mints.json); mints recently bought by smart_money.json wallets
(~10 credits per wallet, cached 10 min; --no-smart to skip); past PASS/CAUTION coins from score_log (survivor re-checks).
Pre-rank (no Helius): real liquidity, liquidity/mcap, 24h volume/liquidity, age, buy/sell balance, spike-only price moves.
Lists:  "cleanest on real liquidity" = younger coins (< 3 days), scored, sorted by risk;
        "cleanest survivors" = >= 3 days old, >= $100k liquidity, steady volume, scored, must pass the survivor gates;
        "biggest movers (mostly traps)" = largest moves, shown with their pre-rank red flags (scored only with --score-movers).
Budget: Helius credits are spent only on --top + --survivors (+ --score-movers) coins; coins scored within --reuse-min
minutes with liquidity within 15% are reused (0 credits).
"""
import argparse, json, math, os, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault("SC_LEDGER_SRC", "fast_scan")
import scorecard, helius_checks as hc, netcache, ds

DS = "https://api.dexscreener.com"
GT = "https://api.geckoterminal.com/api/v2/networks/solana"
SKIP = {"So11111111111111111111111111111111111111112", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN",
        "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So", "J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn",
        "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs", "cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij",
        "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh", "27G8MtK7VtTcCHkpASjSDdkWWYfoqT6ggEuKidVJidD4"} | __import__("majors").all_mints()
SCORES = os.path.join(HERE, ".cache", "scores")
REUSE_LIQ_MOVE = float(os.environ.get("FS_REUSE_LIQ_MOVE", "0.15"))     # Actions: 0.30
SCORED_JSON = os.environ.get("FS_SCORED_JSON")                           # Actions: scored.json (mint -> last score ts, liq, holders)
FREE_ONLY = os.environ.get("FS_FREE_ONLY") == "1"                        # Actions free-only pass: no Helius, nothing scored
GT_DOWN = {"v": False}
_log_lock = threading.Lock()
T0 = time.time()
TIMING = {}


def f(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0


def usd(x): return scorecard.usd(x)


def link(m): return f"https://pump.fun/coin/{m}" if m.endswith("pump") else f"https://dexscreener.com/solana/{m}"


# ---------------------------------------------------------------- market context
def market_context():
    out = {}
    d, e = scorecard.http("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true", None, 2, 15, 120)
    if d: out["px"] = {k: (v.get("usd"), v.get("usd_24h_change")) for k, v in d.items()}
    else: out["px_err"] = e
    d, e = scorecard.http("https://api.alternative.me/fng/?limit=1", None, 2, 10, 600)
    try: out["fng"] = (int(d["data"][0]["value"]), d["data"][0]["value_classification"])
    except Exception: out["fng_err"] = e or "parse"
    d, e = scorecard.http("https://api.coingecko.com/api/v3/coins/categories", None, 2, 20, 600)
    try:
        c = {x["id"]: x for x in d}
        out["sectors"] = {k: (c[k].get("market_cap_change_24h"), c[k].get("volume_24h"), c[k].get("market_cap"))
                          for k in ("solana-meme-coins", "pump-fun") if k in c}
    except Exception:
        out["sectors_err"] = e or "parse"
    return out


def market_header(M):
    L = []
    if M.get("px"):
        L.append("Majors: " + ", ".join(f"{n} ${p:,.0f} ({c:+.1f}% 24h)" if p and p >= 100 else f"{n} ${p:,.2f} ({c:+.1f}% 24h)"
                                        for n, (p, c) in ((k.replace("bitcoin", "BTC").replace("ethereum", "ETH").replace("solana", "SOL"), v) for k, v in M["px"].items()) if p is not None and c is not None))
    else: L.append(f"Majors: unavailable ({M.get('px_err')})")
    L.append(f"Fear & Greed: {M['fng'][0]} ({M['fng'][1]})" if M.get("fng") else f"Fear & Greed: unavailable ({M.get('fng_err')})")
    if M.get("sectors"):
        L.append("Sector 24h (CoinGecko): " + ", ".join(f"{k} {c:+.1f}% (mcap {usd(mc)}, vol {usd(v)})" for k, (c, v, mc) in M["sectors"].items() if c is not None))
    else: L.append(f"Sector: unavailable ({M.get('sectors_err')})")
    return L


# ---------------------------------------------------------------- discovery
def smart_buys(max_wallets=8, max_age_h=12):
    """Mints bought by smart_money.json wallets in their last 50 txs (10 credits per wallet, cached 10 min)."""
    try: W = (json.load(open(os.path.join(HERE, "smart_money.json"))).get("wallets") or [])[:max_wallets]
    except Exception: return {}, 0
    H = hc.Helius(scorecard.http, cap=max_wallets + 2)
    out = {}
    def one(w):
        p = {"sortOrder": "desc", "limit": 50, "transactionDetails": "full", "encoding": "jsonParsed", "maxSupportedTransactionVersion": 1,
             "filters": {"status": "succeeded", "tokenAccounts": "balanceChanged"}}
        try: r, e = H.rpc("getTransactionsForAddress", [w["address"], p])
        except hc.Budget: return []
        got = []
        for tx in (r or {}).get("data") or []:
            if time.time() - (tx.get("blockTime") or 0) > max_age_h * 3600: continue
            m = tx.get("meta") or {}; ks = hc.keys_of(tx)
            if w["address"] not in ks: continue
            i = ks.index(w["address"])
            if m["postBalances"][i] >= m["preBalances"][i]: continue          # SOL went down = buy
            pre = {b["mint"]: int(b["uiTokenAmount"]["amount"]) for b in m.get("preTokenBalances") or [] if b.get("owner") == w["address"]}
            for b in m.get("postTokenBalances") or []:
                if b.get("owner") == w["address"] and b["mint"] not in SKIP and int(b["uiTokenAmount"]["amount"]) > pre.get(b["mint"], 0):
                    got.append(b["mint"])
        return got
    with ThreadPoolExecutor(4) as ex:
        for w, ms in zip(W, ex.map(one, W)):
            for m in ms: out.setdefault(m, set()).add("smart:" + w["address"][:6])
    return out, H.credits


def gt_pools(d):
    """GeckoTerminal pool list -> {mint: pool attrs} (base token only)."""
    out = {}
    for p in (d or {}).get("data") or []:
        bid = (((p.get("relationships") or {}).get("base_token") or {}).get("data") or {}).get("id", "")
        if bid.startswith("solana_"):
            out[bid[7:]] = p["attributes"]
    return out


def discover(smart=True):
    t = time.time()
    srcs = {"boost_top": DS + "/token-boosts/top/v1", "boost_latest": DS + "/token-boosts/latest/v1",
            "profiles": DS + "/token-profiles/latest/v1", "takeovers": DS + "/community-takeovers/latest/v1",
            "gt_trend_1h": GT + "/trending_pools?duration=1h", "gt_trend_6h": GT + "/trending_pools?duration=6h",
            "gt_new": GT + "/new_pools", "gt_pumpswap_vol": GT + "/dexes/pumpswap/pools?sort=h24_volume_usd_desc",
            "gt_top_tx": GT + "/pools?sort=h24_tx_count_desc"}
    found, gtattrs, errs = {}, {}, {}
    with ThreadPoolExecutor(10) as ex:
        futs = {k: ex.submit(scorecard.http, u, None, 3, 20, 120) for k, u in srcs.items()}
        f_mc = ex.submit(market_context)
        f_sm = ex.submit(smart_buys) if smart else None
        for k, fu in futs.items():
            d, e = fu.result()
            if e: errs[k] = e; continue
            if k.startswith("gt_"):
                for m, a in gt_pools(d).items():
                    found.setdefault(m, set()).add(k); gtattrs.setdefault(m, a)
            else:
                n0 = len(found)
                for x in d if isinstance(d, list) else []:
                    if x.get("chainId") == "solana" and x.get("tokenAddress"): found.setdefault(x["tokenAddress"], set()).add(k)
                if len(found) == n0 and not d: errs[k] = "empty"
        M = f_mc.result()
        sm_credits = 0
        if f_sm:
            sm, sm_credits = f_sm.result()
            for m, s in sm.items(): found.setdefault(m, set()).update(s)
    # daemon feed (graduations, rug/burst-wallet buys) - free
    try:
        R = json.load(open(os.path.join(HERE, "recent_mints.json")))
        for r in R.get("mints") or []:
            if time.time() - r["t"] < 6 * 3600: found.setdefault(r["mint"], set()).add("daemon:" + r["why"].split()[0])
    except Exception:
        errs["daemon_feed"] = "recent_mints.json missing (daemon not updated yet?)"
    # survivors re-check: PASS/CAUTION coins logged >= 3 days ago
    try:
        import datetime
        for l in open(os.path.join(HERE, "score_log.jsonl")):
            try: e = json.loads(l)
            except ValueError: continue
            if e.get("verdict") in ("PASSES-BASIC-CHECKS", "CAUTION") and e.get("mint"):
                try:
                    if time.time() - datetime.datetime.fromisoformat(e["time"]).timestamp() > 14 * 86400: continue
                except Exception:
                    continue
                found.setdefault(e["mint"], set()).add("score_log")
    except OSError:
        pass
    for m in list(found):
        if m in SKIP: found.pop(m)
    TIMING["discovery_s"] = round(time.time() - t, 1)
    return found, gtattrs, M, errs, sm_credits


# ---------------------------------------------------------------- free pre-rank
def metrics(ps):
    ps = [p for p in ps if p.get("chainId") == "solana"]
    if not ps: return None
    top = max(ps, key=lambda p: f((p.get("liquidity") or {}).get("usd")))
    liq = sum(f((p.get("liquidity") or {}).get("usd")) for p in ps)
    v = lambda k: sum(f((p.get("volume") or {}).get(k)) for p in ps)
    tx = top.get("txns") or {}
    pc = top.get("priceChange") or {}
    created = min([p.get("pairCreatedAt") for p in ps if p.get("pairCreatedAt")] or [None]) if any(p.get("pairCreatedAt") for p in ps) else None
    return {"ticker": (top.get("baseToken") or {}).get("symbol"), "liq": liq, "mcap": f(top.get("marketCap") or top.get("fdv")),
            "vol24": v("h24"), "vol1": v("h1"), "vol6": v("h6"), "h1": f(pc.get("h1")), "h6": f(pc.get("h6")), "h24": f(pc.get("h24")), "m5": f(pc.get("m5")),
            "b24": f((tx.get("h24") or {}).get("buys")), "s24": f((tx.get("h24") or {}).get("sells")),
            "b1": f((tx.get("h1") or {}).get("buys")), "s1": f((tx.get("h1") or {}).get("sells")),
            "age_h": (time.time() - created / 1000) / 3600 if created else None, "src": top.get("_src") or "dexscreener",
            "price": f(top.get("priceUsd")) or None}


def prerank(m, x, sources, min_liq):
    flags = []
    liq, mc = x["liq"], x["mcap"]
    if liq < min_liq: flags.append(f"thin liq {usd(liq)}")
    lm = liq / mc * 100 if mc else 0
    if mc and lm < 5: flags.append(f"liq/mcap {lm:.1f}%")
    vl = x["vol24"] / max(liq, 1)
    if vl > 25: flags.append(f"churn {vl:.0f}x vol/liq")
    if x["h1"] > 100 or x["h6"] > 300 or x["m5"] > 30: flags.append(f"spike ({x['h1']:+.0f}% 1h, {x['h6']:+.0f}% 6h)")
    if x["h24"] < -50: flags.append(f"dumping {x['h24']:+.0f}% 24h")
    bs = x["b24"] / max(x["s24"], 1)
    if x["b24"] + x["s24"] > 50 and (bs > 3 or bs < 0.33): flags.append(f"lopsided buys/sells {bs:.2f}")
    if x["age_h"] is not None and x["age_h"] < 1: flags.append("< 1h old")
    # cleanliness: deeper liquidity, sane turnover, balanced flow, age, no spike
    clean = 50 + 8 * math.log10(max(liq, 1) / 50000 + 1e-9) * 2
    clean -= 15 * len(flags)
    if 0.3 <= vl <= 8: clean += 8
    if 0.7 <= bs <= 1.6: clean += 6
    if x["age_h"]: clean += min(10, x["age_h"] / 24 * 2)
    if mc and lm >= 10: clean += 5
    mover = abs(x["h1"]) + abs(x["h6"]) / 2 + abs(x["h24"]) / 4 + min(vl, 50)
    return {"mint": m, **x, "liq_mcap_pct": lm, "vol_liq": vl, "bs24": bs, "flags": flags, "clean_pre": round(clean, 1),
            "mover": round(mover, 1), "sources": sorted(sources)}


def survivor_gate_pre(r):
    """Free gates for the survivors path (before scoring)."""
    return (r["age_h"] or 0) >= 72 and r["liq"] >= 100000 and r["vol24"] >= 50000 and r["h24"] > -40 \
        and not any(fl.startswith(("spike", "churn", "lopsided", "liq/mcap", "dumping")) for fl in r["flags"])


def screen(found, gtattrs, min_liq, max_mcap):
    t = time.time()
    mints = list(found)
    pairs = {}
    degraded = ds.degraded()
    if degraded:     # DexS outage: GeckoTerminal pool attributes we already have from discovery are enough to pre-rank
        for m in mints:
            if m not in gtattrs: continue
            a = dict(gtattrs[m]); a["_base"] = m
            pp = ds.gt_to_pairs(m, {"token": {}, "pools": [a]})
            if pp: pairs[m] = pp
    rest = [m for m in mints if m not in pairs]
    pairs.update(ds.batch(rest, max_fallback=0, gt_fallback=True))
    for m in mints:  # coins only GeckoTerminal knows (or DexS dropped)
        if m in pairs or m not in gtattrs: continue
        a = dict(gtattrs[m]); a["_base"] = m
        pp = ds.gt_to_pairs(m, {"token": {}, "pools": [a]})
        if pp: pairs[m] = pp
    rows = []
    for m, ps in pairs.items():
        x = metrics(ps)
        if not x: continue
        if max_mcap and x["mcap"] > max_mcap: continue
        rows.append(prerank(m, x, found.get(m, set()), min_liq))
    TIMING["screen_s"] = round(time.time() - t, 1)
    return rows


def prime_gt(mints):
    """One GeckoTerminal /tokens/multi call per 30 coins, stored under each coin's per-token URL so every scorecard's
    GeckoTerminal fetch is a cache hit (GT allows ~30 calls/min per IP; this was the scan's main bottleneck)."""
    g = {}
    for i in range(0, len(mints), 30):
        ch = mints[i:i + 30]
        url = f"{GT}/tokens/multi/{','.join(ch)}?include=top_pools"
        d, e = scorecard.http(url, None, 3, 20, 120)
        if not d: continue
        inc = {x["id"]: x for x in d.get("included") or []}
        for t in d.get("data") or []:
            m = t["attributes"].get("address")
            ids = [p["id"] for p in ((t.get("relationships") or {}).get("top_pools") or {}).get("data") or []]
            netcache.put(scorecard.GT_TOKEN.format(m=m) + "?include=top_pools", None, {"data": t, "included": [inc[i_] for i_ in ids if i_ in inc]})
            g[m] = True
    return g


# ---------------------------------------------------------------- scoring
def log_score(R, src):
    m = R.get("market") or {}
    with _log_lock, open(os.path.join(HERE, "score_log.jsonl"), "a") as fh:
        fh.write(json.dumps({"mint": R["mint"], "ticker": R["ticker"], "time": R["generated_at"], "verdict": R["verdict"],
                             "price": m.get("price_usd"), "mcap": m.get("mcap_usd"), "liq": m.get("liq_usd"),
                             "risk": (R.get("risk") or {}).get("score"), "src": src,
                             "wv": (R.get("risk") or {}).get("weights_version")}) + "\n")
    try: scorecard.write_check_log(R, src)          # per-check results (check_log.jsonl)
    except Exception: pass


def reusable(m, liq_now, reuse_min):
    p = os.path.join(SCORES, m + ".json")
    try:
        if time.time() - os.path.getmtime(p) > reuse_min * 60: return None
        R = json.load(open(p))
        L = (R.get("market") or {}).get("liq_usd") or 0
        if liq_now and L and abs(L / liq_now - 1) > REUSE_LIQ_MOVE: return None
        if (R.get("risk") or {}).get("incomplete"): return None
        R["_reused"] = time.strftime("%H:%M", time.localtime(os.path.getmtime(p)))
        return R
    except (OSError, ValueError):
        return None


def score_many(mints, workers=8, out=None, log=True, learn=False, liq_now=None, reuse_min=30, src="fast_scan"):
    res, t0 = {}, time.time()
    liq_now = liq_now or {}
    def one(m):
        t = time.time()
        R = reusable(m, liq_now.get(m), reuse_min) if reuse_min else None
        if R: return m, R, None, 0.0
        try:
            R = scorecard.run(m)
        except Exception as e:
            return m, None, f"{type(e).__name__}: {hc.scrub(e)}", time.time() - t
        try:
            os.makedirs(SCORES, exist_ok=True); json.dump(R, open(os.path.join(SCORES, m + ".json"), "w"), default=str)
        except OSError:
            pass
        return m, R, None, time.time() - t
    with ThreadPoolExecutor(max(1, min(workers, len(mints) or 1))) as ex:
        for fu in as_completed([ex.submit(one, m) for m in mints]):
            m, R, err, dt = fu.result()
            res[m] = (R, err, dt)
            if R and log and not R.get("_reused"):
                try: log_score(R, src)
                except Exception as e: print(f"[fast_scan] log failed: {type(e).__name__}", file=sys.stderr)
            if R and out:
                os.makedirs(out, exist_ok=True)
                open(os.path.join(out, m + ".md"), "w").write(scorecard.render(R))
                json.dump(R, open(os.path.join(out, m + ".json"), "w"), indent=1, default=str)
            print(f"[fast_scan] {'reused' if R and R.get('_reused') else 'scored'} {(R or {}).get('ticker') or m[:6]} in {dt:.0f}s" + (f" ERROR {err}" if err else ""), file=sys.stderr)
    learned = []
    if learn:
        import learn_rugs
        for m, (R, err, _) in res.items():
            if not R or R.get("_reused"): continue
            try:
                reason = learn_rugs.is_rug(R)
                if reason:
                    got, n = learn_rugs.locked_learn(R, reason)
                    learned += [(R.get("ticker"), m, k, a, lab) for k, a, lab in got]
            except Exception as e:
                print(f"[fast_scan] learn {m[:6]}: {type(e).__name__}", file=sys.stderr)
    return res, time.time() - t0, learned


def survivor_gates(R):
    """Post-score gates: no rug-funder/operator link, no coordinated launch, exit test passes, creator small or sold out,
    no wash FAIL, authorities clean. Returns list of failed gates."""
    st = {c["n"]: c for c in R.get("checks") or []}
    s = lambda n: (st.get(n) or {}).get("status")
    bad = []
    if s(2) != "PASS": bad.append("authorities")
    if s(15) in ("FAIL", "WARN"): bad.append("rug-funder link")
    if s(19) == "FAIL": bad.append("same operator as a rug")
    if s(14) == "FAIL": bad.append("coordinated launch/cluster")
    if s(16) != "PASS": bad.append("exit test")
    if s(18) == "FAIL": bad.append("wash trading")
    H = R.get("helius") or {}
    ch = H.get("creator_hold_pct")
    if ch is not None and ch > 5: bad.append(f"creator holds {ch:.1f}%")
    if s(13) == "FAIL": bad.append("creator check FAIL")
    if s(11) == "FAIL": bad.append("top holders concentrated")
    return bad


def holder_growth(R):
    """Holder count now vs the last time we saw this coin (RugCheck totalHolders, stored in the kv store)."""
    try:
        import kv
        rc = next((c for c in R["checks"] if c["n"] == 6), {})
        n = int(rc.get("detail", "").split("; ")[-1].split(" holders total")[0])
    except Exception:
        return None
    k = "holders:" + R["mint"]; prev = kv.get(k)
    kv.put(k, {"n": n, "t": time.time()})
    if prev and prev.get("n") and time.time() - prev["t"] > 1800:
        return (n / prev["n"] - 1) * 100, (time.time() - prev["t"]) / 3600, n
    return None if not n else (None, None, n)


def row(R, extra=""):
    rk = R.get("risk") or {}; mk = R.get("market") or {}; m = R["mint"]
    h24 = next((c["value"].split(",")[0] for c in R["checks"] if c["n"] == 9), "")
    age = next((c["value"] for c in R["checks"] if c["n"] == 5), "")
    reuse = f" (reused {R['_reused']})" if R.get("_reused") else ""
    return (f"| {rk.get('score')}{'*' if rk.get('incomplete') else ''} | {R['verdict']} | [{R.get('ticker') or '?'}]({link(m)}) | `{m}` | {usd(mk.get('liq_usd'))} | "
            f"{usd(mk.get('mcap_usd'))} | {age} | {h24} | {'; '.join((rk.get('drivers') or [])[:3])}{extra}{reuse} |")


HDR = ["| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |", "|---|---|---|---|---|---|---|---|---|"]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--mints", nargs="+"); ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--survivors", type=int, default=3); ap.add_argument("--movers", type=int, default=6)
    ap.add_argument("--score-movers", type=int, default=0)
    ap.add_argument("--min-liq", type=float, default=50000); ap.add_argument("--max-mcap", type=float, default=300e6)
    ap.add_argument("--workers", type=int, default=8); ap.add_argument("--out"); ap.add_argument("--reuse-min", type=int, default=30)
    ap.add_argument("--no-smart", action="store_true")
    ap.add_argument("--learn", action="store_true"); ap.add_argument("--json", action="store_true"); ap.add_argument("--no-log", action="store_true")
    a = ap.parse_args()
    import joblock; joblock.guard("fast_scan")          # one scan at a time, nice/ionice, 20-min hard timeout
    if joblock.load_ratio() > 1.0 and a.workers > 3:
        print(f"[fast_scan] box load {os.getloadavg()[0]:.1f} on {os.cpu_count()} cores - scoring with 3 workers instead of {a.workers}", file=sys.stderr)
        a.workers = 3
    rows, M, errs, sm_cr = [], {}, {}, 0
    if a.mints:
        mints = [m for m in a.mints if scorecard.B58.match(m)]; fresh, surv, movers = mints, [], []
    else:
        found, gtattrs, M, errs, sm_cr = discover(not a.no_smart)
        rows = screen(found, gtattrs, a.min_liq, a.max_mcap)
        ok = [r for r in rows if r["liq"] >= a.min_liq]
        survivors_c = sorted([r for r in ok if survivor_gate_pre(r)], key=lambda r: -r["clean_pre"])
        young = sorted([r for r in ok if (r["age_h"] or 0) < 72 and not any(fl.startswith(("spike", "dumping", "< 1h")) for fl in r["flags"])],
                       key=lambda r: -r["clean_pre"])
        movers = sorted([r for r in rows if r["liq"] >= 10000], key=lambda r: -r["mover"])[:a.movers]
        fresh = [r["mint"] for r in young[:a.top]]
        surv = [r["mint"] for r in survivors_c[:a.survivors] if r["mint"] not in fresh]
        mv = [r["mint"] for r in movers[:a.score_movers] if r["mint"] not in fresh + surv]
        mints = fresh + surv + mv
        print(f"[fast_scan] {len(found)} candidate mints from {len(set(s for v in found.values() for s in v))} source tags; {len(rows)} with pair data; "
              f"{len(ok)} >= ${a.min_liq:,.0f} liq; {len(survivors_c)} pass survivor pre-gates ({time.time()-T0:.0f}s)", file=sys.stderr)
    GT_DOWN["v"] = bool(errs) and all(k in errs for k in ("gt_trend_1h", "gt_trend_6h", "gt_new", "gt_pumpswap_vol", "gt_top_tx"))
    if GT_DOWN["v"]: print("[fast_scan] GeckoTerminal DOWN - degraded mode: DEX Screener fields only, unique-buyer counts unavailable", file=sys.stderr)
    t = time.time()
    if not GT_DOWN["v"]: prime_gt(mints)
    TIMING["gt_prime_s"] = round(time.time() - t, 1)
    if FREE_ONLY:
        print(f"[fast_scan] FREE-ONLY pass: {len(mints)} candidate(s) NOT scored (no Helius) - results UNVERIFIED", file=sys.stderr)
        mints = []
    liq_now = {r["mint"]: r["liq"] for r in rows}
    res, dt, learned = score_many(mints, a.workers, a.out, not a.no_log, a.learn, liq_now, a.reuse_min)
    TIMING["scoring_s"] = round(dt, 1)
    if SCORED_JSON:
        try: SJ = json.load(open(SCORED_JSON))
        except Exception: SJ = {}
        for m, (R, e, _) in res.items():
            if not R or R.get("_reused"): continue
            H_ = R.get("helius") or {}
            SJ[m] = {"ts": time.time(), "liq": (R.get("market") or {}).get("liq_usd"), "holders": len(H_.get("holders") or []) or None,
                     "risk": (R.get("risk") or {}).get("score"), "verdict": R.get("verdict")}
        SJ = {k: v for k, v in SJ.items() if time.time() - v.get("ts", 0) < 2 * 86400}
        json.dump(SJ, open(SCORED_JSON, "w"), indent=0)
    total = time.time() - T0
    cs = netcache.stats()
    credits = sum(((R or {}).get("helius_credits_est") or 0) for R, _, _ in res.values() if R and not R.get("_reused")) + sm_cr
    n_new = sum(1 for R, _, _ in res.values() if R and not R.get("_reused"))
    # survivors file for the daemon's clean-mover detector
    sv_out = []
    for m in surv + fresh:
        R = (res.get(m) or (None,))[0]
        if not R: continue
        gates = survivor_gates(R)
        sv_out.append({"mint": m, "ticker": R.get("ticker"), "risk": (R.get("risk") or {}).get("score"), "verdict": R["verdict"],
                       "structural_ok": not gates and ((R.get("risk") or {}).get("score") or 100) <= 55 and ((R.get("market") or {}).get("liq_usd") or 0) >= 50000,
                       "gates_failed": gates, "scored_at": R.get("generated_at"), "path": "survivor" if m in surv else "young"})
    try:
        prev = json.load(open(os.path.join(HERE, "survivors.json"))).get("coins") or []
    except Exception:
        prev = []
    keep = {c["mint"]: c for c in prev if c.get("scored_at") and time.time() - __import__("datetime").datetime.fromisoformat(c["scored_at"]).timestamp() < 36 * 3600}
    keep.update({c["mint"]: c for c in sv_out})
    json.dump({"updated": time.strftime("%Y-%m-%dT%H:%M:%S"), "coins": list(keep.values())}, open(os.path.join(HERE, "survivors.json"), "w"), indent=1)
    netcache.ledger("fast_scan-discovery", sm_cr) if sm_cr else None
    if a.json:
        print(json.dumps({"elapsed_s": round(total, 1), "timing": TIMING, "market": M, "screened": rows[:60],
                          "results": {m: R for m, (R, e, _) in res.items()}, "errors": {m: e for m, (R, e, _) in res.items() if e},
                          "learned": learned, "credits_est": credits, "source_errors": errs}, default=str)); return
    now = time.strftime("%Y-%m-%d %H:%M %Z")
    P = [f"# Market scan {now}", "", "Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.", ""]
    if M: P += ["## Market context"] + [f"- {x}" for x in market_header(M)] + [""]
    def section(title, ms, note, extra_fn=None):
        items = [(res[m][0], m) for m in ms if m in res and res[m][0]]
        items.sort(key=lambda x: ((x[0].get("risk") or {}).get("score") or 999))
        out = [f"## {title}", note, ""] + HDR
        for R, m in items: out.append(row(R, extra_fn(R) if extra_fn else ""))
        if not items: out.append("| - | - | none this run | - | - | - | - | - | - |")
        return out + [""]
    P += section("Cleanest on real liquidity (younger than 3 days)", fresh,
                 f"Top {len(fresh)} by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.")
    def sv_extra(R):
        g = survivor_gates(R); hg = holder_growth(R)
        s = "" if not g else f"; GATES FAILED: {', '.join(g)}"
        if hg and hg[0] is not None: s += f"; holders {hg[0]:+.1f}% in {hg[1]:.0f}h (now {hg[2]:,})"
        elif hg: s += f"; holders {hg[2]:,} (growth n/a: first sighting)"
        return s
    P += section("Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)", surv,
                 "Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. "
                 "Coins that failed a gate are still listed with the gate named.", sv_extra)
    if FREE_ONLY and rows:
        P += ["## Candidates (UNVERIFIED, not scored)", "", "| Ticker | Mint (full CA) | Liq | Mcap | 1h | 24h | Red flags |", "|---|---|---|---|---|---|---|"]
        for r in sorted([r for r in rows if r["liq"] >= a.min_liq], key=lambda r: -r["clean_pre"])[:a.top + a.survivors]:
            P.append(f"| [{r['ticker'] or '?'}]({link(r['mint'])}) | `{r['mint']}` | {usd(r['liq'])} | {usd(r['mcap'])} | {r['h1']:+.0f}% | {r['h24']:+.0f}% | {'; '.join(r['flags']) or 'none flagged (UNVERIFIED)'} |")
        P.append("")
    P += ["## Biggest movers (mostly traps)", "Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.", "",
          "| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in movers:
        R = (res.get(r["mint"]) or (None,))[0]
        P.append(f"| [{r['ticker'] or '?'}]({link(r['mint'])}) | `{r['mint']}` | {usd(r['liq'])} | {usd(r['mcap'])} | {r['h1']:+.0f}% | {r['h6']:+.0f}% | {r['h24']:+.0f}% | "
                 f"{r['vol_liq']:.1f}x | {'; '.join(r['flags']) or 'none flagged (still high risk)'} | {(R.get('risk') or {}).get('score') if R else 'not scored'} |")
    P.append("")
    errs_s = [f"- `{m}`: {e}" for m, (R, e, _) in res.items() if e]
    if errs_s: P += ["Scoring errors:"] + errs_s + [""]
    if learned: P += ["Rug list changes:"] + [f"- {k} {a_} ({lab}) from {t_} `{m}`" for t_, m, k, a_, lab in learned] + [""]
    P += [f"_Timing: total {total:.0f}s (discovery {TIMING.get('discovery_s')}s, screen {TIMING.get('screen_s')}s, GT prime {TIMING.get('gt_prime_s')}s, "
          f"scoring {TIMING.get('scoring_s')}s for {len(mints)} coins, {n_new} newly scored). ~{credits:.0f} Helius credits (smart-money discovery {sm_cr}). "
          f"HTTP cache hits {cs['hit']}/{cs['hit'] + cs['miss']}; Helius 429s {cs.get('h429', 0)}; DEX Screener {'DEGRADED - GeckoTerminal fallback used' if ds.degraded() else 'ok'}._"]
    if FREE_ONLY: P.insert(2, "**UNVERIFIED: free-API-only pass (no Helius scoring this run). Rows below are pre-rank red flags from DEX Screener/GeckoTerminal/pump.fun only.**\n")
    if GT_DOWN["v"]: P.append("_DEGRADED: GeckoTerminal down - DEX Screener fields used; unique-buyer/holder-growth data unavailable._")
    if errs: P.append("_Source gaps: " + "; ".join(f"{k}: {v}" for k, v in errs.items()) + "_")
    if a.out: P.append(f"\n_Full reports: {a.out}/<mint>.md (+ .json)_")
    print("\n".join(P))
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump({"credits_est": round(credits), "free_only": FREE_ONLY, "gt_down": GT_DOWN["v"], "scored": n_new, "reused": len(res) - n_new},
                  open(os.path.join(a.out, "run_stats.json"), "w"))
        open(os.path.join(a.out, "SUMMARY.md"), "w").write("\n".join(P) + "\n")


if __name__ == "__main__":
    main()
