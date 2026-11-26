# Last scan 2026-11-26T11:24:27Z - mode: helius (box heartbeat stale (442 min); budget 287/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 110 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored UHI in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored NORFEATH in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored DOG in 81s
[fast_scan] scored MOODENG in 81s
[fast_scan] scored JIMMY in 82s
# Market scan 2026-11-26 11:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,608 (+3.2% 24h), ETH $1,698 (+3.2% 24h), SOL $70.70 (+4.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +7.1% (mcap $1.89B, vol $352.42M), pump-fun +4.7% (mcap $783.89M, vol $131.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $124.6k | $703.8k | 2.6 d | h24 -37% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $53.3k | $517.2k | 14.3 h | h24 +1027% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $233.4k | $138.4k | 2.6 h | h24 +93% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $90.0k | $1.55M | 12.1 h | h24 +4244% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.26M | 672.5 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,126 (growth n/a: first sighting) |
| 57* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.93M | $29.99M | 806.7 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,025 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.66M | 183.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,199 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $206.3k | $7.75M | +26% | +437% | +24503% | 16.5x | liq/mcap 2.7%; spike (+26% 1h, +437% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $90.0k | $1.55M | +26% | +52% | +4244% | 9.9x | none flagged (still high risk) | 57 |
| [konnichiwa](https://pump.fun/coin/HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump) | `HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump` | $23.8k | $113.3k | +318% | +289% | +289% | 17.9x | thin liq $23.8k; spike (+318% 1h, +289% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $59.5k | $649.9k | +56% | -37% | +1742% | 39.1x | churn 39x vol/liq; spike (+56% 1h, -37% 6h) | not scored |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $39.7k | $270.6k | +16% | +126% | +847% | 37.5x | thin liq $39.7k; churn 37x vol/liq | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $53.3k | $517.2k | +19% | -15% | +1027% | 34.2x | churn 34x vol/liq | 52 |

_Timing: total 155s (discovery 71.6s, screen 1.2s, GT prime 0.4s, scoring 81.5s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/142; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
