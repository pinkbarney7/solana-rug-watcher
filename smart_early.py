#!/usr/bin/env python3
"""Early-survivor smart-wallet list. Info only. Info only - a lead, NOT a buy signal.

  python3 smart_early.py build [--max-calls N]   # rebuild smart_early.json (each routine run; default cap 25 Helius calls
                                                 # = <= 250 credits; most runs ~0 because each coin is fetched once ever)
  python3 smart_early.py list         # print the list
  python3 smart_early.py confluence   # print coins bought by 2+ smart wallets in the last 6 h (from wallet_events.jsonl)

How it works
 1. Coins: every scorecard result JSON in /workspace/scan-*/ and /workspace/scan/ that has Helius launch data
    plus each coin's earliest mint txs (getTransactionsForAddress asc; page 1 is usually already in .cache = free; coins that
    survived get up to 5 pages = the first ~500 txs; others 1 page). Buyers are stored once in smart_early_buyers.json.
 2. Early buy = token balance up at slot offset 4+ and blockTime <= creation + 30 min (slots 0-3 = bundles/snipers).
    Excluded: slots 0-3 (bundles/snipers), the creator, any wallet signed by someone else (bundled), any wallet in a
    common-funder cluster of the coin (helius.clusters, incl. the creator's) or the operator trace group, rug_funders.json.
 3. Outcome now (DEX Screener, batch endpoint): WIN = coin >= 24 h old, liquidity >= $20k and >= 40% of liquidity at scan
    time, market cap >= $100k (far above where a ~30-min buyer entered) and >= 50% of the scan-time cap.
    LOSS = >= 24 h old and liquidity < $5k / no pair / liquidity down >= 80% / market cap < $30k. Else pending.
 4. Excluded: 3+ wallets entering the same 2+ winning coins in the same minute (coordinated group); WIN also needs
    liquidity >= 2% of market cap (fake-cap copycats). Coins created > 60 days ago are skipped. Tier "smart" = >= 2 WINs, wins >= losses, not sniper-like (every entry < 30 s). Tier "candidate" = 1 WIN and 0 losses (shown, not used for confluence).
Caveats: our scan history is small and biased toward coins we chose to scan; holders are not checked for selling; one
person can run many wallets. Past entries say nothing about the next trade.
"""
import glob, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "smart_early.json")
EVENTS = os.path.join(HERE, "wallet_events.jsonl")
RUG = os.path.join(HERE, "rug_funders.json")
SLOT_S = 0.4
BUYERS = os.path.join(HERE, "smart_early_buyers.json")
EARLY_S = 1800
MAX_AGE_D = 60


def fetch_buyers(R, order, max_calls):
    """mint -> {"done": bool, "pages": n, "buyers": {wallet: [slot_offset, t, signer]}} (persisted; resumed across runs)."""
    import helius_checks as hc, scorecard, netcache
    try: B = json.load(open(BUYERS))
    except Exception: B = {}
    H = hc.Helius(scorecard.http, cap=max_calls)
    try:
        for m, want_pages in order:
            b = B.setdefault(m, {"done": False, "pages": 0, "buyers": {}, "tok": None})
            if b["done"] or b["pages"] >= want_pages: continue
            ct = R[m]["helius"]["creation_time"]; s0 = R[m]["helius"].get("creation_slot")
            while b["pages"] < want_pages and not b["done"]:
                d, tok = H.txs_asc(m, 100, b.get("tok"))
                b["pages"] += 1; b["tok"] = tok
                for tx in d:
                    if s0 is None: s0 = tx["slot"]
                    if (tx.get("blockTime") or 0) > ct + EARLY_S: b["done"] = True; break
                    if (tx.get("meta") or {}).get("err"): continue
                    signer = hc.keys_of(tx)[0]
                    for o, dv in hc.mint_deltas(tx, m)[0].items():
                        if dv > 0 and o not in b["buyers"]: b["buyers"][o] = [tx["slot"] - s0, tx.get("blockTime"), signer]
                if not d or not tok: b["done"] = True
    except (hc.Budget, RuntimeError) as e:
        print(f"[smart_early] Helius stop: {hc.scrub(e)}")
    finally:
        tmp = BUYERS + ".tmp"; json.dump(B, open(tmp, "w")); os.replace(tmp, BUYERS)
        if H.credits: netcache.ledger("smart_early", H.credits, H.calls)
        print(f"[smart_early] Helius: {H.calls} calls (~{H.credits} credits), {H.cached} cache hits")
    return B


def load():
    try: return json.load(open(OUT))
    except Exception: return None


def scan_results():
    by = {}
    for f in glob.glob("/workspace/scan-*/*.json") + glob.glob("/workspace/scan/*.json"):
        try: R = json.load(open(f))
        except Exception: continue
        if not isinstance(R, dict) or not R.get("mint"): continue
        H = R.get("helius") or {}
        if not H.get("early") or not H.get("creation_time"): continue
        prev = by.get(R["mint"])
        if not prev or str(R.get("generated_at")) < str(prev.get("generated_at")): by[R["mint"]] = R   # keep the earliest scan
    return by


def hc_on_curve(w):
    import helius_checks as hc
    try: return hc.on_curve(w)
    except Exception: return True


def outcomes(mints):
    import ds
    P = ds.batch(mints, max_fallback=0, gt_fallback=True)
    out = {}
    for m in mints:
        ps = P.get(m) or []
        if not ps: out[m] = None; continue
        ps.sort(key=lambda p: -float((p.get("liquidity") or {}).get("usd") or 0)); t = ps[0]
        out[m] = {"liq": sum(float((p.get("liquidity") or {}).get("usd") or 0) for p in ps), "mcap": t.get("marketCap") or t.get("fdv"),
                  "sym": t["baseToken"].get("symbol")}
    return out


def build(max_calls=25):
    rug = set()
    try: rug = {w["address"] for w in json.load(open(RUG))["wallets"]}
    except Exception: pass
    R = scan_results(); now = time.time()
    O = outcomes(list(R))
    coins, W = {}, {}
    for m, r in R.items():
        H = r["helius"]; mk = r.get("market") or {}
        ct = H["creation_time"]; age_h = (now - ct) / 3600
        o = O.get(m); liq0 = mk.get("liq_usd") or 0; mc0 = mk.get("mcap_usd") or 0
        if age_h > MAX_AGE_D * 24: continue          # early buyers of old coins (e.g. 2024 launches) say little about now
        if age_h < 24: res = "pending"
        elif o is None or o["liq"] < 5000 or (liq0 and o["liq"] < 0.2 * liq0) or (o["mcap"] or 0) < 30000: res = "loss"
        elif o["liq"] >= 20000 and o["liq"] >= 0.4 * liq0 and (o["mcap"] or 0) >= 100000 and (o["mcap"] or 0) >= 0.5 * mc0 \
                and o["liq"] >= 0.02 * (o["mcap"] or 0): res = "win"      # liq < 2% of cap = fake-cap copycat pattern
        else: res = "pending"
        excl = {H.get("creator")} | rug
        for cl in H.get("clusters") or []: excl |= set(cl.get("wallets") or [])
        tr = H.get("trace") or {}
        excl |= set((tr.get("operator_group") or {}).get("early_wallets") or [])
        coins[m] = {"ticker": r.get("ticker"), "result": res, "age_h": round(age_h, 1), "liq_scan": liq0, "mcap_scan": mc0,
                    "liq_now": o and round(o["liq"]), "mcap_now": o and o["mcap"], "risk_at_scan": (r.get("risk") or {}).get("score")}
        excl |= {e["wallet"] for e in H["early"] if (e.get("slot_offset") or 0) <= 3}     # slot 0-3 launch buyers
        coins[m]["_excl"] = excl
    order = sorted(((m, 5 if c["result"] == "win" else 1) for m, c in coins.items() if c["result"] != "pending" or c["age_h"] < 24),
                   key=lambda x: -x[1])
    B = fetch_buyers(R, order, max_calls)
    seen_n = {}
    for m in coins:
        for w in (B.get(m) or {}).get("buyers", {}): seen_n[w] = seen_n.get(w, 0) + 1
    for m, c in coins.items():
        excl = c.pop("_excl"); res = c["result"]; ct = R[m]["helius"]["creation_time"]
        bb = (B.get(m) or {}).get("buyers") or {}
        c["early_buyers_known"] = len(bb); c["buyer_pages"] = (B.get(m) or {}).get("pages", 0)
        for w, (so, t, signer) in bb.items():
            if so <= 3 or w in excl or signer != w or not hc_on_curve(w): continue
            if t and t > ct + EARLY_S: continue
            W.setdefault(w, []).append({"mint": m, "ticker": c["ticker"], "entry_et": time.strftime("%Y-%m-%d %H:%M %Z", time.localtime(t or ct)),
                                        "min_after_launch": round(((t or ct) - ct) / 60, 1), "result": res})
    # coordinated groups: 3+ wallets that entered the same 2+ coins within the same minute = one operator, not "smart"
    sig = {}
    for w, ev in W.items():
        key = tuple(sorted((x["mint"], int(x["min_after_launch"])) for x in ev if x["result"] == "win"))
        if len(key) >= 2: sig.setdefault(key, []).append(w)
    coordinated = {w for ws in sig.values() if len(ws) >= 3 for w in ws}
    wallets = []
    for w, ev in W.items():
        if w in coordinated: continue
        if seen_n.get(w, 0) >= 25 and sum(x["result"] == "loss" for x in ev) > len(ev) / 2: continue   # sniper bot buying everything
        wins = sum(x["result"] == "win" for x in ev); losses = sum(x["result"] == "loss" for x in ev)
        sniper_like = sum(x["min_after_launch"] < 0.5 for x in ev) * 2 >= len(ev)   # half+ entries inside ~30 s: bot/sniper-like
        tier = "smart" if wins >= 2 and wins >= losses and not sniper_like else ("candidate" if wins >= 1 and losses == 0 else None)
        if tier: wallets.append({"address": w, "tier": tier, "wins": wins, "losses": losses, "coins": ev, "sniper_like": sniper_like, "label": f"early-survivor wallet ({wins} wins/{losses} losses)"})
    wallets.sort(key=lambda x: (x["tier"] != "smart", -x["wins"], x["losses"]))
    J = {"built_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "coins_examined": len(R), "coin_results": {k: sum(c["result"] == k for c in coins.values()) for k in ("win", "loss", "pending")},
         "excluded_coordinated": len(coordinated), "n_smart": sum(w["tier"] == "smart" for w in wallets), "n_candidate": sum(w["tier"] == "candidate" for w in wallets),
         "criteria": __doc__.split("How it works")[1].split("Caveats")[0].strip(), "wallets": wallets, "coins": coins}
    tmp = OUT + ".tmp"; json.dump(J, open(tmp, "w"), indent=1); os.replace(tmp, OUT)
    print(f"[smart_early] {len(R)} coins ({J['coin_results']}); {J['n_smart']} smart, {J['n_candidate']} candidate wallets")
    return J


def confluence(hours=6, min_wallets=2):
    J = load() or {}; S = {w["address"]: w for w in J.get("wallets", []) if w["tier"] == "smart"}
    try:
        import json as _j; S2 = {w["address"] for w in _j.load(open(os.path.join(HERE, "smart_money.json"))).get("wallets", [])}
    except Exception: S2 = set()
    cut = time.time() - hours * 3600; hits = {}
    try:
        with open(EVENTS, "rb") as f:
            f.seek(0, 2); f.seek(max(0, f.tell() - 4_000_000)); lines = f.read().decode(errors="ignore").splitlines()[1:]
    except OSError: lines = []
    for l in lines:
        try: e = json.loads(l)
        except ValueError: continue
        if e.get("kind") != "buy" or e.get("t", 0) < cut: continue
        if e["w"] in S or e["w"] in S2: hits.setdefault(e.get("mint"), set()).add(e["w"])
    return {m: sorted(ws) for m, ws in hits.items() if m and len(ws) >= min_wallets}


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        import joblock; joblock.guard("smart_early")
        build(int(sys.argv[sys.argv.index("--max-calls") + 1]) if "--max-calls" in sys.argv else 25)
    elif cmd == "list":
        J = load() or {}
        print(f"built {J.get('built_at')}: {J.get('n_smart')} smart, {J.get('n_candidate')} candidate")
        for w in J.get("wallets", [])[:40]:
            print(w["tier"], w["address"], w["label"], "; ".join(f"{c['ticker']} {c['result']} +{c['min_after_launch']}m" for c in w["coins"]))
    elif cmd == "confluence":
        for m, ws in confluence().items(): print(m, len(ws), " ".join(ws))
