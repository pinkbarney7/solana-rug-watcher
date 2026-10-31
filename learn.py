#!/usr/bin/env python3
"""Free learning layer (DEX Screener + Jupiter quotes only, no Helius, no secrets). Info/risk only - never buy advice.
  python3 learn.py outcomes   per-rule rug precision / false positives -> alerts/rule_stats.md, bar_changes.jsonl (suggestions, NEVER auto-applied)
  python3 learn.py network    rugged-network penalties -> network_penalty.json (wallet links are leads, not proof)
  python3 learn.py paper      $25 simulated paper book -> alerts/paper_book.md + alerts/paper_book.jsonl (SIMULATION, not advice)
  python3 learn.py all
Inputs (whichever exist in LEARN_DIR, default this dir): check_log.jsonl, score_log.jsonl, alerts.jsonl, rug_times.jsonl,
operator_index.json, liq_watchlist.json, scored.json, alerts/outcomes.jsonl."""
import datetime, json, os, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.environ.get("LEARN_DIR", HERE)
A = os.path.join(D, "alerts"); os.makedirs(A, exist_ok=True)
P = lambda *x: os.path.join(D, *x)
UA = {"User-Agent": "rug-watcher/1.0"}
DEAD_LIQ = 1000.0
NOW = time.time()


def ts(s):
    try: return datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()
    except Exception: return None


def jl(p):
    out = []
    if os.path.exists(p):
        for l in open(p):
            try: out.append(json.loads(l))
            except Exception: pass
    return out


def jload(p, d):
    try: return json.load(open(p))
    except Exception: return d


def jsave(p, d):
    tmp = p + ".tmp"; json.dump(d, open(tmp, "w"), indent=1); os.replace(tmp, p)


def et(t): return datetime.datetime.fromtimestamp(t).astimezone().strftime("%Y-%m-%d %H:%M %Z")


def link(m): return f"https://pump.fun/coin/{m}" if m.endswith("pump") else f"https://dexscreener.com/solana/{m}"


def ds(mints):
    """DEX Screener snapshot {mint: {price, liq}}; mints with no pair at all map to {'missing': True}."""
    out = {}; mints = list(dict.fromkeys(m for m in mints if m))
    for i in range(0, len(mints), 30):
        ch = mints[i:i + 30]
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request("https://api.dexscreener.com/tokens/v1/solana/" + ",".join(ch), headers=UA), timeout=20))
        except Exception as e:
            print("dexscreener error:", type(e).__name__); time.sleep(2); continue
        for p in r or []:
            m = (p.get("baseToken") or {}).get("address"); liq = float((p.get("liquidity") or {}).get("usd") or 0)
            if m in ch and (m not in out or liq > out[m]["liq"]): out[m] = {"price": float(p.get("priceUsd") or 0), "liq": liq}
        for m in ch: out.setdefault(m, {"missing": True})
        time.sleep(1.1)   # DEX Screener free limit ~300/min; we stay far below
    return out


# ------------------------------------------------------------------ 1. outcome learning
def outcomes():
    LOG = P("alerts", "learn_log.jsonl")
    st = {r["mint"]: r for r in jl(LOG)}
    # per-check flags from scorecard runs (first run per mint)
    for r in jl(P("check_log.jsonl")):
        if r.get("kind") != "score" or not r.get("mint"): continue
        m = r["mint"]; t = ts(r.get("time"))
        if m in st and st[m].get("flags"): continue
        e = st.setdefault(m, {"mint": m, "t0": t})
        e.update({"ticker": r.get("ticker"), "verdict": r.get("verdict"), "risk": r.get("risk"), "src": r.get("src"),
                  "flags": {str(c["n"]): c.get("s") for c in r.get("checks") or [] if c.get("n") is not None},
                  "p0": r.get("price"), "liq0": r.get("liq"), "t0": e.get("t0") or t})
    for r in jl(P("score_log.jsonl")):
        m = r.get("mint")
        if m and m not in st: st[m] = {"mint": m, "t0": ts(r.get("time")), "ticker": r.get("ticker"), "verdict": r.get("verdict"), "risk": r.get("risk"), "p0": r.get("price"), "liq0": r.get("liq"), "flags": {}}
    for m, r in (jload(P("scored.json"), {}) or {}).items() if isinstance(jload(P("scored.json"), {}), dict) else []:
        if m not in st and isinstance(r, dict): st[m] = {"mint": m, "t0": r.get("t") or NOW, "ticker": r.get("ticker"), "verdict": r.get("verdict"), "risk": r.get("risk"), "p0": r.get("price"), "liq0": r.get("liq"), "flags": {}}
    for r in jl(P("alerts", "outcomes.jsonl")):     # outcomes.py state (Actions)
        m = r.get("mint")
        if m and m not in st: st[m] = {"mint": m, "t0": r.get("t0"), "ticker": r.get("ticker"), "verdict": r.get("verdict"), "risk": r.get("risk"), "p0": r.get("p0"), "liq0": r.get("liq0"), "flags": {}}
    for r in jl(P("alerts.jsonl"))[-5000:]:
        m = r.get("mint")
        if m in st: st[m].setdefault("alert_types", [])
        if m in st and r.get("type") not in st[m]["alert_types"]: st[m]["alert_types"].append(r.get("type"))
    rug = {}
    for r in jl(P("rug_times.jsonl")): rug.setdefault(r["mint"], r.get("detected_et"))
    for r in jl(P("check_log.jsonl")):
        if r.get("kind") == "outcome" and str(r.get("outcome", "")).startswith("dead"): rug.setdefault(r.get("mint"), r.get("time"))
    for m, r in st.items():
        if m in rug: r["rugged"] = True; r["rug_src"] = "liq-pull watch / dead-before-score"
    # forward samples at 1h/6h/24h (+ a 'now' status for history older than 24h, refreshed every 6h)
    due = []
    for m, r in st.items():
        t0 = r.get("t0") or NOW
        for h, s in (("1h", 3600), ("6h", 21600), ("24h", 86400)):
            if h not in r and NOW - t0 >= s and NOW - t0 < s + 3 * 3600: due.append(m)
        if NOW - t0 > 86400 and NOW - (r.get("now_t") or 0) > 6 * 3600: due.append(m)
    due = list(dict.fromkeys(due))[:900]
    snap = ds(due) if due else {}
    for m in due:
        r = st[m]; x = snap.get(m)
        if not x: continue
        t0 = r.get("t0") or NOW; p0 = r.get("p0") or 0
        smp = {"t": round(NOW), "missing": True} if x.get("missing") else {"t": round(NOW), "price": x["price"], "liq": round(x["liq"]), "chg_pct": round((x["price"] / p0 - 1) * 100, 1) if p0 else None}
        for h, s in (("1h", 3600), ("6h", 21600), ("24h", 86400)):
            if h not in r and s <= NOW - t0 < s + 3 * 3600: r[h] = smp
        if NOW - t0 > 86400: r["now"] = smp; r["now_t"] = NOW
        if smp.get("missing") or (smp.get("liq") is not None and smp["liq"] < DEAD_LIQ): r["dead_seen"] = True
    with open(LOG + ".tmp", "w") as f:
        for r in st.values(): f.write(json.dumps(r) + "\n")
    os.replace(LOG + ".tmp", LOG)
    # labels: bad = confirmed pull/dead-before-score OR liq < $1k / delisted at a later sample; good = alive at 24h+ sample
    lab = {}
    for m, r in st.items():
        last = r.get("now") or r.get("24h")
        if r.get("rugged") or r.get("dead_seen"): lab[m] = 1
        elif last and not last.get("missing") and (last.get("liq") or 0) >= DEAD_LIQ: lab[m] = 0
    rows = [st[m] for m in lab]
    base = sum(lab.values()) / max(len(lab), 1)
    stats = {}
    for r in rows:
        y = lab[r["mint"]]
        for n, s in (r.get("flags") or {}).items():
            b = stats.setdefault(n, {})
            k = "FLAG" if s in ("FAIL", "WARN") else "OK" if s == "PASS" else None
            if k: c = b.setdefault(k, [0, 0]); c[0] += 1; c[1] += y
            if s == "FAIL": c = b.setdefault("FAIL", [0, 0]); c[0] += 1; c[1] += y
    span_d = (NOW - min((r.get("t0") or NOW) for r in rows)) / 86400 if rows else 0
    fwd = sum(1 for r in st.values() if "24h" in r)
    L = ["# Rule stats - outcome learning (info/risk only, not advice)", f"Updated {et(NOW)}. Labeled coins: {len(lab)} "
         f"({sum(lab.values())} dead/pulled, {len(lab) - sum(lab.values())} still alive). Base dead rate {base * 100:.1f}%. Forward 24h samples so far: {fwd}.", "",
         "**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. "
         "Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.", "",
         "| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |", "|---|---|---|---|---|---|"]
    sugg = []
    for n in sorted(stats, key=lambda x: int(x) if x.isdigit() else 999):
        f = stats[n].get("FLAG", [0, 0]); o = stats[n].get("OK", [0, 0])
        if not f[0]: continue
        pr = f[1] / f[0]; po = o[1] / o[0] if o[0] else None
        L.append(f"| {n} | {f[0]} | {pr * 100:.0f}% | {f[0] - f[1]} ({(1 - pr) * 100:.0f}%) | {'n/a' if po is None else f'{po * 100:.0f}% of {o[0]}'} | {pr - base:+.0%} |")
        if f[0] >= 30 and o[0] >= 30:
            if pr <= base + 0.03: sugg.append({"check": n, "suggest": "lower weight: flagged coins die no more often than average", "precision": round(pr, 3), "n": f[0], "base": round(base, 3)})
            elif pr >= base + 0.20 and stats[n].get("FAIL", [0])[0] < f[0]: sugg.append({"check": n, "suggest": "consider treating WARN like FAIL: strong lift", "precision": round(pr, 3), "n": f[0], "base": round(base, 3)})
    L += ["", "## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)"]
    if span_d < 7: L.append(f"_Data span {span_d:.1f} days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._")
    old = {(s.get("check"), s.get("suggest")) for s in jl(P("bar_changes.jsonl")) if NOW - (s.get("t") or 0) < 86400}
    for s in sugg:
        L.append(f"- check #{s['check']}: {s['suggest']} (precision {s['precision'] * 100:.0f}% vs base {s['base'] * 100:.0f}%, n={s['n']})")
        if (s["check"], s["suggest"]) not in old:
            open(P("bar_changes.jsonl"), "a").write(json.dumps({"t": round(NOW), "time_et": et(NOW), "src": "learn.py rule stats", "auto_applied": False,
                                                                 "provisional": fwd < 50 or span_d < 7, **s}) + "\n")
    if not sugg: L.append("- none yet (needs n>=30 flagged and n>=30 passing per check)")
    open(P("alerts", "rule_stats.md"), "w").write("\n".join(L) + "\n")
    print(f"outcomes: {len(st)} coins logged, {len(due)} sampled, {len(lab)} labeled, {len(sugg)} suggestions")
    return st, lab


# ------------------------------------------------------------------ 2. operator-network scoring
def network(st=None):
    idx = (jload(P("operator_index.json"), {}) or {}).get("coins", {})
    rugged = {r["mint"]: r.get("detected_et") for r in jl(P("rug_times.jsonl"))}
    for r in (st or {}).values():
        if r.get("rugged") or r.get("dead_seen"): rugged.setdefault(r["mint"], "dead at later sample")
    # wallets in too many coins are routers/exchanges/bots, not an operator: ignore them
    cnt = {}
    for c in idx.values():
        for w in {c.get("creator"), c.get("creator_funder"), *(c.get("funders") or []), *(c.get("hubs") or [])} - {None, ""}: cnt[w] = cnt.get(w, 0) + 1
    try:
        import helius_checks as _hc; EXW = set(_hc.KNOWN_CEX)
    except Exception:
        EXW = set((jload(P("exchange_wallets.json"), {}) or {}).get("wallets", {}))
    w2r = {}
    for m in rugged:
        c = idx.get(m)
        if not c: continue
        for role, ws in (("creator", [c.get("creator")]), ("creator funder", [c.get("creator_funder")]), ("funder", c.get("funders") or []), ("hub", c.get("hubs") or [])):
            for w in ws:
                if w and w not in EXW and cnt.get(w, 0) <= 40: w2r.setdefault(w, {})[m] = (role, c.get("ticker"))
    for w in (jload(P("rug_funders.json"), {}) or {}).get("wallets", []):
        a = w.get("address") if isinstance(w, dict) else None
        if a and a not in EXW and str(w.get("confidence", w.get("level", ""))).lower() == "high": w2r.setdefault(a, {}).setdefault("_rug_list", ("rug-list (high)", w.get("label")))
    live = {m for m, c in idx.items() if NOW - (ts(c.get("t")) or 0) < 7 * 86400}
    wl = jload(P("liq_watchlist.json"), {})
    live |= set((wl.get("coins") if isinstance(wl, dict) and isinstance(wl.get("coins"), dict) else wl if isinstance(wl, dict) else {}) or {})
    out = {}
    for m in live:
        c = idx.get(m)
        if not c or m in rugged: continue
        hits = []
        for role, ws in (("creator", [c.get("creator")]), ("creator funder", [c.get("creator_funder")]), ("funder", c.get("funders") or []), ("hub", c.get("hubs") or [])):
            for w in ws:
                for rm, (rrole, rt) in (w2r.get(w) or {}).items():
                    if rm != m: hits.append({"wallet": w, "role": role, "rug_mint": None if rm == "_rug_list" else rm, "rug_ticker": rt, "rug_role": rrole})
        rms = {h["rug_mint"] for h in hits if h["rug_mint"]}
        if not rms: continue                      # rug-list membership alone is already scored elsewhere
        pen = min(30, 10 * len(rms) + (5 if any(h["role"] in ("creator", "creator funder") for h in hits) else 0))
        out[m] = {"ticker": c.get("ticker"), "penalty": pen, "rugged_coins": sorted(rms)[:10], "n_rugged": len(rms),
                  "via": hits[:6], "updated_et": et(NOW),
                  "note": f"linked to rugged network (lead, not proof): shares {hits[0]['role']} wallet {hits[0]['wallet']} with {len(rms)} rugged coin(s) e.g. {hits[0]['rug_ticker'] or ''} {sorted(rms)[0]}; network penalty +{pen}"}
    jsave(P("network_penalty.json"), {"_note": "Penalties for live/watched coins sharing creator/funder/hub wallets with confirmed rugs. Leads, not proof. Built by learn.py.", "updated_et": et(NOW), "coins": out})
    print(f"network: {len(rugged)} rugged, {len(w2r)} linked wallets, {len(out)} live coins penalised")
    return out


# ------------------------------------------------------------------ 3. paper book (SIMULATION)
SIZE, TP, SL, MAXH = 25.0, 1.0, -0.5, 24 * 3600


def paper():
    LOG = P("alerts", "paper_book.jsonl")
    book = {r["mint"]: r for r in jl(LOG)}
    cands = {}
    for r in jl(P("alerts.jsonl"))[-3000:]:
        t = ts(r.get("ts"))
        if r.get("mint") and r.get("verdict") and r.get("verdict") != "SKIP" and t and NOW - t < 2 * 3600 and r.get("type") in ("new_launch_scored", "clean_mover", "smart_pile_in", "smart_money_buy"):
            cands[r["mint"]] = (r.get("ticker"), r.get("type"), r.get("verdict"), r.get("risk"))
    for r in jl(P("score_log.jsonl"))[-2000:]:
        t = ts(r.get("time"))
        if r.get("mint") and r.get("verdict") not in (None, "SKIP") and t and NOW - t < 2 * 3600: cands.setdefault(r["mint"], (r.get("ticker"), "scored_" + str(r.get("src")), r.get("verdict"), r.get("risk")))
    for m, r in (jload(P("scored.json"), {}) or {}).items() if isinstance(jload(P("scored.json"), {}), dict) else []:
        if isinstance(r, dict) and r.get("verdict") not in (None, "SKIP") and NOW - float(r.get("t") or 0) < 2 * 3600: cands.setdefault(m, (r.get("ticker"), "actions_scored", r.get("verdict"), r.get("risk")))
    new = [m for m in cands if m not in book][:15]
    opn = [m for m, b in book.items() if b.get("status") == "open"]
    snap = ds(new + opn) if (new or opn) else {}
    try:
        sys.path.insert(0, HERE); import profit
    except Exception: profit = None
    for m in new:
        x = snap.get(m) or {}
        if x.get("missing") or not x.get("price"): continue
        ok, why = profit.sellable(m) if profit else (False, "Jupiter gate unavailable")
        if not ok or "unavailable" in why: book[m] = {"mint": m, "status": "not_opened", "why": why, "t": round(NOW)}; continue
        tk, typ, v, rk = cands[m]
        book[m] = {"mint": m, "ticker": tk, "alert_type": typ, "verdict": v, "risk": rk, "status": "open", "size_usd": SIZE, "entry": x["price"],
                   "t_open": round(NOW), "open_et": et(NOW), "gate": why, "peak": x["price"]}
    for m in opn:
        b = book[m]; x = snap.get(m) or {}
        if not x: continue
        px = 0.0 if x.get("missing") or (x.get("liq") or 0) < DEAD_LIQ else x["price"]
        b["peak"] = max(b.get("peak") or 0, px); r = px / b["entry"] - 1 if b["entry"] else -1
        why = "take profit +100%" if r >= TP else "stop -50%" if r <= SL else "24h time exit" if NOW - b["t_open"] >= MAXH else None
        if px == 0: why = "pool dead/delisted (-100%)"
        b["last"], b["ret"] = px, round(r, 4)
        if why: b.update({"status": "closed", "exit": px, "t_close": round(NOW), "close_et": et(NOW), "exit_why": why, "pnl_usd": round(SIZE * r, 2)})
    with open(LOG + ".tmp", "w") as f:
        for b in book.values(): f.write(json.dumps(b) + "\n")
    os.replace(LOG + ".tmp", LOG)
    cl = [b for b in book.values() if b.get("status") == "closed"]; op = [b for b in book.values() if b.get("status") == "open"]
    wins = [b for b in cl if b["pnl_usd"] > 0]
    L = ["# Paper book - SIMULATION ONLY, not advice, no real trades", f"Updated {et(NOW)}. Rules: ${SIZE:.0f} simulated entry at the DEX Screener price when a non-SKIP alert passes the Jupiter $25 sell-back gate; "
         "exit at +100%, -50%, or 24h, checked every run (~10 min), so real fills would differ (slippage, fees, gaps past the stop). Dead pool = -100%.", "",
         f"Closed: {len(cl)} | Open: {len(op)} | Not opened (failed sell gate): {sum(1 for b in book.values() if b.get('status') == 'not_opened')}"]
    if cl:
        tot = sum(b["pnl_usd"] for b in cl)
        L.append(f"Win rate {len(wins) / len(cl) * 100:.0f}% | avg return {sum(b['ret'] for b in cl) / len(cl) * 100:+.1f}% | expectancy ${tot / len(cl):+.2f} per ${SIZE:.0f} trade | total ${tot:+.2f}")
    else: L.append("No closed simulated trades yet - stats appear once positions exit.")
    L += ["", "| ticker | CA | type | verdict | opened | status | return |", "|---|---|---|---|---|---|---|"]
    for b in sorted([b for b in book.values() if b.get("status") in ("open", "closed")], key=lambda b: -b["t_open"])[:50]:
        L.append(f"| {b.get('ticker')} | [`{b['mint']}`]({link(b['mint'])}) | {b.get('alert_type')} | {b.get('verdict')} | {b['open_et']} | {b['status']}{' (' + b['exit_why'] + ')' if b.get('exit_why') else ''} | {b.get('ret', 0) * 100:+.1f}% |")
    open(P("alerts", "paper_book.md"), "w").write("\n".join(L) + "\n")
    print(f"paper: {len(new)} candidates, {len(op)} open, {len(cl)} closed")


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "all"
    st = None
    if c in ("outcomes", "all"): st, _ = outcomes()
    if c in ("network", "all"): network(st)
    if c in ("paper", "all"): paper()
