# Last scan 2026-11-27T05:42:34Z - mode: helius (box heartbeat stale (99 min); budget 50/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 118 with pair data; 25 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 72s
[fast_scan] scored SPCX in 81s
[fast_scan] scored SuperFIONA in 81s
[fast_scan] scored BASKET in 82s
[fast_scan] scored PUMPCHAN in 82s
[fast_scan] scored MPLX in 83s
[fast_scan] scored CINU in 83s
[fast_scan] scored Rizzmas in 84s
# Market scan 2026-11-27 05:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,720 (+1.3% 24h), ETH $1,742 (+2.5% 24h), SOL $73.10 (+2.7% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.6% (mcap $1.92B, vol $282.60M), pump-fun +1.8% (mcap $798.72M, vol $94.96M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $116.3k | $406.1k | 2.0 d | h24 -43% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $51.1k | $306.8k | 8.4 h | h24 +569% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $102.9k | $564.1k | 1.5 d | h24 +5799% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh) | `DksT6u5GDTtZJ1Pq2mDQMmTkqNNPYdLAWKnWd3Dy4Jqh` | $207.6k | $116.8k | 1.3 h | h24 +44% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $277.0k | $12.96M | 1.2 d | h24 +801% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.1% (+9.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $234.2k | $702.5k | 1068.5 d | h24 +52% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,698 (growth n/a: first sighting) |
| 71* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.06M | $29.04M | 1460.1 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders +0.0% in 1h (now 91,302) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.61M | $13.95M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,808 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $132.3k | $3.00M | +8% | +2654% | +2654% | 23.4x | liq/mcap 4.4%; spike (+8% 1h, +2654% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $60.2k | $564.1k | -17% | +12% | +5799% | 31.7x | churn 32x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $56.3k | $595.7k | +5% | +1708% | +1708% | 13.1x | spike (+5% 1h, +1708% 6h); lopsided buys/sells 4.55 | not scored |
| [BIAO](https://dexscreener.com/solana/CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN) | `CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN` | $104.5k | $113.2k | +228% | +593% | +593% | 53.3x | churn 53x vol/liq; spike (+228% 1h, +593% 6h) | not scored |
| [VOLALITY](https://pump.fun/coin/4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump) | `4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump` | $26.3k | $138.8k | +153% | +359% | +359% | 14.5x | thin liq $26.3k; spike (+153% 1h, +359% 6h) | not scored |
| [Gemma](https://pump.fun/coin/C8CZZnPJzPaWhB82EmpKMZc5PEqNnQ46n43j5Fj9pump) | `C8CZZnPJzPaWhB82EmpKMZc5PEqNnQ46n43j5Fj9pump` | $13.6k | $42.5k | +34% | +680% | +46% | 9.0x | thin liq $13.6k; spike (+34% 1h, +680% 6h) | not scored |

_Timing: total 158s (discovery 71.9s, screen 1.4s, GT prime 0.6s, scoring 83.9s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/164; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
