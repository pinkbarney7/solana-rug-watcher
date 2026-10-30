#!/usr/bin/env python3
"""Write status.md: box + Actions heartbeat ages and today's Actions Helius spend."""
import json, os, time, datetime
H = os.path.dirname(os.path.abspath(__file__))
def j(p):
    try: return json.load(open(os.path.join(H, p)))
    except Exception: return {}
box, act, b = j("heartbeat.json"), j("alerts/actions_heartbeat.json"), j("actions_budget.json")
age = lambda d: f"{(time.time() - float(d['ts_epoch'])) / 60:.0f} min" if d.get("ts_epoch") else "never"
L = [f"# Watcher status ({datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M UTC})", "",
     f"- Box heartbeat age: {age(box)} (realtime running: {box.get('realtime_running')}, box Helius {box.get('credits_today')}/{box.get('credit_cap')})",
     f"- Actions heartbeat age: {age(act)} (last mode: {act.get('mode')}, GeckoTerminal down: {act.get('gt_down')})",
     f"- Actions Helius today: {b.get('used', 0)}/{b.get('cap')} credits over {b.get('runs', 0)} runs ({b.get('helius_runs', 0)} used Helius)", ""]
open(os.path.join(H, "status.md"), "w").write("\n".join(L)); print("\n".join(L))
