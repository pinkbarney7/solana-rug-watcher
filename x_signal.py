#!/usr/bin/env python3
"""X (Twitter) mention signal for candidate coins - informational score input, never a gate.

Box scripts cannot call the agent's X tool, so this is a file hook:
  python3 x_signal.py queue            -> x_queue.json: up to 20 candidate mints (passed basic gates), not checked in
                                          the last 6 h, within the daily budget (300 X searches/day, x_budget.json)
  agent: for each queued item, call x.search_posts_all(query=item["query"], max_results=25, sort_order="recency",
         expansions="author_id", user.fields="created_at,public_metrics,verified,description",
         post.fields="created_at,public_metrics,author_id,text") and save the raw result to x_inbox/<mint>.json
  python3 x_signal.py ingest [files]   -> parses x_inbox/*.json (or given files) into x_signal.json, counts budget,
                                          moves processed files to x_inbox/done/
  python3 x_signal.py show [mint]
Scoring: an author is "real" if account age >= 180 d, followers >= 200, and the post is not a retweet / copy of text
seen from other authors. Posts with call/shill wording (Nx, alpha TG, DM, airdrop, "$3K -> $500K MC", ...) count as promo, never real.
bot_spam = >= 60% of posts are retweets, near-identical copies, or promo. x_score 0-100 =
real distinct authors (capped) weighted by their engagement; 0 posts = no buzz (not bad by itself).
"""
import json, os, sys, time, re, glob, datetime, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
Q_F = os.path.join(HERE, "x_queue.json"); OUT_F = os.path.join(HERE, "x_signal.json"); BUD_F = os.path.join(HERE, "x_budget.json")
INBOX = os.path.join(HERE, "x_inbox")
DAILY = 300; PER_QUEUE = 20; RECHECK_S = 6 * 3600

def jload(p, d):
    try: return json.load(open(p))
    except (OSError, ValueError): return d
def jsave(p, o):
    tmp = p + ".tmp"; json.dump(o, open(tmp, "w"), indent=1); os.replace(tmp, p)
def today(): return time.strftime("%Y-%m-%d")
def budget():
    b = jload(BUD_F, {})
    return b if b.get("day") == today() else {"day": today(), "used": 0}

def candidates():
    """mints that passed the basic gates recently: survivors with structural_ok, clean-candidate rows not SKIP (12 h)."""
    out = {}
    for c in jload(os.path.join(HERE, "survivors.json"), {}).get("coins", []):
        if c.get("structural_ok"): out[c["mint"]] = c.get("ticker") or ""
    cut = datetime.datetime.now().astimezone() - datetime.timedelta(hours=12)
    try:
        for l in open(os.path.join(HERE, "clean_shadow.jsonl")).readlines()[-3000:]:
            try: r = json.loads(l)
            except ValueError: continue
            if r.get("verdict") != "SKIP" and datetime.datetime.fromisoformat(r["time"]) > cut: out[r["mint"]] = r.get("ticker") or ""
    except OSError: pass
    return out

def queue():
    b = budget(); S = jload(OUT_F, {}); left = DAILY - b["used"]
    items = []
    for m, tk in candidates().items():
        if len(items) >= min(PER_QUEUE, left): break
        if time.time() - (S.get(m) or {}).get("t", 0) < RECHECK_S: continue
        tk = re.sub(r"[^A-Za-z0-9]", "", tk)
        items.append({"mint": m, "ticker": tk, "query": f"{m} OR ${tk}" if 2 <= len(tk) <= 10 else m})
    jsave(Q_F, {"made": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "budget_left_today": left, "items": items,
                "save_results_to": INBOX + "/<mint>.json"})
    print(f"x queue: {len(items)} mints (budget left today {left}/{DAILY})")

def parse(path):
    raw = open(path).read(); i = raw.find("{")
    return json.loads(raw[i:raw.rindex("}") + 1])

PROMO = re.compile(r"\b\d{1,4}(\.\d)?x\b|alpha|\btg\b|telegram|\bdm\b|join|airdrop|\bcall\b|gem|roi|printing|mooned|parabolic|"
                   r"don.t miss|next (one|gem|runner)|\u2192|\u27a1|->|mcap|\bmc\b|signal|vip|whitelist|giveaway", re.I)
def promo(t): return len(PROMO.findall(t or "")) >= 1

def norm(t): return re.sub(r"https?://\S+|@\w+|\s+", " ", re.sub(r"^RT @\w+:\s*", "", t or "")).strip().lower()[:80]

def score(J, mint):
    posts = J.get("data") or []; users = {u["id"]: u for u in (J.get("includes") or {}).get("users", [])}
    now = time.time(); texts = {}
    for p in posts: texts.setdefault(norm(p.get("text")), set()).add(p.get("author_id"))
    real = {}; rt = dup = 0
    for p in posts:
        t = p.get("text") or ""; u = users.get(p.get("author_id"), {})
        is_rt = t.startswith("RT @"); is_dup = len(texts.get(norm(t), ())) >= 3
        is_pr = not is_rt and not is_dup and promo(t)
        rt += is_rt; dup += (is_dup and not is_rt); pass
        try: age_d = (now - datetime.datetime.fromisoformat(u["created_at"].replace("Z", "+00:00")).timestamp()) / 86400
        except (KeyError, ValueError): age_d = 0
        fol = (u.get("public_metrics") or {}).get("followers_count", 0)
        if age_d >= 180 and fol >= 200 and not is_rt and not is_dup and not is_pr:
            pm = p.get("public_metrics") or {}
            eng = pm.get("like_count", 0) + 2 * pm.get("retweet_count", 0) + pm.get("reply_count", 0)
            r = real.setdefault(u.get("username") or p["author_id"], {"followers": fol, "age_d": int(age_d), "eng": 0})
            r["eng"] += eng
    pr = sum(1 for p in posts if not (p.get("text") or "").startswith("RT @") and len(texts.get(norm(p.get("text")), ())) < 3 and promo(p.get("text")))
    n = len(posts); spam_share = (rt + dup + pr) / n if n else 0
    xs = min(100, round(sum(min(25, 6 + min(10, r["eng"]) + min(9, r["followers"] // 2000)) for r in real.values())))
    return {"t": now, "checked": time.strftime("%Y-%m-%d %H:%M %Z"), "posts": n, "authors": len({p.get("author_id") for p in posts}),
            "real_authors": len(real), "retweet_share": round(rt / n, 2) if n else 0, "copy_share": round(dup / n, 2) if n else 0, "promo_share": round(pr / n, 2) if n else 0,
            "bot_spam": n >= 5 and spam_share >= 0.6, "x_score": xs,
            "top_real": sorted(real, key=lambda k: -real[k]["followers"])[:5],
            "note": "info only; X buzz is easy to fake and often paid"}

def ingest(files):
    files = files or sorted(glob.glob(os.path.join(INBOX, "*.json")))
    S = jload(OUT_F, {}); b = budget(); n = 0
    for f in files:
        mint = os.path.basename(f).split(".")[0]
        try: J = parse(f)
        except (OSError, ValueError) as e:
            print(f"skip {f}: {e}"); continue
        if "--mint" in sys.argv: mint = sys.argv[sys.argv.index("--mint") + 1]
        S[mint] = score(J, mint); b["used"] += 1; n += 1
        if f.startswith(INBOX):
            os.makedirs(os.path.join(INBOX, "done"), exist_ok=True); shutil.move(f, os.path.join(INBOX, "done", os.path.basename(f)))
        r = S[mint]; print(f"{mint[:8]}.. posts {r['posts']}, real authors {r['real_authors']}, bot_spam {r['bot_spam']}, x_score {r['x_score']}")
    S = {m: v for m, v in S.items() if time.time() - v.get("t", 0) < 7 * 86400}
    jsave(OUT_F, S); jsave(BUD_F, b); print(f"ingested {n}; X budget used today {b['used']}/{DAILY}")

def get(mint):
    """for risk.py: latest X signal for a mint (<= 24 h old) or None."""
    v = jload(OUT_F, {}).get(mint)
    return v if v and time.time() - v.get("t", 0) < 86400 else None

if __name__ == "__main__":
    os.makedirs(INBOX, exist_ok=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "queue"
    if cmd == "queue": queue()
    elif cmd == "ingest": ingest([a for a in sys.argv[2:] if not a.startswith("--") and a != (sys.argv[sys.argv.index("--mint") + 1] if "--mint" in sys.argv else None)])
    elif cmd == "show": print(json.dumps(jload(OUT_F, {}) if len(sys.argv) < 3 else get(sys.argv[2]), indent=1))
