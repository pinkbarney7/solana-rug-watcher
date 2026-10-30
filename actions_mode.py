#!/usr/bin/env python3
"""Decide this Actions run's mode and keep the daily Actions Helius budget.
  python3 actions_mode.py decide            -> prints mode=helius|free + reason (GITHUB_OUTPUT format)
  python3 actions_mode.py record out/run_stats.json mode -> adds credits to actions_budget.json, writes alerts/actions_heartbeat.json
Rules: box heartbeat.json fresh (< BOX_FRESH_MIN, default 20 min) -> free-only (the box daemon covers Helius work).
Box heartbeat missing/stale -> Helius scoring allowed until ACTIONS_DAILY_CAP (default 3000) credits/day (ET) are used,
keeping RUN_RESERVE (default 400) headroom for one run; then free-only, results labelled UNVERIFIED."""
import datetime, json, os, sys, time
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__))
BUDGET = os.path.join(HERE, "actions_budget.json")
HB_BOX = os.path.join(HERE, "heartbeat.json")
HB_ACT = os.path.join(HERE, "alerts", "actions_heartbeat.json")
CAP = int(os.environ.get("ACTIONS_DAILY_CAP", "3000"))
RESERVE = int(os.environ.get("RUN_RESERVE", "400"))
FRESH = int(os.environ.get("BOX_FRESH_MIN", "20"))
today = lambda: datetime.datetime.now(ZoneInfo("America/New_York")).date().isoformat()

def budget():
    try: b = json.load(open(BUDGET))
    except Exception: b = {}
    if b.get("day") != today(): b = {"day": today(), "cap": CAP, "used": 0, "runs": 0, "helius_runs": 0}
    b["cap"] = CAP; return b

def box_age_min():
    try: return (time.time() - float(json.load(open(HB_BOX))["ts_epoch"])) / 60
    except Exception: return None

def decide():
    b = budget(); age = box_age_min()
    if age is not None and age < FRESH: mode, why = "free", f"box heartbeat {age:.0f} min old (fresh) - box covers Helius"
    elif b["used"] + RESERVE > b["cap"]: mode, why = "free", f"Actions Helius budget spent ({b['used']}/{b['cap']} today)"
    else: mode, why = "helius", ("box heartbeat missing" if age is None else f"box heartbeat stale ({age:.0f} min)") + f"; budget {b['used']}/{b['cap']}"
    print(f"mode={mode}"); print(f"reason={why}"); print(f"box_age_min={'' if age is None else round(age)}")

def record(stats_path, mode):
    b = budget()
    try: st = json.load(open(stats_path))
    except Exception: st = {}
    cr = int(st.get("credits_est") or 0) if mode == "helius" else 0
    b["used"] += cr; b["runs"] += 1; b["helius_runs"] += mode == "helius"
    json.dump(b, open(BUDGET, "w"), indent=1)
    os.makedirs(os.path.dirname(HB_ACT), exist_ok=True)
    age = box_age_min()
    json.dump({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "ts_epoch": int(time.time()),
               "mode": mode, "helius_used": mode == "helius", "credits_this_run": cr, "credits_today": b["used"], "cap": b["cap"],
               "gt_down": st.get("gt_down"), "scored": st.get("scored"), "reused": st.get("reused"),
               "box_heartbeat_age_min": None if age is None else round(age, 1), "run_ok": bool(st)}, open(HB_ACT, "w"), indent=1)
    print(f"recorded {cr} credits ({mode}); today {b['used']}/{b['cap']}")

if __name__ == "__main__":
    if sys.argv[1] == "decide": decide()
    else: record(sys.argv[2], sys.argv[3])
