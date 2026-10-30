"""Combined risk score 0-100 (higher = riskier) from the scorecard checks. Info/risk only, not advice.

points = base + per-check FAIL/WARN/UNKNOWN weights + a few continuous terms; score = 100 * (1 - exp(-points / K)).
Weights were calibrated on 2026-10-07 against known rugs (AGENTCAT, PAYR, CODIE, A1, swordinu) and coins that held up
better (HIGGS, fone, Agency) plus the report_card outcomes; see README "Risk score calibration".
"""
import math

BASE = 8
K = 70.0
# check number -> points for FAIL / WARN
# Versioned weights. v1 = calibrated 2026-10-07. v2 (2026-10-09, Barney-approved) re-weights from per-check rug rates
# (report card + check corpus): #1 identity 15->20, #5 age 10->18, #6 top-10 10->5, #9 momentum 10->14,
# #11 Helius holders 12->18, #14 common-funder clusters 28->16, #18 wash 16->8, #13 creator WARN 5->9.
# Every score carries "weights_version"; score(R, version="v1") recomputes the old score for comparison.
WEIGHTS = {
    "v1": ({1: 15, 2: 40, 3: 18, 4: 0, 5: 10, 6: 10, 7: 14, 8: 0, 9: 10, 10: 0, 11: 12, 12: 22, 13: 14, 14: 28, 15: 32, 16: 24, 18: 16, 19: 18},
           {1: 2, 2: 8, 3: 7, 4: 7, 5: 5, 6: 4, 7: 5, 8: 4, 9: 5, 10: 2, 11: 4, 12: 7, 13: 5, 14: 9, 15: 10, 16: 7, 18: 7, 19: 6}),
    "v2": ({1: 20, 2: 40, 3: 18, 4: 0, 5: 18, 6: 5, 7: 14, 8: 0, 9: 14, 10: 0, 11: 18, 12: 22, 13: 14, 14: 16, 15: 32, 16: 24, 18: 8, 19: 18},
           {1: 2, 2: 8, 3: 7, 4: 7, 5: 5, 6: 4, 7: 5, 8: 4, 9: 5, 10: 2, 11: 4, 12: 7, 13: 9, 14: 9, 15: 10, 16: 7, 18: 7, 19: 6}),
}
WEIGHTS_VERSION = "v2"
W_FAIL, W_WARN = WEIGHTS[WEIGHTS_VERSION]
W_UNKNOWN = 3
BANDS = ((80, "extreme"), (60, "high"), (35, "elevated"), (0, "lower (still a meme coin)"))


def _num(x):
    try: return float(x)
    except (TypeError, ValueError): return None


MARKET_STATE = {3, 4, 8, 9, 16}     # checks that mostly describe the coin's current state (excluded in structural mode)


_SIG_CACHE = {"t": 0, "conf": {}}
def _signals(mint):
    """Informational signals shown next to the score; never change it."""
    import time as _t, smart_early, x_signal
    if _t.time() - _SIG_CACHE["t"] > 120: _SIG_CACHE.update(t=_t.time(), conf=smart_early.confluence())
    sig = {}
    ws = _SIG_CACHE["conf"].get(mint)
    if ws: sig["smart_confluence"] = {"wallets": len(ws), "addresses": ws[:5], "note": "2+ smart wallets bought in last 6 h - a lead, not proof"}
    x = x_signal.get(mint)
    if x: sig["x"] = {k: x[k] for k in ("x_score", "real_authors", "posts", "bot_spam", "checked") if k in x}
    return sig


def score(R, structural=False, version=None):
    """R = scorecard result dict (checks, market, helius). Returns {"score", "band", "points", "drivers"}.
    structural=True drops current-market-state terms (liquidity, turnover, momentum, exit quotes) - used only to
    calibrate against outcomes without leaking the outcome (a dead coin has no liquidity) into the score."""
    version = version or WEIGHTS_VERSION
    W_FAIL, W_WARN = WEIGHTS[version]
    contrib = []
    for c in R.get("checks", []):
        n, st = c["n"], c["status"]
        if structural and n in MARKET_STATE: continue
        w_unk = 0 if n in MARKET_STATE or n in (1, 10) else W_UNKNOWN   # missing market data: flag INCOMPLETE, don't add risk
        if "not checked" in (c.get("value") or "") and st == "WARN":
            contrib.append((w_unk, f"#{n} not checked")); continue
        if st == "FAIL" and W_FAIL.get(n): contrib.append((W_FAIL[n], f"#{n} {c['name']} FAIL"))
        elif st == "WARN" and W_WARN.get(n): contrib.append((W_WARN[n], f"#{n} {c['name']} WARN"))
        elif st == "UNKNOWN": contrib.append((w_unk, f"#{n} unknown"))
    m = R.get("market") or {}
    liq, mc = _num(m.get("liq_usd")), _num(m.get("mcap_usd"))
    if liq is not None and not structural:
        if liq < 10000: contrib.append((15, f"liquidity only ${liq:,.0f}"))
        if mc and mc > 0:
            r = liq / mc * 100
            if r < 10: contrib.append((round((10 - r) * 1.2, 1), f"liq/mcap {r:.1f}%"))
    H = R.get("helius") or {}
    E = H.get("early") or []
    got = sum(x.get("got_pct", 0) for x in E)
    grp = max([cl.get("early_got_pct", 0) for cl in H.get("clusters") or [] if not cl.get("exchange_like")] + [0])
    tr = H.get("trace") or {}
    og = (tr.get("operator_group") or {}).get("early_got_pct", 0)
    hub = max([h.get("early_got_pct", 0) for h in tr.get("hubs") or [] if not h.get("is_launch_wallet")] + [0])
    coord = max(grp, og, hub)
    if got > 20: contrib.append((round(min(12, (got - 20) * 0.2), 1), f"launch buyers took {got:.0f}% in slots 0-3"))
    if coord > 10: contrib.append((round(min(14, coord * 0.15), 1), f"linked launch group took {coord:.0f}%"))
    cb = H.get("creator_buy_pct") or 0
    if cb > 20: contrib.append((round(min(8, (cb - 20) * 0.2), 1), f"creator bought {cb:.0f}% itself"))
    n_prior = len([x for x in H.get("creator_created") or [] if x != R.get("mint")])
    if n_prior >= 8: contrib.append((6, f"serial launcher ({n_prior}+ other tokens)"))
    pts = BASE + sum(p for p, _ in contrib)
    s = round(100 * (1 - math.exp(-pts / K)))
    band = next(b for t, b in BANDS if s >= t)
    drivers = [f"{lab} (+{p:g})" for p, lab in sorted(contrib, key=lambda x: -x[0])[:5] if p > 0]
    missing = [lab.split()[0] for p, lab in contrib if lab.endswith("not checked") or lab.endswith("unknown")]
    out = {"score": s, "band": band, "points": round(pts, 1), "drivers": drivers, "weights_version": version}
    if not structural and isinstance(R, dict) and R.get("mint"):
        try: out["signals"] = _signals(R["mint"])        # info only: NOT part of the score (calibrated v2 weights unchanged)
        except Exception: pass
    if len(missing) >= 2:
        out["incomplete"] = missing
        out["band"] = band + f", INCOMPLETE - {len(missing)} checks failed ({', '.join(missing)}); score is a floor, re-run"
    return out
