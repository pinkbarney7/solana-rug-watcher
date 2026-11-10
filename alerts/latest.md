# Last scan 2026-11-10T05:42:33Z - mode: helius (box heartbeat stale (101 min); budget 0/3000)

```
[fast_scan] 129 candidate mints from 10 source tags; 125 with pair data; 27 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored XTEN in 71s
[fast_scan] scored MILES in 80s
[fast_scan] scored FLOAT in 80s
[fast_scan] scored CATE in 80s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored NVDAx in 81s
[fast_scan] scored HODLER in 81s
# Market scan 2026-11-10 05:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,774 (+0.7% 24h), ETH $2,124 (-0.1% 24h), SOL $86.20 (-0.7% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $2.45B, vol $357.62M), pump-fun -1.7% (mcap $966.19M, vol $109.33M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $54.6k | $147.1k | 16.9 h | h24 -4% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 62* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $182.2k | $2.45M | 1.1 d | h24 +405% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $632.0k | $2.10M | 20.1 h | h24 +25228% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 73* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $174.3k | $2.30M | 1.0 d | h24 +384% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.30M | $10.13M | 12.3 d | h24 -24% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,156 (growth n/a: first sighting) |
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.75M | 106.6 d | h24 -2% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 426,339 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.75M | $39.68M | 500.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 401,038 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $631.8k | $2.10M | -3% | +4% | +25228% | 0.1x | none flagged (still high risk) | 71 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $92.0k | $1.34M | -11% | +3000% | +3000% | 12.7x | spike (-11% 1h, +3000% 6h) | not scored |
| [MOMO](https://pump.fun/coin/488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump) | `488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump` | $54.3k | $187.2k | +506% | +1577% | +1591% | 1.9x | spike (+506% 1h, +1577% 6h) | not scored |
| [BREW](https://dexscreener.com/solana/52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd) | `52N8mH4XGpnsQJbpexD3oxw1G2zZn7m2jX6VSpkd6btd` | $28.3k | $137.5k | +548% | +448% | +448% | 8.5x | thin liq $28.3k; spike (+548% 1h, +448% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $100.2k | $1.52M | +13% | +386% | +2567% | 17.6x | spike (+13% 1h, +386% 6h) | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.3k | $905.6k | +46% | +335% | +785% | 3.8x | spike (+46% 1h, +335% 6h) | not scored |

_Timing: total 154s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 81.1s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/135; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
