# Last scan 2026-11-10T08:02:55Z - mode: helius (box heartbeat stale (241 min); budget 60/3000)

```
[fast_scan] 130 candidate mints from 9 source tags; 126 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored PREDICT in 72s
[fast_scan] scored SPCX in 80s
[fast_scan] scored HODLER in 81s
[fast_scan] scored BORLY in 82s
[fast_scan] scored ACT in 82s
[fast_scan] scored MILES in 82s
[fast_scan] scored OnlyCats in 83s
[fast_scan] scored FLOAT in 83s
# Market scan 2026-11-10 08:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,834 (+1.5% 24h), ETH $2,118 (+1.3% 24h), SOL $86.08 (+0.7% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.9% (mcap $2.47B, vol $334.31M), pump-fun +1.0% (mcap $971.55M, vol $111.25M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $52.9k | $143.3k | 19.2 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 63* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $161.4k | $2.65M | 1.1 d | h24 +374% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $606.4k | $2.01M | 22.4 h | h24 +24200% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.7k | $1.39M | 8.4 h | h24 +2329% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $92.2k | $1.34M | 7.9 h | h24 +2996% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.27M | $10.13M | 12.4 d | h24 -24% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,401 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.34M | $9.87M | 751.9 d | h24 +15% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders 136,109 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.58M | 167.0 d | h24 +6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 344,262 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $606.2k | $2.01M | -3% | -16% | +24200% | 0.1x | none flagged (still high risk) | 71 |
| [HAMWS](https://pump.fun/coin/Gg36bR4gXvN1hqDu6eoFNynhpfxoYg8oe47a2teZpump) | `Gg36bR4gXvN1hqDu6eoFNynhpfxoYg8oe47a2teZpump` | $71.8k | $221.5k | +521% | +521% | +521% | 8.9x | spike (+521% 1h, +521% 6h); < 1h old | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $92.2k | $1.34M | -4% | +11% | +2996% | 14.5x | none flagged (still high risk) | 71 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.6k | $1.38M | +11% | -21% | +2324% | 19.7x | none flagged (still high risk) | 71 |
| [OpenAI](https://pump.fun/coin/D9qbfie8dUbC8JgkSE35pDXNiTCwyGadMw1ifZXbpump) | `D9qbfie8dUbC8JgkSE35pDXNiTCwyGadMw1ifZXbpump` | $29.6k | $156.0k | +344% | +344% | +344% | 2.1x | thin liq $29.6k; spike (+344% 1h, +344% 6h); < 1h old | not scored |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $27.9k | $124.8k | +90% | +591% | +260% | 18.9x | thin liq $27.9k; spike (+90% 1h, +591% 6h) | not scored |

_Timing: total 156s (discovery 71.9s, screen 1.3s, GT prime 0.2s, scoring 82.9s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/145; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
