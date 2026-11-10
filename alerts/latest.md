# Last scan 2026-11-10T10:35:01Z - mode: helius (box heartbeat stale (393 min); budget 100/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 120 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored AODF in 72s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored ZEC in 81s
[fast_scan] scored FLOAT in 82s
[fast_scan] scored MILES in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored BIG in 82s
[fast_scan] scored BORLY in 83s
# Market scan 2026-11-10 10:34 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,239 (+0.1% 24h), ETH $2,091 (-0.6% 24h), SOL $85.16 (-1.0% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.0% (mcap $2.44B, vol $349.13M), pump-fun -1.6% (mcap $962.15M, vol $111.60M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $58.3k | $168.0k | 21.7 h | h24 +10% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.4k | $802.5k | 1.9 d | h24 +724% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.6k | $1.39M | 11.0 h | h24 +2339% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 78* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $119.42M | 19.9 h | h24 +202208% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $143.6k | $2.91M | 1.2 d | h24 +308% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.26M | $10.14M | 12.5 d | h24 -26% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,438 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.87M | $28.2k | 390.7 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 388,011 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.49M | $13.58M | 167.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 345,358 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $119.42M | +1% | +8% | +202208% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.31 | 78 |
| [DERP404](https://pump.fun/coin/FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump) | `FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump` | $132.3k | $452.8k | +181% | +1210% | +1210% | 15.5x | spike (+181% 1h, +1210% 6h) | not scored |
| [Rockstar](https://pump.fun/coin/45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump) | `45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump` | $51.1k | $447.8k | +175% | +1179% | +1179% | 2.0x | spike (+175% 1h, +1179% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $95.4k | $1.39M | -1% | +7% | +2326% | 21.1x | none flagged (still high risk) | 71 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $40.3k | $264.3k | +20% | -81% | +511% | 39.8x | thin liq $40.3k; churn 40x vol/liq | not scored |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $27.3k | $118.2k | -6% | +243% | +243% | 32.7x | thin liq $27.3k; churn 33x vol/liq | not scored |

_Timing: total 156s (discovery 71.7s, screen 1.3s, GT prime 0.4s, scoring 82.6s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/149; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
