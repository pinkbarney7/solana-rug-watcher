# Last scan 2026-11-10T05:15:37Z - mode: helius (box heartbeat stale (74 min); budget 0/3000)

```
[fast_scan] 128 candidate mints from 9 source tags; 124 with pair data; 28 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored MILES in 71s
[fast_scan] scored XTEN in 79s
[fast_scan] scored HODLER in 80s
[fast_scan] scored NVDAx in 80s
[fast_scan] scored FLOAT in 80s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored CATE in 81s
# Market scan 2026-11-10 05:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,750 (+0.2% 24h), ETH $2,123 (-0.5% 24h), SOL $86.16 (-1.1% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.1% (mcap $2.46B, vol $337.93M), pump-fun -1.9% (mcap $965.05M, vol $111.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $55.8k | $152.4k | 16.4 h | h24 -1% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $632.2k | $2.10M | 19.6 h | h24 +25247% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 73* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $178.0k | $2.41M | 1.0 d | h24 +411% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 73* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $168.3k | $2.21M | 1.0 d | h24 +401% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.31M | $10.12M | 12.3 d | h24 -26% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,156 (growth n/a: first sighting) |
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.80M | 106.5 d | h24 -1% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 426,329 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.75M | $39.59M | 500.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 401,038 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $631.9k | $2.10M | -12% | +2% | +25247% | 0.1x | none flagged (still high risk) | 59 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $108.1k | $1.77M | +25% | +3003% | +3003% | 16.1x | spike (+25% 1h, +3003% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $90.2k | $1.29M | -2% | +2889% | +2889% | 12.6x | spike (-2% 1h, +2889% 6h) | not scored |
| [BREW](https://dexscreener.com/solana/52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd) | `52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd` | $18.5k | $58.6k | +851% | +134% | +134% | 8.5x | thin liq $18.5k; spike (+851% 1h, +134% 6h) | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $82.7k | $851.3k | +36% | +305% | +724% | 3.9x | spike (+36% 1h, +305% 6h) | not scored |
| [KAWAENE](https://pump.fun/coin/Eqx3sZXKgZ49XrZfKkUAdNz8D8keZtQtNG83wisxpump) | `Eqx3sZXKgZ49XrZfKkUAdNz8D8keZtQtNG83wisxpump` | $31.0k | $166.7k | +13% | +350% | +350% | 7.6x | thin liq $31.0k; spike (+13% 1h, +350% 6h) | not scored |

_Timing: total 154s (discovery 71.8s, screen 1.3s, GT prime 0.2s, scoring 81.0s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/137; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
