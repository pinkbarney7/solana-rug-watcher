# Last scan 2026-11-10T10:24:28Z - mode: helius (box heartbeat stale (383 min); budget 90/3000)

```
[fast_scan] 123 candidate mints from 9 source tags; 119 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored PREDICT in 71s
[fast_scan] scored ZEC in 79s
[fast_scan] scored FLOAT in 80s
[fast_scan] scored BORLY in 80s
[fast_scan] scored MILES in 81s
[fast_scan] scored BIG in 81s
[fast_scan] scored SPCX in 81s
# Market scan 2026-11-10 10:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,248 (+0.2% 24h), ETH $2,093 (-0.3% 24h), SOL $85.11 (-1.1% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.0% (mcap $2.44B, vol $344.91M), pump-fun -1.6% (mcap $962.40M, vol $113.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $96.3k | $1.41M | 10.8 h | h24 +2373% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $55.5k | $155.1k | 21.6 h | h24 +1% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $80.3k | $709.3k | 1.9 d | h24 +628% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 69* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $142.0k | $2.89M | 1.2 d | h24 +305% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 4.9% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.26M | $10.07M | 12.5 d | h24 -26% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,433 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.85M | $28.1k | 390.7 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 387,875 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.49M | $13.61M | 167.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 345,358 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DERP404](https://pump.fun/coin/FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump) | `FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump` | $124.1k | $404.5k | +241% | +1070% | +1070% | 12.6x | spike (+241% 1h, +1070% 6h) | not scored |
| [Rockstar](https://pump.fun/coin/45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump) | `45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump` | $46.2k | $369.2k | +248% | +955% | +955% | 2.0x | thin liq $46.2k; spike (+248% 1h, +955% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $96.1k | $1.41M | -6% | +19% | +2365% | 20.8x | none flagged (still high risk) | 59 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $39.5k | $253.7k | +34% | -80% | +487% | 40.5x | thin liq $39.5k; churn 40x vol/liq | not scored |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $28.6k | $127.4k | -1% | +269% | +269% | 30.3x | thin liq $28.6k; churn 30x vol/liq | not scored |
| [DERP404](https://dexscreener.com/solana/5iDbWQtZsUVizH8GEV9ybzCexyNaWU2w5HstBzvbSun4) | `5iDbWQtZsUVizH8GEV9ybzCexyNaWU2w5HstBzvbSun4` | $12.6k | $15.6k | +116% | +116% | +116% | 1.0x | thin liq $12.6k; spike (+116% 1h, +116% 6h); < 1h old | not scored |

_Timing: total 154s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 81.2s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/131; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
