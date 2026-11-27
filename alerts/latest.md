# Last scan 2026-11-27T11:12:30Z - mode: helius (box heartbeat stale (428 min); budget 300/3000)

```
[fast_scan] 113 candidate mints from 10 source tags; 111 with pair data; 23 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 72s
[fast_scan] scored KAI in 81s
[fast_scan] scored PUMPCHAN in 82s
[fast_scan] scored CLAUDIA in 82s
[fast_scan] scored BASKET in 83s
[fast_scan] scored TTWO in 83s
[fast_scan] scored FSD V15 in 83s
[fast_scan] scored SuperFIONA in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-27 11:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,485 (+1.7% 24h), ETH $1,723 (+1.8% 24h), SOL $73.07 (+3.7% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.7% (mcap $1.93B, vol $258.76M), pump-fun +3.0% (mcap $801.12M, vol $91.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $126.9k | $492.6k | 2.3 d | h24 -42% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $138.7k | $811.5k | 1.7 d | h24 +3926% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG) | `4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG` | $230.9k | $131.9k | 2.1 h | h24 +61% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $251.4k | $10.63M | 1.4 d | h24 +21% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.2); #8 Turnover / bot pattern WARN (+4) |
| 63* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $118.3k | $2.37M | 10.5 h | h24 +2075% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 5.0% (+6) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.78M | 123.8 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 438,604) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.38M | $78.29B | 51.4 d | h24 -5% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 62,339 (growth n/a: first sighting) |
| 72* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $652.2k | $96 | 116.4 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +48.7% in 280h (now 391,669) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $63.5k | $541.2k | +19% | +182% | +7419% | 15.2x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $73.2k | $810.8k | -0% | +35% | +3923% | 30.3x | churn 30x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $118.2k | $2.37M | +5% | -22% | +2075% | 29.3x | liq/mcap 5.0%; churn 29x vol/liq | 66 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $31.7k | $186.5k | +56% | +479% | +479% | 26.1x | thin liq $31.7k; churn 26x vol/liq; spike (+56% 1h, +479% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $41.2k | $296.6k | +10% | +24% | +874% | 32.1x | thin liq $41.2k; churn 32x vol/liq | not scored |
| [SNOWBALLZ](https://pump.fun/coin/DCFiFuRwjwdSKcYKmuz47gcSNsjjtZ6Rh8KkLaVCpump) | `DCFiFuRwjwdSKcYKmuz47gcSNsjjtZ6Rh8KkLaVCpump` | $23.1k | $113.2k | +28% | +275% | +275% | 4.3x | thin liq $23.1k | not scored |

_Timing: total 218s (discovery 71.4s, screen 1.9s, GT prime 0.4s, scoring 144.3s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/176; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
