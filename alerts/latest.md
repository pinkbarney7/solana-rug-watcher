# Last scan 2026-11-10T09:31:09Z - mode: helius (box heartbeat stale (329 min); budget 80/3000)

```
[fast_scan] 128 candidate mints from 9 source tags; 122 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 72s
[fast_scan] scored BIG in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BORLY in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored MILES in 82s
[fast_scan] scored PREDICT in 83s
# Market scan 2026-11-10 09:31 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,286 (+0.2% 24h), ETH $2,098 (-0.4% 24h), SOL $85.17 (-1.6% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $2.45B, vol $347.83M), pump-fun -1.2% (mcap $964.14M, vol $111.73M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $81.5k | $727.8k | 1.9 d | h24 +647% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $574.2k | $1.89M | 23.9 h | h24 +22692% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $98.4k | $1.48M | 9.9 h | h24 +2484% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $51.1k | $138.8k | 20.7 h | h24 -10% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 74* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $175.9k | $2.80M | 1.2 d | h24 +339% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.26M | $28.40M | 106.7 d | h24 -2% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 426,365 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.41M | $13.47M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,476 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.88M | $28.3k | 390.7 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,887 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $574.0k | $1.89M | -3% | -18% | +22692% | 0.2x | none flagged (still high risk) | 59 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.7k | $1.40M | +1% | -15% | +2344% | 20.5x | none flagged (still high risk) | 59 |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $28.7k | $127.0k | +268% | +268% | +268% | 21.7x | thin liq $28.7k; spike (+268% 1h, +268% 6h); < 1h old | not scored |
| [AMPED](https://pump.fun/coin/yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump) | `yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump` | $37.1k | $242.3k | -42% | +587% | +587% | 2.0x | thin liq $37.1k; spike (-42% 1h, +587% 6h); lopsided buys/sells 3.21 | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $34.3k | $194.3k | -86% | -85% | +349% | 44.8x | thin liq $34.3k; churn 45x vol/liq | not scored |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $37.5k | $221.0k | +10% | +99% | +526% | 37.3x | thin liq $37.5k; churn 37x vol/liq | not scored |

_Timing: total 156s (discovery 71.6s, screen 1.3s, GT prime 0.2s, scoring 82.5s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/143; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
