# Last scan 2026-11-27T11:24:20Z - mode: helius (box heartbeat stale (440 min); budget 320/3000)

```
[fast_scan] 112 candidate mints from 9 source tags; 110 with pair data; 25 >= $50,000 liq; 5 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 74s
[fast_scan] scored CLAUDIA in 80s
[fast_scan] scored KAI in 80s
[fast_scan] scored Snowball in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored FSD V15 in 82s
[fast_scan] scored SuperFIONA in 82s
[fast_scan] scored baton in 73s
# Market scan 2026-11-27 11:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,572 (+1.6% 24h), ETH $1,724 (+1.5% 24h), SOL $73.19 (+3.5% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.8% (mcap $1.93B, vol $256.77M), pump-fun +3.1% (mcap $801.92M, vol $90.29M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $128.0k | $501.1k | 2.3 d | h24 -39% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 47* | CAUTION | [SuperFIONA](https://dexscreener.com/solana/4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG) | `4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG` | $235.4k | $135.7k | 2.3 h | h24 +66% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $139.0k | $814.5k | 1.7 d | h24 +3896% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 59* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $250.4k | $10.54M | 1.4 d | h24 +34% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $119.5k | $2.41M | 10.6 h | h24 +2116% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 5.0% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [baton](https://pump.fun/coin/Hg5Ja55T5wESq4vyFoiVCMeHXtGyVA69X2UHq8hgpump) | `Hg5Ja55T5wESq4vyFoiVCMeHXtGyVA69X2UHq8hgpump` | $471.4k | $4.67M | 78.6 d | h24 +36% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 90,902 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.85M | 123.8 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,604 (growth n/a: first sighting) |
| 61* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.38M | $78.29B | 51.4 d | h24 -5% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $110.22M | $146.32M | +7049518% | +480686% | +480686% | 0.0x | spike (+7049518% 1h, +480686% 6h) | not scored |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $64.4k | $548.2k | +24% | +180% | +7516% | 15.8x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $73.4k | $814.5k | -2% | +38% | +3896% | 30.3x | churn 30x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $120.1k | $2.44M | +9% | -28% | +2142% | 29.0x | liq/mcap 4.9%; churn 29x vol/liq | 66 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $33.5k | $204.7k | +67% | +535% | +535% | 25.2x | thin liq $33.5k; churn 25x vol/liq; spike (+67% 1h, +535% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $38.7k | $262.2k | +7% | +15% | +761% | 34.2x | thin liq $38.7k; churn 34x vol/liq | not scored |

_Timing: total 220s (discovery 71.7s, screen 1.1s, GT prime 0.5s, scoring 146.7s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/178; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
