"""Check #18: wash-trading / fake-volume detection from recent swaps on the main pool (Helius full txs).
Read-only. Thresholds are heuristics chosen for meme coins, not proof of intent.

Metrics over the last WASH_TXS successful pool txs:
  - tx per unique maker (owner whose balance of the mint changed)
  - churn share: volume from makers with >= 2 buys AND >= 2 sells in the window
  - round-trip share: volume in buy/sell pairs by the same maker with near-identical token size (<= 2% apart),
    excluding same-slot pairs (MEV sandwiches, reported separately)
  - self-funded loop: >= 2 of the top churners share a first funder (non-exchange) or fund each other
  - dust share: trades under $1 (bot spam that inflates tx/maker counts)
FAIL: churn >= 50% and round-trip >= 25%, or a common-funded churner group makes >= 30% of volume.
WARN: churn >= 25%, round-trip >= 10%, tx/maker >= 4, a common-funded churner group, or dust >= 60% of trades.
"""
import os
from collections import defaultdict
import helius_checks as hc

WASH_TXS = int(os.environ.get("WASH_TXS", "200"))
LOOP_LOOKUPS = 6


def gather(mint, pair, http, price_usd=None, decimals=None, pool_accounts=()):
    R = {"pair": pair, "error": None}
    if not hc.KEY: R["error"] = "HELIUS_API_KEY not set"; return R
    if not pair: R["error"] = "no main pool address"; return R
    H = hc.Helius(http, cap=12)
    try:
        txs, tok = [], None
        while len(txs) < WASH_TXS:
            p = {"sortOrder": "desc", "limit": min(100, WASH_TXS - len(txs)), "transactionDetails": "full", "encoding": "jsonParsed",
                 "maxSupportedTransactionVersion": 1, "filters": {"status": "succeeded"}}
            if tok: p["paginationToken"] = tok
            r, e = H.rpc("getTransactionsForAddress", [pair, p])
            if e: raise RuntimeError(e)
            d = (r or {}).get("data") or []
            txs += d; tok = (r or {}).get("paginationToken")
            if not d or not tok: break
        skip = set(pool_accounts) | {pair} | hc.BURN
        trades = []
        for tx in txs:
            dl, _ = hc.mint_deltas(tx, mint)
            for o, dv in dl.items():
                if dv == 0 or o in skip or not hc.on_curve(o): continue
                trades.append({"maker": o, "side": "buy" if dv > 0 else "sell", "amt": abs(dv), "slot": tx["slot"],
                               "t": tx.get("blockTime") or 0, "signer": hc.keys_of(tx)[0]})
        R["n_txs"] = len(txs); R["n_trades"] = len(trades)
        if not trades: R["error"] = "no swaps decoded on main pool"; return R
        R["window_min"] = (max(t["t"] for t in trades) - min(t["t"] for t in trades)) / 60
        mk = defaultdict(lambda: {"buy": [], "sell": []})
        for t in trades: mk[t["maker"]][t["side"]].append(t)
        tot = sum(t["amt"] for t in trades)
        net = {m: sum(t["amt"] for t in v["buy"]) - sum(t["amt"] for t in v["sell"]) for m, v in mk.items()}
        R["makers_net"] = dict(sorted(net.items(), key=lambda kv: -abs(kv[1]))[:300])
        R["makers"] = len(mk); R["tx_per_maker"] = len(trades) / len(mk)
        churn = [m for m, v in mk.items() if len(v["buy"]) >= 2 and len(v["sell"]) >= 2]
        R["churners"] = len(churn)
        R["churn_share"] = sum(t["amt"] for m in churn for s in ("buy", "sell") for t in mk[m][s]) / tot * 100
        rt = sand = 0
        for m, v in mk.items():
            sells = sorted(v["sell"], key=lambda t: t["slot"]); used = set()
            for b in sorted(v["buy"], key=lambda t: t["slot"]):
                for i, sl in enumerate(sells):
                    if i in used: continue
                    if abs(sl["amt"] - b["amt"]) <= 0.02 * max(sl["amt"], b["amt"]):
                        used.add(i)
                        if sl["slot"] == b["slot"]: sand += b["amt"] + sl["amt"]
                        else: rt += b["amt"] + sl["amt"]
                        break
        R["roundtrip_share"] = rt / tot * 100; R["sandwich_share"] = sand / tot * 100
        top = sorted(mk, key=lambda m: -sum(t["amt"] for s in ("buy", "sell") for t in mk[m][s]))
        R["top_maker_share"] = sum(t["amt"] for s in ("buy", "sell") for t in mk[top[0]][s]) / tot * 100
        if price_usd and decimals is not None:
            usd = [t["amt"] / 10 ** decimals * price_usd for t in trades]
            R["dust_share"] = sum(1 for u in usd if u < 1) / len(usd) * 100
            R["window_volume_usd"] = sum(usd)
        # self-funded loop among the biggest churners
        R["loop"] = None
        big = sorted(churn, key=lambda m: -sum(t["amt"] for s in ("buy", "sell") for t in mk[m][s]))[:LOOP_LOOKUPS]
        if len(big) >= 2 and R["churn_share"] >= 20:
            ff = {}
            for m in big:
                try: f = hc.first_funder(H, m)
                except hc.Budget: break
                except Exception: f = None
                ff[m] = f[0] if f else None
            grp = defaultdict(list)
            for m, f in ff.items():
                if f and f not in hc.KNOWN_CEX: grp[f].append(m)
            mutual = [m for m, f in ff.items() if f in ff]          # funded by another churner
            g = max(grp.values(), key=len) if grp else []
            members = set(g if len(g) >= 2 else []) | set(mutual) | {ff[m] for m in mutual}
            members &= set(mk)
            if members:
                share = sum(t["amt"] for m in members for s in ("buy", "sell") for t in mk[m][s]) / tot * 100
                R["loop"] = {"wallets": sorted(members), "share": share,
                             "funder": next((f for f, v in grp.items() if v == g), None) if len(g) >= 2 else None, "mutual": len(mutual)}
    except hc.Budget as e:
        R["error"] = R.get("error") or str(e)
    except Exception as e:
        R["error"] = hc.scrub(f"{type(e).__name__}: {e}")
    R["calls"] = H.calls; R["credits_est"] = H.credits
    return R


def grade(W):
    """(status, value, detail) for check #18."""
    if not W or W.get("error") and not W.get("n_trades"):
        return "WARN", f"not checked - {(W or {}).get('error') or 'no data'}", ""
    sts = []; why = []
    c, r, tpm = W["churn_share"], W["roundtrip_share"], W["tx_per_maker"]
    lp = W.get("loop") or {}
    if (c >= 50 and r >= 25) or lp.get("share", 0) >= 30:
        sts.append("FAIL")
    if c >= 25: why.append(f"churn {c:.0f}%")
    if r >= 10: why.append(f"round trips {r:.0f}%")
    if tpm >= 4: why.append(f"{tpm:.1f} trades/maker")
    if lp: why.append(f"{len(lp['wallets'])} churners share a funder/fund each other ({lp['share']:.0f}% of volume)")
    if (W.get("dust_share") or 0) >= 60: why.append(f"dust trades {W['dust_share']:.0f}%")
    if why: sts.append("WARN")
    st = "FAIL" if "FAIL" in sts else "WARN" if sts else "PASS"
    val = (f"last {W['n_trades']} trades / {W['window_min']:.0f} min: {W['makers']} makers ({tpm:.1f}/maker); "
           f"churn {c:.0f}%, same-size round trips {r:.0f}%, top maker {W['top_maker_share']:.0f}%")
    det = []
    if W.get("dust_share") is not None: det.append(f"dust (<$1) trades {W['dust_share']:.0f}%")
    if W.get("window_volume_usd") is not None: det.append(f"window volume ~${W['window_volume_usd']:,.0f}")
    if W.get("sandwich_share"): det.append(f"same-slot buy/sell pairs (likely MEV sandwiches) {W['sandwich_share']:.0f}% - not counted")
    if lp: det.append(f"loop wallets: {', '.join(hc._short(w) for w in lp['wallets'][:4])}" + (f" (funder {hc._short(lp['funder'])})" if lp.get('funder') else ""))
    if why and st != "PASS": det.append("flags: " + ", ".join(why))
    det.append(f"main pool {hc._short(W['pair'])}; heuristics, not proof")
    if W.get("error"): det.append(f"partial: {W['error']}")
    return st, val, "; ".join(det)
