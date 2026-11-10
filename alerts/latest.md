# Last scan 2026-11-10T09:37:35Z - mode: helius (box heartbeat stale (336 min); budget 80/3000)

```
[fast_scan] 125 candidate mints from 9 source tags; 119 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BORLY in 72s
[fast_scan] scored ZEC in 80s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BIG in 82s
[fast_scan] scored FLOAT in 82s
[fast_scan] scored MILES in 82s
[fast_scan] scored HODLER in 83s
# Market scan 2026-11-10 09:37 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,367 (+0.2% 24h), ETH $2,101 (-0.3% 24h), SOL $85.28 (-1.6% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $2.45B, vol $347.83M), pump-fun -1.2% (mcap $964.14M, vol $111.73M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.3k | $1.33M | 10.0 h | h24 +2225% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $51.1k | $138.8k | 20.8 h | h24 -10% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $80.8k | $714.0k | 1.9 d | h24 +633% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $583.7k | $1.93M | 24.0 h | h24 +23134% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 74* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $176.3k | $2.80M | 1.2 d | h24 +331% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.27M | $10.02M | 12.5 d | h24 -28% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders +0.0% in 1h (now 42,431) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.41M | $13.51M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 344,476 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.88M | $28.2k | 390.7 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 387,887 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $583.4k | $1.93M | +1% | -19% | +23134% | 0.2x | none flagged (still high risk) | 71 |
| [AMPED](https://pump.fun/coin/yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump) | `yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump` | $39.1k | $268.5k | +154% | +661% | +661% | 1.9x | thin liq $39.1k; spike (+154% 1h, +661% 6h); lopsided buys/sells 3.23 | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.3k | $1.33M | -3% | +3% | +2225% | 21.1x | none flagged (still high risk) | 59 |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $29.5k | $140.3k | +306% | +306% | +306% | 21.9x | thin liq $29.5k; spike (+306% 1h, +306% 6h); < 1h old | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $35.9k | $211.8k | -83% | -83% | +390% | 43.2x | thin liq $35.9k; churn 43x vol/liq | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $75.9k | $723.2k | -11% | -9% | +642% | 4.8x | none flagged (still high risk) | 68 |

_Timing: total 156s (discovery 71.6s, screen 1.3s, GT prime 0.4s, scoring 82.5s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/143; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
