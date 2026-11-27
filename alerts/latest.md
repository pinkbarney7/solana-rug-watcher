# Last scan 2026-11-27T08:38:11Z - mode: helius (box heartbeat stale (275 min); budget 150/3000)

```
[fast_scan] 118 candidate mints from 10 source tags; 117 with pair data; 24 >= $50,000 liq; 5 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 72s
[fast_scan] scored Kibo in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored Snowball in 82s
[fast_scan] scored SuperFIONA in 82s
[fast_scan] scored KAI in 83s
[fast_scan] scored Rizzmas in 84s
# Market scan 2026-11-27 08:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,766 (+2.0% 24h), ETH $1,732 (+2.6% 24h), SOL $73.20 (+3.3% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.1% (mcap $1.93B, vol $260.93M), pump-fun +2.5% (mcap $800.74M, vol $90.57M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $110.4k | $703.9k | 1.6 d | h24 +3923% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $234.1k | $134.8k | 2.6 h | h24 +66% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Kibo](https://dexscreener.com/solana/Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z) | `Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z` | $109.2k | $64.7k | 1.1 h | h24 +82% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $240.4k | $9.74M | 1.3 d | h24 +15% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.5% (+9); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $135.5k | $3.11M | 7.9 h | h24 +2760% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.3% (+6.8) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.4k | $623.0k | 1068.6 d | h24 +26% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,722 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.71M | $18.26M | 123.7 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,634 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.87M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,839 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $67.9k | $703.9k | +36% | +34% | +3923% | 29.9x | churn 30x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $135.3k | $3.11M | +18% | +10% | +2760% | 24.3x | liq/mcap 4.3% | 66 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $27.5k | $144.4k | -23% | +348% | +348% | 23.0x | thin liq $27.5k; spike (-23% 1h, +348% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $39.8k | $279.6k | +12% | +34% | +818% | 30.8x | thin liq $39.8k; churn 31x vol/liq | not scored |
| [Kibo](https://dexscreener.com/solana/Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z) | `Me3c36ueyXkeTSdDDHLMydKfB7H7bDbo4Qdz2FoVi2z` | $109.4k | $64.8k | +50% | +83% | +83% | 50.3x | churn 50x vol/liq | 53 |
| [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $149.3k | $95.4k | +81% | +81% | +81% | 19.2x | < 1h old | not scored |

_Timing: total 157s (discovery 71.4s, screen 1.5s, GT prime 0.4s, scoring 84.1s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/158; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
