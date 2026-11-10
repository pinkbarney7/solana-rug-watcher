# Last scan 2026-11-10T09:08:03Z - mode: helius (box heartbeat stale (305 min); budget 70/3000)

```
[fast_scan] 135 candidate mints from 10 source tags; 129 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 78s
[fast_scan] scored MILES in 87s
[fast_scan] scored PREDICT in 87s
[fast_scan] scored ZEC in 87s
[fast_scan] scored 现金牛 in 88s
[fast_scan] scored BIG in 89s
[fast_scan] scored BORLY in 89s
[fast_scan] scored SPCX in 89s
[fast_scan] scored wXRP in 72s
# Market scan 2026-11-10 09:07 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,312 (-0.4% 24h), ETH $2,102 (-1.1% 24h), SOL $85.33 (-2.1% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $2.47B, vol $349.86M), pump-fun -0.6% (mcap $969.19M, vol $113.81M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $51.5k | $140.8k | 20.3 h | h24 -8% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $582.3k | $1.92M | 23.5 h | h24 +23056% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 63* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $170.7k | $2.71M | 1.2 d | h24 +328% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 67* | SKIP | [现金牛](https://dexscreener.com/solana/MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f) | `MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f` | $357.7k | $205.3k | 2.6 h | h24 +50% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $82.6k | $743.0k | 1.8 d | h24 +660% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $98.7k | $1.47M | 9.5 h | h24 +2482% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 65* | SKIP | [wXRP](https://dexscreener.com/solana/6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2) | `6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2` | $486.7k | $1 | 256.1 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,060 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.41M | $13.50M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,433 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.89M | $28.1k | 390.7 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,895 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $582.1k | $1.92M | -5% | -14% | +23056% | 0.2x | none flagged (still high risk) | 59 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $96.8k | $1.43M | +4% | -14% | +2400% | 20.0x | none flagged (still high risk) | 71 |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $27.4k | $130.0k | +267% | +267% | +267% | 10.3x | thin liq $27.4k; spike (+267% 1h, +267% 6h); < 1h old | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $47.5k | $364.1k | -71% | -73% | +742% | 31.4x | thin liq $47.5k; churn 31x vol/liq; spike (-71% 1h, -73% 6h) | not scored |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $34.8k | $190.0k | -26% | +123% | +438% | 40.0x | thin liq $34.8k; churn 40x vol/liq | not scored |
| [AMPED](https://pump.fun/coin/yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump) | `yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump` | $27.4k | $135.5k | -10% | +284% | +284% | 2.5x | thin liq $27.4k; lopsided buys/sells 3.12 | not scored |

_Timing: total 224s (discovery 71.6s, screen 1.5s, GT prime 0.5s, scoring 150.3s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/160; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
