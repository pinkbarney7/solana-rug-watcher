#!/usr/bin/env python3
"""Smart-money list from our own data (read-only; info only - NOT a buy signal).

  python3 smart_money.py build [--coins N] [--wallets N] [--dry-run]   # rebuild smart_money.json (~1.5-2.5k Helius credits)
  python3 smart_money.py list                                          # print the current list
  python3 smart_money.py wallet <ADDR>                                  # stats for one wallet (~20 credits)

How the list is built
 1. Coins: every mint in score_log.jsonl + mints in past scan reports. Keep coins that "held up": >= $50k liquidity now
    and not down >= 70% from the first logged market cap (up to --coins, default 25, by liquidity).
 2. Wallets seen on those coins: buyers in the first 200 mint txs (excluding slots 0-3 = bundles/snipers and the creator)
    and current top-20 holders. Candidates = wallets seen on 2+ coins, then early buyers that still hold (up to --wallets, default 60).
 3. For each candidate: last ~200 txs (getTransactionsForAddress, SOL/WSOL-quoted single-token swaps only) -> per-token positions.
    Closed position = sold >= 50% of what it bought in the window. Realized PnL = SOL received - SOL cost of the sold part.
 4. Tier "consistent" = >= 5 closed positions, win rate >= 40%, realized >= +2 SOL, profit factor (gross wins / gross losses) >= 1.5,
    not bot-like (200 txs span >= 3 h and median hold >= 1 min). Tier "profitable" = >= 5 closed, >= +3 SOL, profit factor >= 2
    but failing the win-rate or bot filters (labelled bot/sniper-like or low win rate). Coins with mcap > $150M are not used.
    Excluded: rug_funders.json wallets, coin creators, slots 0-3 launch buyers of any examined coin, known CEX wallets, PDAs.
Caveats: small samples (a few weeks of history at most, 4-20 closed positions per wallet), USDC-quoted and multi-hop swaps
are skipped, transfers between a trader's own wallets look like buys/sells, fees/tips are inside the SOL deltas, and past
results say nothing about the next trade. Copy-trading these wallets is a well-known way to become exit liquidity.
"""
import json, os, statistics, sys, time
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import helius_checks as hc

OUT = os.path.join(HERE, "smart_money.json")
WSOL = "So11111111111111111111111111111111111111112"
import majors
STABLE = {"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"} | majors.all_mints()
MIN_CLOSED, MIN_WIN, MIN_PNL, MIN_PF = 5, 0.40, 2.0, 1.5
MAX_MCAP = 150e6        # skip large established coins (their "early buyers" are from another era)


def load():
    try: return json.load(open(OUT))
    except Exception: return None


# ---------------------------------------------------------------- per-wallet swap stats
def wallet_stats(H, w, pages=2):
    txs, tok = [], None
    for _ in range(pages):
        p = {"sortOrder": "desc", "limit": 100, "transactionDetails": "full", "encoding": "jsonParsed",
             "maxSupportedTransactionVersion": 1, "filters": {"status": "succeeded", "tokenAccounts": "balanceChanged"}}
        if tok: p["paginationToken"] = tok
        r, e = H.rpc("getTransactionsForAddress", [w, p])
        if e: raise RuntimeError(e)
        d = (r or {}).get("data") or []
        txs += d; tok = (r or {}).get("paginationToken")
        if not d or not tok: break
    pos = defaultdict(lambda: {"bt": 0, "st": 0, "sol_in": 0.0, "sol_out": 0.0, "fb": None, "ls": None, "nb": 0, "ns": 0})
    swaps = skipped = 0
    for tx in txs:
        m = tx.get("meta") or {}; keys = hc.keys_of(tx)
        if w not in keys: continue
        i = keys.index(w)
        sol = (m["postBalances"][i] - m["preBalances"][i]) / 1e9
        td = defaultdict(int)
        for side, sg in (("preTokenBalances", -1), ("postTokenBalances", 1)):
            for b in m.get(side) or []:
                if b.get("owner") == w: td[b["mint"]] += sg * int(b["uiTokenAmount"]["amount"])
        sol += td.pop(WSOL, 0) / 1e9
        td = {k: v for k, v in td.items() if v}
        if any(k in STABLE for k in td) or len(td) != 1: skipped += bool(td); continue
        (mint, dv), = td.items()
        t = tx.get("blockTime") or 0
        P = pos[mint]
        if dv > 0 and sol < -0.001:
            P["bt"] += dv; P["sol_in"] += -sol; P["nb"] += 1; P["fb"] = min(P["fb"] or t, t); swaps += 1
        elif dv < 0 and sol > 0.0005:
            P["st"] += -dv; P["sol_out"] += sol; P["ns"] += 1; P["ls"] = max(P["ls"] or t, t); swaps += 1
    closed = []
    for mint, P in pos.items():
        if P["bt"] <= 0 or P["st"] < 0.5 * P["bt"]: continue
        frac = min(1.0, P["st"] / P["bt"])
        pnl = P["sol_out"] - P["sol_in"] * frac
        hold = (P["ls"] - P["fb"]) if (P["ls"] and P["fb"]) else None
        closed.append({"mint": mint, "pnl_sol": pnl, "cost_sol": P["sol_in"] * frac, "hold_s": hold})
    ts = [tx.get("blockTime") or 0 for tx in txs if tx.get("blockTime")]
    span_h = (max(ts) - min(ts)) / 3600 if ts else 0
    holds = [c["hold_s"] for c in closed if c["hold_s"] is not None and c["hold_s"] >= 0]
    wins = sum(1 for c in closed if c["pnl_sol"] > 0)
    gw = sum(c["pnl_sol"] for c in closed if c["pnl_sol"] > 0); gl = -sum(c["pnl_sol"] for c in closed if c["pnl_sol"] < 0)
    return {"address": w, "txs": len(txs), "swaps": swaps, "skipped_multi": skipped, "window_h": round(span_h, 1),
            "positions": len(pos), "closed": len(closed), "wins": wins,
            "win_rate": round(wins / len(closed), 3) if closed else None,
            "realized_sol": round(sum(c["pnl_sol"] for c in closed), 3),
            "profit_factor": round(gw / gl, 2) if gl > 0 else (99.0 if gw > 0 else None),
            "trades_per_day": round(len(txs) / max(span_h / 24, 1 / 24), 1),
            "median_hold_min": round(statistics.median(holds) / 60, 1) if holds else None,
            "best": sorted(closed, key=lambda c: -c["pnl_sol"])[:3]}


def is_smart(s):
    return (s["closed"] >= MIN_CLOSED and (s["win_rate"] or 0) >= MIN_WIN and s["realized_sol"] >= MIN_PNL
            and (s.get("profit_factor") or 0) >= MIN_PF and s["window_h"] >= 3 and (s["median_hold_min"] or 0) >= 1)


# ---------------------------------------------------------------- build
def sol_price(http):
    d, e = http("https://api.dexscreener.com/latest/dex/tokens/" + WSOL)
    ps = [p for p in (d or {}).get("pairs") or [] if p.get("chainId") == "solana" and p["baseToken"]["address"] == WSOL
          and p["quoteToken"]["symbol"] in ("USDC", "USDT")]
    ps.sort(key=lambda p: -float((p.get("liquidity") or {}).get("usd") or 0))
    return float(ps[0]["priceUsd"]) if ps else None


def build(n_coins=25, n_wallets=50, dry=False):
    import scorecard, ds, learn_rugs
    t0 = time.time()
    H = hc.Helius(scorecard.http, cap=int(os.environ.get("SM_MAX_CALLS", "400")))
    first = {}
    for line in open(os.path.join(HERE, "score_log.jsonl")):
        try: e = json.loads(line)
        except Exception: continue
        if e.get("mint") and e["mint"] not in first: first[e["mint"]] = e
    mints = list(first) + [m for m in learn_rugs.harvest_mints() if m not in first]
    cur = ds.summary(mints)
    held = []
    for m, c in cur.items():
        if c["liq"] < 50000 or float(c.get("mcap") or 0) > MAX_MCAP: continue
        f = first.get(m)
        if f and f.get("mcap") and c.get("mcap") and float(c["mcap"]) < 0.3 * float(f["mcap"]): continue
        held.append((c["liq"], m, c.get("sym")))
    held = [(m, s) for _, m, s in sorted(held, reverse=True)[:n_coins]]
    print(f"[smart_money] {len(mints)} mints known, {len(cur)} with pairs, {len(held)} held up -> examining", file=sys.stderr)
    RL = set(hc.load_rug_list())
    seen = defaultdict(lambda: {"early": set(), "holder": set()})
    excluded = set(RL) | set(hc.KNOWN_CEX)
    coins_used = []
    for m, sym in held:
        try:
            txs, tok = [], None
            for _ in range(2):
                d, tok = H.txs_asc(m, 100, tok); txs += d
                if not d or not tok: break
            if not txs: continue
            s0 = txs[0]["slot"]; excluded.add(hc.keys_of(txs[0])[0])
            for tx in txs:
                if (tx.get("meta") or {}).get("err"): continue
                dl, _ = hc.mint_deltas(tx, m)
                for o, dv in dl.items():
                    if dv <= 0 or not hc.on_curve(o): continue
                    if tx["slot"] <= s0 + hc.EARLY_SLOTS: excluded.add(o)
                    else: seen[o]["early"].add(m)
            la, e = H.rpc("getTokenLargestAccounts", [m])
            if not e:
                acc = H.accounts([x["address"] for x in la["value"]])
                for x in la["value"]:
                    try: o = acc[x["address"]]["data"]["parsed"]["info"]["owner"]
                    except Exception: continue
                    if hc.on_curve(o): seen[o]["holder"].add(m)
            coins_used.append({"mint": m, "ticker": sym, "liq": cur[m]["liq"]})
        except hc.Budget:
            print("[smart_money] Helius cap reached while reading coins", file=sys.stderr); break
        except Exception as ex:
            print(f"[smart_money] {sym} {m}: {hc.scrub(ex)}", file=sys.stderr)
    for w in list(seen):
        if w in excluded: seen.pop(w)
    multi = sorted([w for w, v in seen.items() if len(v["early"] | v["holder"]) >= 2], key=lambda w: -len(seen[w]["early"] | seen[w]["holder"]))
    believers = [w for w, v in seen.items() if v["early"] & v["holder"] and w not in multi]
    cands = (multi + believers)[:n_wallets]
    print(f"[smart_money] {len(seen)} wallets seen; {len(multi)} on 2+ coins, {len(believers)} early+still holding; checking {len(cands)}", file=sys.stderr)
    stats = []
    from concurrent.futures import ThreadPoolExecutor
    def one(w):
        try: return wallet_stats(H, w)
        except hc.Budget: return None
        except Exception: return None
    with ThreadPoolExecutor(4) as ex:
        for s in ex.map(one, cands):
            if s: stats.append(s)
    # PDAs / program wallets: drop accounts owned by programs
    info = H.accounts([s["address"] for s in stats]) if stats else {}
    stats = [s for s in stats if not (info.get(s["address"]) or {}).get("owner") not in (None, hc.SYSTEM_PROGRAM)]
    px = sol_price(scorecard.http)
    smart = []
    for s in stats:
        s["seen_in"] = sorted(seen[s["address"]]["early"] | seen[s["address"]]["holder"])
        s["roles"] = {"early": len(seen[s["address"]]["early"]), "holder": len(seen[s["address"]]["holder"])}
        s["realized_usd_est"] = round(s["realized_sol"] * px) if px else None
        s["bot_like"] = s["window_h"] < 3 or (s["median_hold_min"] is not None and s["median_hold_min"] < 1)
        if is_smart(s): s["tier"] = "consistent"; smart.append(s)
        elif s["closed"] >= MIN_CLOSED and s["realized_sol"] >= 3 and (s.get("profit_factor") or 0) >= 2:
            s["tier"] = "profitable-fast (bot/sniper-like)" if s["bot_like"] else "profitable (low win rate)"
            smart.append(s)
    smart.sort(key=lambda s: (s["tier"] != "consistent", -s["realized_sol"]))
    J = {"built_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sol_usd": px,
         "criteria": f">= {MIN_CLOSED} closed positions, win rate >= {MIN_WIN:.0%}, realized >= +{MIN_PNL} SOL, profit factor >= {MIN_PF}, window >= 3 h, median hold >= 1 min",
         "coins_used": coins_used, "candidates_checked": len(stats), "helius_calls": H.calls, "credits_est": H.credits,
         "wallets": smart, "n_consistent": sum(1 for x in smart if x["tier"] == "consistent"),
         "near_misses": sorted([s for s in stats if s not in smart and s["closed"] >= 2 and s["realized_sol"] > 0],
                                                key=lambda s: -s["realized_sol"])[:15],
         "caveats": __doc__.split("Caveats:")[1].strip()}
    if not dry:
        tmp = OUT + ".tmp"; json.dump(J, open(tmp, "w"), indent=1); os.replace(tmp, OUT)
    print(f"[smart_money] {len(smart)} smart wallets from {len(stats)} checked ({H.calls} Helius calls, ~{H.credits} credits, {time.time()-t0:.0f}s)", file=sys.stderr)
    return J


# ---------------------------------------------------------------- scorecard check #17
def check(mint, H, W):
    """(status, value, detail). Always INFO: never a buy signal and never changes the verdict."""
    J = load()
    if not J: return "INFO", "smart-money list not built (run: python3 smart_money.py build)", ""
    SM = {w["address"]: w for w in J.get("wallets", [])}
    if not SM: return "INFO", f"smart-money list empty (built {J.get('built_at')})", ""
    hold = [h["owner"] for h in (H or {}).get("holders") or [] if h["owner"] in SM]
    early = [x["wallet"] for x in (H or {}).get("early") or [] if x["wallet"] in SM]
    net = (W or {}).get("makers_net") or {}
    nb = [m for m, v in net.items() if m in SM and v > 0]; ns = [m for m, v in net.items() if m in SM and v < 0]
    allw = list(dict.fromkeys(hold + early + nb + ns))
    if not allw:
        return "INFO", f"none of {len(SM)} tracked smart-money wallets in top holders / launch buyers / last trades", f"list built {J.get('built_at', '?')[:16]}; small sample, info only"
    val = f"{len(allw)} of {len(SM)} tracked wallet(s): {len(hold)} in top holders, {len(early)} launch buyer(s), {len(nb)} net buyer(s) / {len(ns)} net seller(s) in last trades"
    det = "; ".join(f"{hc._short(w)} [{SM[w].get('tier', 'consistent')}] ({SM[w]['closed']} closed, win {SM[w]['win_rate']:.0%}, {SM[w]['realized_sol']:+.1f} SOL)" for w in allw[:4])
    det += "; info only, NOT a buy signal - smart wallets also exit into late buyers; small samples"
    return "INFO", val, det


def main(a):
    cmd = a[0] if a else "list"
    num = lambda f, d: int(a[a.index(f) + 1]) if f in a else d
    if cmd == "build":
        import joblock; joblock.guard("smart_money")
        J = build(num("--coins", 25), num("--wallets", 60), "--dry-run" in a)
    elif cmd == "wallet":
        import scorecard
        print(json.dumps(wallet_stats(hc.Helius(scorecard.http), a[1]), indent=1)); return
    else:
        J = load()
        if not J: print("no smart_money.json yet - run: python3 smart_money.py build"); return
    print(f"Smart-money list (built {J['built_at']}; {len(J['wallets'])} wallets from {J['candidates_checked']} checked on {len(J['coins_used'])} coins). Info only, not a buy signal.")
    for s in J["wallets"]:
        print(f"  [{s.get('tier', 'consistent')}] {s['address']}  closed {s['closed']:>2}  win {s['win_rate']:.0%}  realized {s['realized_sol']:+8.2f} SOL"
              f"  (~${s['realized_usd_est'] or 0:,})  PF {s.get('profit_factor')}  median hold {s['median_hold_min']} min  window {s['window_h']} h  seen on {len(s['seen_in'])} coin(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
