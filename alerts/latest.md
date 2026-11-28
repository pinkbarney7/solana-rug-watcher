# Last scan 2026-11-28T05:11:53Z - mode: helius (box heartbeat stale (64 min); budget 10/3000)

```
[fast_scan] 128 candidate mints from 10 source tags; 127 with pair data; 25 >= $50,000 liq; 11 pass survivor pre-gates (64s)
[fast_scan] scored UGOS in 77s
[fast_scan] scored USOI in 77s
[fast_scan] scored PUMPCHAN in 77s
[fast_scan] scored Pnut  in 77s
[fast_scan] scored MoonBoy in 78s
[fast_scan] scored ACT in 78s
[fast_scan] scored Rizzmas in 78s
# Market scan 2026-11-28 05:11 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,800 (-2.9% 24h), ETH $1,656 (-4.8% 24h), SOL $71.31 (-2.3% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.6% (mcap $1.87B, vol $270.43M), pump-fun +1.5% (mcap $804.74M, vol $96.59M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $321.0k | $17.45M | 2.2 d | h24 +57% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $102.8k | $455.3k | 8.6 h | h24 +924% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $934.0k | $173.58M | 1.3 d | h24 +64% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $775.8k | $119.83M | 1.4 d | h24 +19% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.8k | $637.9k | 1069.5 d | h24 -7% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,801 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.18M | $9.13M | 769.7 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 136,193 (growth n/a: first sighting) |
| 56* | SKIP | [Pnut ](https://pump.fun/coin/2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump) | `2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump` | $2.04M | $26.86M | 757.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 269,294 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $94.9k | $1.76M | +4799% | +4799% | +4799% | 6.7x | spike (+4799% 1h, +4799% 6h); < 1h old | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $64.0k | $793.9k | +35% | +2323% | +2323% | 10.5x | spike (+35% 1h, +2323% 6h); lopsided buys/sells 4.21 | not scored |
| [Frogger](https://pump.fun/coin/GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump) | `GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump` | $22.3k | $99.5k | +232% | +232% | +232% | 21.7x | thin liq $22.3k; spike (+232% 1h, +232% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $69.0k | $499.5k | -16% | +82% | +1023% | 58.9x | churn 59x vol/liq | 55 |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $19.9k | $80.8k | +180% | +180% | +180% | 24.6x | thin liq $19.9k; spike (+180% 1h, +180% 6h); < 1h old | not scored |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $47.9k | $426.8k | +3% | -36% | +1147% | 28.1x | thin liq $47.9k; churn 28x vol/liq | not scored |

_Timing: total 142s (discovery 62.5s, screen 1.3s, GT prime 0.1s, scoring 78.2s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 52/142; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
