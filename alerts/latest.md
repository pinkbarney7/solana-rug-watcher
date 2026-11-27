# Last scan 2026-11-27T12:44:41Z - mode: helius (box heartbeat stale (521 min); budget 475/3000)

```
[fast_scan] 105 candidate mints from 9 source tags; 103 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored UGOS in 71s
[fast_scan] scored Snowball in 79s
[fast_scan] scored SPCX in 79s
[fast_scan] scored ZEC in 80s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored BASKET in 81s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 12:44 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,507 (+1.2% 24h), ETH $1,721 (+1.0% 24h), SOL $72.98 (+2.9% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.6% (mcap $1.94B, vol $253.65M), pump-fun +3.9% (mcap $812.06M, vol $97.07M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $118.7k | $436.1k | 2.3 d | h24 -40% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $124.3k | $609.1k | 1.8 d | h24 +4444% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $265.1k | $11.83M | 1.5 d | h24 +27% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.2% (+9.3); #11 not checked (+3) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $795.8k | $123.60M | 15.4 h | h24 +415937% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.7k | $637.8k | 1068.8 d | h24 +20% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,728 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.55M | $13.68M | 184.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,432 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.40M | $18.7k | 407.8 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 2h (now 396,763) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UOF](https://pump.fun/coin/YPNSU64SduS3P3uTjCNVBDFz3TgrdiHbDhAndaGpump) | `YPNSU64SduS3P3uTjCNVBDFz3TgrdiHbDhAndaGpump` | $830.7k | $133.43M | +436846% | +436846% | +436846% | 0.5x | liq/mcap 0.6%; spike (+436846% 1h, +436846% 6h); < 1h old | not scored |
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $795.7k | $123.58M | +2% | +18% | +415856% | 0.5x | liq/mcap 0.6%; lopsided buys/sells 187.88 | 75 |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $61.1k | $640.9k | +17% | +232% | +8805% | 18.4x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $63.3k | $609.1k | -15% | +4% | +4444% | 36.2x | churn 36x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $40.6k | $295.2k | +12% | +1738% | +816% | 24.6x | thin liq $40.6k; spike (+12% 1h, +1738% 6h) | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $23.8k | $114.5k | +20% | +298% | +298% | 14.8x | thin liq $23.8k | not scored |

_Timing: total 156s (discovery 71.6s, screen 1.1s, GT prime 0.3s, scoring 83.0s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
