# Last scan 2026-11-27T10:00:16Z - mode: helius (box heartbeat stale (357 min); budget 240/3000)

```
[fast_scan] 115 candidate mints from 10 source tags; 113 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 74s
[fast_scan] scored CLAUDIA in 80s
[fast_scan] scored KAI in 81s
[fast_scan] scored PETER in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored MOSTO in 83s
[fast_scan] scored PUMPCHAN in 83s
[fast_scan] scored Rizzmas in 84s
# Market scan 2026-11-27 10:00 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,594 (+1.2% 24h), ETH $1,728 (+1.6% 24h), SOL $73.45 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.5% (mcap $1.93B, vol $257.84M), pump-fun +2.7% (mcap $802.72M, vol $89.36M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $153.2k | $789.4k | 1.7 d | h24 +479% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $248.0k | $10.30M | 1.4 d | h24 +116% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $112.6k | $2.14M | 9.3 h | h24 +1867% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.3% (+5.7) |
| 69* | SKIP | [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $155.0k | $165.0k | 2.0 h | h24 +213% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 69* | SKIP | [PETER](https://dexscreener.com/solana/9p3H9N4sbSTaBe95stavYTH3b4B5gcQUjsJF1BTNCBze) | `9p3H9N4sbSTaBe95stavYTH3b4B5gcQUjsJF1BTNCBze` | $218.7k | $163.9k | 2.3 h | h24 +211% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.7k | $627.6k | 1068.7 d | h24 +19% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,720 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.50M | $79.38B | 51.3 d | h24 -5% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders +1.0% in 32h (now 62,340) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.84M | 184.1 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,723 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $65.5k | $398.6k | +66% | +111% | +5437% | 7.7x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $73.5k | $816.5k | -13% | +30% | +4267% | 29.7x | churn 30x vol/liq | 45 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $112.4k | $2.14M | -12% | -22% | +1867% | 30.2x | churn 30x vol/liq | 60 |
| [MONKY](https://dexscreener.com/solana/isE5fLXFx1K6eDwgoBMvSkE3UyFZmKCwVJ7c8Nu9qnH) | `isE5fLXFx1K6eDwgoBMvSkE3UyFZmKCwVJ7c8Nu9qnH` | $26.9k | $24.1k | +221% | +221% | +221% | 14.4x | thin liq $26.9k; spike (+221% 1h, +221% 6h); < 1h old | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $40.3k | $284.2k | -6% | +63% | +833% | 32.2x | thin liq $40.3k; churn 32x vol/liq | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $26.4k | $131.8k | +14% | +309% | +309% | 28.5x | thin liq $26.4k; churn 28x vol/liq; spike (+14% 1h, +309% 6h) | not scored |

_Timing: total 158s (discovery 71.6s, screen 1.5s, GT prime 0.6s, scoring 83.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
