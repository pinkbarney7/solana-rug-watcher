# Last scan 2026-11-27T13:09:27Z - mode: helius (box heartbeat stale (546 min); budget 475/3000)

```
[fast_scan] 102 candidate mints from 10 source tags; 99 with pair data; 21 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 70s
[fast_scan] scored TROLL in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored PUMPCHAN in 79s
[fast_scan] scored UGOS in 79s
[fast_scan] scored Rizzmas in 80s
# Market scan 2026-11-27 13:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,472 (+1.2% 24h), ETH $1,721 (+1.0% 24h), SOL $73.07 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.6% (mcap $1.94B, vol $253.37M), pump-fun +3.8% (mcap $810.82M, vol $96.54M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $121.4k | $671.7k | 1.8 d | h24 +4475% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $259.7k | $11.33M | 1.5 d | h24 +24% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.3% (+9.3); #11 not checked (+3) |
| 75* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $801.3k | $125.07M | 15.8 h | h24 +420882% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $223.7k | $642.2k | 1068.8 d | h24 +20% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,728 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.99M | $21.79M | 847.1 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 219,031) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.55M | $13.76M | 184.2 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,432 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $801.3k | $125.09M | +3% | +18% | +420943% | 0.5x | liq/mcap 0.6%; lopsided buys/sells 183.81 | 75 |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $60.0k | $610.7k | +4% | +216% | +8384% | 19.4x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $67.3k | $684.6k | +5% | +28% | +4563% | 34.2x | churn 34x vol/liq | 52 |
| [ChokingCat](https://pump.fun/coin/ExpdNM5YykDnGTmyxCH5B3s7mdWi1cEreDvK6ic8pump) | `ExpdNM5YykDnGTmyxCH5B3s7mdWi1cEreDvK6ic8pump` | $22.1k | $93.5k | +206% | +206% | +206% | 11.3x | thin liq $22.1k; spike (+206% 1h, +206% 6h); < 1h old | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $35.4k | $223.8k | -1% | +113% | +595% | 29.2x | thin liq $35.4k; churn 29x vol/liq | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $20.3k | $83.9k | -45% | +192% | +192% | 19.7x | thin liq $20.3k | not scored |

_Timing: total 153s (discovery 71.4s, screen 1.1s, GT prime 0.8s, scoring 79.9s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/126; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
