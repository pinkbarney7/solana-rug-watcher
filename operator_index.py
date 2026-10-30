"""Same-operator matching across coins (check #19). Zero extra Helius credits: it reuses data the scorecard already has.

Every scored coin leaves a fingerprint in operator_index.json (file-locked): creator, creator's funder, non-exchange
cluster funders, multi-hop hubs, launch (slots 0-3) buyers, launch-bundle % and creation-slot %. A new coin is linked
to an earlier one when they share
  strong: the same creator, the same creator funder, a shared cluster funder / hub, or 3+ of the same launch buyers
  weak:   launch buyers took the same % of supply to 2 decimals (>= 20%) -- e.g. RARINU vs A1 both 91.19% (2026-10-07)
Wallets that appear as launch buyers on 6+ indexed coins are treated as generic snipers/bots and ignored.
Status: FAIL = strong link to a coin that was a coordinated launch (#14 FAIL), rug-linked (#15 FAIL) or is a rug-list mint;
WARN = any other strong link, or a weak link plus any shared wallet; INFO-only weak links otherwise; PASS = none.
"""
import fcntl, json, os, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "operator_index.json")
SNIPER_N = 6
MAX_COINS = 3000


def _load():
    try: return json.load(open(IDX))
    except Exception: return {"coins": {}}


def fingerprint(R):
    H = R.get("helius") or {}
    if not H.get("creator"): return None
    import helius_checks as hc
    ex = set(hc.KNOWN_CEX) | set(hc.KNOWN_MIXERS)
    cf = H.get("creator_funder"); cf = cf[0] if isinstance(cf, (list, tuple)) and cf else None
    clus = [c["funder"] for c in H.get("clusters") or [] if not c.get("exchange_like") and c["funder"] not in ex]
    hubs = [h["hub"] for h in (H.get("trace") or {}).get("hubs") or [] if not h.get("busy")]
    early = [x["wallet"] for x in (H.get("early") or [])[:40]]
    st = {c["n"]: c["status"] for c in R.get("checks") or []}
    return {"ticker": R.get("ticker"), "t": R.get("generated_at"), "creator": H["creator"],
            "creator_funder": cf if cf not in ex else None, "funders": sorted(set(clus))[:20], "hubs": hubs[:6], "early": early,
            "bundle_pct": round(sum(x.get("got_pct", 0) for x in H.get("early") or []), 2),
            "slot0_pct": round(sum(x.get("slot0_pct", 0) for x in H.get("early") or []), 2),
            "c14": st.get(14), "c15": st.get(15), "verdict": R.get("verdict"), "risk": (R.get("risk") or {}).get("score")}


def record(R):
    import majors
    if majors.is_major(R.get("mint")): return          # USDC/USDT/wSOL etc. are not operator coins
    fp = fingerprint(R)
    if not fp: return
    with open(IDX + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        D = _load(); D["coins"][R["mint"]] = fp
        if len(D["coins"]) > MAX_COINS:
            for m in sorted(D["coins"], key=lambda m: D["coins"][m].get("t") or "")[:len(D["coins"]) - MAX_COINS]: D["coins"].pop(m)
        tmp = IDX + ".tmp"; json.dump(D, open(tmp, "w")); os.replace(tmp, IDX)


def links(mint, fp, D=None):
    D = D or _load()
    coins = {m: c for m, c in D["coins"].items() if m != mint}
    freq = Counter(w for c in coins.values() for w in set(c.get("early") or []))
    snipers = {w for w, n in freq.items() if n >= SNIPER_N - 1}
    my_early = set(fp.get("early") or []) - snipers
    my_fund = set(fp.get("funders") or []) | set(fp.get("hubs") or []) | ({fp["creator_funder"]} if fp.get("creator_funder") else set())
    out = []
    for m, c in coins.items():
        why, strong = [], False
        if c.get("creator") == fp["creator"]: why.append("same creator"); strong = True
        if fp.get("creator_funder") and fp["creator_funder"] == c.get("creator_funder"): why.append(f"same creator funder {fp['creator_funder'][:6]}.."); strong = True
        theirs = set(c.get("funders") or []) | set(c.get("hubs") or []) | ({c["creator_funder"]} if c.get("creator_funder") else set())
        sf = (my_fund & theirs) - ({fp["creator_funder"]} if fp.get("creator_funder") == c.get("creator_funder") else set())
        if sf: why.append(f"shared funder/hub {', '.join(sorted(a[:6] + '..' for a in sf)[:3])}"); strong = True
        se = my_early & set(c.get("early") or [])
        if len(se) >= 3: why.append(f"{len(se)} shared launch buyers"); strong = True
        elif se: why.append(f"{len(se)} shared launch buyer(s)")
        weak = fp.get("bundle_pct", 0) >= 20 and abs(fp.get("bundle_pct", 0) - (c.get("bundle_pct") or -1)) < 0.005
        if weak: why.append(f"identical launch-bundle share {fp['bundle_pct']:.2f}%")
        if strong or weak:
            bad = c.get("c14") == "FAIL" or c.get("c15") == "FAIL"
            out.append({"mint": m, "ticker": c.get("ticker"), "strong": strong, "weak_only": not strong, "bad": bad,
                        "why": why, "their_verdict": c.get("verdict"), "their_risk": c.get("risk"), "seen": c.get("t")})
    out.sort(key=lambda x: (not x["strong"], not x["bad"]))
    return out


def check(mint, H, ticker=None):
    """(status, value, detail, links) for scorecard check #19."""
    fp = fingerprint({"mint": mint, "helius": H, "checks": [], "ticker": ticker})
    if not fp: return "INFO", "not checked - no Helius launch data", "", []
    import helius_checks as hc
    rug_mints = {m for w in hc.load_rug_list().values() for m in w.get("linked_mints") or []}
    L = links(mint, fp)
    for x in L:
        if x["mint"] in rug_mints: x["bad"] = True
    strong = [x for x in L if x["strong"]]; bad = [x for x in strong if x["bad"]]
    weak_plus = [x for x in L if x["weak_only"] and len(x["why"]) >= 2]
    n = len(_load()["coins"])
    if not L: return "PASS", f"no operator overlap with {n} indexed coins", "", []
    st = "FAIL" if bad else "WARN" if (strong or weak_plus) else "INFO"
    top = L[0]
    val = (f"{len(strong)} strong / {len(L) - len(strong)} weak link(s) to other coins; top: {top.get('ticker') or '?'} "
           f"{top['mint']} ({'; '.join(top['why'])}" + (", that coin was a coordinated launch / rug-linked" if top["bad"] else "") + ")")
    det = "; ".join(f"{x.get('ticker') or '?'} {x['mint'][:6]}..: {', '.join(x['why'])}" for x in L[1:5])
    det = (det + "; " if det else "") + f"index has {n} coins; wallets seen as launch buyers on {SNIPER_N}+ coins are ignored as snipers"
    return st, val, det, L[:10]


def backfill(paths):
    """Index saved scorecard JSONs (no API calls)."""
    import glob
    n = 0
    files = sorted({f for p in paths for f in glob.glob(p)}, key=os.path.getmtime)
    for f in files:
        try:
            R = json.load(open(f))
            if isinstance(R, dict) and R.get("mint") and (R.get("helius") or {}).get("creator"): record(R); n += 1
        except Exception:
            pass
    return n


if __name__ == "__main__":
    import sys
    if sys.argv[1:2] == ["backfill"]:
        print("indexed", backfill(sys.argv[2:] or ["/workspace/scan*/*.json", "/workspace/livetest*/*.json", "/workspace/scorecard*/livetest*/*.json", "/workspace/scorecard*/examples/*.json", "/workspace/**/*scorecard*.json"]))
    elif sys.argv[1:2] == ["links"]:
        D = _load(); m = sys.argv[2]
        for x in links(m, D["coins"][m], D): print(x)
    else:
        D = _load(); print(len(D["coins"]), "coins indexed")
