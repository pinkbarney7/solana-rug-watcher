"""Short-lived on-disk response cache + thread-safe per-host rate limiters for the scorecard tools.

- Cache: .cache/<aa>/<sha1>.json, keyed by URL (API key stripped) + JSON body. Only successful responses are stored.
  Default TTL 180 s (SC_CACHE_TTL). Immutable Helius history queries (ascending history, slot-bounded
  history) are kept 6 h. SC_NO_CACHE=1 disables the cache. The API key is never part of a key or a file.
- Rate limits are per process (token bucket per host). Helius: HELIUS_RPS (default 8; the free plan allows 10/s).
"""
import hashlib, json, os, re, threading, time

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, ".cache")
TTL = int(os.environ.get("SC_CACHE_TTL", "180"))
DISABLED = os.environ.get("SC_NO_CACHE") == "1"
HIST_TTL = 6 * 3600
IMM_TTL = 7 * 86400          # immutable history (full asc pages, slot-bounded pages, single txs): kept 7 days
BUSY_TTL = 6 * 3600          # getSignaturesForAddress(limit 1000) busy-wallet probe
LEDGER = os.path.join(HERE, "credit_ledger.jsonl")
_stats = {"hit": 0, "miss": 0}
_slock = threading.Lock()


def _clean_url(url):
    return re.sub(r"api-key=[^&]*", "api-key=", url)


def _key(url, body):
    raw = _clean_url(url) + "|" + (json.dumps(body, sort_keys=True) if body is not None else "")
    return hashlib.sha1(raw.encode()).hexdigest()


def ttl_for(url, body):
    """Seconds to cache this request (0 = do not cache)."""
    if "helius-rpc.com" in url and isinstance(body, dict):
        m, p = body.get("method"), body.get("params") or []
        if m in ("getTransaction",):
            return IMM_TTL
        if m == "getTransactionsForAddress" and len(p) > 1 and isinstance(p[1], dict):
            o = p[1]; f = o.get("filters") or {}
            if "lt" in (f.get("slot") or {}) or "lte" in (f.get("slot") or {}):
                return IMM_TTL                      # history before a fixed slot never changes
            if o.get("sortOrder") == "asc":
                return -IMM_TTL                     # negative = immutable only if the page came back full (see put)
        if m == "getSignaturesForAddress" and len(p) > 1 and isinstance(p[1], dict) and (p[1].get("limit") or 0) >= 1000:
            return BUSY_TTL
        return TTL
    if "lite-api.jup.ag" in url:
        return 60
    return TTL


def _full_page(body, data):
    try:
        lim = body["params"][1].get("limit") or 1000
        return len(((data or {}).get("result") or {}).get("data") or []) >= lim
    except Exception:
        return False


def get(url, body, ttl):
    if DISABLED or not ttl:
        return None
    if ttl < 0:          # asc history: full pages are immutable; partial pages (young wallets) only 1 h
        p0 = os.path.join(DIR, _key(url, body)[:2], _key(url, body) + ".json")
        try:
            age = time.time() - os.path.getmtime(p0)
            if age <= 3600 or (age <= -ttl and os.path.exists(p0 + ".full")):
                with open(p0) as f: d = json.load(f)
                with _slock: _stats["hit"] += 1
                return d
        except (OSError, ValueError):
            pass
        with _slock: _stats["miss"] += 1
        return None
    p = os.path.join(DIR, _key(url, body)[:2], _key(url, body) + ".json")
    try:
        if time.time() - os.path.getmtime(p) <= ttl:
            with open(p) as f:
                d = json.load(f)
            with _slock: _stats["hit"] += 1
            return d
    except (OSError, ValueError):
        pass
    with _slock: _stats["miss"] += 1
    return None


def put(url, body, data):
    if DISABLED:
        return
    k = _key(url, body); d = os.path.join(DIR, k[:2])
    try:
        os.makedirs(d, exist_ok=True)
        tmp = os.path.join(d, f".{k}.{os.getpid()}.{threading.get_ident()}.tmp")
        with open(tmp, "w") as f:
            json.dump(data, f)
        os.replace(tmp, os.path.join(d, k + ".json"))
        if isinstance(body, dict) and ttl_for(url, body) < 0 and _full_page(body, data):
            open(os.path.join(d, k + ".json.full"), "w").close()
    except OSError:
        pass


def prune(max_age=86400, imm_age=IMM_TTL, max_mb=400):
    """Delete expired cache files. Small responses expire after max_age; files bigger than 8 KB (tx histories, which
    are the expensive immutable ones) are kept for imm_age. If the cache exceeds max_mb, oldest files go first."""
    n = 0; files_all = []
    now = time.time()
    for root, _, files in os.walk(DIR):
        for fn in files:
            p = os.path.join(root, fn)
            try:
                st = os.stat(p); age = now - st.st_mtime
                lim = imm_age if (st.st_size > 8192 or fn.endswith(".full")) else max_age
                if age > lim: os.remove(p); n += 1
                else: files_all.append((st.st_mtime, st.st_size, p))
            except OSError:
                pass
    tot = sum(x[1] for x in files_all)
    for mt, sz, p in sorted(files_all):
        if tot <= max_mb * 1e6: break
        try: os.remove(p); tot -= sz; n += 1
        except OSError: pass
    return n


def ledger(src, credits, calls=None, extra=None):
    """Append one Helius credit-usage record (estimated) to credit_ledger.jsonl; shared by the daemon and all scans."""
    if not credits and not calls: return
    import datetime, fcntl
    rec = {"ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "src": src, "credits": round(float(credits or 0), 1)}
    if calls is not None: rec["calls"] = calls
    if extra: rec.update(extra)
    try:
        with open(LEDGER + ".lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            with open(LEDGER, "a") as f: f.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def stats():
    return dict(_stats)


class RateLimiter:
    def __init__(self, rps):
        self.gap = 1.0 / rps if rps > 0 else 0
        self.lock = threading.Lock()
        self.next = 0.0

    def wait(self):
        if not self.gap: return
        with self.lock:
            now = time.monotonic()
            t = max(now, self.next)
            self.next = t + self.gap
        d = t - time.monotonic()
        if d > 0: time.sleep(d)


_LIMITS = {
    "helius-rpc.com": float(os.environ.get("HELIUS_RPS", "8")),
    "api.dexscreener.com": 4.0,          # 300 req/min on token endpoints, 60/min on some others
    "api.geckoterminal.com": 0.45,       # ~30 req/min public limit
    "api.rugcheck.xyz": 3.0,
    "lite-api.jup.ag": float(os.environ.get("JUP_RPS", "3")),
    "solana-rpc.publicnode.com": 5.0,
    "frontend-api-v3.pump.fun": 1.0,
}
_lims = {}
_llock = threading.Lock()


HELIUS_TOTAL_RPS = float(os.environ.get("HELIUS_TOTAL_RPS", "8"))   # shared by ALL processes (scans + daemon); free plan = 10/s
_RL_FILE = os.environ.get("HELIUS_RL_FILE", "/tmp/scorecard_helius_rate.lock")   # box-wide, shared by dev+prod copies


def penalize(seconds=2.0, path=_RL_FILE):
    """After a Helius 429: push the shared next-slot forward so every process (daemon + scans) backs off together."""
    import fcntl
    try:
        with open(path, "a+") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.seek(0)
            try: nxt = float(f.read().strip() or 0)
            except ValueError: nxt = 0.0
            t = max(nxt, time.time() + seconds)
            f.seek(0); f.truncate(); f.write(repr(t)); f.flush()
        with _slock: _stats["h429"] = _stats.get("h429", 0) + 1
    except OSError:
        pass


def shared_wait(path=_RL_FILE, rps=HELIUS_TOTAL_RPS):
    """Cross-process token bucket: a file (under flock) holds the next free time slot."""
    import fcntl
    gap = 1.0 / rps
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a+") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.seek(0)
            try: nxt = float(f.read().strip() or 0)
            except ValueError: nxt = 0.0
            now = time.time()
            t = max(now, nxt)
            if t - now > 60: t = now          # stale/garbage value guard (penalize() pushes at most a few s)
            f.seek(0); f.truncate(); f.write(repr(t + gap)); f.flush()
        d = t - time.time()
        if d > 0: time.sleep(d)
    except OSError:
        time.sleep(gap)


def limit(url):
    host = re.sub(r"^https?://([^/?]+).*$", r"\1", url)
    host = next((h for h in _LIMITS if host.endswith(h)), host)
    if host == "helius-rpc.com":
        return shared_wait()
    if host == "api.geckoterminal.com":      # ~30 calls/min per IP: shared by the daemon and every scan on this box
        return shared_wait(path="/tmp/scorecard_gt_rate.lock", rps=_LIMITS[host])
    with _llock:
        lim = _lims.get(host)
        if lim is None:
            lim = _lims[host] = RateLimiter(_LIMITS.get(host, 5.0))
    lim.wait()
