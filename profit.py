#!/usr/bin/env python3
"""Free profitability gates (info/risk only - never a buy signal). No secrets used or printed.
  cheap_ok(liq, mc, symbol)        -> (ok, why)  free pre-filter before any Helius scoring
  sellable(mint)                   -> (ok, why)  Jupiter public quote: can $25 be bought AND sold back (hard gate)
  hourly_ok(used_today, daily)     -> (ok, allowance)  paced cumulative Helius allowance with overnight reserve
  family_mute(symbol, mint) / family_muted(symbol) -> copycat-ticker mute for 24 h after a confirmed rug
  rugcheck_liq(mint)               -> float|None  RugCheck free report liquidity (second source when GeckoTerminal is down)
  python3 profit.py digest         -> alerts/outcome_digest.md hit-rate summary + bar_changes.jsonl suggestions
  python3 profit.py status
"""
import datetime, json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
MUTE_F = os.path.join(HERE, "family_mute.json")
BAR_LOG = os.path.join(HERE, "bar_changes.jsonl")
UA = {"User-Agent": "rug-watcher/1.0"}
MUTE_S = 24 * 3600
OVERNIGHT_RESERVE = float(os.environ.get("PF_OVERNIGHT_RESERVE", "0.15"))   # 15% of the day kept for 00-08 ET
HOURLY_SLACK = float(os.environ.get("PF_HOURLY_SLACK", "1500"))             # burst room above the paced line


def _get(url, timeout=15):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout))
    except Exception:
        return None


def cheap_ok(liq, mc, symbol=None):
    liq = float(liq or 0); mc = float(mc or 0)
    if family_muted(symbol): return False, f"ticker family '{norm(symbol)}' muted 24h after a confirmed rug"
    if mc and liq / mc < 0.01: return False, f"liq/mcap {liq / mc * 100:.2f}% (manufactured cap)"
    if liq < 20000: return False, f"liquidity ${liq:,.0f} < $20k"
    return True, "ok"


def sellable(mint):
    try:
        sys.path.insert(0, HERE); import exit_liq
        R = exit_liq.test(mint); st, val, _ = exit_liq.grade(R)
        return st != "FAIL", f"Jupiter exit test {st}: {val}"
    except Exception as e:
        return True, f"Jupiter check unavailable ({type(e).__name__}) - not gated"


def hourly_ok(used, daily):
    now = datetime.datetime.now().astimezone(); h = now.hour + now.minute / 60
    night = daily * OVERNIGHT_RESERVE
    allow = night * h / 8 if h < 8 else night + (daily - night) * (h - 8) / 16   # paced so nothing runs out before midnight
    allow = min(daily, allow + HOURLY_SLACK)
    return used < allow, round(allow)


def norm(s):
    s = re.sub(r"[^A-Z0-9]", "", str(s or "").upper())
    return s


def _mutes():
    try: d = json.load(open(MUTE_F))
    except Exception: d = {}
    t = time.time(); return {k: v for k, v in d.items() if t - v.get("t", 0) < MUTE_S}


def family_mute(symbol, mint, why="confirmed rug"):
    k = norm(symbol)
    if len(k) < 2: return
    d = _mutes(); d[k] = {"t": time.time(), "mint": mint, "why": why}
    tmp = MUTE_F + ".tmp"; json.dump(d, open(tmp, "w")); os.replace(tmp, MUTE_F)


def family_muted(symbol):
    k = norm(symbol); return bool(k) and k in _mutes()


def rugcheck_liq(mint):
    d = _get(f"https://api.rugcheck.xyz/v1/tokens/{mint}/report")
    if not isinstance(d, dict): return None
    v = d.get("totalMarketLiquidity")
    if v is None: v = sum(float(m.get("lp", {}).get("lpLockedUSD") or 0) + float(m.get("lp", {}).get("lpUnlocked") or 0) * 0 for m in d.get("markets") or [])
    try: return float(v)
    except Exception: return None


def digest(path=None):
    """Hit-rate by verdict/alert type from outcomes.jsonl (written by outcomes.py). Suggests (logs, never auto-applies) bar changes."""
    cands = [path] if path else [os.path.join(HERE, "alerts", "outcomes.jsonl"), os.path.join(HERE, "outcomes.jsonl")]
    rows = []
    for p in cands:
        if p and os.path.exists(p):
            rows = [json.loads(l) for l in open(p) if l.strip()]; break
    by = {}
    for r in rows:
        k = r.get("verdict") or r.get("type") or "?"
        for hz in ("1h", "6h", "24h"):
            o = (r.get("samples") or r.get("outcomes") or {}).get(hz)
            if not o: continue
            b = by.setdefault((k, hz), {"n": 0, "dead": 0, "up": 0})
            b["n"] += 1
            ch = o.get("price_chg_pct") if isinstance(o, dict) else None
            liq = o.get("liq") if isinstance(o, dict) else None
            if liq is not None and liq < 5000: b["dead"] += 1
            elif ch is not None and ch > 0: b["up"] += 1
    out = ["# Outcome digest (info/risk only, not advice)", f"Updated {datetime.datetime.now().astimezone():%Y-%m-%d %H:%M %Z}. Coins tracked: {len(rows)}.", "",
           "| verdict | horizon | n | dead (<$5k liq) | up vs first score |", "|---|---|---|---|---|"]
    sugg = []
    for (k, hz), b in sorted(by.items()):
        out.append(f"| {k} | {hz} | {b['n']} | {b['dead']} ({b['dead'] * 100 // max(b['n'], 1)}%) | {b['up']} ({b['up'] * 100 // max(b['n'], 1)}%) |")
        if hz == "24h" and b["n"] >= 10 and k != "SKIP" and b["dead"] / b["n"] > 0.5:
            sugg.append({"t": time.time(), "verdict": k, "suggest": "tighten: >50% of non-SKIP coins dead at 24h", "n": b["n"], "dead": b["dead"]})
    if not by: out.append("| (no samples yet) | | | | |")
    for s in sugg:
        open(BAR_LOG, "a").write(json.dumps(s) + "\n")
    out += ["", "Bar suggestions are logged to bar_changes.jsonl and need a human yes before they change alerting."]
    os.makedirs(os.path.join(HERE, "alerts"), exist_ok=True)
    open(os.path.join(HERE, "alerts", "outcome_digest.md"), "w").write("\n".join(out) + "\n")
    return "\n".join(out)


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "status"
    if c == "digest": print(digest())
    elif c == "sell": print(sellable(sys.argv[2]))
    elif c == "rugcheck": print(rugcheck_liq(sys.argv[2]))
    else: print(json.dumps({"mutes": _mutes(), "hourly_example_16k": hourly_ok(0, 16000)[1]}, indent=1))
