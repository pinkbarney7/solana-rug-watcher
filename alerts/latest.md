# Last scan 2026-11-10T07:56:42Z - mode: helius (box heartbeat stale (235 min); budget 50/3000)

```
[fast_scan] 131 candidate mints from 10 source tags; 129 with pair data; 27 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored MILES in 72s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored HODLER in 81s
[fast_scan] scored OnlyCats in 82s
[fast_scan] scored FLOAT in 82s
[fast_scan] scored ACT in 82s
[fast_scan] scored BORLY in 83s
[fast_scan] scored SPCX in 83s
# Market scan 2026-11-10 07:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,817 (+1.2% 24h), ETH $2,119 (+1.3% 24h), SOL $86.10 (+0.7% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.9% (mcap $2.47B, vol $334.31M), pump-fun +1.0% (mcap $971.55M, vol $111.25M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $50.9k | $134.4k | 19.1 h | h24 -12% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 63* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $160.2k | $2.64M | 1.1 d | h24 +374% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $606.4k | $2.01M | 22.3 h | h24 +24200% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.3k | $1.32M | 8.3 h | h24 +2210% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $91.5k | $1.32M | 7.8 h | h24 +2951% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.27M | $10.15M | 12.4 d | h24 -24% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,400 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.36M | $10.06M | 751.9 d | h24 +18% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders 136,109 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.64M | 167.0 d | h24 +6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,262 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $606.2k | $2.01M | -1% | +17% | +24200% | 0.1x | none flagged (still high risk) | 71 |
| [HAMWS](https://pump.fun/coin/Gg36bR4gXvN1hqDu6eoFNynhpfxoYg8oe47a2teZpump) | `Gg36bR4gXvN1hqDu6eoFNynhpfxoYg8oe47a2teZpump` | $64.9k | $192.6k | +440% | +440% | +440% | 8.0x | spike (+440% 1h, +440% 6h); < 1h old | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $91.6k | $1.32M | -6% | +8% | +2951% | 14.6x | none flagged (still high risk) | 71 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.4k | $1.32M | +11% | +42% | +2210% | 20.1x | none flagged (still high risk) | 71 |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $25.7k | $106.7k | +81% | +438% | +208% | 20.4x | thin liq $25.7k; spike (+81% 1h, +438% 6h) | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $73.8k | $680.3k | -6% | +391% | +565% | 4.8x | spike (-6% 1h, +391% 6h) | not scored |

_Timing: total 156s (discovery 71.6s, screen 1.4s, GT prime 0.4s, scoring 83.0s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/145; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
