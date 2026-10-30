#!/usr/bin/env python3
"""Exit-liquidity test via Jupiter public quote API (read-only quotes, no wallet, no swap).
Buy $X of the token with USDC (quote), then quote selling exactly those tokens back to USDC and to SOL.
  python3 exit_liq.py <MINT> [--json]
"""
import json, sys, time
try:
    import requests
except ImportError:
    requests = None
import urllib.request, urllib.parse
Q = "https://lite-api.jup.ag/swap/v1/quote"
USDC = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
SOL = "So11111111111111111111111111111111111111112"
SIZES = (25, 100)

def quote(inp, out, amt):
    url = Q + "?" + urllib.parse.urlencode({"inputMint": inp, "outputMint": out, "amount": int(amt), "slippageBps": 5000})
    try:
        import netcache
    except ImportError:
        netcache = None
    if netcache:
        hit = netcache.get(url, None, 60)
        if hit is not None: return hit, None
    code = 0
    for i in range(4):
        if netcache: netcache.limit(url)          # shared Jupiter limiter (per process)
        try:
            if requests:
                r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"}); code, d = r.status_code, (r.json() if r.text else {})
            else:
                with urllib.request.urlopen(url, timeout=15) as r: code, d = r.status, json.load(r)
        except Exception as e:
            code, d = 0, {"error": f"{type(e).__name__}"}
        if code == 429 or code >= 500 or code == 0: time.sleep(1.5 * (i + 1)); continue
        if code != 200 or "outAmount" not in d: return None, (d.get("error") or d.get("errorCode") or f"HTTP {code}")
        if netcache: netcache.put(url, None, d)
        return d, None
    return None, f"HTTP {code}"

def route(d): return " > ".join(dict.fromkeys(s["swapInfo"].get("label", "?") for s in d.get("routePlan", [])))

def test(mint, sol_leg=False):
    """Quotes run in two parallel rounds: ($1 ref, $25 buy, $100 buy) then (sell $25, sell $100). The SOL-leg reference
    quotes are skipped unless sol_leg=True (they are not used in the grade)."""
    from concurrent.futures import ThreadPoolExecutor
    R = {"mint": mint, "sizes": {}, "error": None}
    with ThreadPoolExecutor(3) as ex:
        fr = ex.submit(quote, USDC, mint, 1e6)
        fb = {usd: ex.submit(quote, USDC, mint, usd * 1e6) for usd in SIZES}
        ref, e = fr.result(); buys = {usd: f.result() for usd, f in fb.items()}
    if not ref: R["error"] = f"no buy route ({e})"; return R
    ref_rate = int(ref["outAmount"])                # tokens(raw) per $1
    with ThreadPoolExecutor(4) as ex:
        fs = {usd: ex.submit(quote, mint, USDC, int(b["outAmount"])) for usd, (b, _) in buys.items() if b}
        f2 = {usd: ex.submit(quote, mint, SOL, int(b["outAmount"])) for usd, (b, _) in buys.items() if b and sol_leg}
        sells = {usd: f.result() for usd, f in fs.items()}; sols = {usd: f.result() for usd, f in f2.items()}
    for usd in SIZES:
        b, e = buys[usd]
        if not b: R["sizes"][usd] = {"error": f"no buy route ({e})"}; continue
        tokens = int(b["outAmount"])
        s, e = sells[usd]
        if not s: R["sizes"][usd] = {"error": f"no sell route ({e})", "buy_route": route(b)}; continue
        back = int(s["outAmount"]) / 1e6
        fair = tokens / ref_rate                    # $ value of those tokens at the $1 marginal rate
        s2 = (sols.get(usd) or (None, None))[0]
        R["sizes"][usd] = {
            "tokens_raw": tokens, "buy_route": route(b), "sell_route": route(s),
            "sell_usdc": back, "sell_impact_pct": max(0.0, (1 - back / fair) * 100) if fair else None,
            "jup_sell_impact_pct": float(s.get("priceImpactPct") or 0) * 100,
            "round_trip_loss_pct": (1 - back / usd) * 100,
            "sell_to_sol_lamports": int(s2["outAmount"]) if s2 else None, "sell_sol_route": route(s2) if s2 else None}
    return R

def grade(R):
    """Return (status, value, detail)."""
    if R.get("error"): return "FAIL", f"no route - {R['error']}", "Jupiter quote API"
    a = R["sizes"].get(25, {}); b = R["sizes"].get(100, {})
    if a.get("error"): return "FAIL", f"$25: {a['error']}", ""
    imp, rt = a["sell_impact_pct"], a["round_trip_loss_pct"]
    st = "FAIL" if imp > 15 else "WARN" if (imp > 5 or rt > 10) else "PASS"
    val = f"$25 sell impact {imp:.1f}%, round-trip loss {rt:.1f}%"
    if b and not b.get("error"): val += f"; $100 sell impact {b['sell_impact_pct']:.1f}%, round-trip {b['round_trip_loss_pct']:.1f}%"
    elif b: val += f"; $100: {b['error']}"
    det = f"route sell: {a['sell_route']}; buy: {a['buy_route']}; Jupiter quotes only (no swap), USDC legs; fees/taxes included in quotes"
    return st, val, det

if __name__ == "__main__":
    R = test(sys.argv[1]); 
    if "--json" in sys.argv: print(json.dumps(R, indent=1))
    else: print(grade(R))
