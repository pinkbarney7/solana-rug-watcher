# Last scan 2026-11-27T06:55:04Z - mode: helius (box heartbeat stale (172 min); budget 110/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 113 with pair data; 21 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 68s
[fast_scan] scored MPLX in 76s
[fast_scan] scored SPCX in 77s
[fast_scan] scored PUMPCHAN in 78s
[fast_scan] scored Rizzmas in 78s
# Market scan 2026-11-27 06:55 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,618 (+1.9% 24h), ETH $1,731 (+2.8% 24h), SOL $72.93 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.4% (mcap $1.92B, vol $270.27M), pump-fun +2.3% (mcap $797.93M, vol $98.39M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $98.2k | $576.4k | 1.5 d | h24 +3808% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.4k | $10.34M | 1.2 d | h24 +541% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $232.0k | $691.6k | 1068.5 d | h24 +50% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,702 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.90M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,725 (growth n/a: first sighting) |
| 73* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.00M | $27.14M | 1460.2 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,310 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $76.3k | $1.07M | +48% | +3157% | +3157% | 12.0x | spike (+48% 1h, +3157% 6h); lopsided buys/sells 3.06 | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $61.1k | $578.9k | -8% | -18% | +3824% | 31.9x | churn 32x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $132.2k | $2.99M | -2% | +334% | +2644% | 24.0x | liq/mcap 4.4%; spike (-2% 1h, +334% 6h) | not scored |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $199.0k | $208.4k | +62% | +581% | +581% | 56.7x | churn 57x vol/liq; spike (+62% 1h, +581% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $35.3k | $224.1k | -12% | -33% | +636% | 33.3x | thin liq $35.3k; churn 33x vol/liq | not scored |
| [OFFICIAL](https://dexscreener.com/solana/5z8YzMuZBYKpCGjSPxsJQg8k3dENcdWgxdhiceq6mpiJ) | `5z8YzMuZBYKpCGjSPxsJQg8k3dENcdWgxdhiceq6mpiJ` | $48.2k | $34.1k | +99% | +99% | +99% | 2.9x | thin liq $48.2k; spike (+99% 1h, +99% 6h); lopsided buys/sells 3.77; < 1h old | not scored |

_Timing: total 152s (discovery 71.8s, screen 1.3s, GT prime 0.2s, scoring 78.4s for 5 coins, 5 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/110; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
