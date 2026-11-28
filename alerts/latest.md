# Last scan 2026-11-28T05:09:08Z - mode: helius (box heartbeat stale (61 min); budget 0/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 126 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored USOI in 79s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored UGOS in 80s
[fast_scan] scored Pnut  in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-28 05:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,855 (-2.7% 24h), ETH $1,658 (-4.5% 24h), SOL $71.44 (-2.0% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.6% (mcap $1.87B, vol $270.43M), pump-fun +1.5% (mcap $804.74M, vol $96.59M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $321.0k | $17.45M | 2.2 d | h24 +57% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $102.8k | $455.3k | 8.5 h | h24 +924% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $934.0k | $173.58M | 1.3 d | h24 +64% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $775.8k | $119.83M | 1.4 d | h24 +19% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.8k | $637.9k | 1069.5 d | h24 -7% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,801 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.18M | $9.13M | 769.7 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 69h (now 136,193) |
| 56* | SKIP | [Pnut ](https://pump.fun/coin/2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump) | `2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump` | $2.04M | $26.86M | 757.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders +0.0% in 395h (now 269,294) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $84.7k | $1.42M | +3844% | +3844% | +3844% | 6.1x | spike (+3844% 1h, +3844% 6h); < 1h old | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $64.1k | $796.5k | +38% | +2331% | +2331% | 10.5x | spike (+38% 1h, +2331% 6h); lopsided buys/sells 4.21 | not scored |
| [Frogger](https://pump.fun/coin/GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump) | `GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump` | $30.9k | $171.2k | +472% | +472% | +472% | 14.5x | thin liq $30.9k; spike (+472% 1h, +472% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $67.9k | $483.4k | -21% | +63% | +987% | 59.8x | churn 60x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $46.9k | $410.5k | -4% | -41% | +1099% | 28.6x | thin liq $46.9k; churn 29x vol/liq | not scored |
| [Zhaki](https://pump.fun/coin/2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump) | `2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump` | $32.9k | $185.8k | +37% | +59% | +513% | 46.3x | thin liq $32.9k; churn 46x vol/liq | not scored |

_Timing: total 156s (discovery 71.4s, screen 1.4s, GT prime 0.3s, scoring 82.5s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/143; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
