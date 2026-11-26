# Last scan 2026-11-26T10:46:09Z - mode: helius (box heartbeat stale (402 min); budget 287/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 114 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (76s)
[fast_scan] scored UHI in 72s
[fast_scan] scored NORFEATH in 80s
[fast_scan] scored DOG in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored Grodia in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored Anthropic in 82s
[fast_scan] scored JIMMY in 84s
[fast_scan] scored MOODENG in 71s
# Market scan 2026-11-26 10:46 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,598 (+2.9% 24h), ETH $1,696 (+3.1% 24h), SOL $70.79 (+4.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +7.5% (mcap $1.90B, vol $354.55M), pump-fun +5.1% (mcap $785.00M, vol $137.45M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $126.2k | $743.3k | 2.6 d | h24 -31% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $51.1k | $478.0k | 13.7 h | h24 +942% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $51.0k | $482.1k | 12.3 h | h24 +1266% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $220.3k | $127.6k | 2.0 h | h24 +78% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Anthropic](https://dexscreener.com/solana/8Di9FbUApRwpaEoTBh8xdDtqeq5nhn6mbyXetbLiDanA) | `8Di9FbUApRwpaEoTBh8xdDtqeq5nhn6mbyXetbLiDanA` | $179.4k | $128.7k | 1.3 h | h24 +152% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 63* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $85.1k | $1.39M | 11.4 h | h24 +3791% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #16 Exit liquidity (Jupiter quotes) WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.27M | 672.4 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,128 (growth n/a: first sighting) |
| 56* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.86M | $27.92M | 806.7 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,020 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.67M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,262 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $184.5k | $6.26M | +6% | +360% | +19778% | 15.5x | liq/mcap 2.9%; spike (+6% 1h, +360% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $85.1k | $1.39M | +25% | +39% | +3791% | 10.0x | none flagged (still high risk) | 63 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $40.1k | $277.5k | -6% | +871% | +871% | 36.0x | thin liq $40.1k; churn 36x vol/liq; spike (-6% 1h, +871% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $51.0k | $482.1k | +31% | -56% | +1266% | 44.6x | churn 45x vol/liq | 52 |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $51.1k | $478.0k | +1% | -19% | +942% | 34.7x | churn 35x vol/liq | 52 |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $39.1k | $228.7k | -11% | -51% | +687% | 105.8x | thin liq $39.1k; churn 106x vol/liq | not scored |

_Timing: total 220s (discovery 75.2s, screen 1.1s, GT prime 0.4s, scoring 143.6s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
