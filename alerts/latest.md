# Last scan 2026-11-14T02:46:45Z - mode: helius (box heartbeat stale (5127 min); budget 50/3000)

```
[fast_scan] 131 candidate mints from 10 source tags; 130 with pair data; 31 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored Max in 80s
[fast_scan] scored AMC in 86s
[fast_scan] scored UODF in 87s
[fast_scan] scored SWJ in 87s
[fast_scan] scored NVDAx in 88s
[fast_scan] scored XTO in 89s
[fast_scan] scored TTWO in 89s
[fast_scan] scored FOOD in 90s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-14 02:46 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $67,399 (-4.0% 24h), ETH $1,900 (-4.6% 24h), SOL $75.60 (-5.8% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.9% (mcap $2.26B, vol $381.42M), pump-fun -2.5% (mcap $877.97M, vol $123.77M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $232.9k | $1.64M | 2.2 d | h24 -16% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $205.1k | $1.20M | 1.2 d | h24 +226% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SWJ](https://dexscreener.com/solana/69HP7ackfKESQGJFaPzYYXUA8vpRKd2Xu5FGhVmC33a) | `69HP7ackfKESQGJFaPzYYXUA8vpRKd2Xu5FGhVmC33a` | $230.9k | $149.8k | 1.8 h | h24 +99% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.02M | $196.70M | 1.6 d | h24 +30% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $168.0k | $5.00M | 8.1 h | h24 +12454% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 3.4% (+8) |
| 75* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $657.4k | $81.22M | 12.7 h | h24 +240126% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.74M | $17.28M | 110.4 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 9h (now 428,927) |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.21M | $98 | 103.1 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.3% in 4h (now 244,320) |
| 72* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.70M | $35.62M | 504.7 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders +0.2% in 4h (now 432,278) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $657.4k | $81.23M | -2% | -3% | +240133% | 0.8x | liq/mcap 0.8%; lopsided buys/sells 2029.22 | 75 |
| [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $168.0k | $5.00M | +10% | +7% | +12454% | 9.3x | liq/mcap 3.4% | 65 |
| [PEACEFROG](https://pump.fun/coin/m7SihqeaWimE1zpBzjHBwKJbbhuaczX5fHvGoNupump) | `m7SihqeaWimE1zpBzjHBwKJbbhuaczX5fHvGoNupump` | $27.7k | $106.9k | -9% | +5174% | +355% | 13.2x | thin liq $27.7k; spike (-9% 1h, +5174% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump) | `B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump` | $84.1k | $1.24M | +21% | +1303% | +1303% | 13.7x | spike (+21% 1h, +1303% 6h) | not scored |
| [WOHAIHAO](https://pump.fun/coin/4B1mCGeSjTadzH7okALwdFm8taxoHbZBFCTA1nZRpump) | `4B1mCGeSjTadzH7okALwdFm8taxoHbZBFCTA1nZRpump` | $33.3k | $209.2k | +81% | +585% | +585% | 6.4x | thin liq $33.3k; spike (+81% 1h, +585% 6h) | not scored |
| [WISHMAS](https://pump.fun/coin/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump) | `9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump` | $32.7k | $168.7k | +38% | +448% | +448% | 44.5x | thin liq $32.7k; churn 45x vol/liq; spike (+38% 1h, +448% 6h) | not scored |

_Timing: total 225s (discovery 71.4s, screen 1.4s, GT prime 0.6s, scoring 151.7s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/180; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
