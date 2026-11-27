# Last scan 2026-11-27T10:53:20Z - mode: helius (box heartbeat stale (410 min); budget 290/3000)

```
[fast_scan] 111 candidate mints from 10 source tags; 109 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 71s
[fast_scan] scored CLAUDIA in 79s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored pippin in 81s
[fast_scan] scored FSD V15 in 81s
[fast_scan] scored Rizzmas in 81s
[fast_scan] scored Snowball in 81s
# Market scan 2026-11-27 10:53 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,577 (+1.9% 24h), ETH $1,727 (+2.0% 24h), SOL $73.45 (+4.2% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.8% (mcap $1.93B, vol $258.29M), pump-fun +3.2% (mcap $802.90M, vol $90.21M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $137.8k | $853.5k | 1.7 d | h24 +4536% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $253.4k | $10.75M | 1.4 d | h24 +57% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.2); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $117.7k | $2.33M | 10.1 h | h24 +2043% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.0% (+5.9) |
| 63* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.8k | $628.1k | 1068.7 d | h24 +18% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,720 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.51M | $18.48M | 747.6 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,589 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.38M | $78.29B | 51.4 d | h24 -6% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 62,337 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $116.92M | $146.88M | +482526% | +482526% | +482526% | 0.0x | spike (+482526% 1h, +482526% 6h); < 1h old | not scored |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $64.2k | $483.5k | +16% | +156% | +6617% | 13.6x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $75.3k | $853.5k | -1% | +36% | +4536% | 29.3x | churn 29x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $117.1k | $2.32M | +4% | -21% | +2028% | 29.4x | churn 29x vol/liq | 60 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $31.4k | $180.7k | +41% | +461% | +461% | 25.4x | thin liq $31.4k; churn 25x vol/liq; spike (+41% 1h, +461% 6h) | not scored |
| [NIW](https://pump.fun/coin/CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump) | `CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump` | $22.0k | $117.9k | +14% | +306% | +306% | 0.2x | thin liq $22.0k; spike (+14% 1h, +306% 6h) | not scored |

_Timing: total 154s (discovery 71.4s, screen 1.2s, GT prime 0.4s, scoring 81.1s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/144; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
