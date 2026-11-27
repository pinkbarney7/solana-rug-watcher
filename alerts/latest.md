# Last scan 2026-11-27T10:03:26Z - mode: helius (box heartbeat stale (360 min); budget 240/3000)

```
[fast_scan] 118 candidate mints from 10 source tags; 116 with pair data; 23 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 77s
[fast_scan] scored Snowball in 86s
[fast_scan] scored Snowball in 86s
[fast_scan] scored CLAUDIA in 87s
[fast_scan] scored SPCX in 87s
[fast_scan] scored PUMPCHAN in 88s
[fast_scan] scored Rizzmas in 89s
# Market scan 2026-11-27 10:03 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,598 (+1.2% 24h), ETH $1,728 (+1.5% 24h), SOL $73.44 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.5% (mcap $1.93B, vol $257.84M), pump-fun +2.7% (mcap $802.72M, vol $89.36M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $147.4k | $857.7k | 1.7 d | h24 +3927% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Snowball](https://dexscreener.com/solana/BPpM8BtKZa5s4iN4M7hWZxrnYqB77jnUvB8vY7UdLxe) | `BPpM8BtKZa5s4iN4M7hWZxrnYqB77jnUvB8vY7UdLxe` | $101.2k | $58.8k | 1.2 h | h24 +65% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $250.1k | $10.47M | 1.4 d | h24 +116% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $115.7k | $2.26M | 9.3 h | h24 +1972% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.8) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.7k | $626.6k | 1068.7 d | h24 +19% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,720 (growth n/a: first sighting) |
| 67* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.50M | $79.38B | 51.4 d | h24 -5% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 62,338 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.84M | 184.1 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,723 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $69.5k | $446.0k | +59% | +136% | +6097% | 7.8x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $75.5k | $857.7k | -3% | +42% | +3927% | 28.9x | churn 29x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $115.5k | $2.26M | -11% | -15% | +1972% | 29.4x | churn 29x vol/liq | 60 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $40.4k | $284.4k | -18% | +53% | +834% | 32.1x | thin liq $40.4k; churn 32x vol/liq | not scored |
| [NIW](https://pump.fun/coin/CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump) | `CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump` | $20.8k | $104.8k | +42% | +261% | +261% | 0.1x | thin liq $20.8k | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $24.6k | $114.5k | -4% | +255% | +255% | 30.7x | thin liq $24.6k; churn 31x vol/liq | not scored |

_Timing: total 162s (discovery 71.4s, screen 1.5s, GT prime 0.4s, scoring 88.8s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/142; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
