# Last scan 2026-11-27T16:36:25Z - mode: helius (box heartbeat stale (24 min); budget 485/3000)

```
[fast_scan] 109 candidate mints from 9 source tags; 107 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (72s)
[fast_scan] scored UGOS in 77s
[fast_scan] scored PUMPCHAN in 86s
[fast_scan] scored SPCX in 86s
[fast_scan] scored GAIB in 86s
[fast_scan] scored ZEC in 87s
[fast_scan] scored Snowball in 87s
[fast_scan] scored pippin in 88s
# Market scan 2026-11-27 16:36 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,013 (-0.6% 24h), ETH $1,671 (-0.8% 24h), SOL $72.01 (+1.9% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $1.90B, vol $278.38M), pump-fun +3.4% (mcap $803.22M, vol $97.10M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $122.0k | $865.0k | 1.9 d | h24 +1387% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [GAIB](https://dexscreener.com/solana/2JjmRdQ71UzAUkTCGsFXNEBdqYBAbh9LMzSb8eHnzYJT) | `2JjmRdQ71UzAUkTCGsFXNEBdqYBAbh9LMzSb8eHnzYJT` | $170.3k | $131.0k | 2.7 h | h24 +62% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $302.2k | $15.50M | 1.6 d | h24 +69% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.7); #11 not checked (+3) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $822.2k | $133.66M | 19.2 h | h24 +449800% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $17.71M | 747.8 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 6h (now 182,581) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.51M | $13.68M | 184.4 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.1% in 3h (now 399,983) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.32M | $18.6k | 408.0 d | h24 +8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 4h (now 397,186) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $822.4k | $133.72M | +3% | +14% | +449988% | 0.6x | liq/mcap 0.6%; lopsided buys/sells 160.02 | 75 |
| [HOLD](https://pump.fun/coin/BuNeErf9FjL6dgzE74S21Qm9EeBaYMJXSW4A8ihxpump) | `BuNeErf9FjL6dgzE74S21Qm9EeBaYMJXSW4A8ihxpump` | $25.1k | $112.5k | +1021% | +1347% | +289% | 42.9x | thin liq $25.1k; churn 43x vol/liq; spike (+1021% 1h, +1347% 6h) | not scored |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $60.3k | $705.3k | +35% | +1961% | +1961% | 8.2x | spike (+35% 1h, +1961% 6h) | not scored |
| [Elfball](https://pump.fun/coin/92tFJ6CvgCuoS1c34Qy5g3RPVRDmLyHtknMnuoYqpump) | `92tFJ6CvgCuoS1c34Qy5g3RPVRDmLyHtknMnuoYqpump` | $38.4k | $301.2k | +809% | +809% | +809% | 8.0x | thin liq $38.4k; spike (+809% 1h, +809% 6h); lopsided buys/sells 3.73; < 1h old | not scored |
| [REVINU](https://pump.fun/coin/7j1a6959WYMBwUNVV64NtzwAKfKU8hXC5auJdFHbpump) | `7j1a6959WYMBwUNVV64NtzwAKfKU8hXC5auJdFHbpump` | $35.2k | $260.4k | +620% | +620% | +620% | 2.9x | thin liq $35.2k; spike (+620% 1h, +620% 6h); lopsided buys/sells 6.79; < 1h old | not scored |
| [NBA](https://pump.fun/coin/AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump) | `AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump` | $28.8k | $174.5k | +321% | +321% | +321% | 4.1x | thin liq $28.8k; spike (+321% 1h, +321% 6h); lopsided buys/sells 4.70; < 1h old | not scored |

_Timing: total 160s (discovery 71.3s, screen 1.1s, GT prime 0.2s, scoring 87.5s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/137; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
