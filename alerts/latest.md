# Last scan 2026-11-27T05:32:39Z - mode: helius (box heartbeat stale (89 min); budget 40/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 123 with pair data; 25 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored CINU in 72s
[fast_scan] scored SuperFIONA in 80s
[fast_scan] scored CATE in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored Snowball in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored BASKET in 84s
# Market scan 2026-11-27 05:32 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,680 (+1.2% 24h), ETH $1,744 (+2.6% 24h), SOL $73.13 (+2.5% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.3% (mcap $1.92B, vol $284.44M), pump-fun +1.8% (mcap $797.48M, vol $97.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $117.6k | $418.0k | 2.0 d | h24 -44% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $53.3k | $331.2k | 8.3 h | h24 +623% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $104.7k | $581.3k | 1.5 d | h24 +6273% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh) | `DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh` | $201.7k | $112.9k | 1.1 h | h24 +40% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $263.0k | $11.73M | 1.2 d | h24 +701% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.2% (+9.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.72M | $18.66M | 123.5 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,378 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.61M | $13.95M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,808 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.63M | $18.8k | 407.5 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 396,952 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $133.2k | $3.04M | +15% | +2688% | +2688% | 23.2x | liq/mcap 4.4%; spike (+15% 1h, +2688% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $61.2k | $582.0k | -15% | +7% | +6281% | 31.1x | churn 31x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $61.2k | $702.5k | +21% | +2032% | +2032% | 11.4x | spike (+21% 1h, +2032% 6h); lopsided buys/sells 4.71 | not scored |
| [BIAO](https://dexscreener.com/solana/CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN) | `CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN` | $95.9k | $99.4k | +284% | +508% | +508% | 49.5x | churn 50x vol/liq; spike (+284% 1h, +508% 6h) | not scored |
| [VOLALITY](https://pump.fun/coin/4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump) | `4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump` | $26.9k | $145.7k | +308% | +382% | +382% | 11.5x | thin liq $26.9k; spike (+308% 1h, +382% 6h) | not scored |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $125.4k | $101.9k | +233% | +233% | +233% | 36.2x | churn 36x vol/liq; spike (+233% 1h, +233% 6h); < 1h old | not scored |

_Timing: total 157s (discovery 71.4s, screen 1.4s, GT prime 0.2s, scoring 84.2s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 13/158; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
