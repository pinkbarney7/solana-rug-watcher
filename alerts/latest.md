# Last scan 2026-11-27T08:02:24Z - mode: helius (box heartbeat stale (239 min); budget 150/3000)

```
[fast_scan] 116 candidate mints from 10 source tags; 115 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored Snowball in 76s
[fast_scan] scored SuperFIONA in 76s
[fast_scan] scored ZEC in 76s
[fast_scan] scored KAI in 76s
[fast_scan] scored SPCX in 77s
[fast_scan] scored PUMPCHAN in 77s
[fast_scan] scored Rizzmas in 78s
# Market scan 2026-11-27 08:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,639 (+1.9% 24h), ETH $1,734 (+2.7% 24h), SOL $73.30 (+3.5% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $1.92B, vol $259.70M), pump-fun +2.2% (mcap $798.72M, vol $91.84M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $91.6k | $448.5k | 1.6 d | h24 +3185% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $222.6k | $125.6k | 2.0 h | h24 +55% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $248.2k | $10.36M | 1.3 d | h24 +43% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $130.8k | $2.91M | 7.3 h | h24 +2572% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.5% (+6.6) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $219.9k | $619.3k | 1068.6 d | h24 +31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,719 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.81M | 184.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,681 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.53M | $18.3k | 407.6 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 396,770 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $54.1k | $454.1k | -17% | -10% | +3207% | 36.6x | churn 37x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $127.8k | $2.78M | -6% | +6% | +2453% | 25.4x | liq/mcap 4.6%; churn 25x vol/liq | 66 |
| [NOTHING](https://dexscreener.com/solana/D2F9eCcbSVrmuPzUJf8pUaKGdB6V21ph7aFonFUJxJYY) | `D2F9eCcbSVrmuPzUJf8pUaKGdB6V21ph7aFonFUJxJYY` | $28.7k | $25.9k | +227% | +227% | +227% | 7.8x | thin liq $28.7k; spike (+227% 1h, +227% 6h); < 1h old | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $27.4k | $146.1k | +96% | +354% | +354% | 20.4x | thin liq $27.4k; spike (+96% 1h, +354% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $36.8k | $241.2k | +18% | +4% | +692% | 32.7x | thin liq $36.8k; churn 33x vol/liq | not scored |
| [DragonRiders](https://dexscreener.com/solana/5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh) | `5xrT8y2KU2YwzipwCMNxxTc8KAGQd4wjtGTc2WyJJCMh` | $32.4k | $133.0k | +11% | +172% | +172% | 30.8x | thin liq $32.4k; churn 31x vol/liq | not scored |

_Timing: total 150s (discovery 70.9s, screen 1.1s, GT prime 0.3s, scoring 77.5s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 51/140; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
