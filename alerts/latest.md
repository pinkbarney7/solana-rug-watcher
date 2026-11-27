# Last scan 2026-11-27T12:17:48Z - mode: helius (box heartbeat stale (495 min); budget 445/3000)

```
[fast_scan] 111 candidate mints from 9 source tags; 108 with pair data; 26 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 73s
[fast_scan] scored UATF in 80s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored UGOS in 81s
[fast_scan] scored Snowball in 82s
[fast_scan] scored PAXG in 82s
[fast_scan] scored FSD V15 in 83s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 12:17 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,608 (+1.7% 24h), ETH $1,722 (+1.3% 24h), SOL $73.21 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.3% (mcap $1.93B, vol $255.20M), pump-fun +2.3% (mcap $799.96M, vol $88.71M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $127.2k | $509.0k | 2.3 d | h24 -34% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $124.9k | $602.5k | 1.7 d | h24 +3802% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $266.1k | $11.87M | 1.4 d | h24 +31% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.2% (+9.3); #11 not checked (+3) |
| 63* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #8 Turnover / bot pattern WARN (+4) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.2k | $122.59M | 14.9 h | h24 +412520% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $218.5k | $611.9k | 1068.8 d | h24 +18% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 395,725) |
| 56* | SKIP | [PAXG](https://dexscreener.com/solana/CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22) | `CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22` | $45.25M | $45.37M | 243.4 d | h24 -2% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 29 (growth n/a: first sighting) |
| 56* | SKIP | [UATF](https://dexscreener.com/solana/A2pRKGwsyLi47pLZEaJah17cN2CHezPrEYfwDpP1tL5R) | `A2pRKGwsyLi47pLZEaJah17cN2CHezPrEYfwDpP1tL5R` | $11.70M | $11.90M | 160.9 d | h24 -0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 39 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.2k | $122.59M | +3% | +17% | +412520% | 0.5x | liq/mcap 0.6%; lopsided buys/sells 194.38 | 75 |
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $2.27M | $2.66M | -98% | +8649% | +8649% | 0.1x | spike (-98% 1h, +8649% 6h) | not scored |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $62.3k | $634.8k | +21% | +225% | +8720% | 17.5x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $63.4k | $607.2k | -23% | -8% | +3832% | 35.9x | churn 36x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $34.2k | $211.3k | +31% | +1000% | +556% | 28.0x | thin liq $34.2k; churn 28x vol/liq; spike (+31% 1h, +1000% 6h) | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $24.2k | $119.5k | +316% | +316% | +316% | 11.3x | thin liq $24.2k; spike (+316% 1h, +316% 6h); < 1h old | not scored |

_Timing: total 156s (discovery 71.7s, screen 1.2s, GT prime 0.4s, scoring 83.2s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/165; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
