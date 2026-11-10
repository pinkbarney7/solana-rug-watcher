# Last scan 2026-11-10T07:22:08Z - mode: helius (box heartbeat stale (199 min); budget 30/3000)

```
[fast_scan] 136 candidate mints from 10 source tags; 134 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored MILES in 72s
[fast_scan] scored OnlyCats in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored XTEN in 83s
[fast_scan] scored BORLY in 83s
[fast_scan] scored HODLER in 83s
[fast_scan] scored FLOAT in 74s
# Market scan 2026-11-10 07:22 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,627 (+1.0% 24h), ETH $2,116 (+1.3% 24h), SOL $86.04 (+0.8% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $2.47B, vol $340.32M), pump-fun -0.3% (mcap $968.87M, vol $111.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $96.4k | $1.47M | 7.2 h | h24 +3292% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $55.6k | $151.6k | 18.5 h | h24 -1% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 63* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $151.4k | $2.53M | 1.1 d | h24 +374% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 70* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $89.3k | $1.21M | 7.7 h | h24 +2025% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $632.7k | $2.11M | 21.7 h | h24 +25335% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 73* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $159.4k | $2.73M | 1.1 d | h24 +369% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.29M | $10.47M | 12.4 d | h24 -22% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,394 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.35M | $9.98M | 751.8 d | h24 +15% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders 136,105 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.46M | $13.50M | 167.0 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.1% in 2h (now 344,084) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $632.5k | $2.11M | +1% | +19% | +25335% | 0.1x | none flagged (still high risk) | 71 |
| [Rockstar](https://pump.fun/coin/DAE1rsrmNjQvodCpkna7XtDTNFm7e5KgT1u6oQZfpump) | `DAE1rsrmNjQvodCpkna7XtDTNFm7e5KgT1u6oQZfpump` | $56.0k | $535.9k | +331% | +1421% | +1421% | 1.2x | spike (+331% 1h, +1421% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $96.4k | $1.47M | +10% | +28% | +3291% | 13.3x | none flagged (still high risk) | 59 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $89.3k | $1.21M | -19% | +26% | +2025% | 20.7x | none flagged (still high risk) | 70 |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $41.9k | $279.9k | +72% | +215% | +692% | 32.4x | thin liq $41.9k; churn 32x vol/liq | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $79.2k | $782.0k | -10% | +378% | +664% | 4.3x | spike (-10% 1h, +378% 6h) | not scored |

_Timing: total 219s (discovery 71.6s, screen 1.4s, GT prime 0.4s, scoring 146.0s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/164; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
