# Last scan 2026-11-27T07:59:32Z - mode: helius (box heartbeat stale (236 min); budget 150/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 118 with pair data; 26 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored Snowball in 72s
[fast_scan] scored SuperFIONA in 80s
[fast_scan] scored 哈基米 in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored ZEC in 82s
[fast_scan] scored KAI in 82s
[fast_scan] scored PUMPCHAN in 83s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 07:59 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,700 (+2.0% 24h), ETH $1,734 (+2.6% 24h), SOL $73.25 (+3.5% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $1.92B, vol $259.70M), pump-fun +2.2% (mcap $798.72M, vol $91.84M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $91.6k | $448.5k | 1.6 d | h24 +3185% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $222.6k | $125.6k | 1.9 h | h24 +55% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $248.2k | $10.36M | 1.3 d | h24 +43% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $130.8k | $2.91M | 7.3 h | h24 +2572% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.5% (+6.6) |
| 69* | SKIP | [哈基米](https://dexscreener.com/solana/3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41) | `3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41` | $209.3k | $160.3k | 1.8 h | h24 +205% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |

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
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $53.8k | $448.5k | -19% | -9% | +3185% | 36.8x | churn 37x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $130.7k | $2.91M | -8% | +0% | +2572% | 24.8x | liq/mcap 4.5% | 66 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $28.6k | $158.8k | +107% | +393% | +393% | 19.4x | thin liq $28.6k; spike (+107% 1h, +393% 6h) | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $28.0k | $149.3k | -85% | +353% | +353% | 37.4x | thin liq $28.0k; churn 37x vol/liq; spike (-85% 1h, +353% 6h) | not scored |
| [哈基米](https://dexscreener.com/solana/3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41) | `3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41` | $209.4k | $160.3k | +59% | +205% | +205% | 39.8x | churn 40x vol/liq | 69 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $37.7k | $252.5k | +21% | +9% | +729% | 31.9x | thin liq $37.7k; churn 32x vol/liq | not scored |

_Timing: total 155s (discovery 70.8s, screen 1.1s, GT prime 0.4s, scoring 82.9s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/158; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
