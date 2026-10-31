"""Helius-powered on-chain checks (#11-#14) for scorecard.py.

Reads HELIUS_API_KEY from the environment. The key is never printed: every error
string is scrubbed before it leaves this module.
"""
import os, time, threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ.get("HELIUS_API_KEY", "").strip()
RPC_URL = "https://mainnet.helius-rpc.com/?api-key="
MAX_CALLS = int(os.environ.get("HELIUS_MAX_CALLS", "240"))
SYSTEM_PROGRAM = "11111111111111111111111111111111"
BURN = {SYSTEM_PROGRAM, "1nc1nerator11111111111111111111111111111111"}
EARLY_SLOTS = 3          # creation slot + next 3 slots
BUNDLE_PAGES = 6         # x100 txs scanned from the start of the mint's history
FUNDER_LOOKUPS = 32
# Known CEX hot wallets on Solana. Only addresses labelled by at least one reputable explorer/intel
# source or two independent public lists (checked 2026-10-07). Sources:
#  [R] Range intel labels (app.range.org)  [S] Solscan account label  [O] Orb/Helius explorer label
#  [G] public label list gist.github.com/andrewn6/d3718022044435bff899823d6413dfa7
#  [W] exchange list in reddit.com/r/copy_trade/comments/1ipddgf (wallets-alpha/Solana-Wallets)
KNOWN_CEX = {
    "5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9": "Binance",        # [R] "Binance-linked hot wallet" (GoPlus), [G], [W]
    "H8sMJSCQxfKiFTCfDR3DUMLPwcRbM61LGFJ8N4dK3WjS": "Coinbase",       # [R] "Coinbase: Hot Wallet (H8sM)", [G]
    "5VCwKtCXgCJ6kit5FybXjvriW3xELsFDhYrPSqtJNmcD": "OKX",            # [G], [W]
    "is6MTRHEgyFLNTfYcuV4QBWLjrZBfmhVNYR6ccgr8KV": "OKX",             # [S] "OKX: Hot Wallet 1"
    "AC5RDfQFmDS1deWZos921JfqscXdByf8BKHs5ACWjtW2": "Bybit",          # [G], [W]
    "CK8i4zFXkDE2KWfyg7g9S748r6mwxajbcKcyGhQMR3qQ": "Bybit",          # [O] "Bybit Hot Wallet 3"
    "5LZkATrLwHYCQj2YuVbjjgsDZzBk6YfL4pFQRJmtboT2": "Bybit",          # [O] "Bybit Hot Wallet 4"
    "FWznbcNXWQuHTawe9RxvQ2LdCENssh12dsznf4RiouN5": "Kraken",         # [G], [W]
    "BmFdpraQhkiDQE6SnfG5omcA1VwzqfXrwtNYBwWTymy6": "KuCoin",         # [G], [W]
    "ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ": "MEXC",           # [G], [W]
    "AobVSwdW9BbpMdJvTqeCN4hPAmh4rHm7vwLnQ5ATSyrS": "Crypto.com",     # [G], analyzer69000.com/investigations/gotm
}
# exchange / hub hot wallets maintained in exchange_wallets.json (public labels + audit heuristics) join KNOWN_CEX
def _load_exchanges():
    try:
        import json as _j
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exchange_wallets.json")
        return {a: (v.get("label") if isinstance(v, dict) else str(v)) for a, v in _j.load(open(p)).get("wallets", {}).items()}
    except Exception:
        return {}
EXCHANGE_WALLETS = _load_exchanges()
for _a, _l in EXCHANGE_WALLETS.items(): KNOWN_CEX.setdefault(_a, _l)


def is_exchange(a):
    return a in KNOWN_CEX


# Jito tip accounts (a transfer to one of these = the tx was sent as / inside a Jito bundle)
JITO_TIP = {"96gYZGLnJYVFmbjzopPSU6QiEV5fGqZNyN9nmNhvrZU5", "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gRe",
            "Cw8CFyM9FkoMi7K7Crf6HNQqf4uEMzpKw6QNghXLvLkY", "ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49",
            "DfXygSm4jCyNCybVYYK6DwvWqjKee8pbDmJGcLWNDXjh", "ADuUkR4vqLUMWXxW9gh6D6L8pMSawimctcNZ5pGwDcEt",
            "DttWaMuVvTiduZRnguLF7jNxTgiMBZ1hyAumKUiL2KRL", "3AVi9Tg9Uo68tJfuvoKvqKNWKkC5wPdSSdeBnizKZ6jT"}


def jito_tip(tx):
    """Lamports paid to Jito tip accounts in this tx (0 if none)."""
    try:
        ks = keys_of(tx); m = tx.get("meta") or {}; pre, post = m.get("preBalances") or [], m.get("postBalances") or []
        return sum(post[j] - pre[j] for j, k in enumerate(ks) if k in JITO_TIP and j < len(post) and post[j] > pre[j])
    except Exception:
        return 0


RUG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rug_funders.json")
def load_rug_list():
    try:
        import json as _j
        return {w["address"]: w for w in _j.load(open(RUG_FILE)).get("wallets", []) if w.get("address") not in KNOWN_CEX}
    except Exception:
        return {}
# Privacy pools / mixers: funding from these is never ignored and is flagged.
KNOWN_MIXERS = {
    "4AV2Qzp3N4c9RfzyEbNZs2wqWfW4EwKnnxFAZCndvfGh": "Privacy Cash SOL pool",  # [O] "Privacy Cash SOL Pool"
}


class Budget(Exception):
    pass


def scrub(s):
    s = str(s)
    return s.replace(KEY, "***") if KEY else s


class Helius:
    def __init__(self, http, cap=None):
        self.http = http      # scorecard.http(url, body) -> (data, err)
        self.calls = 0
        self.errors = []
        self.cap = cap or MAX_CALLS
        self.cached = 0
        self.credits = 0          # estimated Helius credits (getTransactionsForAddress = 10 per 100 full txs, others 1)
        self._lock = threading.Lock()

    def rpc(self, method, params):
        if not KEY:
            return None, "HELIUS_API_KEY not set"
        body = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
        try:
            import netcache
            hit = netcache.get(RPC_URL + KEY, body, netcache.ttl_for(RPC_URL + KEY, body))
        except Exception:
            hit = None
        if hit is not None and not hit.get("error"):
            self.cached += 1
            return hit.get("result"), None
        with self._lock:
            if self.calls >= self.cap:
                raise Budget(f"Helius call cap ({self.cap}) reached")
            self.calls += 1
        d, err = self.http(RPC_URL + KEY, body)
        if not err and not (d or {}).get("error"):
            r = (d or {}).get("result")
            if method == "getTransactionsForAddress":
                n = len((r or {}).get("data") or []) if isinstance(r, dict) else 0
                full = (params[1] if len(params) > 1 else {}).get("transactionDetails") == "full"
                c = max(1, -(-n // 100)) * 10 if full else 10
            else:
                c = 1
            with self._lock: self.credits += c
        if err:
            err = scrub(err); self.errors.append(f"{method}: {err}"); return None, err
        if d.get("error"):
            err = scrub(f"RPC error: {d['error'].get('message')}")
            self.errors.append(f"{method}: {err}"); return None, err
        return d.get("result"), None

    def accounts(self, addrs, parsed=True):
        out = {}
        addrs = list(dict.fromkeys(a for a in addrs if a))
        for i in range(0, len(addrs), 100):
            ch = addrs[i:i + 100]
            r, e = self.rpc("getMultipleAccounts", [ch, {"encoding": "jsonParsed" if parsed else "base64"}])
            if e: raise RuntimeError(e)
            for a, v in zip(ch, (r or {}).get("value") or []):
                out[a] = v
        return out

    def txs_asc(self, addr, limit=100, token=None):
        p = {"sortOrder": "asc", "limit": limit, "transactionDetails": "full",
             "encoding": "jsonParsed", "maxSupportedTransactionVersion": 1}
        if token: p["paginationToken"] = token
        r, e = self.rpc("getTransactionsForAddress", [addr, p])
        if e: raise RuntimeError(e)
        return (r or {}).get("data") or [], (r or {}).get("paginationToken")


# ---------------------------------------------------------------- ed25519 on-curve (PDA detection)
_P = 2 ** 255 - 19
_D = (-121665 * pow(121666, _P - 2, _P)) % _P
_B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def b58dec(s):
    n = 0
    for c in s: n = n * 58 + _B58.index(c)
    b = n.to_bytes((n.bit_length() + 7) // 8, "big") if n else b""
    return b"\0" * (len(s) - len(s.lstrip("1"))) + b

def on_curve(addr):
    """True for normal wallet keys; False for PDAs (program-derived, nobody holds the key)."""
    try:
        b = b58dec(addr)
        if len(b) != 32: return True
        y = int.from_bytes(b, "little") & ((1 << 255) - 1)
        if y >= _P: return False
        u, v = (y * y - 1) % _P, (_D * y * y + 1) % _P
        x2 = u * pow(v, _P - 2, _P) % _P
        return x2 == 0 or pow(x2, (_P - 1) // 2, _P) == 1
    except Exception:
        return True


def keys_of(tx):
    return [k["pubkey"] if isinstance(k, dict) else k for k in tx["transaction"]["message"]["accountKeys"]]


def mint_deltas(tx, mint):
    """{owner: delta_raw}, {owner: set(token_account)} for this mint in one tx."""
    keys = keys_of(tx); m = tx.get("meta") or {}
    pre, post = defaultdict(int), defaultdict(int); tas = defaultdict(set)
    for side, store in ((m.get("preTokenBalances") or [], pre), (m.get("postTokenBalances") or [], post)):
        for b in side:
            if b.get("mint") != mint or not b.get("owner"): continue
            store[b["owner"]] += int(b["uiTokenAmount"]["amount"])
            tas[b["owner"]].add(keys[b["accountIndex"]])
    return {o: post[o] - pre[o] for o in set(pre) | set(post)}, tas


def first_funder(H, w):
    """First inbound SOL transfer to wallet w: (funder, sol, blockTime) or None. Found results never change, so they
    are memoised in the persistent kv store (shared by every scan and the daemon): a repeat wallet costs 0 credits."""
    try:
        import kv
        hit = kv.get("ff:" + w)
        if hit: return tuple(hit)
    except Exception:
        kv = None
    r = _first_funder(H, w)
    if r and kv:
        try: kv.put("ff:" + w, list(r))
        except Exception: pass
    return r


def _first_funder(H, w):
    data, _ = H.txs_asc(w, limit=10)
    for tx in data:
        m = tx.get("meta") or {}
        if m.get("err"): continue
        keys = keys_of(tx)
        if w not in keys: continue
        i = keys.index(w)
        pre, post = m.get("preBalances") or [], m.get("postBalances") or []
        if i >= len(post) or post[i] <= pre[i] or i == 0: continue
        drops = [(pre[j] - post[j], keys[j]) for j in range(len(keys)) if j != i and j < len(post) and pre[j] > post[j]]
        if not drops: continue
        _, src = max(drops)
        return src, (post[i] - pre[i]) / 1e9, tx.get("blockTime")
    return None


# ---------------------------------------------------------------- multi-hop funding trace
TRACE_TARGETS = int(os.environ.get("HELIUS_TRACE_TARGETS", "24"))   # creator + early buyers traced at hop 1
TRACE_L2, TRACE_L3 = 10, 5        # funder nodes expanded at hop 2 / hop 3
TRACE_OUT = 7                     # candidate hubs whose outgoing SOL transfers are scanned (2 calls each)
TRACE_TXS = 25                    # txs read per wallet before the launch (one getTransactionsForAddress call, 10 credits)
TRACE_MIN_SOL = 0.02
TRACE_MIN_EARLY = float(os.environ.get("HELIUS_TRACE_MIN_EARLY", "5"))   # trace buyers only if slots 0-3 got >= this % (creator always)


def funding_sources(H, w, before_slot, n=TRACE_TXS):
    """Inbound SOL transfers to w (first funder handled separately) in its last n successful txs before before_slot.
    Returns {sender: {"sol": total, "n": count, "t": latest blockTime}}. Swaps (w's token balances change) are skipped."""
    p = {"sortOrder": "desc", "limit": n, "transactionDetails": "full", "encoding": "jsonParsed",
         "maxSupportedTransactionVersion": 1, "filters": {"slot": {"lt": before_slot}, "status": "succeeded"}}
    r, e = H.rpc("getTransactionsForAddress", [w, p])
    if e: raise RuntimeError(e)
    out = {}
    for tx in (r or {}).get("data") or []:
        m = tx.get("meta") or {}
        keys = keys_of(tx)
        if w not in keys: continue
        i = keys.index(w)
        pre, post = m.get("preBalances") or [], m.get("postBalances") or []
        if i >= len(post) or post[i] - pre[i] < TRACE_MIN_SOL * 1e9: continue
        if any(b.get("owner") == w for b in (m.get("postTokenBalances") or []) + (m.get("preTokenBalances") or [])
               if b.get("mint") != "So11111111111111111111111111111111111111112"):
            continue      # token movement in the same tx = swap/sell, not a funding transfer
        drops = [(pre[j] - post[j], keys[j]) for j in range(len(keys)) if j != i and j < len(post) and pre[j] > post[j]]
        if not drops: continue
        _, src = max(drops)
        if src == w or not on_curve(src): continue
        o = out.setdefault(src, {"sol": 0.0, "n": 0, "t": 0})
        o["sol"] += (post[i] - pre[i]) / 1e9; o["n"] += 1; o["t"] = max(o["t"], tx.get("blockTime") or 0)
    return out


def outflows(H, f, before_slot, pages=2):
    """Wallets that received >= TRACE_MIN_SOL SOL from f in f's last pages*100 successful txs before before_slot."""
    out, tok = {}, None
    for _ in range(pages):
        p = {"sortOrder": "desc", "limit": 100, "transactionDetails": "full", "encoding": "jsonParsed",
             "maxSupportedTransactionVersion": 1, "filters": {"slot": {"lt": before_slot}, "status": "succeeded"}}
        if tok: p["paginationToken"] = tok
        r, e = H.rpc("getTransactionsForAddress", [f, p])
        if e: raise RuntimeError(e)
        data = (r or {}).get("data") or []
        for tx in data:
            m = tx.get("meta") or {}; keys = keys_of(tx)
            if f not in keys: continue
            i = keys.index(f); pre, post = m.get("preBalances") or [], m.get("postBalances") or []
            if i >= len(post) or pre[i] - post[i] < TRACE_MIN_SOL * 1e9: continue
            for j, k in enumerate(keys):
                if j == i or j >= len(post): continue
                g = post[j] - pre[j]
                if g >= TRACE_MIN_SOL * 1e9 and on_curve(k):
                    o = out.setdefault(k, {"sol": 0.0, "n": 0, "t": 0})
                    o["sol"] += g / 1e9; o["n"] += 1; o["t"] = max(o["t"], tx.get("blockTime") or 0)
        tok = (r or {}).get("paginationToken")
        if not tok or len(data) < 100: break
    return out


def busy_check(H, f):
    """True if f looks exchange-like (1000+ signatures in < 2 days). Known CEX -> True, mixers -> False."""
    if f in KNOWN_CEX: return True
    if f in KNOWN_MIXERS: return False
    r, e = H.rpc("getSignaturesForAddress", [f, {"limit": 1000}])
    if e or not r: return None
    span = (r[0].get("blockTime") or 0) - (r[-1].get("blockTime") or 0)
    return len(r) >= 1000 and span < 2 * 86400


def trace(H, R, creator, early, first_fund, s0, hold_pct):
    """Follow first funder + top-up funders for the creator and launch buyers up to 3 hops and find hubs:
    a wallet that (directly or via 1-2 intermediate wallets) funded 3+ launch buyers, or the creator + 2+ buyers."""
    T = {"targets": 0, "edges": 0, "expanded": [0, 0, 0], "partial": None}
    total_early = sum(x["got_pct"] for x in early)
    tg = [creator]
    if total_early >= TRACE_MIN_EARLY or os.environ.get("HELIUS_TRACE_ALWAYS") == "1":
        tg += [x["wallet"] for x in early if x["got_pct"] >= 0.3 or x["slot0_pct"] > 0][:TRACE_TARGETS - 1]
    else:
        T["skipped_buyers"] = f"slots 0-{EARLY_SLOTS} buyers got {total_early:.1f}% (< {TRACE_MIN_EARLY}%), only creator traced"
    T["targets"] = len(tg)
    before = s0 + EARLY_SLOTS + 1
    parents = defaultdict(dict)          # child -> {funder: {"sol", "n", "kind"}}
    def add_edges(w, srcs, kind):
        for f, v in srcs.items():
            if f == w: continue
            e = parents[w].setdefault(f, {"sol": 0.0, "n": 0, "kinds": set()})
            e["sol"] += v.get("sol", 0); e["n"] += v.get("n", 1); e["kinds"].add(kind)
    for w in tg:
        ff = first_fund.get(w)
        if ff: add_edges(w, {ff[0]: {"sol": ff[1], "n": 1}}, "first")
    def expand(nodes, n):
        res = {}
        def one(w):
            try: return w, funding_sources(H, w, before, n), None
            except Budget as be: return w, None, be
            except Exception: return w, None, None
        with ThreadPoolExecutor(6) as ex:
            for w, srcs, be in ex.map(one, nodes):
                if be: T["partial"] = str(be)
                if srcs is not None: res[w] = srcs
        return res
    busy = {}
    def is_busy(f):
        if f not in busy:
            try: busy[f] = busy_check(H, f)
            except Budget as be: T["partial"] = str(be); busy[f] = None
            except Exception: busy[f] = None
        return busy[f]
    # hop 1: top-ups for every target (first funders already known)
    for w, srcs in expand(tg, TRACE_TXS).items(): add_edges(w, srcs, "top-up")
    T["expanded"][0] = len(tg)
    tset = set(tg)
    frontier = tg
    for hop, cap in ((2, TRACE_L2), (3, TRACE_L3)):
        if T["partial"]: break
        # candidate funders at this hop, ranked by how many targets they (already) reach
        reach = defaultdict(set)
        for w in frontier:
            for f in parents.get(w, {}):
                reach[f].add(w)
        cand = [f for f in sorted(reach, key=lambda f: -len(reach[f])) if f not in tset and f not in KNOWN_CEX and f not in KNOWN_MIXERS]
        nxt = []
        for f in cand:
            if len(nxt) >= cap: break
            if len(reach[f]) >= 2 and is_busy(f): continue     # exchange-like: do not walk through it
            nxt.append(f)
        if not nxt: break
        ff_new = {}
        def _ff(f):
            try: return f, first_funder(H, f)
            except Exception: return f, None
        with ThreadPoolExecutor(6) as ex:
            for f, ffr in ex.map(_ff, nxt): ff_new[f] = ffr
        for f, ffr in ff_new.items():
            if ffr: add_edges(f, {ffr[0]: {"sol": ffr[1], "n": 1}}, "first")
        for f, srcs in expand(nxt, 15).items(): add_edges(f, srcs, "top-up")
        T["expanded"][hop - 1] = len(nxt)
        tset |= set(nxt); frontier = nxt
    # signer links: a launch buy signed/paid by another wallet = same operator (edge owner -> signer)
    for x in early:
        for sg in x.get("signers") or []:
            if sg != x["wallet"]:
                add_edges(x["wallet"], {sg: {"sol": 0, "n": 1}}, "signer")
    # outflow scan of candidate hubs: catches hubs that funded wallets long before the launch (beyond TRACE_TXS)
    reach1 = defaultdict(set)
    for w, ps in list(parents.items()):
        for f in ps: reach1[f].add(w)
    cf = first_fund.get(creator)
    cands = ([creator] + ([cf[0]] if cf else []) + list(parents.get(creator, {}))
             + sorted([f for f in reach1 if len(reach1[f]) >= 2], key=lambda f: -len(reach1[f])))
    cands = [f for f in dict.fromkeys(cands) if f not in KNOWN_CEX and f not in KNOWN_MIXERS]
    scanned = []
    tg_set = set(tg)
    early_set = {x["wallet"] for x in early}
    for f in cands:
        if len(scanned) >= TRACE_OUT or T["partial"]: break
        if f != creator and is_busy(f): continue
        try:
            outs = outflows(H, f, before)
        except Budget as be:
            T["partial"] = str(be); break
        except Exception:
            continue
        scanned.append(f)
        for k, v in outs.items():
            if k in early_set or k == creator or k in tset:
                add_edges(k, {f: v}, "outflow")
    T["outflow_scanned"] = scanned
    # ancestors of each target within 3 hops (never walking through exchange-like / CEX / mixer nodes)
    early_got = {x["wallet"]: x["got_pct"] for x in early}
    anc = defaultdict(dict)       # ancestor -> {target: hops}
    for w in tg:
        level = {w}; seen = {w}
        for d in (1, 2, 3):
            nl = set()
            for c in level:
                for f in parents.get(c, {}):
                    if f in seen: continue
                    seen.add(f)
                    anc[f].setdefault(w, d)
                    if f in KNOWN_CEX or f in KNOWN_MIXERS or busy.get(f): continue
                    nl.add(f)
            level = nl
    hubs = []
    for a, ts in anc.items():
        eb = [t for t in ts if t != creator]
        inc = creator in ts
        if not (len(eb) >= 3 or (inc and len(eb) >= 2)): continue
        if a in KNOWN_CEX: continue
        bz = busy.get(a)
        if bz is None and a not in KNOWN_MIXERS and a != creator and a not in early_set: bz = is_busy(a)
        got = sum(early_got.get(t, 0) for t in eb)
        op_like = bool(inc and len(eb) >= 2 and got > 10)
        if bz and not op_like: continue
        direct = [t for t in eb if ts[t] == 1]
        hubs.append({"hub": a, "is_launch_wallet": a in early_set or a == creator,
                     "n_early": len(eb), "early_wallets": sorted(eb, key=lambda t: -early_got.get(t, 0)),
                     "early_got_pct": got, "held_pct": sum(hold_pct.get(t, 0) for t in eb) + (hold_pct.get(creator, 0) if inc else 0),
                     "includes_creator": inc, "creator_hops": ts.get(creator), "direct": len(direct),
                     "direct_got_pct": sum(early_got.get(t, 0) for t in direct),
                     "direct_outflow": len([t for t in direct if "outflow" in parents.get(t, {}).get(a, {}).get("kinds", set())]),
                     "max_hops": max(ts.values()), "busy": bool(bz), "mixer": KNOWN_MIXERS.get(a)})
    # rank: external wallets first, then creator link, breadth, direct links
    hubs.sort(key=lambda h: (h["is_launch_wallet"], not h["includes_creator"], -h["n_early"], -h["direct"], h["max_hops"]))
    keep = []
    for h in hubs:
        if any(set(h["early_wallets"]) <= set(k["early_wallets"]) and h["includes_creator"] <= k["includes_creator"]
               and (h["is_launch_wallet"] or h["max_hops"] > k["max_hops"]) for k in keep):
            continue
        keep.append(h)
    # operator group: wallets connected to the creator through any non-busy funding/signer link (undirected)
    adj = defaultdict(set)
    for c, ps in parents.items():
        for f in ps:
            if f in KNOWN_CEX or f in KNOWN_MIXERS or busy.get(f): continue
            adj[c].add(f); adj[f].add(c)
    comp, stack = {creator}, [creator]
    while stack:
        for nb in adj[stack.pop()]:
            if nb not in comp: comp.add(nb); stack.append(nb)
    ge = [w for w in comp if w in early_set]
    T["operator_group"] = {"n_early": len(ge), "early_got_pct": sum(early_got.get(w, 0) for w in ge),
                           "held_pct": sum(hold_pct.get(w, 0) for w in ge), "n_wallets": len(comp),
                           "early_wallets": sorted(ge, key=lambda t: -early_got.get(t, 0))}
    T["edges"] = sum(len(v) for v in parents.values())
    T["nodes_funded"] = len(parents)
    T["hubs"] = keep[:6]
    T["n_early_total"] = len(early)
    T["ancestors_checked"] = sorted(anc)           # used by #15 (rug-list link through any hop)
    T["ancestor_hops"] = {a: min(ts.values()) for a, ts in anc.items()}
    T["ancestor_reach"] = {a: sorted(ts) for a, ts in anc.items()}
    R["trace"] = T


# ---------------------------------------------------------------- gather everything once
def gather(mint, http, known_pools=()):
    H = Helius(http)
    R = {"enabled": bool(KEY), "error": None}
    if not KEY:
        R["error"] = "HELIUS_API_KEY not set"; return R
    try:
        _gather(H, mint, R, set(known_pools) | BURN)
    except Budget as e:
        R["error"] = str(e)
    except Exception as e:
        R["error"] = scrub(f"{type(e).__name__}: {e}")
    R["calls"] = H.calls
    R["cached_calls"] = H.cached
    R["credits_est"] = H.credits
    R["call_errors"] = H.errors[:5]
    return R


def _gather(H, mint, R, known):
    sup, e = H.rpc("getTokenSupply", [mint])
    if e: raise RuntimeError(e)
    supply = int(sup["value"]["amount"]); R["supply"] = supply; R["decimals"] = sup["value"]["decimals"]
    pctf = lambda raw: raw / supply * 100 if supply else 0
    # ---- holders
    la, e = H.rpc("getTokenLargestAccounts", [mint])
    R["holders_err"] = e
    owner_amt = defaultdict(int); ta_owner = {}
    if not e:
        tas = [x["address"] for x in la["value"]]
        acc = H.accounts(tas)
        for x in la["value"]:
            v = acc.get(x["address"])
            try: o = v["data"]["parsed"]["info"]["owner"]
            except Exception: o = None
            if o: owner_amt[o] += int(x["amount"]); ta_owner[x["address"]] = o
    oinfo = H.accounts(list(owner_amt)) if owner_amt else {}
    def classify(o, ta=None):
        if o in known or (ta and ta in known): return "known pool/burn"
        v = oinfo.get(o)
        if v and v.get("executable"): return "program"
        if v and v.get("owner") not in (None, SYSTEM_PROGRAM): return f"program-owned ({v['owner'][:6]}..)"
        if not on_curve(o): return "PDA (program-controlled)"
        return None
    holders, excluded = [], []
    for o, amt in sorted(owner_amt.items(), key=lambda kv: -kv[1]):
        lab = classify(o, next((t for t, ow in ta_owner.items() if ow == o), None))
        (excluded if lab else holders).append({"owner": o, "pct": pctf(amt), "label": lab})
    R["holders"], R["holders_excluded"], R["largest_accounts_n"] = holders, excluded, len(owner_amt)
    # ---- launch: earliest txs
    txs, tok = [], None
    for _ in range(BUNDLE_PAGES):
        d, tok = H.txs_asc(mint, 100, tok)
        txs += d
        if not d or not tok or d[-1]["slot"] > txs[0]["slot"] + EARLY_SLOTS: break
    if not txs: raise RuntimeError("no transactions found for mint")
    s0 = txs[0]["slot"]; R["creation_slot"] = s0; R["creation_time"] = txs[0].get("blockTime")
    R["creation_sig"] = txs[0]["transaction"]["signatures"][0]
    creator = keys_of(txs[0])[0]; R["creator"] = creator
    buys = defaultdict(lambda: {"slot0": 0, "early": 0, "signers": set(), "tas": set(), "first_slot": None, "jito0": 0})
    creator_buy = 0
    J = {"create_tipped": jito_tip(txs[0]) > 0, "slot0_txs": 0, "slot0_tipped": 0}
    for tx in txs:
        if tx["slot"] > s0 + EARLY_SLOTS: break
        if (tx.get("meta") or {}).get("err"): continue
        signer = keys_of(tx)[0]
        tip = jito_tip(tx) if tx["slot"] == s0 else 0
        if tx["slot"] == s0: J["slot0_txs"] += 1; J["slot0_tipped"] += 1 if tip > 0 else 0
        dl, tas = mint_deltas(tx, mint)
        for o, dv in dl.items():
            if dv <= 0: continue
            if o == creator: creator_buy += dv; continue
            if o in known or not on_curve(o): continue
            b = buys[o]; b["early"] += dv; b["signers"].add(signer); b["tas"] |= tas[o]
            if tx["slot"] == s0:
                b["slot0"] += dv
                if tip > 0: b["jito0"] += dv
            b["first_slot"] = b["first_slot"] if b["first_slot"] is not None else tx["slot"]
    # remove program-owned owners among buyers (bonding curves that are on-curve are rare, but check)
    binfo = H.accounts(list(buys)) if buys else {}
    for o in list(buys):
        v = binfo.get(o)
        if v and (v.get("executable") or v.get("owner") not in (None, SYSTEM_PROGRAM)): buys.pop(o)
    # current balances of the token accounts they used
    allta = [t for b in buys.values() for t in b["tas"]]
    tinfo = H.accounts(allta) if allta else {}
    for o, b in buys.items():
        held = 0
        for t in b["tas"]:
            try:
                i = tinfo[t]["data"]["parsed"]["info"]
                if i.get("mint") == mint: held += int(i["tokenAmount"]["amount"])
            except Exception: pass
        b["held"] = max(held, owner_amt.get(o, 0))
    R["early"] = [{"wallet": o, "slot_offset": b["first_slot"] - s0, "got_pct": pctf(b["early"]),
                   "slot0_pct": pctf(b["slot0"]), "held_pct": pctf(b["held"]), "signers": sorted(b["signers"])}
                  for o, b in sorted(buys.items(), key=lambda kv: -kv[1]["early"])]
    R["creator_buy_pct"] = pctf(creator_buy)
    R["txs_scanned"] = len(txs)
    J["tipped_buyers"] = sum(1 for b in buys.values() if b["jito0"] > 0)
    J["tipped_pct"] = pctf(sum(b["jito0"] for b in buys.values()))
    J["bundled_launch"] = bool(J["create_tipped"] and J["tipped_buyers"] >= 1)
    R["jito"] = J
    # ---- creator
    ca, e = H.rpc("getTokenAccountsByOwner", [creator, {"mint": mint}, {"encoding": "jsonParsed"}])
    R["creator_hold_pct"] = None if e else pctf(sum(int(a["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"]) for a in ca["value"]))
    ctx, _ = H.txs_asc(creator, 100)
    created = []
    for tx in ctx:
        keys = tx["transaction"]["message"]["accountKeys"]
        mints = {b.get("mint") for b in (tx.get("meta") or {}).get("postTokenBalances") or []}
        for k in keys:
            if isinstance(k, dict) and k.get("signer") and k["pubkey"] in mints and k["pubkey"] != creator:
                created.append(k["pubkey"])
    created = list(dict.fromkeys(created))
    R["creator_created"] = created
    # dev sells / transfers after launch (from the same creator history page: 0 extra credits)
    dm = {"sold_pct": 0.0, "transferred_pct": 0.0, "recipients": {}, "n_sells": 0, "post_launch_txs": 0, "last_seen": None}
    for tx in ctx:
        if tx.get("slot", 0) <= s0 or (tx.get("meta") or {}).get("err"): continue
        dm["post_launch_txs"] += 1; dm["last_seen"] = tx.get("blockTime")
        dl, _ = mint_deltas(tx, mint)
        d_c = dl.get(creator, 0)
        if d_c >= 0: continue
        ks = keys_of(tx); m_ = tx.get("meta") or {}
        ci = ks.index(creator) if creator in ks else None
        sol_up = ci is not None and (m_["postBalances"][ci] - m_["preBalances"][ci]) > 0.001e9
        recv = {o: v for o, v in dl.items() if o != creator and v > 0 and o not in known and on_curve(o)}
        if recv and not sol_up:
            for o, v in recv.items():
                dm["recipients"][o] = dm["recipients"].get(o, 0) + pctf(v)
            dm["transferred_pct"] += pctf(sum(recv.values()))
        else:
            dm["sold_pct"] += pctf(-d_c); dm["n_sells"] += 1
            if dm.get("first_sell_t") is None: dm["first_sell_t"] = tx.get("blockTime")
        if dm.get("first_exit_t") is None: dm["first_exit_t"] = tx.get("blockTime")     # first sell OR transfer out
    dm["covered"] = len(ctx) < 100
    R["dev_moves"] = dm
    R["creator_history_truncated"] = len(ctx) >= 100
    # ---- funders (creator, top 15 holders, early buyers by size)
    targets = [creator] + [h["owner"] for h in holders[:15]] + [x["wallet"] for x in R["early"]]
    targets = list(dict.fromkeys(targets))[:FUNDER_LOOKUPS]
    fund = {}
    def _ff(w):
        try: return w, first_funder(H, w), None
        except Budget as e: return w, None, e
        except Exception: return w, None, None
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(_ff, targets))
    for w, f, be in res:
        fund[w] = f
    if any(be for _, _, be in res): raise next(be for _, _, be in res if be)
    R["funders"] = {w: (f[0] if f else None) for w, f in fund.items()}
    R["funder_detail"] = {w: f for w, f in fund.items() if f}
    R["creator_funder"] = fund.get(creator)
    # high-volume funder check (likely exchange / router) for funders shared by >=2 wallets
    cnt = defaultdict(list)
    for w, f in R["funders"].items():
        if f: cnt[f].append(w)
    hubs = {}
    for f, ws in cnt.items():
        if len(ws) < 2: continue
        if f in KNOWN_CEX: hubs[f] = "cex"; continue
        if f in KNOWN_MIXERS: hubs[f] = False; continue
        r, e = H.rpc("getSignaturesForAddress", [f, {"limit": 1000}])
        if e or not r: hubs[f] = None; continue
        span = (r[0].get("blockTime") or 0) - (r[-1].get("blockTime") or 0)
        hubs[f] = len(r) >= 1000 and span < 2 * 86400   # 1000+ txs in <2 days -> exchange-like
    hold_pct = {h["owner"]: h["pct"] for h in holders}
    for x in R["early"]: hold_pct[x["wallet"]] = max(hold_pct.get(x["wallet"], 0), x["held_pct"])
    if R["creator_hold_pct"]: hold_pct[creator] = max(hold_pct.get(creator, 0), R["creator_hold_pct"])
    early_set = {x["wallet"] for x in R["early"]}
    R["clusters"] = sorted([{"funder": f, "wallets": ws, "held_pct": sum(hold_pct.get(w, 0) for w in ws),
                             "early_got_pct": sum(x["got_pct"] for x in R["early"] if x["wallet"] in ws),
                             "includes_creator": creator in ws or f == creator,
                             "n_early": len(early_set & set(ws)),
                             "exchange_like": bool(hubs.get(f)), "known_cex": KNOWN_CEX.get(f),
                             "mixer": KNOWN_MIXERS.get(f)} for f, ws in cnt.items() if len(ws) >= 2],
                           key=lambda c: -c["held_pct"])
    # busy funder that funded the creator AND launch buyers taking >10% is operator-like, not an exchange
    for c in R["clusters"]:
        c["operator_like"] = bool(c["exchange_like"] and not c["known_cex"] and c["includes_creator"] and c["n_early"] >= 2 and c["early_got_pct"] > 10)
        if c["operator_like"]: c["exchange_like"] = False
    # wallets funded directly by the creator
    # 2nd hop for the creator (funder's funder), skipped for known CEX/mixers
    cf = fund.get(creator)
    R["creator_funder2"] = None
    if cf and cf[0] not in KNOWN_CEX and cf[0] not in KNOWN_MIXERS:
        try: R["creator_funder2"] = first_funder(H, cf[0])
        except Budget: raise
        except Exception: pass
    try:
        trace(H, R, creator, R["early"], fund, s0, hold_pct)
    except Budget as e:
        R["trace"] = {"partial": str(e), "hubs": [], "ancestors_checked": []}
    except Exception as e:
        R["trace"] = {"error": scrub(f"{type(e).__name__}: {e}"), "hubs": [], "ancestors_checked": []}
    R["mixer_funded"] = {w: KNOWN_MIXERS[f] for w, f in R["funders"].items() if f in KNOWN_MIXERS}
    R["creator_funded"] = [w for w, f in R["funders"].items() if f == creator]
    R["funder_checked"] = sum(1 for f in fund.values() if f)
    R["funder_targets"] = len(targets)


# ---------------------------------------------------------------- checks
def _short(a): return a[:6] + ".." + a[-4:]

def checks(mint, H, chk, unk):
    out = []
    names = {11: "Helius top holders", 12: "Launch bundle / snipers", 13: "Creator wallet", 14: "Common-funder clusters", 15: "Known rug-funder link"}
    if not H or not H.get("enabled"):
        why = "not checked - " + ((H or {}).get("error") or "Helius disabled")
        return [chk(n, nm, "WARN", why) for n, nm in names.items()]
    fatal = H.get("error")
    # 11
    n = 11
    try:
        if H.get("holders_err") or "holders" not in H: raise RuntimeError(H.get("holders_err") or fatal)
        hs = H["holders"]; top = hs[:10]; t10 = sum(h["pct"] for h in top); big = hs[0] if hs else None
        st = "FAIL" if (t10 > 40 or (big and big["pct"] > 15)) else "WARN" if (t10 > 25 or (big and big["pct"] > 5)) else "PASS"
        exc = H["holders_excluded"]
        val = f"top-10 {t10:.1f}% of supply; largest {big['pct']:.2f}% ({_short(big['owner'])})" if big else "no wallet holders in top-20 accounts"
        det = (f"from getTokenLargestAccounts ({H['largest_accounts_n']} owners); excluded {len(exc)} = "
               f"{sum(x['pct'] for x in exc):.1f}% ({', '.join(sorted({x['label'] for x in exc})) or 'none'})")
        out.append(chk(n, names[n], st, val, det))
    except Exception as e:
        out.append(chk(n, names[n], "WARN", f"not checked - {scrub(e)}"))
    # 12
    n = 12
    try:
        if "early" not in H: raise RuntimeError(fatal)
        E = H["early"]; s0 = [x for x in E if x["slot0_pct"] > 0]
        got0 = sum(x["slot0_pct"] for x in E); got = sum(x["got_pct"] for x in E); held = sum(x["held_pct"] for x in E)
        sig0 = {s for x in s0 for s in x["signers"]}
        st = "FAIL" if held > 20 else "WARN" if (held > 5 or got0 > 10 or got > 20) else "PASS"
        cb = H.get("creator_buy_pct") or 0; ch = H.get("creator_hold_pct") or 0
        if cb > 20: st = "FAIL" if (ch > 10 or st == "FAIL") else ("WARN" if st == "PASS" else st)
        val = (f"creation slot: {len(s0)} wallet(s)/{len(sig0)} signer(s) bought {got0:.1f}%; "
               f"slots 0-{EARLY_SLOTS}: {len(E)} wallet(s) got {got:.1f}%, still hold {held:.1f}%")
        top = ", ".join(f"{_short(x['wallet'])} +{x['slot_offset']} {x['got_pct']:.1f}%->{x['held_pct']:.1f}%" for x in E[:4])
        ts = time.strftime("%Y-%m-%d %H:%M %Z", time.localtime(H["creation_time"])) if H.get("creation_time") else "?"
        det = f"created slot {H['creation_slot']} @ {ts}; creator's own buy {H['creator_buy_pct']:.1f}% (excluded from bundle sums)" + (f"; top: {top}" if top else "")
        if cb > 20: det += f"; creator bought {cb:.1f}% itself at launch, still holds {ch:.1f}%" + (" (FAIL: >10% still held)" if ch > 10 else "")
        if got0 > 10 and held <= 5: det += "; bundle bought big then dumped (sell pressure already taken)"
        J = H.get("jito") or {}
        if J.get("bundled_launch"):
            det += f"; JITO-BUNDLED LAUNCH: create tx + {J['tipped_buyers']} buyer(s) in the creation slot paid Jito tips and got {J['tipped_pct']:.1f}%"
            if J["tipped_pct"] > 10 and st == "PASS": st = "WARN"
        elif J.get("slot0_tipped"):
            det += f"; {J['slot0_tipped']}/{J['slot0_txs']} creation-slot tx(s) paid Jito tips"
        out.append(chk(n, names[n], st, val, det))
    except Exception as e:
        out.append(chk(n, names[n], "WARN", f"not checked - {scrub(e)}"))
    # 13
    n = 13
    try:
        if "creator" not in H: raise RuntimeError(fatal)
        c = H["creator"]; hp = H.get("creator_hold_pct"); f = H.get("creator_funder")
        sts = []
        if hp is None: sts.append("WARN")
        else: sts.append("FAIL" if hp >= 20 else "WARN" if hp >= 5 else "PASS")
        prior = [m for m in H.get("creator_created", []) if m != mint]
        if len(prior) >= 3: sts.append("WARN")
        if H.get("creator_funded"): sts.append("WARN")
        incl = [cl for cl in H.get("clusters", []) if cl["includes_creator"] and cl["n_early"] and not cl["exchange_like"]]
        if incl: sts.append("WARN")
        val = f"deployer {_short(c)} holds {'n/a' if hp is None else f'{hp:.2f}%'}; funded by " + (
            f"{_short(f[0])} ({f[1]:.3f} SOL)" if f else "unknown")
        det = f"{len(prior)}{'+' if H.get('creator_history_truncated') else ''} other token(s) created in its first 100 txs"
        if prior: det += " (" + ", ".join(_short(m) for m in prior[:3]) + ")"
        if H.get("creator_funded"): det += f"; creator directly funded {len(H['creator_funded'])} checked holder/early wallet(s)"
        if incl: det += "; creator shares a funder with early buyers"
        if f and f[0] in KNOWN_CEX: det += f"; funder is a known {KNOWN_CEX[f[0]]} hot wallet"
        dm = H.get("dev_moves") or {}
        if dm.get("transferred_pct", 0) > 0.5:
            hold_now = {h["owner"]: h["pct"] for h in H.get("holders") or []}
            still = sum(hold_now.get(o, 0) for o in dm["recipients"])
            det += (f"; DEV TRANSFERRED {dm['transferred_pct']:.1f}% to {len(dm['recipients'])} wallet(s) after launch"
                    f" (they still hold {still:.1f}% among top holders)")
            sts.append("FAIL" if still > 10 else "WARN" if (dm["transferred_pct"] > 5 or still > 3) else "PASS")
        if dm.get("sold_pct", 0) > 0.5:
            det += f"; dev sold {dm['sold_pct']:.1f}% in {dm['n_sells']} tx(s) after launch"
            if (hp or 0) < 1 and not dm.get("transferred_pct"): det += " (sold out)"
        if dm and not dm.get("covered", True): det += "; post-launch dev moves: partial (creator history > 100 txs)"
        mx = H.get("mixer_funded") or {}
        if c in mx: sts.append("WARN"); det += f"; creator funded from mixer ({mx[c]})"
        elif mx: det += f"; {len(mx)} checked wallet(s) funded from a mixer"
        out.append(chk(n, names[n], max(sts, key=lambda s: {"FAIL": 2, "WARN": 1, "PASS": 0}[s]), val, det))
    except Exception as e:
        out.append(chk(n, names[n], "WARN", f"not checked - {scrub(e)}"))
    # 14
    n = 14
    try:
        if "clusters" not in H: raise RuntimeError(fatal)
        cl = H["clusters"]; real = [c for c in cl if not c["exchange_like"]]
        big = real[0] if real else None
        _lo = [c for c in real if c["includes_creator"] and c["early_got_pct"] > 20]
        if _lo and (not big or big["held_pct"] <= 25): big = _lo[0]
        worst_early = max([c["early_got_pct"] for c in real] or [0])
        launch_op = [c for c in real if c["includes_creator"] and c["early_got_pct"] > 20]
        st = "FAIL" if (big and big["held_pct"] > 25) or launch_op else "WARN" if (big and (big["held_pct"] > 5 or big["includes_creator"] or worst_early > 10)) else "PASS"
        if H["funder_checked"] < H["funder_targets"] / 2 and st == "PASS": st = "WARN"
        val = (f"{len(real)} cluster(s) sharing a first funder" + (f"; largest {len(big['wallets'])} wallets hold {big['held_pct']:.1f}% (funder {_short(big['funder'])}"
               + (f", got {big['early_got_pct']:.1f}% at launch" if big['early_got_pct'] else "") + ")" if big else ""))
        det = f"funder found for {H['funder_checked']}/{H['funder_targets']} wallets (creator, top-15 holders, early buyers)"
        ex = [c for c in cl if c["exchange_like"]]
        if ex: det += f"; {len(ex)} exchange-like funder(s) ignored ({', '.join(_short(c['funder']) + (' [' + c['known_cex'] + ']' if c.get('known_cex') else ' [busy, unlabelled]') + ' x' + str(len(c['wallets'])) for c in ex[:3])})"
        mxc = [c for c in cl if c.get("mixer")]
        if mxc:
            det += f"; mixer-funded cluster ({mxc[0]['mixer']}) x{len(mxc[0]['wallets'])}"
            if st == "PASS": st = "WARN"
        if launch_op: det += f"; creator's funder {_short(launch_op[0]['funder'])} also funded {launch_op[0]['n_early']} launch buyer(s) that got {launch_op[0]['early_got_pct']:.1f}% (coordinated launch)"
        ops = [c for c in real if c.get("operator_like")]
        if ops: det += f"; {len(ops)} busy funder(s) kept as operator-like (funded creator + launch buyers)"
        if worst_early > 10: det += f"; a cluster got {worst_early:.1f}% at launch"
        # multi-hop trace (first funder + top-ups + hub outflows + shared signers, up to 3 hops)
        T = H.get("trace") or {}
        hubs = [h for h in T.get("hubs") or [] if not h.get("is_launch_wallet")] or list(T.get("hubs") or [])
        og = T.get("operator_group") or {}
        if hubs:
            h = hubs[0]
            hs = (f"hub {_short(h['hub'])} linked to " + ("creator (" + str(h['creator_hops']) + " hop) + " if h["includes_creator"] else "")
                  + f"{h['n_early']} launch buyer(s) ({h['direct']} direct" + (f", {h['direct_outflow']} found via the hub's own transfers" if h.get('direct_outflow') else "")
                  + f", max {h['max_hops']} hops) that got {h['early_got_pct']:.1f}% at launch, still hold {h['held_pct']:.1f}%")
            hub_op = h["includes_creator"] and h["early_got_pct"] > 20
            if hub_op or h["held_pct"] > 25:
                st = "FAIL"; hs += " (coordinated launch via multi-hop hub)" if hub_op else " (hub-linked wallets hold >25%)"
                if hub_op: det += f"; hub {_short(h['hub'])} funded creator + launch buyers (coordinated launch)"
            elif (h["n_early"] >= 3 and h["early_got_pct"] > 10) or h["includes_creator"]:
                st = "WARN" if st == "PASS" else st
            val += "; " + hs
        if og.get("n_early", 0) >= 2:
            det += f"; operator group (wallets linked to the creator by funding/signing): {og['n_early']} launch buyer(s), got {og['early_got_pct']:.1f}%, hold {og['held_pct']:.1f}%"
            if og["early_got_pct"] > 20 and st != "FAIL": st = "FAIL"; det += " (coordinated launch)"
            elif st == "PASS": st = "WARN"
        if T.get("skipped_buyers"): det += f"; trace: {T['skipped_buyers']}"
        elif T: det += f"; trace: {T.get('targets', 0)} wallets, hop2 {T.get('expanded', [0,0,0])[1]}, hop3 {T.get('expanded', [0,0,0])[2]}, hub outflows {len(T.get('outflow_scanned') or [])}"
        if T.get("partial"): det += f" (partial: {T['partial']})"
        if T.get("error"): det += f" (trace error: {T['error']})"
        out.append(chk(n, names[n], st, val, det))
    except Exception as e:
        out.append(chk(n, names[n], "WARN", f"not checked - {scrub(e)}"))
    # 15
    n = 15
    try:
        if "funders" not in H: raise RuntimeError(fatal)
        RL = load_rug_list(); c = H["creator"]; hits = []
        def hit(role, w, via, addr):
            r = RL.get(addr)
            if r and mint not in (r.get("linked_mints") or []) or (r and len(r.get("linked_mints") or []) > 1):
                hits.append((r["confidence"], role, w, via, r))
        busy = {cl["funder"] for cl in H.get("clusters", []) if cl.get("exchange_like")} | {a for a, r in RL.items() if r.get("busy")}
        busy_info = 0
        for w, f in H["funders"].items():
            role = "creator" if w == c else "holder/early buyer"
            hit(role, w, "is", w)
            if f and f in busy and role != "creator" and f in RL: busy_info += 1; continue   # busy service-like funder: only the creator link counts
            if f: hit(role, w, "funded by", f)
        f2 = H.get("creator_funder2")
        if f2: hit("creator", c, "2nd-hop funded by", f2[0])
        T = H.get("trace") or {}
        reach = T.get("ancestor_reach") or {}; hops = T.get("ancestor_hops") or {}
        for a in T.get("ancestors_checked") or []:
            if a not in RL: continue
            ts = reach.get(a, [])
            if c in ts: hit("creator", c, f"{hops.get(a, '?')}-hop funded (trace) by", a)
            elif ts and not RL[a].get("busy"): hit("holder/early buyer", ts[0], f"{hops.get(a, '?')}-hop funded (trace) by", a)
        for hb in T.get("hubs") or []:
            hit("launch hub", hb["hub"], "is", hb["hub"])
        # de-duplicate (same listed wallet reached several ways)
        _seen = set(); hits[:] = [h for h in hits if not (h[4]["address"], h[1]) in _seen and not _seen.add((h[4]["address"], h[1]))]
        lows = [h for h in hits if h[0] == "low"]          # low-confidence (auto-discovered) entries: listed in detail, not scored
        hits[:] = [h for h in hits if h[0] != "low"]
        hits.sort(key=lambda h: (h[0] != "high", h[1] != "creator"))
        st = "FAIL" if any(h[0] == "high" for h in hits) else "WARN" if hits else "PASS"
        val = (f"{len(hits)} link(s) to listed rug wallets; top: {hits[0][1]} {_short(hits[0][2])} {hits[0][3]} {_short(hits[0][4]['address'])} ({hits[0][4]['label']}, {hits[0][0]})" if hits
               else f"no links to {len(RL)} listed rug wallets")
        det = f"checked creator + {len(H['funders']) - 1} holders/early buyers (wallet and first funder) + creator 2nd hop" + ("" if f2 else " (2nd hop n/a)") + f" + {len(T.get('ancestors_checked') or [])} multi-hop ancestors"
        if busy_info: det += f"; {busy_info} holder link(s) via busy listed funder not scored"
        if lows: det += "; low-confidence list links (info, not scored): " + ", ".join(f"{h[1]} {_short(h[2])} {h[3]} {_short(h[4]['address'])}" for h in lows[:3])
        if hits: det += "; " + "; ".join(f"{h[1]} {_short(h[2])} {h[3]} {_short(h[4]['address'])} [{h[0]}]" for h in hits[1:4])
        out.append(chk(n, names[n], st, val, det))
    except Exception as e:
        out.append(chk(n, names[n], "WARN", f"not checked - {scrub(e)}"))
    if fatal:
        for c in out:
            if "not checked" not in c["value"]: c["detail"] = (c["detail"] + "; " if c["detail"] else "") + f"partial: {fatal}"
    return out
