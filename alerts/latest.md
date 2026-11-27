# Last scan 2026-11-27T06:50:39Z - mode: helius (box heartbeat stale (167 min); budget 100/3000)

```
[fast_scan] 118 candidate mints from 10 source tags; 115 with pair data; 21 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored MPLX in 69s
[fast_scan] scored Snowball in 77s
[fast_scan] scored SPCX in 77s
[fast_scan] scored PUMPCHAN in 77s
[fast_scan] scored Rizzmas in 79s
# Market scan 2026-11-27 06:50 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,645 (+2.0% 24h), ETH $1,732 (+2.8% 24h), SOL $72.84 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.4% (mcap $1.92B, vol $270.27M), pump-fun +2.3% (mcap $797.93M, vol $98.39M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $99.1k | $588.8k | 1.5 d | h24 +4085% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.4k | $10.36M | 1.2 d | h24 +539% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $231.4k | $689.9k | 1068.5 d | h24 +49% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 395,702) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.48M | $13.92M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,725 (growth n/a: first sighting) |
| 73* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $2.99M | $27.10M | 1460.2 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,310 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $71.0k | $934.9k | +42% | +2738% | +2738% | 12.6x | spike (+42% 1h, +2738% 6h); lopsided buys/sells 3.10 | not scored |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $135.9k | $3.17M | +6% | +933% | +2806% | 23.3x | liq/mcap 4.3%; spike (+6% 1h, +933% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $61.6k | $588.8k | +2% | -16% | +4085% | 31.6x | churn 32x vol/liq | 52 |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $195.3k | $202.9k | +70% | +563% | +563% | 56.0x | churn 56x vol/liq; spike (+70% 1h, +563% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $35.2k | $223.3k | -7% | -26% | +633% | 33.3x | thin liq $35.2k; churn 33x vol/liq | not scored |
| [SIDOOR](https://dexscreener.com/solana/zcRvzm7gAfYGde8gRwaSYxNryL47SjLVUQLAf1bdoor) | `zcRvzm7gAfYGde8gRwaSYxNryL47SjLVUQLAf1bdoor` | $71.1k | $784.7k | +47% | +132% | +288% | 4.3x | none flagged (still high risk) | not scored |

_Timing: total 152s (discovery 71.4s, screen 1.3s, GT prime 0.2s, scoring 79.2s for 5 coins, 5 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 5/110; Helius 429s 65; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
