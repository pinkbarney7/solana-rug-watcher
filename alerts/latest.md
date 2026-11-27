# Last scan 2026-11-27T12:34:51Z - mode: helius (box heartbeat stale (512 min); budget 455/3000)

```
[fast_scan] 110 candidate mints from 10 source tags; 108 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (64s)
[fast_scan] scored BASKET in 74s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Snowball in 82s
[fast_scan] scored PAXG in 82s
[fast_scan] scored Rizzmas in 82s
[fast_scan] scored FSD V15 in 83s
[fast_scan] scored UGOS in 83s
# Market scan 2026-11-27 12:34 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,531 (+1.6% 24h), ETH $1,719 (+1.2% 24h), SOL $72.95 (+3.2% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.4% (mcap $1.93B, vol $252.31M), pump-fun +4.0% (mcap $813.18M, vol $94.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $119.5k | $444.5k | 2.3 d | h24 -39% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $125.5k | $624.2k | 1.8 d | h24 +4177% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $264.6k | $11.78M | 1.5 d | h24 +25% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.2% (+9.3); #11 not checked (+3) |
| 63* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $221.7k | $143.0k | 1.1 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #8 Turnover / bot pattern WARN (+4) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.5k | $123.10M | 15.2 h | h24 +414251% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $223.0k | $638.8k | 1068.8 d | h24 +23% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,728 (growth n/a: first sighting) |
| 56* | SKIP | [PAXG](https://dexscreener.com/solana/CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22) | `CvuLMpiNq6VdaT7k7P7arU65sW5cu8q1z6hPT4wCzL22` | $45.25M | $45.37M | 243.4 d | h24 -0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 29 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.54M | $13.65M | 184.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.1% in 3h (now 400,512) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $2.22M | $2.65M | +118490% | +8619% | +8619% | 0.1x | spike (+118490% 1h, +8619% 6h) | not scored |
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $794.7k | $123.15M | +2% | +18% | +414407% | 0.5x | liq/mcap 0.6%; lopsided buys/sells 189.96 | 75 |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $60.6k | $629.2k | +25% | +222% | +8642% | 18.4x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $64.2k | $625.3k | -16% | +2% | +4098% | 35.6x | churn 36x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $38.2k | $261.4k | +10% | +1349% | +711% | 25.9x | thin liq $38.2k; churn 26x vol/liq; spike (+10% 1h, +1349% 6h) | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $26.5k | $140.6k | +104% | +389% | +389% | 12.4x | thin liq $26.5k; spike (+104% 1h, +389% 6h) | not scored |

_Timing: total 147s (discovery 63.2s, screen 1.1s, GT prime 0.4s, scoring 82.8s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 11/165; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
