# Last scan 2026-11-28T13:18:01Z - mode: helius (box heartbeat stale (549 min); budget 394/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 111 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored ACT in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored Fireball in 88s
[fast_scan] scored BITCOINU in 99s
[fast_scan] scored NINE in 100s
[fast_scan] scored BITCOINU in 105s
[fast_scan] scored Rizzmas in 81s
# Market scan 2026-11-28 13:17 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,204 (-3.7% 24h), ETH $1,647 (-4.3% 24h), SOL $70.78 (-3.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.9% (mcap $1.82B, vol $360.45M), pump-fun -1.9% (mcap $791.42M, vol $143.66M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [NINE](https://dexscreener.com/solana/GKHx5vA1PKRWuXvPdD5UVqPdhGgaQHzYNaiHg7WPrcsB) | `GKHx5vA1PKRWuXvPdD5UVqPdhGgaQHzYNaiHg7WPrcsB` | $215.9k | $123.2k | 2.1 h | h24 +72% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 47* | CAUTION | [BITCOINU](https://dexscreener.com/solana/54TPNZr3giK5DFkBgUGjn9WR88a9G876mW6XMpB6gfty) | `54TPNZr3giK5DFkBgUGjn9WR88a9G876mW6XMpB6gfty` | $201.2k | $109.7k | 1.1 h | h24 +39% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $188.5k | $876.1k | 16.6 h | h24 +1870% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $51.8k | $483.2k | 23.1 h | h24 +1312% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $310.8k | $16.42M | 2.5 d | h24 +44% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.7); #6 unknown (+3) |
| 62* | SKIP | [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $78.4k | $1.16M | 8.5 h | h24 +3136% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $225.5k | $672.8k | 1069.8 d | h24 +5% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,818 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.16M | $8.90M | 770.1 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 136,201 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.85M | $14.04M | 20785.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,627 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $78.2k | $1.15M | +9% | +32% | +3118% | 20.7x | none flagged (still high risk) | 62 |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $68.1k | $890.9k | -19% | -4% | +2619% | 14.1x | lopsided buys/sells 3.12 | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $92.2k | $858.4k | +10% | +111% | +1830% | 49.7x | churn 50x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $51.8k | $483.2k | +14% | +1% | +1312% | 35.3x | churn 35x vol/liq | 56 |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $42.6k | $303.8k | -5% | +9% | +953% | 45.1x | thin liq $42.6k; churn 45x vol/liq | not scored |
| [Mojave](https://dexscreener.com/solana/44ip5iXnsaCFvK7du9XdhzvbdXWxrWSyjNQDByeBamGX) | `44ip5iXnsaCFvK7du9XdhzvbdXWxrWSyjNQDByeBamGX` | $191.7k | $143.3k | +60% | +180% | +180% | 36.8x | churn 37x vol/liq; lopsided buys/sells 3.06 | not scored |

_Timing: total 225s (discovery 71.7s, screen 1.1s, GT prime 0.4s, scoring 151.5s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
