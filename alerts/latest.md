# Last scan 2026-11-27T05:29:34Z - mode: helius (box heartbeat stale (86 min); budget 30/3000)

```
[fast_scan] 128 candidate mints from 10 source tags; 124 with pair data; 25 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored SuperFIONA in 72s
[fast_scan] scored SPCX in 80s
[fast_scan] scored ZEC in 81s
[fast_scan] scored CINU in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored Snowball in 82s
[fast_scan] scored PUMPCHAN in 83s
[fast_scan] scored BASKET in 84s
# Market scan 2026-11-27 05:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,663 (+1.2% 24h), ETH $1,744 (+2.6% 24h), SOL $73.16 (+2.6% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.3% (mcap $1.92B, vol $284.44M), pump-fun +1.8% (mcap $797.48M, vol $97.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $118.0k | $420.7k | 2.0 d | h24 -43% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $100.1k | $578.9k | 1.5 d | h24 +6428% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh) | `DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh` | $200.3k | $111.9k | 1.1 h | h24 +38% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $53.4k | $338.8k | 8.2 h | h24 +639% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $264.1k | $11.82M | 1.2 d | h24 +699% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.2% (+9.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.72M | $18.62M | 123.5 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,378 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.61M | $13.95M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,808 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.62M | $18.7k | 407.5 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 2h (now 396,952) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $131.9k | $2.98M | +8% | +2634% | +2634% | 23.4x | liq/mcap 4.4%; spike (+8% 1h, +2634% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $61.6k | $589.0k | -12% | +8% | +6542% | 30.9x | churn 31x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $59.8k | $673.8k | +15% | +1945% | +1945% | 11.3x | spike (+15% 1h, +1945% 6h); lopsided buys/sells 4.74 | not scored |
| [BIAO](https://dexscreener.com/solana/CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN) | `CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN` | $92.4k | $93.4k | +471% | +471% | +471% | 48.8x | churn 49x vol/liq; spike (+471% 1h, +471% 6h); < 1h old | not scored |
| [VOLALITY](https://pump.fun/coin/4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump) | `4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump` | $25.8k | $135.7k | +349% | +349% | +349% | 11.1x | thin liq $25.8k; spike (+349% 1h, +349% 6h); < 1h old | not scored |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $123.5k | $99.8k | +226% | +226% | +226% | 34.7x | churn 35x vol/liq; spike (+226% 1h, +226% 6h); < 1h old | not scored |

_Timing: total 157s (discovery 71.3s, screen 1.5s, GT prime 0.4s, scoring 83.7s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/159; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
