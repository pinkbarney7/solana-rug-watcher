"""Major non-meme mints (stablecoins, wrapped/liquid-staked SOL, wrapped BTC/ETH, large infra tokens).
Buying these is routine treasury/swap activity, never an operator or smart-money "meme buy" signal, so the realtime
daemon, wallet_watch, smart_money, fast_scan discovery and wallet profiles ignore them. Extra mints can be added to
non_meme_mints.json (a JSON list or {"mints": [...]}) without code changes."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
NON_MEME = {
    "So11111111111111111111111111111111111111112": "wSOL",
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v": "USDC",
    "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB": "USDT",
    "2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo": "PYUSD",
    "USDSwr9ApdHk5bvJKMjzff41FfuX8bSxdKcR81vTwcA": "USDS",
    "USD1ttGY1N17NEEHLmELoaybftRBUSErhqYiQzvEmuB": "USD1",
    "HzwqbKZw8HxMN6bF2yFZNrht3c2iXXzpKcFu7uBEDKtr": "EURC",
    "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So": "mSOL",
    "J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn": "JitoSOL",
    "bSo13r4TkiE4KumL71LsHTPpL2euBYLFx6h9HP3piy1": "bSOL",
    "jupSoLaHXQiZZTSfEWMTRRgpnyFm8f6sZdosWBjx93v": "JupSOL",
    "5oVNBeEEQvYi1cX3ir8Dx5n1P7pdxydbGF2X4TxVusJm": "INF",
    "cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij": "cbBTC",
    "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs": "wETH",
    "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN": "JUP",
    "jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL": "JTO",
    "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R": "RAY",
    "HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3": "PYTH",
}
_EXTRA = [0.0, set()]


def all_mints():
    p = os.path.join(HERE, "non_meme_mints.json")
    try:
        mt = os.path.getmtime(p)
        if mt != _EXTRA[0]:
            d = json.load(open(p)); d = d.get("mints", []) if isinstance(d, dict) else d
            _EXTRA[0], _EXTRA[1] = mt, {str(x) for x in d}
    except (OSError, ValueError):
        pass
    return set(NON_MEME) | _EXTRA[1]


def is_major(mint):
    return bool(mint) and (mint in NON_MEME or mint in _EXTRA[1] or mint in all_mints())
