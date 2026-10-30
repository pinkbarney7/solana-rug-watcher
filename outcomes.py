#!/usr/bin/env python3
"""Free outcome tracker (DEX Screener only, no Helius).
For coins scored in the last ~30h (score_log.jsonl + scored.json) record price/liq at ~1h/6h/24h after first score.
Writes alerts/outcomes.jsonl (state) and alerts/outcomes.md (summary by verdict)."""
import json, os, time, datetime, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_J = os.path.join(HERE, "alerts", "outcomes.jsonl"); OUT_M = os.path.join(HERE, "alerts", "outcomes.md")
HORIZONS = {"1h": 3600, "6h": 6 * 3600, "24h": 24 * 3600}; WIN = 900  # sample once inside [h, h+window) or later if missed

def ts(s):
    try: return datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()
    except Exception: return None

def ds(mints):
    out = {}
    for i in range(0, len(mints), 30):
        try:
            req = urllib.request.Request("https://api.dexscreener.com/tokens/v1/solana/" + ",".join(mints[i:i + 30]), headers={"User-Agent": "rug-watcher"})
            for p in json.load(urllib.request.urlopen(req, timeout=20)) or []:
                m = p["baseToken"]["address"]; liq = (p.get("liquidity") or {}).get("usd") or 0
                if m not in out or liq > out[m]["liq"]: out[m] = {"price": float(p.get("priceUsd") or 0), "liq": liq, "mcap": p.get("marketCap") or p.get("fdv")}
        except Exception as e: print("dexscreener error:", type(e).__name__)
        time.sleep(1)
    return out

def main():
    st = {}
    if os.path.exists(OUT_J):
        for l in open(OUT_J):
            try: r = json.loads(l); st[r["mint"]] = r
            except Exception: pass
    now = time.time()
    for path in ("score_log.jsonl",):
        p = os.path.join(HERE, path)
        if not os.path.exists(p): continue
        for l in open(p):
            try: r = json.loads(l)
            except Exception: continue
            t = ts(r.get("time")); m = r.get("mint")
            if not m or not t or now - t > 30 * 3600 or m in st: continue
            st[m] = {"mint": m, "ticker": r.get("ticker"), "t0": t, "verdict": r.get("verdict"), "risk": r.get("risk"),
                     "p0": r.get("price"), "liq0": r.get("liq"), "mcap0": r.get("mcap")}
    st = {m: r for m, r in st.items() if now - r["t0"] < 26 * 3600}
    due = [m for m, r in st.items() for h, s in HORIZONS.items() if h not in r and now - r["t0"] >= s]
    snap = ds(sorted(set(due))) if due else {}
    for m, r in st.items():
        for h, s in HORIZONS.items():
            if h not in r and now - r["t0"] >= s and m in snap:
                x = snap[m]; p0, l0 = r.get("p0") or 0, r.get("liq0") or 0
                r[h] = {"price": x["price"], "liq": x["liq"], "chg_pct": round((x["price"] / p0 - 1) * 100, 1) if p0 else None,
                        "liq_chg_pct": round((x["liq"] / l0 - 1) * 100, 1) if l0 else None, "late_min": round((now - r["t0"] - s) / 60)}
            elif h not in r and now - r["t0"] >= s + 3 * 3600 and m not in snap:
                r[h] = {"missing": True}  # delisted / no pairs = likely dead
    os.makedirs(os.path.dirname(OUT_J), exist_ok=True)
    with open(OUT_J, "w") as f:
        for r in st.values(): f.write(json.dumps(r) + "\n")
    L = ["# Outcomes (DEX Screener, free) - " + datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
         "", "Price/liquidity change after first score. Info only; a low risk score means fewer red flags, not safe.", "",
         "| verdict | horizon | n | median price chg | dead (liq<$1k or delisted) |", "|---|---|---|---|---|"]
    for v in sorted({r.get("verdict") for r in st.values()} - {None}):
        for h in HORIZONS:
            xs = [r[h] for r in st.values() if r.get("verdict") == v and h in r]
            if not xs: continue
            ch = sorted(x["chg_pct"] for x in xs if x.get("chg_pct") is not None)
            dead = sum(1 for x in xs if x.get("missing") or (x.get("liq") or 0) < 1000)
            L.append(f"| {v} | {h} | {len(xs)} | {ch[len(ch)//2] if ch else 'n/a'}% | {dead} |")
    L += ["", "| ticker | CA | verdict | risk | 1h | 6h | 24h |", "|---|---|---|---|---|---|---|"]
    f = lambda x: "-" if not x else ("delisted" if x.get("missing") else f"{x.get('chg_pct')}% / liq ${x.get('liq', 0):,.0f}")
    for r in sorted(st.values(), key=lambda r: -r["t0"])[:60]:
        L.append(f"| {r.get('ticker')} | `{r['mint']}` | {r.get('verdict')} | {r.get('risk')} | {f(r.get('1h'))} | {f(r.get('6h'))} | {f(r.get('24h'))} |")
    open(OUT_M, "w").write("\n".join(L) + "\n")
    print(f"outcomes: tracking {len(st)}, sampled {len(snap)}")

if __name__ == "__main__": main()
