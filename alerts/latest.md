# Last scan 2026-11-28T05:23:34Z - mode: helius (box heartbeat stale (75 min); budget 30/3000)

```
[fast_scan] 123 candidate mints from 9 source tags; 122 with pair data; 23 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Pnut  in 71s
[fast_scan] scored MoonBoy in 79s
[fast_scan] scored PUMPCHAN in 79s
[fast_scan] scored UGOS in 80s
[fast_scan] scored USOI in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored Rizzmas in 81s
# Market scan 2026-11-28 05:23 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,733 (-3.1% 24h), ETH $1,656 (-4.9% 24h), SOL $71.26 (-2.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.5% (mcap $1.86B, vol $277.81M), pump-fun +1.0% (mcap $801.33M, vol $96.11M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $105.5k | $515.9k | 8.7 h | h24 +1060% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $320.9k | $17.47M | 2.2 d | h24 +49% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $934.2k | $173.94M | 1.3 d | h24 +65% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $775.0k | $119.81M | 1.4 d | h24 +18% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.4k | $637.7k | 1069.5 d | h24 -7% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,801 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.18M | $9.11M | 769.7 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 136,192 (growth n/a: first sighting) |
| 56* | SKIP | [Pnut ](https://pump.fun/coin/2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump) | `2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump` | $2.03M | $26.79M | 757.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 269,294 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $78.2k | $1.20M | +3240% | +3240% | +3240% | 10.2x | spike (+3240% 1h, +3240% 6h); < 1h old | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $66.2k | $851.9k | +43% | +2500% | +2500% | 10.2x | spike (+43% 1h, +2500% 6h); lopsided buys/sells 4.17 | not scored |
| [Frogger](https://pump.fun/coin/GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump) | `GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump` | $26.7k | $132.0k | +234% | +341% | +341% | 21.1x | thin liq $26.7k; spike (+234% 1h, +341% 6h) | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $22.3k | $95.2k | +230% | +230% | +230% | 25.3x | thin liq $22.3k; churn 25x vol/liq; spike (+230% 1h, +230% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $70.3k | $515.9k | -20% | +26% | +1060% | 58.1x | churn 58x vol/liq | 54 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $47.9k | $426.9k | +1% | -34% | +1147% | 28.3x | thin liq $47.9k; churn 28x vol/liq | not scored |

_Timing: total 155s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 81.3s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/143; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
