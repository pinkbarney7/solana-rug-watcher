#!/usr/bin/env python3
"""Helius credit reserve for a trading-session window (read-only helper: reads credit_ledger.jsonl and
realtime_status.json, makes no API calls). Config: credit_reserve.json (read live; no restart needed).

  python3 credit_reserve.py status          # used today, reserve, what batch jobs / the daemon may spend now

Before a window (same ET day): batch jobs (fast_scan, wallet_discovery, smart_money, learn_rugs, wallet_watch) refuse to
start once box-wide usage + reserve would exceed plan_daily, and the daemon's cap is lowered by daemon_reserve (its
auto-scores stop earlier; websocket watching continues). Inside the window: full budgets; batch jobs still refuse if
fewer than batch_min_left credits are left for the day. ca_check.py (manual checks) is never blocked; it shows the state.
All numbers are estimates from our own ledger, not Helius billing data."""
import datetime, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(HERE, "credit_reserve.json")
LEDGER = os.environ.get("CR_LEDGER") or os.path.join(HERE, "credit_ledger.jsonl")   # CR_* overrides: tests only
STATUS = os.environ.get("CR_STATUS") or os.path.join(HERE, "realtime_status.json")
HELIUS_JOBS = {"smart_early", "fast_scan", "wallet_discovery", "smart_money", "learn_rugs", "wallet_watch"}
_c = {"m": None, "d": None}
_u = {"t": 0, "v": 0.0}


def now_et():
    if os.environ.get("CR_NOW"): return datetime.datetime.fromisoformat(os.environ["CR_NOW"]).astimezone()
    return datetime.datetime.now().astimezone()


def conf():
    try:
        m = os.path.getmtime(CONF)
        if _c["m"] != m: _c["d"] = json.load(open(CONF)); _c["m"] = m
    except (OSError, ValueError):
        _c["d"] = None; _c["m"] = None
    return _c["d"] or {}


def state(t=None):
    """{'phase': None|'before'|'in'|'after', 'window': {...}, 'start': dt, 'end': dt} for today's (ET) window."""
    t = t or now_et()
    for w in conf().get("windows") or []:
        if w.get("date") != t.date().isoformat(): continue
        try:
            s = datetime.datetime.fromisoformat(f"{w['date']}T{w['start']}").astimezone()
            e = datetime.datetime.fromisoformat(f"{w['date']}T{w['end']}").astimezone()
        except (KeyError, ValueError):
            continue
        ph = "before" if t < s else ("in" if t < e else "after")
        if ph == "after": continue
        return {"phase": ph, "window": w, "start": s, "end": e}
    return {"phase": None, "window": None}


def used_today(cache_s=60):
    """Estimated Helius credits used box-wide today (ET): ledger + the daemon's not-yet-flushed current hour."""
    if time.time() - _u["t"] < cache_s: return _u["v"]
    day = now_et().date().isoformat(); tot = 0.0
    try:
        with open(LEDGER) as f:
            for line in f:
                if not line.startswith('{"ts": "' + day): continue
                try: tot += float(json.loads(line).get("credits") or 0)
                except ValueError: pass
    except OSError:
        pass
    try:
        s = json.load(open(STATUS))
        hk = now_et().strftime("%Y-%m-%dT%H")
        for k, v in ((s.get("hour_credits") or {}).get(hk) or {}).items():
            if k != "score_credits": tot += float(v or 0)
    except (OSError, ValueError, AttributeError):
        pass
    _u.update(t=time.time(), v=tot)
    return tot


def plan():
    return float(conf().get("plan_daily") or 33000)


def daemon_cap(base, daemon_today=None):
    """Effective daily cap for the realtime daemon right now."""
    st = state()
    if st["phase"] != "before": return base
    w = st["window"]; cap = base - float(w.get("daemon_reserve") or 0)
    if daemon_today is not None:     # also never let the daemon push box-wide usage into the session reserve
        left = plan() - float(w.get("reserve") or 0) - used_today()
        cap = min(cap, daemon_today + max(left, 0))
    return max(cap, 0)


def batch_ok(name, est=0):
    """(ok, message) for a credit-using batch job. SC_IGNORE_RESERVE=1 overrides."""
    if name not in HELIUS_JOBS or os.environ.get("SC_IGNORE_RESERVE"): return True, ""
    st = state()
    if not st["phase"]: return True, ""
    w = st["window"]; u = used_today(cache_s=0); p = plan()
    if st["phase"] == "before":
        r = float(w.get("reserve") or 0)
        if u + est + r > p:
            return False, (f"credit reserve: ~{u:,.0f} of ~{p:,.0f} credits used today and {r:,.0f} are held for "
                           f"{w.get('label', 'the session')} ({w['start']}-{w['end']} ET); not starting {name} (SC_IGNORE_RESERVE=1 overrides)")
    else:
        mn = float(w.get("batch_min_left") or 0)
        if p - u - est < mn:
            return False, (f"credit reserve: session window open ({w['start']}-{w['end']} ET) and only ~{p - u:,.0f} credits left today "
                           f"(batch jobs need {mn:,.0f}); not starting {name} (SC_IGNORE_RESERVE=1 overrides)")
    return True, ""


def summary():
    st = state(); u = used_today(cache_s=0); p = plan()
    L = [f"Helius credits used today (box-wide estimate): ~{u:,.0f} of ~{p:,.0f} (~{p - u:,.0f} left)"]
    if not st["phase"]:
        L.append("credit reserve: no active window today")
    else:
        w = st["window"]
        L.append(f"credit reserve: {w.get('label', '')} {w['start']}-{w['end']} ET - phase {st['phase'].upper()}; "
                 f"reserve {float(w.get('reserve') or 0):,.0f}, daemon_reserve {float(w.get('daemon_reserve') or 0):,.0f}")
        ok, msg = batch_ok("fast_scan")
        L.append("batch jobs: " + ("allowed now" if ok else "BLOCKED - " + msg))
    return "\n".join(L)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        print(summary())
        try:
            s = json.load(open(STATUS))
            print(f"daemon: ~{s.get('credits_today', 0):,.0f} today; base cap {s.get('daily_credit_cap')}, effective cap now "
                  f"{s.get('effective_credit_cap', s.get('daily_credit_cap'))} (paused={s.get('paused_helius')})")
        except (OSError, ValueError):
            pass
    else:
        print(__doc__)
