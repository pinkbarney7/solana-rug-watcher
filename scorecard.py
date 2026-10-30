#!/usr/bin/env python3
"""Solana token scorecard: pass/warn/fail checks from free public sources.

Usage: python3 scorecard.py <MINT> [--json] [--out FILE]
Not financial advice. Nearly all meme coins are high risk.
"""
import argparse, json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import helius_checks
import exit_liq
import netcache
import wash
import smart_money
import risk as risk_mod
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

try:
    import requests
except ImportError:  # stdlib fallback
    requests = None
    import urllib.request, urllib.error

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0.0.0 Safari/537.36")
RPC = "https://solana-rpc.publicnode.com"
DS_TOKEN = "https://api.dexscreener.com/latest/dex/tokens/{m}"
DS_SEARCH = "https://api.dexscreener.com/latest/dex/search"
GT_TOKEN = "https://api.geckoterminal.com/api/v2/networks/solana/tokens/{m}"
GT_POOLS = GT_TOKEN + "/pools"
RC_REPORT = "https://api.rugcheck.xyz/v1/tokens/{m}/report"
SYSTEM_PROGRAM = "11111111111111111111111111111111"
BURN = {SYSTEM_PROGRAM, "1nc1nerator11111111111111111111111111111111"}
B58 = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")
RANK = {"FAIL": 3, "WARN": 2, "UNKNOWN": 1, "PASS": 0, "INFO": -1}   # INFO never affects the verdict
DISCLAIMER = "Not advice. Nearly all meme coins are high risk."


# ---------------------------------------------------------------- HTTP
def http(url, body=None, retries=5, timeout=25, ttl=None):
    """Return (data, error). Backs off on 429 (honours Retry-After) and 5xx.
    Successful responses are cached briefly (netcache: ~3 min, 6 h for immutable Helius history)."""
    ttl = netcache.ttl_for(url, body) if ttl is None else ttl
    hit = netcache.get(url, body, ttl)
    if hit is not None:
        return hit, None
    hdr = {"User-Agent": UA, "Accept": "application/json"}
    if body is not None:
        hdr["Content-Type"] = "application/json"
    last = "unknown error"
    for i in range(retries):
        netcache.limit(url)
        try:
            if requests:
                r = (requests.post(url, json=body, headers=hdr, timeout=timeout) if body is not None
                     else requests.get(url, headers=hdr, timeout=timeout))
                code, text, ra = r.status_code, r.text, r.headers.get("Retry-After")
            else:
                req = urllib.request.Request(
                    url, data=json.dumps(body).encode() if body is not None else None, headers=hdr)
                try:
                    with urllib.request.urlopen(req, timeout=timeout) as r:
                        code, text, ra = r.status, r.read().decode("utf-8", "replace"), None
                except urllib.error.HTTPError as e:
                    code, text, ra = e.code, e.read().decode("utf-8", "replace"), e.headers.get("Retry-After")
            if code == 429 or code >= 500:
                last = f"HTTP {code}"
                if code == 429 and "helius-rpc.com" in url:
                    netcache.penalize(min(2 * 2 ** i, 8))     # every process backs off together
                try:
                    wait = float(ra) if ra else 0
                except ValueError:
                    wait = 0
                time.sleep(min(max(wait, 2 * 2 ** i), 45))
                continue
            if code != 200:
                return None, f"HTTP {code}"
            d = json.loads(text)
            if ttl and not (isinstance(d, dict) and d.get("error")):
                netcache.put(url, body, d)
            return d, None
        except Exception as e:  # network / JSON errors
            last = f"{type(e).__name__}: {e}"
            time.sleep(min(2 * 2 ** i, 20))
    return None, f"gave up after {retries} tries ({last})"


def rpc(method, params):
    d, err = http(RPC, {"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
    if err:
        return None, err
    if d.get("error"):
        return None, f"RPC error: {d['error'].get('message')}"
    return d.get("result"), None


# ---------------------------------------------------------------- helpers
def num(x):
    try:
        if x is None or x == "":
            return None
        return float(x)
    except (TypeError, ValueError):
        return None

def usd(x):
    if x is None: return "n/a"
    if abs(x) >= 1e9: return f"${x/1e9:.2f}B"
    if abs(x) >= 1e6: return f"${x/1e6:.2f}M"
    if abs(x) >= 1e3: return f"${x/1e3:.1f}k"
    return f"${x:,.0f}"

def pct(x, d=1):
    return "n/a" if x is None else f"{x:.{d}f}%"

def dur(sec):
    if sec < 3600: return f"{sec/60:.0f} min"
    if sec < 86400: return f"{sec/3600:.1f} h"
    return f"{sec/86400:.1f} d"

def worst(statuses):
    """FAIL > WARN > UNKNOWN > PASS (a PASS with an unknown part is not a full PASS)."""
    return max(statuses, key=lambda s: RANK[s]) if statuses else "UNKNOWN"

def chk(n, name, status, value, detail=""):
    return {"n": n, "name": name, "status": status, "value": value, "detail": detail}

def unk(n, name, why):
    return chk(n, name, "UNKNOWN", why)


# ---------------------------------------------------------------- data fetch
def gather(mint):
    S = {"errors": {}}
    with ThreadPoolExecutor(5) as ex:   # independent sources fetched in parallel
        # GeckoTerminal allows ~30 req/min: one call (token + top 3 pools); the full /pools list only if that has no pools
        f_ds, f_gt, f_rc = (ex.submit(http, u.format(m=mint)) for u in (DS_TOKEN, GT_TOKEN + "?include=top_pools", RC_REPORT))
        f_rpc = ex.submit(rpc, "getAccountInfo", [mint, {"encoding": "jsonParsed"}])
        (d_ds, e_ds), (d_gt, e_gt), (d_rc, e_rc) = f_ds.result(), f_gt.result(), f_rc.result()
        inc = [x for x in (d_gt or {}).get("included") or [] if x.get("type") == "pool"]
        d_gp, e_gp = ({"data": inc}, None) if inc else http(GT_POOLS.format(m=mint))
    d, e = d_ds, e_ds
    S["ds_pairs"] = (d or {}).get("pairs") or [] if not e else None
    S["ds_source"] = "dexscreener"
    if not S["ds_pairs"]:
        # DEX Screener's token endpoint sometimes answers 200 with no pairs for every coin: try search, then GeckoTerminal
        import ds as _ds
        ps, src = _ds.token_pairs(mint)
        if ps: S["ds_pairs"], S["ds_source"], e = ps, "dexscreener-search", None
        else:
            g = {"token": (d_gt or {}).get("data", {}).get("attributes") or {}, "pools": []}
            for x in (d_gt or {}).get("included") or []:
                if x.get("type") != "pool": continue
                rel = x.get("relationships") or {}
                a = dict(x["attributes"]); a["_base"] = ((rel.get("base_token") or {}).get("data") or {}).get("id", "")[7:]
                a["_quote"] = ((rel.get("quote_token") or {}).get("data") or {}).get("id", "")[7:]
                a["_dex"] = ((rel.get("dex") or {}).get("data") or {}).get("id"); g["pools"].append(a)
            gp = _ds.gt_to_pairs(mint, g)
            if gp:
                S["ds_pairs"], S["ds_source"], e = gp, "geckoterminal-fallback", None
                S["errors"]["dexscreener"] = "token endpoint returned no pairs; used GeckoTerminal pools (socials unavailable)"
            else:
                # only call it "no pairs" when DexS is healthy AND GeckoTerminal answered with no pools
                S["no_pairs_confirmed"] = bool(d_gt) and not _ds.degraded()
                if not S["no_pairs_confirmed"]:
                    S["errors"]["dexscreener"] = "no pairs returned (DEX Screener degraded or GeckoTerminal unavailable) - market checks UNKNOWN"
    if e: S["errors"]["dexscreener"] = e
    d, e = d_gt, e_gt
    S["gt_token"] = (d or {}).get("data", {}).get("attributes") if not e else None
    if e: S["errors"]["geckoterminal token"] = e
    d, e = d_gp, e_gp
    S["gt_pools"] = (d or {}).get("data") if not e else None
    if e: S["errors"]["geckoterminal pools"] = e
    d, e = d_rc, e_rc
    S["rc"] = d if not e else None
    if e: S["errors"]["rugcheck"] = e
    r, e = f_rpc.result()
    S["rpc_mint"] = r if not e else None
    S["rpc_mint_missing"] = (not e) and (r or {}).get("value") is None
    if e: S["errors"]["solana rpc"] = e
    # copycat search (needs ticker)
    sym = None
    exact = [p for p in (S["ds_pairs"] or []) if (p.get("baseToken") or {}).get("address") == mint]
    if exact:
        sym = exact[0]["baseToken"].get("symbol")
    elif S["gt_token"]:
        sym = S["gt_token"].get("symbol")
    elif S["rc"]:
        sym = (S["rc"].get("tokenMeta") or {}).get("symbol")
    S["symbol"] = sym
    S["ds_search"] = None
    if sym:
        d, e = http(DS_SEARCH + "?q=" + requests.utils.quote(sym) if requests else
                    DS_SEARCH + "?q=" + urllib.request.quote(sym))
        if e: S["errors"]["dexscreener search"] = e
        else: S["ds_search"] = (d or {}).get("pairs") or []
    return S


def derive(mint, S):
    """Shared, source-normalised view of the token."""
    D = {}
    ex = [p for p in (S["ds_pairs"] or []) if (p.get("baseToken") or {}).get("address") == mint
          and p.get("chainId") == "solana"]
    ex.sort(key=lambda p: -(num((p.get("liquidity") or {}).get("usd")) or 0))
    D["pairs"] = ex
    D["main"] = ex[0] if ex else None
    rc = S["rc"] or {}
    tm = rc.get("tokenMeta") or {}
    gt = S["gt_token"] or {}
    ext = {}
    try:
        for x in S["rpc_mint"]["value"]["data"]["parsed"]["info"].get("extensions", []):
            ext[x["extension"]] = x.get("state")
    except Exception:
        pass
    D["rpc_ext"] = ext
    m = D["main"]
    D["name"] = (m["baseToken"].get("name") if m else None) or gt.get("name") or tm.get("name") or (ext.get("tokenMetadata") or {}).get("name")
    D["symbol"] = (m["baseToken"].get("symbol") if m else None) or gt.get("symbol") or tm.get("symbol") or (ext.get("tokenMetadata") or {}).get("symbol")
    gp = sorted(S["gt_pools"] or [], key=lambda p: -(num(p["attributes"].get("reserve_in_usd")) or 0))
    D["gt_main"] = gp[0]["attributes"] if gp else None
    D["gt_pool_addrs"] = {p["attributes"].get("address") for p in gp}
    return D


# ---------------------------------------------------------------- checks
def c1_identity(mint, S, D):
    n, name = 1, "Identity / copycats"
    if S["ds_pairs"] is None:
        return unk(n, name, "DEX Screener unreachable")
    if not D["main"]:
        if not S.get("no_pairs_confirmed"):
            return unk(n, name, "no pair data (DEX Screener returned no pairs and GeckoTerminal had none/failed) - treated as UNKNOWN, not as delisted")
        return chk(n, name, "FAIL", "mint has no Solana pairs on DEX Screener or GeckoTerminal",
                   "cannot confirm the token you hold is the one being discussed")
    notes = []
    sym, nm = D["symbol"], D["name"]
    # cross-check metadata
    other = []
    tmeta = D["rpc_ext"].get("tokenMetadata") or {}
    rcm = (S["rc"] or {}).get("tokenMeta") or {}
    for src, s in (("RPC", tmeta.get("symbol")), ("RugCheck", rcm.get("symbol")),
                   ("GeckoTerminal", (S["gt_token"] or {}).get("symbol"))):
        if s and sym and s.strip().lower() != sym.strip().lower():
            other.append(f"{src} ticker '{s}' != '{sym}'")
    if S["ds_search"] is None:
        return chk(n, name, "UNKNOWN", f"exact mint confirmed ({nm} / {sym}); copycat search failed",
                   "; ".join(other))
    cop = {}
    for p in S["ds_search"]:
        b = p.get("baseToken") or {}
        if p.get("chainId") == "solana" and b.get("address") != mint and \
                (b.get("symbol") or "").strip().lower() == (sym or "").strip().lower():
            liq = num((p.get("liquidity") or {}).get("usd")) or 0
            cop[b["address"]] = max(cop.get(b["address"], 0), liq)
    k = len(cop)
    mainliq = sum(num((p.get("liquidity") or {}).get("usd")) or 0 for p in D["pairs"])
    big = [a for a, l in cop.items() if l > mainliq]
    sat = len(S["ds_search"]) >= 30
    val = f"exact mint confirmed on {'GeckoTerminal (DEX Screener down)' if S.get('ds_source') == 'geckoterminal-fallback' else 'DEX Screener'}; {k}{'+' if sat else ''} other Solana token(s) with ticker '{sym}'"
    if k:
        val += f" ({sum(1 for l in cop.values() if l >= 10000)} with >=$10k liq; largest {usd(max(cop.values()))})"
    det = []
    if big:
        top = max(cop, key=cop.get)
        det.append(f"{len(big)} same-ticker token(s) have MORE liquidity than this one (largest: {top}, {usd(cop[top])}) - double-check the mint")
    det += other
    if sat: det.append("search returned 30+ pairs, so copycat count is a lower bound")
    status = "WARN" if (k or other) else "PASS"
    return chk(n, name, status, val, "; ".join(det))


def c2_authorities(mint, S, D):
    n, name = 2, "Authorities / extensions"
    fails, warns, via = [], [], "RPC"
    info = None
    try:
        info = S["rpc_mint"]["value"]["data"]["parsed"]["info"]
        prog = S["rpc_mint"]["value"]["data"]["program"]
        ext = D["rpc_ext"]
    except Exception:
        info = None
    if info is None:
        rc = S["rc"]
        if not rc:
            return unk(n, name, "no mint data from Solana RPC or RugCheck (unreachable or mint not found)")
        via = "RugCheck (RPC unavailable)"
        t = rc.get("token") or {}
        info = {"mintAuthority": t.get("mintAuthority"), "freezeAuthority": t.get("freezeAuthority")}
        prog = "spl-token-2022" if "Tokenz" in (rc.get("tokenProgram") or "") else "spl-token"
        ext = {}
        te = rc.get("token_extensions") or {}
        if te.get("transferFeeConfig"): ext["transferFeeConfig"] = te["transferFeeConfig"]
        if te.get("permanentDelegate"): ext["permanentDelegate"] = te["permanentDelegate"]
        if te.get("transferHook"): ext["transferHook"] = te["transferHook"]
        if te.get("defaultAccountState"): ext["defaultAccountState"] = te["defaultAccountState"]
        if te.get("nonTransferable"): ext["nonTransferable"] = {}
    ma, fa = info.get("mintAuthority"), info.get("freezeAuthority")
    if ma: fails.append(f"mint authority ACTIVE ({ma[:6]}..)")
    if fa: fails.append(f"freeze authority ACTIVE ({fa[:6]}..)")
    for e, st in ext.items():
        st = st or {}
        if e == "transferFeeConfig":
            fees = [st.get("newerTransferFee") or {}, st.get("olderTransferFee") or {}] if "newerTransferFee" in st or "olderTransferFee" in st else [st]
            bps = max([num(f.get("transferFeeBasisPoints", f.get("pct"))) or 0 for f in fees])
            if bps > 0: fails.append(f"transfer fee {bps} bps" if "newerTransferFee" in st else f"transfer fee {bps}")
            elif st.get("transferFeeConfigAuthority"): warns.append("transfer-fee extension present at 0 bps (authority can raise it)")
        elif e == "permanentDelegate":
            if st.get("delegate") or st: fails.append(f"permanent delegate {str(st.get('delegate') or st)[:12]}..")
        elif e == "transferHook":
            if st.get("programId") or (via != "RPC" and st): fails.append(f"transfer hook program {str(st.get('programId') or '')[:8]}..")
            elif st.get("authority"): warns.append("transfer-hook extension unset but authority can set it")
        elif e == "defaultAccountState":
            if (st.get("accountState") or "").lower() == "frozen": fails.append("default account state FROZEN")
        elif e == "nonTransferable":
            fails.append("non-transferable")
        elif e == "pausableConfig":
            if st.get("authority"): fails.append("pausable (authority can pause transfers)")
        elif e == "mintCloseAuthority":
            if st.get("closeAuthority"): warns.append("mint close authority set")
    status = "FAIL" if fails else ("WARN" if warns else "PASS")
    val = (f"{prog}; mint auth {'REVOKED' if not ma else 'ACTIVE'}, freeze auth {'REVOKED' if not fa else 'ACTIVE'}; "
           f"extensions: {', '.join(sorted(ext)) or 'none'}")
    if via != "RPC": val += f" [via {via}]"
    det = "; ".join(fails + warns)
    return chk(n, name, status, val, det)


def total_liq(D):
    return sum(num((p.get("liquidity") or {}).get("usd")) or 0 for p in D["pairs"])


def mcap(D, S):
    m = D["main"]
    if m:
        v = num(m.get("marketCap"))
        if v: return v, "DEX Screener market cap"
        v = num(m.get("fdv"))
        if v: return v, "DEX Screener FDV"
    v = num((S["gt_token"] or {}).get("market_cap_usd")) or num((S["gt_token"] or {}).get("fdv_usd"))
    if v: return v, "GeckoTerminal FDV"
    return None, None


def c3_liq_mc(mint, S, D):
    n, name = 3, "Liquidity vs market cap"
    if not D["main"]:
        return unk(n, name, "no DEX Screener pair data")
    mc, src = mcap(D, S)
    liq = total_liq(D)
    if not mc: return unk(n, name, "market cap unavailable")
    r = liq / mc * 100
    st = "FAIL" if r < 5 else "WARN" if r < 10 else "PASS"
    m = D["main"]
    q, pn, pu = num((m.get("liquidity") or {}).get("quote")), num(m.get("priceNative")), num(m.get("priceUsd"))
    det = f"liq {usd(liq)} (both sides of pools) / mcap {usd(mc)} ({src})"
    if q and pn and pu and m["quoteToken"].get("symbol") == "SOL":
        det += f"; SOL-side of main pool ~{usd(q * pu / pn)}"
    return chk(n, name, st, f"{r:.1f}%", det)


def c4_liq_abs(mint, S, D):
    n, name = 4, "Liquidity (absolute)"
    if not D["main"]: return unk(n, name, "no DEX Screener pair data")
    liq = total_liq(D)
    xs = [f"DexS {usd(liq)}"]
    g = num((S["gt_token"] or {}).get("total_reserve_in_usd"))
    if g is not None: xs.append(f"GeckoT {usd(g)}")
    r = num((S["rc"] or {}).get("totalMarketLiquidity"))
    if r is not None: xs.append(f"RugCheck {usd(r)}")
    return chk(n, name, "WARN" if liq < 50000 else "PASS", usd(liq),
               f"{len(D['pairs'])} Solana pair(s); " + " | ".join(xs))


def c5_age(mint, S, D):
    n, name = 5, "Token / pool age"
    ts = []
    for p in D["pairs"]:
        if p.get("pairCreatedAt"): ts.append((p["pairCreatedAt"] / 1000, "DexS pair"))
    for p in S["gt_pools"] or []:
        s = p["attributes"].get("pool_created_at")
        if s:
            try: ts.append((datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp(), "GeckoT pool"))
            except ValueError: pass
    s = (S["rc"] or {}).get("detectedAt")
    if s:
        try: ts.append((datetime.fromisoformat(s[:26].rstrip("Z").split(".")[0] + "+00:00").timestamp(), "RugCheck first seen"))
        except ValueError: pass
    if not ts: return unk(n, name, "no creation timestamp from any source")
    t, src = min(ts)
    age = time.time() - t
    st = "FAIL" if age < 3600 else "WARN" if age < 86400 else "PASS"
    when = datetime.fromtimestamp(t).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    return chk(n, name, st, dur(age), f"earliest: {src} @ {when}; pump.fun bonding-curve time before pair creation may be missed")


def excluded_owners(mint, S, D):
    """Owners to treat as pool/program (not real holders). Returns (set, labels, error)."""
    rc = S["rc"] or {}
    ex, labels = {}, {}
    for k, v in (rc.get("knownAccounts") or {}).items():
        ex[k] = f"{v.get('name')} ({v.get('type')})"
    for m in rc.get("markets") or []:
        for key in ("pubkey", "liquidityA", "liquidityB"):
            if m.get(key): ex.setdefault(m[key], "pool account")
    for p in D["pairs"]:
        ex.setdefault(p.get("pairAddress"), "DEX pair")
    for a in D["gt_pool_addrs"]:
        ex.setdefault(a, "DEX pool")
    for b in BURN: ex.setdefault(b, "burn")
    # program-owned owner accounts via RPC (PDAs that exist on-chain)
    err = None
    owners = [h.get("owner") for h in rc.get("topHolders") or [] if h.get("owner") and h.get("owner") not in ex]
    for i in range(0, len(owners), 10):  # publicnode rejects larger batches (HTTP 403)
        r, e = rpc("getMultipleAccounts", [owners[i:i + 10], {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0}}])
        if e:
            err = e
            continue
        for o, a in zip(owners[i:i + 10], (r or {}).get("value") or []):
            if a and (a.get("executable") or a.get("owner") != SYSTEM_PROGRAM):
                ex[o] = f"program-owned ({a.get('owner')[:6]}..)"
    return ex, err


def c6_holders(mint, S, D):
    n, name = 6, "Top-10 holders (excl. pools/programs)"
    rc = S["rc"]
    if not rc or not rc.get("topHolders"): return unk(n, name, "RugCheck holder data unavailable")
    ex, err = excluded_owners(mint, S, D)
    rows = rc["topHolders"]
    kept, dropped = [], []
    for h in rows:
        lab = ex.get(h.get("owner")) or ex.get(h.get("address"))
        (dropped if lab else kept).append((h, lab))
    top = [h for h, _ in kept][:10]
    tot = sum(h["pct"] for h in top)
    dp = sum(h["pct"] for h, _ in dropped)
    nonpool = 100 - dp
    st = "FAIL" if tot > 40 else "WARN" if tot > 25 else "PASS"
    det = f"excluded {len(dropped)} of top {len(rows)} accounts = {dp:.1f}% of supply ({', '.join(sorted({l for _, l in dropped}))[:90] or 'none'})"
    if len(top) < 10: det += f"; only {len(top)} wallets left in RugCheck's top-{len(rows)} (lower bound)"
    if nonpool > 0 and dp > 0: det += f"; = {tot / nonpool * 100:.0f}% of non-pool supply"
    if err: det += "; program-owner lookup via RPC failed"
    det += f"; {rc.get('totalHolders')} holders total"
    return chk(n, name, st, f"{tot:.1f}% of supply", det)


def c7_insiders(mint, S, D):
    n, name = 7, "Insiders / bundles / LP lock"
    rc = S["rc"]
    if not rc: return unk(n, name, "RugCheck unreachable")
    sup = num((rc.get("token") or {}).get("supply")) or 0
    sts, parts = [], []
    nets = rc.get("insiderNetworks")
    gi = rc.get("graphInsidersDetected")
    if sup:
        held = sum(num(x.get("currentHolding")) or 0 for x in nets or []) / sup * 100
        big = max([x.get("size", 0) for x in nets or []] or [0])
        sts.append("FAIL" if held >= 30 else "WARN" if (held >= 10 or nets) else "PASS")
        parts.append(f"insider networks: {len(nets or [])} holding {held:.1f}% (largest {big} wallets); graph insiders {gi if gi is not None else 'n/a'}")
        cb = (num(rc.get("creatorBalance")) or 0) / sup * 100
        sts.append("FAIL" if cb >= 20 else "WARN" if cb >= 5 else "PASS")
        parts.append(f"creator balance {cb:.2f}%")
    else:
        sts.append("UNKNOWN"); parts.append("supply missing")
    flagged = [h for h in rc.get("topHolders") or [] if h.get("insider")]
    if flagged:
        sts.append("WARN"); parts.append(f"{len(flagged)} top holder(s) flagged insider ({sum(h['pct'] for h in flagged):.1f}%)")
    # LP lock: liquidity-weighted over markets that have LP tokens (CLMM/DLMM/orderbook positions have none)
    lk = tot = 0.0
    skipped = 0.0
    for m in rc.get("markets") or []:
        l = m.get("lp") or {}
        liq = (num(l.get("baseUSD")) or 0) + (num(l.get("quoteUSD")) or 0)
        if not liq: continue
        if (l.get("lpMint") or SYSTEM_PROGRAM) == SYSTEM_PROGRAM:
            skipped += liq; continue
        tot += liq
        lk += min(num(l.get("lpLockedUSD")) or 0, liq)
    if tot > 0:
        p = lk / tot * 100
        sts.append("FAIL" if p < 10 else "WARN" if p < 80 else "PASS")
        parts.append(f"LP locked/burned {p:.1f}% of {usd(tot)} LP-token liquidity (per RugCheck)" +
                     (f"; {usd(skipped)} in pools with no LP token (DLMM/CLMM etc.) can't be 'locked'" if skipped else ""))
    else:
        sts.append("UNKNOWN"); parts.append("LP locked %: no LP-token market data from RugCheck")
    rk = [f"{r['name']} {r.get('value','')}".strip() for r in rc.get("risks") or []]
    if rc.get("rugged"): sts.append("FAIL"); parts.append("RugCheck marks token RUGGED")
    return chk(n, name, worst(sts), "; ".join(parts), ("RugCheck risks: " + ", ".join(rk)) if rk else "RugCheck risks: none listed")


def c8_activity(mint, S, D):
    n, name = 8, "Turnover / bot pattern"
    if not D["pairs"]: return unk(n, name, "no DEX Screener pair data")
    liq = total_liq(D)
    vol = sum(num((p.get("volume") or {}).get("h24")) or 0 for p in D["pairs"])
    if not liq: return unk(n, name, "zero liquidity")
    to = vol / liq
    sts = ["WARN" if to > 10 else "PASS"]
    parts = [f"24h vol {usd(vol)} / liq {usd(liq)} = {to:.1f}x"]
    det = []
    g = D["gt_main"]
    t = ((g or {}).get("transactions") or {}).get("h24")
    if t and (t.get("buyers") or t.get("sellers")):
        tx = (t.get("buys") or 0) + (t.get("sells") or 0)
        w = (t.get("buyers") or 0) + (t.get("sellers") or 0)
        r = tx / w if w else None
        parts.append(f"24h {t['buys']} buys/{t['sells']} sells from {t['buyers']} buyers/{t['sellers']} sellers (main pool) = {r:.2f} tx per wallet-side")
        sts.append("WARN" if r and r > 10 else "PASS")
        # bot-ish heuristics (informational, WARN only on strong signals)
        if tx:
            bs = t["buys"] / max(t["sells"], 1)
            if bs > 5 or bs < 0.2: sts.append("WARN"); det.append(f"lopsided buy/sell count ratio {bs:.2f}")
            avg = (num(((g or {}).get("volume_usd") or {}).get("h24")) or 0) / tx
            det.append(f"avg trade {usd(avg)}")
        for win in ("h1", "h6"):
            tw = ((g or {}).get("transactions") or {}).get(win) or {}
            ww = (tw.get("buyers") or 0) + (tw.get("sellers") or 0)
            txw = (tw.get("buys") or 0) + (tw.get("sells") or 0)
            if ww and txw / ww > 10: sts.append("WARN"); det.append(f"{win}: {txw} tx from {ww} wallet-sides (>10x)")
    else:
        sts.append("UNKNOWN"); parts.append("unique-wallet counts unavailable (GeckoTerminal)")
        m = D["main"]
        tx = m.get("txns", {}).get("h24") if m else None
        if tx: det.append(f"DexS 24h: {tx.get('buys')} buys / {tx.get('sells')} sells")
    return chk(n, name, worst(sts), "; ".join(parts), "; ".join(det))


def c9_momentum(mint, S, D):
    n, name = 9, "Price momentum"
    pc = dict((D["main"] or {}).get("priceChange") or {})
    gc = (D["gt_main"] or {}).get("price_change_percentage") or {}
    for k in ("m5", "h1", "h6", "h24"):
        if pc.get(k) is None and gc.get(k) is not None: pc[k] = gc[k]
    h6, h24 = num(pc.get("h6")), num(pc.get("h24"))
    if h6 is None and h24 is None: return unk(n, name, "no price-change data")
    vals = [v for v in (h6, h24) if v is not None]
    mx = max(vals)
    st = "FAIL" if mx >= 500 else "WARN" if mx > 200 else "PASS"
    fmt = lambda k: f"{k} {num(pc.get(k)):+.0f}%" if num(pc.get(k)) is not None else f"{k} n/a"
    det = ""
    if min(vals) <= -70: det = "already down >=70% - a past pump/dump, check is about chasing pumps only"
    return chk(n, name, st, f"{fmt('h24')}, {fmt('h6')}, {fmt('h1')}, {fmt('m5')}", det)


def c10_meta(mint, S, D):
    n, name = 10, "Socials / metadata"
    sts, parts = [], []
    infos = [p.get("info") or {} for p in D["pairs"]]
    if S.get("ds_source") == "geckoterminal-fallback" and D["pairs"]:
        sts.append("UNKNOWN"); parts.append("socials: unknown (DEX Screener down; GeckoTerminal fallback has no socials)")
    elif S["ds_pairs"] is None or not D["pairs"]:
        sts.append("UNKNOWN"); parts.append("socials: no DEX Screener pair data" if S["ds_pairs"] is not None else "socials: DEX Screener unreachable")
    else:
        webs = [w["url"] for i in infos for w in i.get("websites") or []]
        xs = [s["url"] for i in infos for s in i.get("socials") or [] if s.get("type") in ("twitter", "x")]
        tg = [s["url"] for i in infos for s in i.get("socials") or [] if s.get("type") == "telegram"]
        parts.append(f"website {'yes' if webs else 'NO'}, X {'yes' if xs else 'NO'}" + (", telegram yes" if tg else "")
                     + (f" ({(xs or webs)[0][:40]})" if (xs or webs) else ""))
        sts.append("PASS" if webs and xs else "WARN")
    tmeta = D["rpc_ext"].get("tokenMetadata")
    rcm = (S["rc"] or {}).get("tokenMeta")
    if tmeta is not None:
        ua = tmeta.get("updateAuthority")
        parts.append("metadata IMMUTABLE (update authority none)" if not ua else f"metadata MUTABLE (update authority {ua[:6]}..)")
        sts.append("PASS" if not ua else "WARN")
    elif rcm is not None:
        mu = rcm.get("mutable")
        parts.append("metadata " + ("MUTABLE" if mu else "IMMUTABLE") + " (per RugCheck)")
        sts.append("WARN" if mu else "PASS")
    else:
        sts.append("UNKNOWN"); parts.append("metadata mutability: no source reachable")
    return chk(n, name, worst(sts), "; ".join(parts))


CHECKS = [c1_identity, c2_authorities, c3_liq_mc, c4_liq_abs, c5_age, c6_holders, c7_insiders, c8_activity, c9_momentum, c10_meta]


def run(mint):
    S = gather(mint)
    D = derive(mint, S)
    known = set(D["gt_pool_addrs"]) | {p.get("pairAddress") for p in D["pairs"]}
    for m in (S["rc"] or {}).get("markets") or []:
        known |= {m.get(k) for k in ("pubkey", "liquidityA", "liquidityB")}
    known |= {k for k, v in ((S["rc"] or {}).get("knownAccounts") or {}).items()
              if (v or {}).get("type") not in ("CREATOR",)}
    known.discard(None)
    try: dec = S["rpc_mint"]["value"]["data"]["parsed"]["info"]["decimals"]
    except Exception: dec = None
    main_pair = (D["main"] or {}).get("pairAddress")
    with ThreadPoolExecutor(3) as ex:    # Helius gather, Jupiter exit quotes and wash-trade read run in parallel
        f_h = ex.submit(helius_checks.gather, mint, http, known)
        f_x = ex.submit(exit_liq.test, mint)
        f_w = ex.submit(wash.gather, mint, main_pair, http, num((D["main"] or {}).get("priceUsd")), dec, known)
        S["helius"] = f_h.result()
        try: S["exit"] = f_x.result()
        except Exception as e: S["exit"] = {"error": f"quote errored: {type(e).__name__}", "sizes": {}}
        try: S["wash"] = f_w.result()
        except Exception as e: S["wash"] = {"error": f"{type(e).__name__}"}
    res = []
    for f in CHECKS:
        try:
            res.append(f(mint, S, D))
        except Exception as e:  # a bug/odd data must not fake a result
            res.append(unk(CHECKS.index(f) + 1, f.__doc__ or f.__name__, f"check errored: {type(e).__name__}: {e}"))
    try:
        res += helius_checks.checks(mint, S["helius"], chk, unk)
    except Exception as e:
        res.append(chk(11, "Helius on-chain checks", "WARN", f"not checked - {helius_checks.scrub(e)}"))
    try:
        st, val, det = exit_liq.grade(S["exit"])
        res.append(chk(16, "Exit liquidity (Jupiter quotes)", st, val, det))
    except Exception as e:
        res.append(unk(16, "Exit liquidity (Jupiter quotes)", f"quote errored: {type(e).__name__}"))
    try:
        st, val, det = smart_money.check(mint, S["helius"], S.get("wash"))
        res.append(chk(17, "Smart-money wallets (info)", st, val, det))
    except Exception as e:
        res.append(chk(17, "Smart-money wallets (info)", "INFO", f"not checked - {type(e).__name__}"))
    try:
        st, val, det = wash.grade(S.get("wash"))
        res.append(chk(18, "Wash trading (recent swaps)", st, val, det))
    except Exception as e:
        res.append(chk(18, "Wash trading (recent swaps)", "WARN", f"not checked - {helius_checks.scrub(e)}"))
    try:
        import operator_index
        st, val, det, links_ = operator_index.check(mint, S.get("helius") or {}, D["symbol"])
        res.append(chk(19, "Same operator as other coins", st, val, det))
        S["operator_links"] = links_
    except Exception as e:
        res.append(chk(19, "Same operator as other coins", "INFO", f"not checked - {type(e).__name__}: {helius_checks.scrub(e)}"))
    counts = {k: sum(1 for r in res if r["status"] == k) for k in RANK}
    if counts["FAIL"]: v = "SKIP"
    elif counts["WARN"] >= 3: v = "CAUTION"
    else: v = "PASSES-BASIC-CHECKS"
    links = {"dexscreener": f"https://dexscreener.com/solana/{mint}"}
    if mint.endswith("pump"): links["pump.fun"] = f"https://pump.fun/coin/{mint}"
    links["rugcheck"] = f"https://rugcheck.xyz/tokens/{mint}"
    unchecked = [f"#{r['n']} {r['name']}: {r['value']}" for r in res if r["status"] == "UNKNOWN"]
    unchecked += [f"source unreachable - {k}: {v_}" for k, v_ in S["errors"].items()]
    H = S.get("helius") or {}
    if H.get("error"): unchecked.append(f"Helius: {H['error']}")
    unchecked += [
        "Helius holder list = top 20 token accounts only; CEX/custodial wallets are not labelled",
        f"Bundle scan covers slots 0-{helius_checks.EARLY_SLOTS} after creation only; funder trace = first funder + top-ups in the last {helius_checks.TRACE_TXS} pre-launch txs + outflows of up to {helius_checks.TRACE_OUT} candidate hubs, max 3 hops (mixers/exchanges not walked through)",
        "Wash-trade check reads only the last ~200 pool txs; social accounts' authenticity, team doxxing and contract audit are not verified",
    ]
    W = S.get("wash") or {}
    out = {"mint": mint, "name": D["name"], "ticker": D["symbol"], "links": links,
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "checks": res, "counts": counts, "verdict": v, "disclaimer": DISCLAIMER,
            "could_not_check": unchecked, "source_errors": S["errors"],
            "market": {"price_usd": num((D["main"] or {}).get("priceUsd")), "mcap_usd": mcap(D, S)[0],
                       "liq_usd": (total_liq(D) if D["pairs"] else (0.0 if S.get("no_pairs_confirmed") else None)),
                       "source": S.get("ds_source") if D["pairs"] else None},
            "exit": S.get("exit"),
            "wash": {k: v for k, v in W.items() if k != "makers_net"},
            "helius": {k: v for k, v in H.items() if k not in ("funder_detail",)},
            "helius_credits_est": (H.get("credits_est") or 0) + (W.get("credits_est") or 0)}
    if isinstance(out["helius"].get("trace"), dict):
        out["helius"]["trace"] = {k: v for k, v in out["helius"]["trace"].items() if k not in ("ancestor_reach",)}
    out["operator_links"] = S.get("operator_links") or []
    out["ds_source"] = S.get("ds_source")
    try:
        out["risk"] = risk_mod.score(out)
    except Exception as e:
        out["risk"] = {"score": None, "band": "n/a", "drivers": [f"risk score errored: {type(e).__name__}"]}
    try:
        import operator_index
        operator_index.record(out)
    except Exception:
        pass
    try:
        netcache.ledger(os.environ.get("SC_LEDGER_SRC", "scorecard"), out["helius_credits_est"], (H.get("calls") or 0), {"mint": mint})
    except Exception:
        pass
    return out


def esc(s): return str(s).replace("|", "\\|")

def render(R):
    L = [f"# Token scorecard: {R['name'] or 'UNKNOWN'} (${R['ticker'] or '?'})", "",
         f"- **Mint:** `{R['mint']}`",
         "- **Links:** " + " | ".join(f"[{k}]({u})" for k, u in R["links"].items()),
         f"- **Generated:** {R['generated_at']}", ""]
    rk = R.get("risk") or {}
    if rk.get("score") is not None:
        L += [f"**Risk score: {rk['score']}/100 ({rk['band']}; weights {rk.get('weights_version', 'v1')})** - verdict {R['verdict']}. Main drivers: " + "; ".join(rk.get("drivers") or ["none"]), ""]
    L += ["| # | Check | Status | Actual |", "|---|---|---|---|"]
    for c in R["checks"]:
        val = c["value"] + (f" - _{c['detail']}_" if c["detail"] else "")
        L.append(f"| {c['n']} | {esc(c['name'])} | **{c['status']}** | {esc(val)} |")
    k = R["counts"]
    L += ["", f"**Verdict: {R['verdict']}** - {k['FAIL']} FAIL, {k['WARN']} WARN, {k['PASS']} PASS, {k['UNKNOWN']} UNKNOWN"
          + (f"; risk score {rk['score']}/100" if rk.get("score") is not None else "") + f". _{R['disclaimer']}_", ""]
    if k["UNKNOWN"]: L.append(f"_{k['UNKNOWN']} check(s) UNKNOWN, so the verdict is incomplete._\n")
    L += ["**Could not check / limits:**"] + [f"- {x}" for x in R["could_not_check"]]
    return "\n".join(L) + "\n"


def write_check_log(R, src):
    """One line per scorecard run in check_log.jsonl: every check's status + key value, risk (current and v1 weights)."""
    import fcntl
    rk = R.get("risk") or {}; m = R.get("market") or {}
    try: v1 = risk_mod.score(R, version="v1")["score"] if rk.get("weights_version") != "v1" else rk.get("score")
    except Exception: v1 = None
    rec = {"kind": "score", "time": R["generated_at"], "mint": R["mint"], "ticker": R["ticker"], "src": src,
           "run": "rescore" if "rescore" in src else "first", "verdict": R["verdict"], "counts": R.get("counts"),
           "risk": rk.get("score"), "weights_version": rk.get("weights_version"), "risk_v1": v1,
           "incomplete": rk.get("incomplete"), "price": m.get("price_usd"), "mcap": m.get("mcap_usd"), "liq": m.get("liq_usd"),
           "ds_source": R.get("ds_source"), "credits": R.get("helius_credits_est"),
           "checks": [{"n": c["n"], "s": c["status"], "v": str(c.get("value") or "")[:140]} for c in R.get("checks") or []]}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_log.jsonl")
    with open(path + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        with open(path, "a") as f: f.write(json.dumps(rec, default=str) + "\n")


def main():
    ap = argparse.ArgumentParser(description="Solana token pass/fail scorecard (free sources). " + DISCLAIMER)
    ap.add_argument("mint")
    ap.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    ap.add_argument("--out", help="also write output to this file")
    ap.add_argument("--no-log", action="store_true", help="do not append to score_log.jsonl")
    ap.add_argument("--no-check-log", action="store_true", help="do not append per-check results to check_log.jsonl")
    ap.add_argument("--src", default="scorecard", help=argparse.SUPPRESS)
    a = ap.parse_args()
    if not B58.match(a.mint):
        sys.exit("error: not a valid base58 Solana address")
    R = run(a.mint)
    if not a.no_log:
        try:
            m = R.get("market") or {}
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "score_log.jsonl"), "a") as f:
                f.write(json.dumps({"mint": R["mint"], "ticker": R["ticker"], "time": R["generated_at"], "verdict": R["verdict"],
                                    "price": m.get("price_usd"), "mcap": m.get("mcap_usd"), "liq": m.get("liq_usd"),
                                    "risk": (R.get("risk") or {}).get("score"), "src": a.src,
                                    "wv": (R.get("risk") or {}).get("weights_version")}) + "\n")
        except Exception as e:
            print(f"(score_log write failed: {type(e).__name__})", file=sys.stderr)
    if not a.no_check_log:       # per-check results (first scores AND re-scores; re-scores skip score_log but not this)
        try:
            write_check_log(R, a.src)
        except Exception as e:
            print(f"(check_log write failed: {type(e).__name__})", file=sys.stderr)
    out = json.dumps(R, indent=2) if a.json else render(R)
    print(out)
    if a.out:
        open(a.out, "w").write(out + "\n")


if __name__ == "__main__":
    main()
