# Last scan 2026-11-14T09:31:13Z - mode: helius (box heartbeat stale (5532 min); budget 0/3000)

```
[fast_scan] 136 candidate mints from 9 source tags; 135 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored JENSEN in 72s
[fast_scan] scored AMC in 80s
[fast_scan] scored SHARKBUX in 81s
[fast_scan] scored UODF in 81s
[fast_scan] scored SWJ in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored FOOD in 83s
[fast_scan] scored TTWO in 71s
# Market scan 2026-11-14 09:31 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $67,015 (-2.6% 24h), ETH $1,900 (-1.9% 24h), SOL $75.49 (-5.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.9% (mcap $2.23B, vol $323.18M), pump-fun -3.0% (mcap $874.61M, vol $117.94M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 37* | CAUTION | [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $52.3k | $437.9k | 1.4 d | h24 -33% | #8 Turnover / bot pattern WARN (+4); #11 not checked (+3); #12 not checked (+3) |
| 39* | CAUTION | [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $162.3k | $976.4k | 1.5 d | h24 +23% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [SWJ](https://dexscreener.com/solana/Hx2SXLBtX8X1n3asiGtppaPWoyraveDDriVgCFJQrne) | `Hx2SXLBtX8X1n3asiGtppaPWoyraveDDriVgCFJQrne` | $322.5k | $183.0k | 4.7 h | h24 +84% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [JENSEN](https://pump.fun/coin/B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump) | `B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump` | $73.2k | $914.5k | 8.6 h | h24 +933% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 66* | SKIP | [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $151.8k | $4.04M | 14.8 h | h24 +10036% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 3.8% (+7.5) |
| 75* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $848.4k | $135.02M | 19.4 h | h24 +399234% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.07M | $98 | 103.4 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.2% in 7h (now 244,894) |
| 72* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.62M | $35.74M | 505.0 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders +0.0% in 7h (now 432,327) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.40M | $12.78M | 171.1 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.2% in 11h (now 360,936) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $848.4k | $135.04M | +3% | +66% | +399292% | 0.7x | liq/mcap 0.6%; lopsided buys/sells 2702.57 | 75 |
| [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $151.3k | $4.01M | -8% | +9% | +9965% | 13.7x | liq/mcap 3.8% | 66 |
| [FUND](https://dexscreener.com/solana/Aq38XaBAkzAtwbpvFKEzKg9hp1eZrEFV5W9H6XJjFUND) | `Aq38XaBAkzAtwbpvFKEzKg9hp1eZrEFV5W9H6XJjFUND` | $21.2k | $85.4k | +488% | +152% | +152% | 16.6x | thin liq $21.2k; spike (+488% 1h, +152% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump) | `B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump` | $73.6k | $925.8k | -1% | -27% | +946% | 24.3x | none flagged (still high risk) | 58 |
| [VICECITY](https://pump.fun/coin/Ep13piLgesAxM32dB4hVAsmhfWcsTJqVKmQHkYCKpump) | `Ep13piLgesAxM32dB4hVAsmhfWcsTJqVKmQHkYCKpump` | $26.4k | $122.8k | -23% | +296% | +296% | 20.5x | thin liq $26.4k | not scored |
| [ASTRALIS](https://pump.fun/coin/DWsutTNJSjG5mkhGsPevvT8xbRtVYQBLZdxqxm2Upump) | `DWsutTNJSjG5mkhGsPevvT8xbRtVYQBLZdxqxm2Upump` | $22.3k | $83.2k | -50% | +177% | +177% | 61.1x | thin liq $22.3k; churn 61x vol/liq | not scored |

_Timing: total 216s (discovery 70.9s, screen 1.3s, GT prime 0.4s, scoring 143.0s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
