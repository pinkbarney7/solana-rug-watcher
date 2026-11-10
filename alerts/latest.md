# Last scan 2026-11-10T05:23:51Z - mode: helius (box heartbeat stale (82 min); budget 0/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 124 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored XTEN in 71s
[fast_scan] scored MILES in 79s
[fast_scan] scored FLOAT in 80s
[fast_scan] scored CATE in 80s
[fast_scan] scored PREDICT in 80s
[fast_scan] scored HODLER in 81s
[fast_scan] scored NVDAx in 81s
# Market scan 2026-11-10 05:23 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,747 (+0.4% 24h), ETH $2,122 (-0.5% 24h), SOL $86.03 (-1.2% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.3% (mcap $2.46B, vol $355.44M), pump-fun -1.7% (mcap $966.58M, vol $112.03M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $54.9k | $145.7k | 16.5 h | h24 -5% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 62* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $179.0k | $2.41M | 1.0 d | h24 +412% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $646.3k | $2.15M | 19.8 h | h24 +25883% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 73* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $168.7k | $2.20M | 1.0 d | h24 +383% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.31M | $10.13M | 12.3 d | h24 -25% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,151 (growth n/a: first sighting) |
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.83M | 106.5 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 426,329 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.75M | $39.62M | 500.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 401,038 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $646.1k | $2.15M | -3% | +4% | +25883% | 0.1x | none flagged (still high risk) | 71 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $94.3k | $1.41M | +9% | +3164% | +3164% | 12.2x | spike (+9% 1h, +3164% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $103.1k | $1.62M | +30% | +2732% | +2732% | 17.0x | spike (+30% 1h, +2732% 6h) | not scored |
| [BREW](https://dexscreener.com/solana/52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd) | `52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd` | $22.6k | $89.4k | +536% | +256% | +256% | 8.0x | thin liq $22.6k; spike (+536% 1h, +256% 6h) | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $83.0k | $858.9k | +22% | +316% | +743% | 3.9x | spike (+22% 1h, +316% 6h) | not scored |
| [KAWAENE](https://pump.fun/coin/Eqx3sZXKgZ49XrZfKkUAdNz8D8keZtQtNG83wisxpump) | `Eqx3sZXKgZ49XrZfKkUAdNz8D8keZtQtNG83wisxpump` | $31.1k | $167.8k | +26% | +353% | +353% | 8.0x | thin liq $31.1k; spike (+26% 1h, +353% 6h) | not scored |

_Timing: total 154s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 80.9s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/137; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
