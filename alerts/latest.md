# Last scan 2026-11-10T10:05:29Z - mode: helius (box heartbeat stale (364 min); budget 90/3000)

```
[fast_scan] 126 candidate mints from 9 source tags; 121 with pair data; 25 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 72s
[fast_scan] scored SPCX in 80s
[fast_scan] scored FLOAT in 80s
[fast_scan] scored BORLY in 81s
[fast_scan] scored MILES in 81s
[fast_scan] scored BIG in 82s
[fast_scan] scored CLAUDIA in 82s
[fast_scan] scored PREDICT in 82s
# Market scan 2026-11-10 10:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,459 (+0.3% 24h), ETH $2,103 (-0.2% 24h), SOL $85.52 (-0.9% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $2.46B, vol $347.47M), pump-fun -1.2% (mcap $966.54M, vol $108.83M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $608.2k | $2.01M | 1.0 d | h24 +11729% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $57.2k | $163.4k | 21.2 h | h24 +7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $81.3k | $729.6k | 1.9 d | h24 +649% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 73* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.8k | $1.34M | 10.5 h | h24 +2240% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 78* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $139.7k | $2.89M | 1.2 d | h24 +328% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 40* | CAUTION | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $684.5k | $6.62M | 34.4 d | h24 +14% | #7 Insiders / bundles / LP lock WARN (+5); #6 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link |
| 58* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.26M | $10.07M | 12.5 d | h24 -26% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #6 unknown (+3); GATES FAILED: rug-funder link, exit test |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.45M | $13.63M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 344,454 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $608.0k | $2.01M | +5% | -15% | +11729% | 0.1x | none flagged (still high risk) | 56 |
| [DERP404](https://pump.fun/coin/FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump) | `FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump` | $113.1k | $352.5k | +920% | +920% | +920% | 9.1x | spike (+920% 1h, +920% 6h); < 1h old | not scored |
| [Rockstar](https://pump.fun/coin/45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump) | `45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump` | $44.4k | $340.4k | +217% | +872% | +872% | 1.6x | thin liq $44.4k; spike (+217% 1h, +872% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $93.5k | $1.33M | -11% | -17% | +2223% | 21.3x | none flagged (still high risk) | 73 |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $34.7k | $189.9k | +49% | +450% | +450% | 21.8x | thin liq $34.7k; spike (+49% 1h, +450% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $39.4k | $252.5k | +9% | -81% | +484% | 40.2x | thin liq $39.4k; churn 40x vol/liq | not scored |

_Timing: total 156s (discovery 71.7s, screen 1.3s, GT prime 0.5s, scoring 82.1s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/142; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
