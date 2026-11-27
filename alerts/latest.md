# Last scan 2026-11-27T06:14:57Z - mode: helius (box heartbeat stale (132 min); budget 80/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 120 with pair data; 22 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored Rizzmas in 70s
[fast_scan] scored Snowball in 77s
[fast_scan] scored PUMPCHAN in 77s
[fast_scan] scored MPLX in 78s
[fast_scan] scored SPCX in 78s
# Market scan 2026-11-27 06:14 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,764 (+2.1% 24h), ETH $1,739 (+3.3% 24h), SOL $73.05 (+3.3% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.6% (mcap $1.92B, vol $266.92M), pump-fun +1.7% (mcap $798.34M, vol $87.47M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $108.4k | $651.8k | 1.5 d | h24 +5020% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.6k | $10.35M | 1.2 d | h24 +664% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $231.9k | $690.8k | 1068.5 d | h24 +49% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,701 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.96M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,772 (growth n/a: first sighting) |
| 73* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.04M | $28.33M | 1460.1 d | h24 +19% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,308 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $141.1k | $3.41M | +7% | +3029% | +3029% | 22.2x | liq/mcap 4.1%; spike (+7% 1h, +3029% 6h) | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $68.4k | $870.0k | +55% | +2541% | +2541% | 12.2x | spike (+55% 1h, +2541% 6h); lopsided buys/sells 3.54 | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $64.3k | $639.7k | +9% | +51% | +5251% | 30.0x | churn 30x vol/liq | 52 |
| [NVIDIA](https://pump.fun/coin/C6oCcRXnB6SEp3Pmi9gL8DHVsoEWR9aaZtf9UGj8pump) | `C6oCcRXnB6SEp3Pmi9gL8DHVsoEWR9aaZtf9UGj8pump` | $25.1k | $132.0k | +334% | +334% | +334% | 4.9x | thin liq $25.1k; spike (+334% 1h, +334% 6h); < 1h old | not scored |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $165.6k | $157.7k | +90% | +416% | +416% | 48.3x | churn 48x vol/liq; spike (+90% 1h, +416% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $36.1k | $233.7k | -1% | +131% | +667% | 32.1x | thin liq $36.1k; churn 32x vol/liq | not scored |

_Timing: total 152s (discovery 71.8s, screen 1.4s, GT prime 0.5s, scoring 78.3s for 5 coins, 5 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 5/111; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
