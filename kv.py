"""Tiny persistent key-value store (sqlite, WAL) shared by all processes: first-funder results, launch analyses,
operator fingerprints. Values are JSON. Never stores API keys."""
import json, os, sqlite3, threading, time
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, ".cache", "kv.sqlite")
_local = threading.local()
STATS = {"hit": 0, "miss": 0}


def _db():
    c = getattr(_local, "c", None)
    if c is None:
        os.makedirs(os.path.dirname(PATH), exist_ok=True)
        c = sqlite3.connect(PATH, timeout=30)
        c.execute("PRAGMA journal_mode=WAL"); c.execute("PRAGMA synchronous=NORMAL")
        c.execute("CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT, t REAL)")
        _local.c = c
    return c


def get(k, max_age=None):
    try:
        r = _db().execute("SELECT v, t FROM kv WHERE k=?", (k,)).fetchone()
    except sqlite3.Error:
        return None
    if not r or (max_age is not None and time.time() - r[1] > max_age):
        STATS["miss"] += 1; return None
    STATS["hit"] += 1
    return json.loads(r[0])


def put(k, v):
    for i in range(3):
        try:
            c = _db(); c.execute("INSERT OR REPLACE INTO kv VALUES (?,?,?)", (k, json.dumps(v, default=list), time.time())); c.commit(); return
        except sqlite3.OperationalError:
            time.sleep(0.2 * (i + 1))


def items(prefix):
    try:
        return [(k, json.loads(v), t) for k, v, t in _db().execute("SELECT k, v, t FROM kv WHERE k LIKE ?", (prefix + "%",))]
    except sqlite3.Error:
        return []
