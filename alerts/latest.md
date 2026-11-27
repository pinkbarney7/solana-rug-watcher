# Last scan 2026-11-27T12:29:34Z - mode: helius (box heartbeat stale (506 min); budget 445/3000)

```
[fast_scan] 109 candidate mints from 10 source tags; 106 with pair data; 23 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 72s
[fast_scan] scored PAXG in 81s
[fast_scan] scored Snowball in 81s
[fast_scan] scored BASKET in 82s
[fast_scan] scored UGOS in 82s
[fast_scan] scored CATE in 82s
[fast_scan] scored FSD V15 in 83s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 12:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,552 (+1.6% 24h), ETH $1,720 (+1.2% 24h), SOL $73.06 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.4% (mcap $1.93B, vol $252.31M), pump-fun +4.0% (mcap $813.18M, vol $94.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $118.3k | $432.9k | 2.3 d | h24 -43% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $125.5k | $624.1k | 1.8 d | h24 +3980% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $263.6k | $11.68M | 1.5 d | h24 +24% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.3% (+9.3); #11 not checked (+3) |
| 63* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #8 Turnover / bot pattern WARN (+4) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.8k | $123.03M | 15.1 h | h24 +414006% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.6k | $635.6k | 1068.8 d | h24 +22% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,725 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.68M | 123.8 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,638 (growth n/a: first sighting) |
| 56* | SKIP | [PAXG](https://dexscreener.com/solana/CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22) | `CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22` | $45.25M | $45.37M | 243.4 d | h24 -0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 29 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $2.22M | $2.66M | +118689% | +8630% | +8630% | 0.1x | spike (+118689% 1h, +8630% 6h) | not scored |
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.8k | $123.03M | +2% | +18% | +414006% | 0.5x | liq/mcap 0.6%; lopsided buys/sells 190.95 | 75 |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $60.4k | $625.7k | +28% | +220% | +8592% | 18.3x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $64.3k | $627.2k | -18% | +3% | +4001% | 35.5x | churn 36x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $38.9k | $272.2k | +22% | +1274% | +745% | 25.2x | thin liq $38.9k; churn 25x vol/liq; spike (+22% 1h, +1274% 6h) | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $23.2k | $109.7k | +90% | +282% | +282% | 13.5x | thin liq $23.2k | not scored |

_Timing: total 156s (discovery 71.4s, screen 1.1s, GT prime 0.5s, scoring 83.3s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/165; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
