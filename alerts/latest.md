# Last scan 2026-11-27T08:27:35Z - mode: helius (box heartbeat stale (264 min); budget 150/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 114 with pair data; 25 >= $50,000 liq; 5 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 71s
[fast_scan] scored CATE in 79s
[fast_scan] scored SPCX in 80s
[fast_scan] scored Snowball in 80s
[fast_scan] scored SuperFIONA in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 08:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,947 (+2.1% 24h), ETH $1,738 (+2.9% 24h), SOL $73.45 (+3.6% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.0% (mcap $1.93B, vol $258.38M), pump-fun +2.4% (mcap $800.27M, vol $90.45M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $98.4k | $650.5k | 1.6 d | h24 +3473% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $232.3k | $133.2k | 2.4 h | h24 +64% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $244.7k | $10.04M | 1.3 d | h24 +47% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $132.9k | $2.99M | 7.7 h | h24 +2649% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.4% (+6.7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.0k | $629.3k | 1068.6 d | h24 +26% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,722 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.72M | $18.41M | 123.7 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 438,634) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.87M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,681 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $65.2k | $650.5k | +25% | +15% | +3473% | 30.8x | churn 31x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $132.3k | $2.97M | +15% | -3% | +2627% | 24.7x | liq/mcap 4.5% | 66 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $41.7k | $305.8k | +39% | +15% | +904% | 29.2x | thin liq $41.7k; churn 29x vol/liq | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $25.5k | $125.8k | -1% | +290% | +290% | 24.2x | thin liq $25.5k | not scored |
| [Kibo](https://dexscreener.com/solana/Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z) | `Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z` | $105.9k | $62.6k | +76% | +76% | +76% | 45.0x | churn 45x vol/liq; < 1h old | not scored |
| [DragonRiders](https://dexscreener.com/solana/5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh) | `5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh` | $35.1k | $153.6k | +5% | +125% | +214% | 28.9x | thin liq $35.1k; churn 29x vol/liq | not scored |

_Timing: total 156s (discovery 71.9s, screen 1.1s, GT prime 0.3s, scoring 82.6s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
