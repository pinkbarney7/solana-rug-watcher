# Last scan 2026-11-10T06:24:45Z - mode: helius (box heartbeat stale (142 min); budget 10/3000)

```
[fast_scan] 126 candidate mints from 9 source tags; 123 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored MILES in 72s
[fast_scan] scored XTEN in 80s
[fast_scan] scored HODLER in 80s
[fast_scan] scored AICoin in 81s
[fast_scan] scored BORLY in 81s
[fast_scan] scored OnlyCats in 82s
[fast_scan] scored ACT in 82s
[fast_scan] scored FLOAT in 82s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-10 06:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,521 (+0.3% 24h), ETH $2,115 (-0.3% 24h), SOL $85.81 (-0.4% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.7% (mcap $2.46B, vol $358.28M), pump-fun -1.0% (mcap $965.35M, vol $117.49M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $53.7k | $142.5k | 17.5 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 53* | SKIP | [AICoin](https://dexscreener.com/solana/6w792EhabdMTGqZtp77wWV5vZvvs4U89CqB8CYZesPq) | `6w792EhabdMTGqZtp77wWV5vZvvs4U89CqB8CYZesPq` | $158.5k | $99.5k | 1.7 h | h24 +110% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 62* | SKIP | [XTEN](https://dexscreener.com/solana/DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP) | `DMvcPrWsThg3eyM96jEFTqFYrVSEV7jVzU5HEggRdTzP` | $145.3k | $2.50M | 1.1 d | h24 +365% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $627.6k | $2.09M | 20.8 h | h24 +25116% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $97.4k | $1.44M | 6.8 h | h24 +2429% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $91.1k | $1.32M | 6.3 h | h24 +2950% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.35M | $10.02M | 751.8 d | h24 +15% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 136,095 (growth n/a: first sighting) |
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $28.67M | 106.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 426,339 (growth n/a: first sighting) |
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.32M | $10.61M | 12.4 d | h24 -22% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,365 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $627.4k | $2.09M | -3% | +16% | +25116% | 0.1x | none flagged (still high risk) | 71 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $90.8k | $1.31M | -8% | +106% | +2929% | 13.3x | none flagged (still high risk) | 71 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $97.4k | $1.44M | -9% | +87% | +2429% | 18.5x | none flagged (still high risk) | 71 |
| [FOMO](https://pump.fun/coin/6WnKXhoo7kfTPSFNrfvP87dj3HjPShQdsETwq1S1pump) | `6WnKXhoo7kfTPSFNrfvP87dj3HjPShQdsETwq1S1pump` | $24.1k | $108.1k | +203% | +203% | +203% | 0.3x | thin liq $24.1k; spike (+203% 1h, +203% 6h); < 1h old | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $83.2k | $862.5k | -5% | +313% | +743% | 4.0x | spike (-5% 1h, +313% 6h) | not scored |
| [Pepetide](https://pump.fun/coin/bUMdQe5SYhBuyNzvF5sfxngPeUsiMR3fqPyYf85pump) | `bUMdQe5SYhBuyNzvF5sfxngPeUsiMR3fqPyYf85pump` | $25.6k | $118.4k | -52% | +236% | +236% | 3.5x | thin liq $25.6k | not scored |

_Timing: total 216s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 143.2s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/161; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
