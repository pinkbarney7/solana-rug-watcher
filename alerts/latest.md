# Last scan 2026-11-27T07:23:15Z - mode: helius (box heartbeat stale (200 min); budget 120/3000)

```
[fast_scan] 120 candidate mints from 10 source tags; 118 with pair data; 23 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored ZEC in 79s
[fast_scan] scored 哈基米 in 80s
[fast_scan] scored KAI in 81s
[fast_scan] scored Snowball in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Rizzmas in 82s
# Market scan 2026-11-27 07:23 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,781 (+2.3% 24h), ETH $1,735 (+3.0% 24h), SOL $73.00 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.5% (mcap $1.92B, vol $262.28M), pump-fun +2.4% (mcap $798.68M, vol $91.99M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $93.0k | $492.6k | 1.5 d | h24 +3400% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [哈基米](https://dexscreener.com/solana/3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41) | `3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41` | $175.7k | $122.3k | 1.2 h | h24 +133% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $249.1k | $10.48M | 1.2 d | h24 +288% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #9 Price momentum WARN (+5) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $125.6k | $2.70M | 6.6 h | h24 +2375% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.7% (+6.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.0k | $621.9k | 1068.6 d | h24 +33% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,702 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.89M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,792 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.64M | $18.5k | 407.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 396,894) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $72.9k | $977.9k | +6% | +2868% | +2868% | 13.2x | spike (+6% 1h, +2868% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $56.3k | $492.6k | -18% | -18% | +3400% | 34.9x | churn 35x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $24.0k | $112.3k | +600% | +249% | +249% | 18.7x | thin liq $24.0k; spike (+600% 1h, +249% 6h) | not scored |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $125.7k | $2.70M | -14% | -25% | +2382% | 25.5x | liq/mcap 4.7%; churn 26x vol/liq | 66 |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $220.7k | $242.8k | +43% | +694% | +694% | 61.5x | churn 61x vol/liq; spike (+43% 1h, +694% 6h) | not scored |
| [EXEN](https://pump.fun/coin/5VKCLbHMRPCCTWq8dWUTMxihuuHsHjoC9vEYDhrFpump) | `5VKCLbHMRPCCTWq8dWUTMxihuuHsHjoC9vEYDhrFpump` | $22.6k | $108.1k | +257% | +257% | +257% | 5.0x | thin liq $22.6k; spike (+257% 1h, +257% 6h); < 1h old | not scored |

_Timing: total 154s (discovery 71.1s, screen 1.1s, GT prime 0.3s, scoring 81.7s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/142; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
