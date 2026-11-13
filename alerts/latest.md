# Last scan 2026-11-13T22:49:13Z - mode: helius (box heartbeat stale (4891 min); budget 40/3000)

```
[fast_scan] 134 candidate mints from 10 source tags; 133 with pair data; 29 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored XTO in 78s
[fast_scan] scored SPCX in 87s
[fast_scan] scored WANTED in 87s
[fast_scan] scored SHARKBUX in 87s
[fast_scan] scored FOOD in 88s
[fast_scan] scored TTWO in 89s
[fast_scan] scored NVDAx in 89s
[fast_scan] scored Max in 91s
# Market scan 2026-11-13 22:49 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $68,356 (-4.2% 24h), ETH $1,929 (-4.1% 24h), SOL $78.32 (-3.7% 24h)
- Fear & Greed: 20 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.1% (mcap $2.31B, vol $386.67M), pump-fun -2.8% (mcap $899.66M, vol $128.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $259.7k | $1.79M | 2.1 d | h24 -13% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 50* | SKIP | [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $213.4k | $1.08M | 1.1 d | h24 +2849% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [WANTED](https://pump.fun/coin/BeLVQE2tK7fVvg6EpVgUzUWhSi95XpL7mqJM3nANpump) | `BeLVQE2tK7fVvg6EpVgUzUWhSi95XpL7mqJM3nANpump` | $50.3k | $439.0k | 9.7 h | h24 +1089% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $59.2k | $543.4k | 23.3 h | h24 +644% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.04M | $197.85M | 1.5 d | h24 +38% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.16M | $98 | 102.9 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders 243,643 (growth n/a: first sighting) |
| 72* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.60M | $35.56M | 504.5 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders +0.7% in 5h (now 431,395) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.31M | $12.93M | 170.6 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 25h (now 360,197) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $159.9k | $4.42M | +3% | +10995% | +10995% | 7.4x | liq/mcap 3.6%; spike (+3% 1h, +10995% 6h) | not scored |
| [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $101.3k | $1.08M | +20% | -30% | +2849% | 106.7x | churn 107x vol/liq | 50 |
| [PEACEFROG](https://pump.fun/coin/m7SihqeaWimE1zpBzjHBwKJbbhuaczX5fHvGoNupump) | `m7SihqeaWimE1zpBzjHBwKJbbhuaczX5fHvGoNupump` | $34.7k | $161.8k | +17% | +589% | +589% | 6.3x | thin liq $34.7k; spike (+17% 1h, +589% 6h) | not scored |
| [WISHMAS](https://pump.fun/coin/9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump) | `9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump` | $24.9k | $103.9k | +213% | +237% | +237% | 39.6x | thin liq $24.9k; churn 40x vol/liq; spike (+213% 1h, +237% 6h) | not scored |
| [SPEED](https://pump.fun/coin/7csfMgiRcBy9Y4GbGVMz8qJWFUk718KG58xfCKpXpump) | `7csfMgiRcBy9Y4GbGVMz8qJWFUk718KG58xfCKpXpump` | $48.9k | $421.4k | +40% | +367% | +367% | 16.0x | thin liq $48.9k; spike (+40% 1h, +367% 6h) | not scored |
| [WANTED](https://pump.fun/coin/BeLVQE2tK7fVvg6EpVgUzUWhSi95XpL7mqJM3nANpump) | `BeLVQE2tK7fVvg6EpVgUzUWhSi95XpL7mqJM3nANpump` | $50.1k | $434.8k | -19% | -45% | +1078% | 18.1x | none flagged (still high risk) | 52 |

_Timing: total 164s (discovery 71.6s, screen 1.5s, GT prime 0.6s, scoring 90.5s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/159; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
