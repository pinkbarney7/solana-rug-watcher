#!/usr/bin/env python3
"""Grow rug_funders.json from dead / coordinated-launch coins. Info/risk tool only, not advice.

  python3 learn_rugs.py <MINT> [<MINT> ...]      # scorecard + learn for each mint (prints scorecard markdown)
  python3 learn_rugs.py --from-json r1.json ...  # learn from saved `scorecard.py --json` outputs
  python3 learn_rugs.py --harvest [--max 12] [--dry-run]   # re-scan dead coins found in past reports (skips ones harvested before)
  --no-learn  only score, do not write the list

A coin counts as a rug when: (a) it is down >= 90% from its peak (GeckoTerminal daily OHLCV high, top pool)
and has < $10k liquidity, or (b) scorecard check #14 FAILs as a coordinated launch.
Then its creator, plus any non-CEX funder of a creator-including cluster and the creator's first funder,
are added as medium confidence. They become high when linked to 2+ rug mints. Entries are deduped by address.
Never prints HELIUS_API_KEY (the scorecard scrubs it).
"""
import json, os, re, subprocess, sys, time, glob, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helius_checks as hc
LIST = hc.RUG_FILE
UA = {"User-Agent": "Mozilla/5.0"}
try:
    import requests
    def get(u):
        r = requests.get(u, headers=UA, timeout=20); r.raise_for_status(); return r.json()
except ImportError:
    import urllib.request
    def get(u):
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20))

def load():
    try: return json.load(open(LIST))
    except Exception: return {"_note": "", "wallets": []}

import fcntl
def locked_learn(J, reason):
    """Reload + learn + save under an exclusive lock so parallel runs don't drop each other's additions."""
    with open(LIST + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        D = load(); got = learn(J, reason, D); save(D)
        return got, len(D["wallets"])

def save(d):
    tmp = LIST + ".tmp"; json.dump(d, open(tmp, "w"), indent=1); os.replace(tmp, LIST)

def dex_batch(mints):
    import ds
    return {m: {**v, "toptl": 0} for m, v in ds.summary(mints).items()}

def drawdown(pool, price):
    """% below the highest daily high (last 30 days) of the pool, or None."""
    try:
        d = get(f"https://api.geckoterminal.com/api/v2/networks/solana/pools/{pool}/ohlcv/day?limit=30")
        hi = max(float(c[2]) for c in d["data"]["attributes"]["ohlcv_list"])
        cur = price or float(d["data"]["attributes"]["ohlcv_list"][0][4])
        return (1 - cur / hi) * 100 if hi > 0 else None, hi
    except Exception:
        return None, None

def score(mint):
    r = subprocess.run([sys.executable, os.path.join(HERE, "scorecard.py"), mint, "--json"], capture_output=True, text=True, timeout=240)
    return json.loads(r.stdout)

def is_rug(J, dx=None):
    """Return (reason or None, meta)."""
    reasons = []
    c14 = next((c for c in J.get("checks", []) if c["n"] == 14), None)
    if c14 and c14["status"] == "FAIL" and "coordinated launch" in (c14.get("detail") or ""):
        reasons.append("coordinated-launch FAIL (#14)")
    if dx is None: dx = dex_batch([J["mint"]]).get(J["mint"])
    if dx and dx["top"]:
        dd, hi = drawdown(dx["top"], dx["price"])
        if dd is not None and dd >= 90 and dx["liq"] < 10000:
            reasons.append(f"down {dd:.1f}% from 30d daily high ${hi:.3g}, liquidity ${dx['liq']:,.0f}")
    return "; ".join(reasons) or None

def learn(J, reason, D):
    H = J.get("helius") or {}
    mint = J["mint"]; tick = J.get("ticker") or "?"
    if not H.get("creator"): return []
    cand = [(H["creator"], f"{tick} creator", f"Deployer of {tick} ({mint}); {reason}")]
    cf = H.get("creator_funder")
    seen_f = set()
    for cl in H.get("clusters", []):
        f = cl["funder"]
        if cl.get("includes_creator") and not cl.get("known_cex") and not cl.get("mixer") and not (cl.get("exchange_like") and not cl.get("operator_like")):
            seen_f.add(f)
            cand.append((f, f"{tick} operator funder", f"Funded {tick} creator + {len(cl['wallets']) - 1} other checked wallet(s); cluster got {cl['early_got_pct']:.1f}% at launch; {reason}"))
    # multi-hop hubs (trace): an external wallet linked to the creator + launch buyers, or to 3+ launch buyers that got >10%
    for hb in (H.get("trace") or {}).get("hubs") or []:
        f = hb["hub"]
        if hb.get("is_launch_wallet") or hb.get("busy") or hb.get("mixer") or f in seen_f or f in hc.KNOWN_CEX: continue
        if hb.get("includes_creator") or (hb.get("n_early", 0) >= 3 and hb.get("early_got_pct", 0) > 10):
            seen_f.add(f)
            cand.append((f, f"{tick} launch hub", f"Multi-hop hub: linked to {'the creator + ' if hb.get('includes_creator') else ''}{hb['n_early']} launch buyer(s) "
                         f"({hb.get('direct', 0)} direct, max {hb.get('max_hops')} hops) that got {hb.get('early_got_pct', 0):.1f}% at launch; {reason}"))
    busy = {cl["funder"] for cl in H.get("clusters", []) if cl.get("exchange_like") and not cl.get("operator_like")}
    if cf and cf[0] not in seen_f and cf[0] not in busy and cf[0] not in hc.KNOWN_CEX and cf[0] not in hc.KNOWN_MIXERS:
        cand.append((cf[0], f"{tick} creator funder", f"First SOL funder of the {tick} creator ({cf[1]:.3f} SOL); {reason}"))
    idx = {w["address"]: w for w in D["wallets"]}
    added = []
    today = datetime.date.today().isoformat()
    for a, label, ev in cand:
        if a in hc.KNOWN_CEX: continue
        w = idx.get(a)
        if w:
            if mint not in w["linked_mints"]:
                w["linked_mints"].append(mint); w["evidence"] += f" | {ev}"
                if len(w["linked_mints"]) >= 2: w["confidence"] = "high"
                added.append(("updated", a, label))
        else:
            w = {"address": a, "label": label, "evidence": ev, "source": "learn_rugs.py (scorecard Helius + DexS/GeckoTerminal)",
                 "first_seen": today, "linked_mints": [mint], "confidence": "medium"}
            D["wallets"].append(w); idx[a] = w; added.append(("added", a, label))
    return added

MINT_RE = re.compile(r"(?<![1-9A-HJ-NP-Za-km-z])[1-9A-HJ-NP-Za-km-z]{32,44}(?![1-9A-HJ-NP-Za-km-z])")
def harvest_mints():
    files = glob.glob("/workspace/meme-market-watch-*.md") + glob.glob("/workspace/*scan*.md") + glob.glob("/workspace/deep-market-search-*.md")
    for d in glob.glob("/workspace/scan*") + glob.glob("/workspace/livetest*"):
        if os.path.isdir(d): files += glob.glob(d + "/**/*.md", recursive=True)
    ms = {}
    for f in files:
        try: txt = open(f, errors="ignore").read()
        except Exception: continue
        # token mints only: link targets, or addresses ending in "pump" (pump.fun vanity)
        found = re.findall(r"(?:pump\.fun/coin/|dexscreener\.com/solana/|rugcheck\.xyz/tokens/|\"mint\": \")([1-9A-HJ-NP-Za-km-z]{32,44})", txt)
        found += [m for m in MINT_RE.findall(txt) if m.endswith("pump")]
        for m in found: ms.setdefault(m, f)
    for m in [os.path.basename(f)[:-3] for f in glob.glob("/workspace/livetest*/*.md")]: ms.setdefault(m, "livetest")
    return ms

def main(argv):
    if argv and argv[0] not in ("-h", "--help"):
        import joblock; joblock.guard("learn_rugs")    # harvest + learning share one lock (both edit the rug list)
    learn_on = "--no-learn" not in argv; dry = "--dry-run" in argv
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and not (i and argv[i - 1] == "--max")]
    D = load(); log = []
    if "--harvest" in argv:
        ms = harvest_mints(); print(f"harvest: {len(ms)} candidate addresses from past reports", file=sys.stderr)
        dx = dex_batch(list(ms)); print(f"harvest: {len(dx)} are Solana tokens with DEX pairs", file=sys.stderr)
        targets = []
        for m, x in dx.items():
            if x["liq"] < 10000 and x["top"]:
                dd, hi = drawdown(x["top"], x["price"]); time.sleep(2.1)   # GeckoTerminal ~30 req/min
                if dd is not None and dd >= 90: targets.append((m, x, dd))
        print(f"harvest: {len(targets)} dead coins (>=90% off 30d high, liq <$10k)", file=sys.stderr)
        done = set()
        try:
            import kv
            done = {m for m, _, _ in targets if kv.get("harvested:" + m)}
        except Exception:
            kv = None
        mx = int(argv[argv.index("--max") + 1]) if "--max" in argv else 12     # credit guard: ~250-850 credits per cold scorecard
        todo = [t for t in targets if t[0] not in done][:mx]
        print(f"harvest: {len(done)} already harvested earlier, scoring {len(todo)} now (--max {mx})", file=sys.stderr)
        for m, x, dd in todo:
            try: J = score(m)
            except Exception as e: print(f"  {m}: scorecard failed ({hc.scrub(e)})", file=sys.stderr); continue
            reason = f"down {dd:.1f}% from 30d daily high, liquidity ${x['liq']:,.0f}"
            c14 = next((c for c in J.get("checks", []) if c["n"] == 14), None)
            if c14 and c14["status"] == "FAIL" and "coordinated launch" in (c14.get("detail") or ""): reason += "; coordinated-launch FAIL (#14)"
            got = locked_learn(J, reason)[0] if not dry else []
            if kv and not dry: kv.put("harvested:" + m, {"t": time.time(), "changes": len(got)})
            log.append((m, J.get("ticker"), reason, got)); print(f"  {J.get('ticker')} {m}: {len(got)} wallet change(s)", file=sys.stderr)
    paths = [a for a in args if a.endswith(".json")] if "--from-json" in argv else []
    for a in (args if "--from-json" not in argv else []):
        J = score(a)
        import scorecard as _sc
        print(_sc.render(J))
        reason = is_rug(J)
        if reason and learn_on and not dry: log.append((a, J.get("ticker"), reason, locked_learn(J, reason)[0]))
    for p in paths:
        J = json.load(open(p)); reason = is_rug(J)
        if reason and learn_on and not dry: log.append((J["mint"], J.get("ticker"), reason, locked_learn(J, reason)[0]))
    D = load()
    print(f"\n[learn_rugs] list size {len(D['wallets'])}; changes this run:", file=sys.stderr)
    for m, t, reason, got in log:
        for kind, a, label in got: print(f"  {kind} {a} ({label}) from {t} {m}: {reason}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])
