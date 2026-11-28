# Last scan 2026-11-28T12:52:12Z - mode: helius (box heartbeat stale (523 min); budget 394/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 114 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored MoonBoy in 71s
[fast_scan] scored ACT in 79s
[fast_scan] scored BITCOINU in 80s
[fast_scan] scored NINE in 80s
[fast_scan] scored SPCX in 80s
[fast_scan] scored BASKET in 82s
[fast_scan] scored PUMPCHAN in 88s
[fast_scan] scored UGOS in 106s
[fast_scan] scored Rizzmas in 77s
# Market scan 2026-11-28 12:52 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,185 (-3.8% 24h), ETH $1,647 (-4.3% 24h), SOL $70.78 (-3.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.6% (mcap $1.82B, vol $368.43M), pump-fun -1.8% (mcap $792.23M, vol $143.79M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [NINE](https://dexscreener.com/solana/GKHx5vA1PKRWuXvPdD5UVqPdhGgaQHzYNaiHg7WPrcsB) | `GKHx5vA1PKRWuXvPdD5UVqPdhGgaQHzYNaiHg7WPrcsB` | $202.1k | $114.7k | 1.6 h | h24 +60% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 47* | CAUTION | [BASKET](https://dexscreener.com/solana/RTmAZjczYvBBjaysjSn4bdQvQAqZxxNCEvyZKQZuZh4) | `RTmAZjczYvBBjaysjSn4bdQvQAqZxxNCEvyZKQZuZh4` | $102.7k | $58.7k | 1.1 h | h24 +52% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $169.8k | $850.2k | 16.2 h | h24 +1811% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $314.3k | $16.80M | 2.5 d | h24 +46% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.8); #6 unknown (+3) |
| 59* | SKIP | [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $77.9k | $1.15M | 8.1 h | h24 +3101% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 63* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $978.9k | $192.34M | 1.6 d | h24 +55% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $223.9k | $663.3k | 1069.8 d | h24 +4% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,812 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.17M | $8.96M | 770.1 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 136,201 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.85M | $14.18M | 20785.5 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.0% in 1h (now 403,627) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $77.9k | $1.15M | +13% | +39% | +3101% | 20.4x | none flagged (still high risk) | 59 |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $60.4k | $705.0k | -37% | -24% | +2051% | 15.5x | lopsided buys/sells 3.16 | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $91.7k | $850.2k | +13% | +75% | +1811% | 49.5x | churn 49x vol/liq | 54 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $49.5k | $442.1k | +16% | -0% | +1192% | 36.5x | thin liq $49.5k; churn 37x vol/liq | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $44.5k | $330.6k | -5% | +50% | +1046% | 42.8x | thin liq $44.5k; churn 43x vol/liq | not scored |
| [Mojave](https://dexscreener.com/solana/44ip5iXnsaCFvK7du9XdhzvbdXWxrWSyjNQDByeBamGX) | `44ip5iXnsaCFvK7du9XdhzvbdXWxrWSyjNQDByeBamGX` | $173.9k | $124.9k | +90% | +144% | +144% | 28.7x | churn 29x vol/liq; lopsided buys/sells 3.08 | not scored |

_Timing: total 221s (discovery 71.8s, screen 1.2s, GT prime 0.4s, scoring 147.9s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/176; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
