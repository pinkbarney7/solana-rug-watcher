# Last scan 2026-11-27T08:13:31Z - mode: helius (box heartbeat stale (250 min); budget 150/3000)

```
[fast_scan] 114 candidate mints from 9 source tags; 113 with pair data; 26 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 71s
[fast_scan] scored ZEC in 79s
[fast_scan] scored SPCX in 79s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored SuperFIONA in 80s
[fast_scan] scored Snowball in 81s
[fast_scan] scored Rizzmas in 82s
# Market scan 2026-11-27 08:13 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,845 (+2.0% 24h), ETH $1,736 (+2.7% 24h), SOL $73.30 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.8% (mcap $1.92B, vol $258.80M), pump-fun +2.3% (mcap $799.85M, vol $90.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $91.7k | $441.9k | 1.6 d | h24 +2679% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $227.2k | $129.1k | 2.1 h | h24 +59% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $244.2k | $10.02M | 1.3 d | h24 +48% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $129.1k | $2.83M | 7.5 h | h24 +2500% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.6% (+6.5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.2k | $625.0k | 1068.6 d | h24 +24% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,719 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.85M | 184.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,681 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.57M | $18.4k | 407.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 396,770 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $53.4k | $441.9k | -15% | -24% | +2679% | 37.2x | churn 37x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $129.4k | $2.85M | +2% | +6% | +2514% | 25.2x | liq/mcap 4.5%; churn 25x vol/liq | 66 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $24.8k | $120.9k | +13% | +275% | +275% | 23.6x | thin liq $24.8k | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $37.2k | $245.8k | +17% | +9% | +707% | 32.4x | thin liq $37.2k; churn 32x vol/liq | not scored |
| [DragonRiders](https://dexscreener.com/solana/5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh) | `5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh` | $35.7k | $159.1k | +35% | +179% | +226% | 28.2x | thin liq $35.7k; churn 28x vol/liq | not scored |
| [Kibo](https://dexscreener.com/solana/Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z) | `Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z` | $102.0k | $61.8k | +74% | +74% | +74% | 34.8x | churn 35x vol/liq; < 1h old | not scored |

_Timing: total 155s (discovery 71.8s, screen 1.1s, GT prime 0.2s, scoring 82.1s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
