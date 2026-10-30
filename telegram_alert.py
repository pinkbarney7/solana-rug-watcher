#!/usr/bin/env python3
"""Telegram backup alerts from GitHub Actions. Information and risk only - never buy advice.
Sends only when (Actions mode == helius OR box heartbeat stale > BOX_FRESH_MIN) AND the alert meets the standing bar.
Skips silently if TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID are unset. Dedup 24h via sent_alerts.json. Never exits non-zero.
Bar on Actions: rug-list launch with traction (liq>=$20k or mcap>=$100k), clean mover risk<=40, source outage (GeckoTerminal down),
2+ smart wallets. Liquidity pulls are NOT sent from Actions (only one confirmed source there); funding bursts live on the box daemon."""
import json, os, sys, time, datetime, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
SENT = os.path.join(HERE, "sent_alerts.json"); HB_BOX = os.path.join(HERE, "heartbeat.json")
FRESH = int(os.environ.get("BOX_FRESH_MIN", "20"))

def link(m): return f"https://pump.fun/coin/{m}" if m.endswith("pump") else f"https://dexscreener.com/solana/{m}"

def box_age():
    try: return (time.time() - float(json.load(open(HB_BOX))["ts_epoch"])) / 60
    except Exception: return None

def candidates(since, stats):
    out = []
    if stats.get("gt_down"):
        out.append(("outage:gt:" + datetime.date.today().isoformat(), "Data source outage: GeckoTerminal is down. Unique-buyer checks are off and liquidity drops can't be confirmed by a second source."))
    p = os.path.join(HERE, "check_log.jsonl")
    if not os.path.exists(p): return out
    for l in open(p):
        try: r = json.loads(l)
        except Exception: continue
        try: t = datetime.datetime.fromisoformat(str(r["time"]).replace("Z", "+00:00")).timestamp()
        except Exception: continue
        if t < since or not r.get("mint"): continue
        m, risk, liq, mcap = r["mint"], r.get("risk"), r.get("liq") or 0, r.get("mcap") or 0
        ck = {c["n"]: c["s"] for c in r.get("checks") or []}
        sm = next((c["v"] for c in r.get("checks") or [] if c["n"].startswith("Smart-money")), "")
        head = f"{r.get('ticker')} - risk {risk}/100, {r.get('verdict')}. Liq ${liq:,.0f}, mcap ${mcap:,.0f}.\nCA: {m}\n{link(m)}"
        if ck.get("Known rug-funder link") == "FAIL" and (liq >= 20000 or mcap >= 100000):
            out.append((f"ruglaunch:{m}", "Rug-list wallet launch with traction: " + head + "\nWallet links are leads, not proof."))
        elif risk is not None and risk <= 40 and not r.get("incomplete"):
            out.append((f"clean:{m}", "Clean mover (fewer red flags, NOT safe): " + head))
        import re
        n = re.search(r"(\d+)\s+smart", sm or "")
        if n and int(n.group(1)) >= 2:
            out.append((f"smart:{m}", f"{n.group(1)} smart wallets bought the same coin: " + head + "\nWallet links are leads, not proof."))
    return out

def main():
    tok, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not tok or not chat: print("telegram: secrets not set - skipping"); return
    mode = sys.argv[1] if len(sys.argv) > 1 else "free"; age = box_age()
    if not (mode == "helius" or age is None or age > FRESH): print(f"telegram: box healthy ({age:.0f} min) - box handles alerts"); return
    try: stats = json.load(open(os.path.join(HERE, "out", "run_stats.json")))
    except Exception: stats = {}
    since = float(os.environ.get("RUN_START_EPOCH") or time.time() - 900)
    try: sent = json.load(open(SENT))
    except Exception: sent = {}
    now = time.time(); sent = {k: v for k, v in sent.items() if now - v < 86400}
    n = 0
    for key, txt in candidates(since, stats):
        if key in sent or n >= 5: continue
        body = "[Backup watcher - GitHub] " + txt + "\nInfo/risk only, not advice."
        try:
            urllib.request.urlopen(urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendMessage",
                data=urllib.parse.urlencode({"chat_id": chat, "text": body, "disable_web_page_preview": "true"}).encode()), timeout=15)
            sent[key] = now; n += 1
        except Exception as e: print("telegram send failed:", type(e).__name__)
    json.dump(sent, open(SENT, "w"), indent=0); print(f"telegram: sent {n}")

if __name__ == "__main__":
    try: main()
    except Exception as e: print("telegram: error", type(e).__name__)
