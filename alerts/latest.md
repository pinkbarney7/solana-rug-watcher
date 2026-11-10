# Last scan 2026-11-10T06:09:23Z - mode: helius (box heartbeat stale (127 min); budget 10/3000)

```
[fast_scan] 131 candidate mints from 9 source tags; 127 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BORLY in 72s
[fast_scan] scored AICoin in 80s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored TROLL in 81s
[fast_scan] scored ACT in 82s
[fast_scan] scored XTEN in 82s
[fast_scan] scored HODLER in 83s
[fast_scan] scored MILES in 83s
[fast_scan] scored FLOAT in 73s
# Market scan 2026-11-10 06:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,693 (+0.3% 24h), ETH $2,121 (-0.3% 24h), SOL $86.07 (-0.5% 24h)
- Fear & Greed: unavailable (gave up after 2 tries (HTTP 502))
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $2.47B, vol $359.49M), pump-fun -0.6% (mcap $968.66M, vol $117.55M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [AICoin](https://dexscreener.com/solana/6w792EhabdMTGqZtp77wWV5vZvvs4U89CqB8CYZesPq) | `6w792EhabdMTGqZtp77wWV5vZvvs4U89CqB8CYZesPq` | $154.5k | $97.0k | 1.4 h | h24 +105% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $627.6k | $2.09M | 20.5 h | h24 +25116% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $97.0k | $1.43M | 6.5 h | h24 +2403% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $53.7k | $142.5k | 17.3 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 73* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $178.5k | $2.35M | 1.1 d | h24 +354% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 73* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $143.2k | $2.49M | 1.1 d | h24 +373% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.32M | $10.59M | 12.3 d | h24 -22% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,307 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.35M | $9.92M | 751.8 d | h24 +13% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders +0.0% in 21h (now 136,091) |
| 68* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.46M | $28.54M | 829.8 d | h24 +7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 218,323 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $627.4k | $2.09M | -1% | +1% | +25116% | 0.1x | none flagged (still high risk) | 59 |
| [DINGA](https://pump.fun/coin/AmaENUv7SQowxEaWrZtT9gyR9HHJUBg9ULx6wce4pump) | `AmaENUv7SQowxEaWrZtT9gyR9HHJUBg9ULx6wce4pump` | $456.6k | $1.27M | +2150% | +3543% | +3543% | 0.5x | spike (+2150% 1h, +3543% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $91.4k | $1.32M | +16% | +541% | +2962% | 13.1x | spike (+16% 1h, +541% 6h) | not scored |
| [MOMO](https://pump.fun/coin/488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump) | `488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump` | $41.4k | $110.7k | -29% | +892% | +900% | 2.9x | thin liq $41.4k; spike (-29% 1h, +892% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $97.0k | $1.43M | -20% | +76% | +2403% | 18.4x | none flagged (still high risk) | 59 |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.3k | $904.9k | -4% | +338% | +784% | 3.8x | spike (-4% 1h, +338% 6h) | not scored |

_Timing: total 219s (discovery 71.8s, screen 1.4s, GT prime 0.4s, scoring 145.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/166; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
