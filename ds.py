"""Shared DEX Screener access (Solana) with fallbacks. Info/risk only.

DEX Screener's token endpoints sometimes return HTTP 200 with ZERO pairs for every token (seen 2026-10-07 ~15:48-16:05 ET:
/latest/dex/tokens and /tokens/v1 empty while /latest/dex/search still worked). That made healthy coins look delisted
(false liq_pull alerts) and left #3/#4/#8/#9/#10 UNKNOWN. So:
  token_pairs(m)   per-mint /latest/dex/tokens -> if empty, /latest/dex/search?q=<mint> (exact baseToken match)
  batch(mints)     /tokens/v1 (30 per call) -> mints that came back empty retried with token_pairs (bounded)
  degraded()       canary: True if the token endpoint returns no pairs for a coin that always has pairs (BONK)
Empty answers are never cached.
"""
import time, threading
import requests
try:
    import netcache
except ImportError:
    netcache = None
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36", "Accept": "application/json"}
DS = "https://api.dexscreener.com"
CANARY = "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"     # BONK: always has many Solana pairs
_canary = {"t": 0, "bad": False}
_cl = threading.Lock()
STATS = {"fallback_search": 0, "fallback_ok": 0}


def _get(url, ttl=60):
    if netcache:
        hit = netcache.get(url, None, ttl)
        if hit is not None: return hit
    for i in range(3):
        if netcache: netcache.limit(url)
        try:
            r = requests.get(url, headers=H, timeout=20)
            if r.status_code == 429 or r.status_code >= 500: time.sleep(1.5 * 2 ** i); continue
            if r.status_code != 200: return None
            d = r.json()
            nonempty = (isinstance(d, list) and d) or (isinstance(d, dict) and d.get("pairs"))
            if netcache and nonempty: netcache.put(url, None, d)
            return d
        except Exception:
            time.sleep(1.0 * 2 ** i)
    return None


def _sol(ps, mint):
    return [p for p in ps or [] if p.get("chainId") == "solana" and (p.get("baseToken") or {}).get("address") == mint]


def token_pairs(mint, ttl=60):
    """(pairs, source). source = 'tokens' | 'search' | None (no pairs anywhere) | 'error'."""
    d = _get(f"{DS}/latest/dex/tokens/{mint}", ttl)
    ps = _sol((d or {}).get("pairs"), mint) if isinstance(d, dict) else []
    if ps: return ps, "tokens"
    STATS["fallback_search"] += 1
    s = _get(f"{DS}/latest/dex/search?q={mint}", ttl)
    ps2 = _sol((s or {}).get("pairs"), mint) if isinstance(s, dict) else []
    if ps2: STATS["fallback_ok"] += 1; return ps2, "search"
    if d is None and s is None: return [], "error"
    return [], None


GT = "https://api.geckoterminal.com/api/v2/networks/solana"


def _f(x):
    try: return float(x)
    except (TypeError, ValueError): return None


def gt_multi(mints, ttl=60):
    """GeckoTerminal /tokens/multi (30 per call, ~30 calls/min public limit) -> mint -> {"token": attrs, "pools": [pool dicts]}.
    Pool dicts carry attributes plus _base/_quote/_dex ids. Also gives unique buyers/sellers per m5/m15/m30/h1/h6/h24."""
    out = {}
    mints = list(dict.fromkeys(mints))
    for i in range(0, len(mints), 30):
        ch = mints[i:i + 30]
        url = f"{GT}/tokens/multi/{','.join(ch)}?include=top_pools"
        d = None
        if netcache: d = netcache.get(url, None, ttl)
        if d is None:
            for k in range(3):
                if netcache: netcache.limit(url)
                try:
                    r = requests.get(url, headers=H, timeout=20)
                    if r.status_code == 429: time.sleep(3 * 2 ** k); continue
                    d = r.json() if r.status_code == 200 else None
                    if d and netcache: netcache.put(url, None, d)
                    break
                except Exception:
                    time.sleep(2)
        if not d: continue
        pools = {}
        for x in d.get("included") or []:
            if x.get("type") != "pool": continue
            rel = x.get("relationships") or {}
            a = dict(x["attributes"]); a["_base"] = ((rel.get("base_token") or {}).get("data") or {}).get("id", "")[7:]
            a["_quote"] = ((rel.get("quote_token") or {}).get("data") or {}).get("id", "")[7:]
            a["_dex"] = ((rel.get("dex") or {}).get("data") or {}).get("id")
            pools[x["id"]] = a
        for t in d.get("data") or []:
            m = t["attributes"].get("address")
            ids = [p["id"] for p in ((t.get("relationships") or {}).get("top_pools") or {}).get("data") or []]
            out[m] = {"token": t["attributes"], "pools": [pools[i_] for i_ in ids if i_ in pools]}
    return out


def gt_to_pairs(mint, g):
    """Convert gt_multi()[mint] to DEX Screener-like pair dicts (only pools where the mint is the base token).
    Missing vs DexS: socials/websites (info), boosts. Marked with "_src": "geckoterminal"."""
    out = []
    tok = (g or {}).get("token") or {}
    for a in (g or {}).get("pools") or []:
        if a.get("_base") != mint: continue
        tx = a.get("transactions") or {}; v = a.get("volume_usd") or {}; pc = a.get("price_change_percentage") or {}
        try:
            import datetime
            ca = int(datetime.datetime.fromisoformat(a["pool_created_at"].replace("Z", "+00:00")).timestamp() * 1000)
        except Exception:
            ca = None
        out.append({"chainId": "solana", "dexId": a.get("_dex"), "pairAddress": a.get("address"), "_src": "geckoterminal",
                    "url": f"https://www.geckoterminal.com/solana/pools/{a.get('address')}",
                    "baseToken": {"address": mint, "symbol": tok.get("symbol") or ((a.get("name") or "").split(" / ")[0].strip() or None), "name": tok.get("name")},
                    "quoteToken": {"address": a.get("_quote"), "symbol": "SOL" if a.get("_quote") == "So11111111111111111111111111111111111111112" else None},
                    "priceUsd": a.get("base_token_price_usd"), "priceNative": a.get("base_token_price_quote_token"),
                    "liquidity": {"usd": _f(a.get("reserve_in_usd"))},
                    "marketCap": _f(a.get("market_cap_usd")) or _f(tok.get("market_cap_usd")), "fdv": _f(a.get("fdv_usd")),
                    "volume": {k: _f(v.get(k)) for k in ("m5", "m15", "m30", "h1", "h6", "h24")},
                    "priceChange": {k: _f(pc.get(k)) for k in ("m5", "m15", "m30", "h1", "h6", "h24")},
                    "txns": {k: {"buys": (tx.get(k) or {}).get("buys"), "sells": (tx.get(k) or {}).get("sells"),
                                 "buyers": (tx.get(k) or {}).get("buyers"), "sellers": (tx.get(k) or {}).get("sellers")}
                             for k in ("m5", "m15", "m30", "h1", "h6", "h24")},
                    "pairCreatedAt": ca, "info": {}})
    return out


def batch(mints, max_fallback=40, ttl=60, gt_fallback=True):   # gt_fallback: True | "degraded" (only on outage) | False
    """mint -> [pairs]. Uses /tokens/v1 (30 per call); empty mints are retried via GeckoTerminal multi (30 per call)
    when DEX Screener is degraded, else per mint with the search fallback (up to max_fallback)."""
    mints = list(dict.fromkeys(mints)); out = {}
    for i in range(0, len(mints), 30):
        ch = mints[i:i + 30]
        d = _get(f"{DS}/tokens/v1/solana/" + ",".join(ch), ttl)
        for p in d if isinstance(d, list) else []:
            m = (p.get("baseToken") or {}).get("address")
            if m in ch and p.get("chainId") == "solana": out.setdefault(m, []).append(p)
    missing = [m for m in mints if m not in out]
    if missing and gt_fallback and (degraded() or (gt_fallback is True and len(missing) > 10)):
        g = gt_multi(missing, ttl)
        for m in missing:
            ps = gt_to_pairs(m, g.get(m))
            if ps: out[m] = ps
        missing = [m for m in missing if m not in out]
        STATS["gt_fallback"] = STATS.get("gt_fallback", 0) + 1
        if degraded(): return out
    for m in missing[:max_fallback]:
        ps, _ = token_pairs(m, ttl)
        if ps: out[m] = ps
    return out


def degraded(max_age=120):
    """True if DEX Screener's token endpoint is returning empty results (checked at most every max_age s)."""
    with _cl:
        if time.time() - _canary["t"] < max_age: return _canary["bad"]
        _canary["t"] = time.time()
    d = _get(f"{DS}/latest/dex/tokens/{CANARY}", 0)
    bad = not (isinstance(d, dict) and _sol(d.get("pairs"), CANARY))
    _canary["bad"] = bad
    return bad


def pairs(mints):
    """mint -> [pairs] using the per-mint endpoint (+ search fallback; GeckoTerminal when DEX Screener is degraded).
    The batch endpoint drops pairs on busy tokens, so it is not used here."""
    mints = list(dict.fromkeys(mints)); out = {}
    if degraded():
        g = gt_multi(mints)
        return {m: ps for m in mints for ps in [gt_to_pairs(m, g.get(m))] if ps}
    for m in mints:
        ps, _ = token_pairs(m)
        if ps: out[m] = ps
    return out


def summary(mints):
    """mint -> {liq (all pairs), top (pair addr), price, mcap, h1, sym} from the deepest pair."""
    out = {}
    for m, ps in pairs(mints).items():
        ps.sort(key=lambda p: -float((p.get("liquidity") or {}).get("usd") or 0)); t = ps[0]
        out[m] = {"liq": sum(float((p.get("liquidity") or {}).get("usd") or 0) for p in ps), "top": t["pairAddress"],
                  "price": float(t.get("priceUsd") or 0) or None, "mcap": t.get("marketCap") or t.get("fdv"),
                  "h1": (t.get("priceChange") or {}).get("h1"), "sym": t["baseToken"].get("symbol"),
                  "src": "geckoterminal" if t.get("_src") == "geckoterminal" else "dexscreener"}
    return out


def confirm_gone(mints):
    """For coins with no DEX Screener pairs: ask GeckoTerminal. Returns mint -> "gone" (GT answered and has no pool with
    >= $1k reserve), a summary dict (GT still has pools - use it), or "unknown" (GT failed too: never treat as a pull)."""
    out = {}
    if not mints: return out
    g = gt_multi(list(mints), ttl=0)
    for m in mints:
        if m not in g:
            out[m] = "unknown" if not g else "gone"      # GT answered for others but not this one = no GT token/pool
            continue
        ps = gt_to_pairs(m, g[m])
        L = sum((p.get("liquidity") or {}).get("usd") or 0 for p in ps)
        if not ps or L < 1000: out[m] = "gone"; continue
        t = max(ps, key=lambda p: (p.get("liquidity") or {}).get("usd") or 0)
        out[m] = {"liq": L, "top": t["pairAddress"], "price": float(t.get("priceUsd") or 0) or None, "mcap": t.get("marketCap") or t.get("fdv"),
                  "h1": (t.get("priceChange") or {}).get("h1"), "sym": t["baseToken"].get("symbol"), "src": "geckoterminal"}
    return out
