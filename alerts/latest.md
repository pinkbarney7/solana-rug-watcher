# Last scan 2026-11-10T05:38:19Z - mode: helius (box heartbeat stale (97 min); budget 0/3000)

```
[fast_scan] 126 candidate mints from 9 source tags; 122 with pair data; 30 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 72s
[fast_scan] scored BORLY in 81s
[fast_scan] scored MILES in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored PREDICT in 83s
[fast_scan] scored XTEN in 83s
[fast_scan] scored FLOAT in 83s
[fast_scan] scored NVDAx in 83s
# Market scan 2026-11-10 05:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,699 (+0.5% 24h), ETH $2,121 (-0.4% 24h), SOL $86.06 (-1.0% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $2.45B, vol $357.62M), pump-fun -1.7% (mcap $966.19M, vol $109.33M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $632.0k | $2.10M | 20.0 h | h24 +25228% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.7k | $1.39M | 6.0 h | h24 +2342% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $54.6k | $147.1k | 16.8 h | h24 -4% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 73* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $181.4k | $2.44M | 1.1 d | h24 +408% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 73* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $172.2k | $2.26M | 1.0 d | h24 +378% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.30M | $10.10M | 12.3 d | h24 -24% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,153 (growth n/a: first sighting) |
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.88M | 106.6 d | h24 -2% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 426,329 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.75M | $39.65M | 500.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 401,038 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $631.8k | $2.10M | -7% | +4% | +25228% | 0.1x | none flagged (still high risk) | 59 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $90.7k | $1.31M | -11% | +2921% | +2921% | 12.8x | spike (-11% 1h, +2921% 6h) | not scored |
| [MOMO](https://pump.fun/coin/488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump) | `488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump` | $55.8k | $198.1k | +538% | +1674% | +1690% | 1.8x | spike (+538% 1h, +1674% 6h) | not scored |
| [BREW](https://dexscreener.com/solana/52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd) | `52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd` | $27.9k | $135.3k | +440% | +439% | +439% | 8.3x | thin liq $27.9k; spike (+440% 1h, +439% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $96.9k | $1.43M | +9% | +266% | +2400% | 18.2x | none flagged (still high risk) | 59 |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $87.1k | $941.9k | +39% | +353% | +821% | 3.7x | spike (+39% 1h, +353% 6h) | not scored |

_Timing: total 157s (discovery 72.0s, screen 1.4s, GT prime 0.4s, scoring 83.0s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/148; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
