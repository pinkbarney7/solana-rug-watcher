# Last scan 2026-11-10T05:56:42Z - mode: helius (box heartbeat stale (115 min); budget 10/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 123 with pair data; 26 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 72s
[fast_scan] scored PREDICT in 80s
[fast_scan] scored NVDAx in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored XTEN in 82s
[fast_scan] scored MILES in 82s
[fast_scan] scored FLOAT in 83s
[fast_scan] scored BORLY in 83s
# Market scan 2026-11-10 05:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,895 (+0.6% 24h), ETH $2,128 (-0.0% 24h), SOL $86.44 (-0.3% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.2% (mcap $2.47B, vol $359.32M), pump-fun -0.6% (mcap $969.12M, vol $114.62M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $625.5k | $2.08M | 20.3 h | h24 +25039% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $54.6k | $147.1k | 17.1 h | h24 -4% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 62* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $177.5k | $2.35M | 1.1 d | h24 +374% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $99.0k | $1.48M | 6.3 h | h24 +2499% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 74* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $142.5k | $2.50M | 1.1 d | h24 +388% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.63M | 106.6 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 426,339 (growth n/a: first sighting) |
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.33M | $10.41M | 12.3 d | h24 -24% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,189 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.75M | $39.70M | 500.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 400,946 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $625.3k | $2.08M | -1% | +6% | +25039% | 0.1x | none flagged (still high risk) | 59 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $91.7k | $1.33M | -1% | +2974% | +2974% | 12.9x | spike (-1% 1h, +2974% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $99.0k | $1.48M | +6% | +146% | +2499% | 17.9x | none flagged (still high risk) | 71 |
| [BREW](https://dexscreener.com/solana/52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd) | `52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd` | $28.0k | $125.8k | +374% | +401% | +401% | 10.0x | thin liq $28.0k; spike (+374% 1h, +401% 6h) | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.2k | $904.0k | +56% | +333% | +784% | 3.8x | spike (+56% 1h, +333% 6h) | not scored |
| [MUBBO](https://pump.fun/coin/JBUe4NZu4rm4Ej5AsLZECZLHvnWpFRmhn9oPLXCVpump) | `JBUe4NZu4rm4Ej5AsLZECZLHvnWpFRmhn9oPLXCVpump` | $21.1k | $78.0k | +108% | +108% | +108% | 9.3x | thin liq $21.1k; spike (+108% 1h, +108% 6h); < 1h old | not scored |

_Timing: total 156s (discovery 71.8s, screen 1.4s, GT prime 0.4s, scoring 82.8s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/143; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
