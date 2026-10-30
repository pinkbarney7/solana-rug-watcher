"""Batch-job guard: one copy per job name, low CPU/IO priority, hard timeout (read-only helper, no API calls).

  import joblock; joblock.guard("fast_scan")         # at the top of main()

- Lock: locks/<name>.lock (flock). A second copy prints "SKIPPED: ... already running" and exits 0, so overlapping
  routine runs cannot stack (SC_LOCK_WAIT=<s> waits for the lock first).
- Priority: nice +10 and ionice idle, so the realtime daemon (nice 0) always gets the CPU first.
- Timeout: a watchdog thread kills the job's children and exits 124 after the per-job limit (SC_JOB_TIMEOUT overrides).
- Load: if the 1-min load is above 3x the cores, waits up to 2 min for it to drop before starting (prints a note).
Set SC_NO_JOBLOCK=1 to bypass (tests only)."""
import fcntl, os, subprocess, sys, threading, time
HERE = os.path.dirname(os.path.abspath(__file__))
LOCKD = os.path.join(HERE, "locks")
TIMEOUTS = {"smart_early": 600, "fast_scan": 1200, "learn_rugs": 1800, "wallet_watch": 900, "wallet_discovery": 900, "liq_watch": 240,
            "report_card": 420, "smart_money": 2400}
_HELD = []


def load_ratio():
    try: return os.getloadavg()[0] / (os.cpu_count() or 1)
    except OSError: return 0.0


def holder(name):
    try: return open(os.path.join(LOCKD, name + ".lock")).read().strip()
    except OSError: return ""


def running(name):
    """True if another process holds the lock for this job."""
    os.makedirs(LOCKD, exist_ok=True)
    with open(os.path.join(LOCKD, name + ".lock"), "a+") as f:
        try: fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB); fcntl.flock(f, fcntl.LOCK_UN); return False
        except BlockingIOError: return True


def _expire(name, to):
    sys.stderr.write(f"\nTIMEOUT: {name} ran longer than {to}s - stopping it (partial output may exist)\n"); sys.stderr.flush()
    try: subprocess.run(["pkill", "-TERM", "-P", str(os.getpid())], timeout=5)
    except Exception: pass
    time.sleep(3)
    try: subprocess.run(["pkill", "-KILL", "-P", str(os.getpid())], timeout=5)
    except Exception: pass
    os._exit(124)


def guard(name, timeout=None, nice=10, wait=None):
    if os.environ.get("SC_NO_JOBLOCK"): return
    os.makedirs(LOCKD, exist_ok=True)
    f = open(os.path.join(LOCKD, name + ".lock"), "a+")
    wait = float(os.environ.get("SC_LOCK_WAIT", wait or 0)); t0 = time.time()
    while True:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB); break
        except BlockingIOError:
            if time.time() - t0 >= wait:
                f.seek(0); who = f.read().strip()
                print(f"SKIPPED: {name} is already running ({who or 'holder unknown'}); not starting a second copy.", flush=True)
                sys.exit(0)
            time.sleep(5)
    f.seek(0); f.truncate(); f.write(f"pid {os.getpid()} since {time.strftime('%Y-%m-%d %H:%M:%S %Z')}: {' '.join(sys.argv)[:200]}"); f.flush()
    _HELD.append(f)
    try:                                   # session credit reserve (credit_reserve.json): credit-using jobs wait their turn
        import credit_reserve
        ok, msg = credit_reserve.batch_ok(name)
        if not ok:
            print(f"SKIPPED: {name} - {msg}", flush=True); sys.exit(0)
    except ImportError:
        pass
    try: os.nice(nice)
    except OSError: pass
    try: subprocess.run(["ionice", "-c3", "-p", str(os.getpid())], capture_output=True, timeout=5)
    except Exception: pass
    t1 = time.time()
    if load_ratio() > 3:
        sys.stderr.write(f"[joblock] box load {os.getloadavg()[0]:.1f} on {os.cpu_count()} cores - waiting up to 2 min for it to drop before {name}\n")
        while load_ratio() > 3 and time.time() - t1 < 120: time.sleep(10)
    to = int(os.environ.get("SC_JOB_TIMEOUT") or timeout or TIMEOUTS.get(name, 1800))
    t = threading.Timer(to, _expire, args=(name, to)); t.daemon = True; t.start()
