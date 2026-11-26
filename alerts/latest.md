# Last scan 2026-11-26T11:06:20Z - mode: helius (box heartbeat stale (424 min); budget 287/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 112 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored Grodia in 72s
[fast_scan] scored DOG in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored UHI in 82s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored NORFEATH in 82s
[fast_scan] scored MOODENG in 83s
# Market scan 2026-11-26 11:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,462 (+2.8% 24h), ETH $1,693 (+2.9% 24h), SOL $70.46 (+4.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.9% (mcap $1.89B, vol $355.28M), pump-fun +4.4% (mcap $781.99M, vol $129.85M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $126.9k | $736.1k | 2.6 d | h24 -33% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $53.1k | $522.2k | 12.7 h | h24 +1380% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $52.3k | $499.7k | 14.0 h | h24 +989% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $227.2k | $133.2k | 2.3 h | h24 +86% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $86.0k | $1.42M | 11.8 h | h24 +3877% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.15M | 672.5 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,126 (growth n/a: first sighting) |
| 56* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.91M | $29.51M | 806.7 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,019 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.66M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,262 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $206.9k | $7.86M | +50% | +417% | +24832% | 15.2x | liq/mcap 2.6%; spike (+50% 1h, +417% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $85.6k | $1.41M | +22% | +32% | +3847% | 10.2x | none flagged (still high risk) | 59 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $37.9k | $248.8k | +9% | +1316% | +770% | 38.7x | thin liq $37.9k; churn 39x vol/liq; spike (+9% 1h, +1316% 6h) | not scored |
| [konnichiwa](https://pump.fun/coin/HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump) | `HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump` | $23.6k | $113.6k | +290% | +290% | +290% | 13.2x | thin liq $23.6k; spike (+290% 1h, +290% 6h); < 1h old | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $52.5k | $510.2k | +18% | -51% | +1346% | 43.9x | churn 44x vol/liq | 52 |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $50.3k | $463.5k | +3% | -24% | +910% | 35.8x | churn 36x vol/liq | 52 |

_Timing: total 156s (discovery 71.6s, screen 1.2s, GT prime 0.3s, scoring 82.6s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/158; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
