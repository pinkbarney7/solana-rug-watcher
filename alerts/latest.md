# Last scan 2026-11-10T09:55:09Z - mode: helius (box heartbeat stale (354 min); budget 90/3000)

```
[fast_scan] 125 candidate mints from 9 source tags; 120 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored MILES in 72s
[fast_scan] scored ZEC in 80s
[fast_scan] scored BIG in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored FLOAT in 81s
[fast_scan] scored PREDICT in 82s
[fast_scan] scored BORLY in 82s
[fast_scan] scored HODLER in 82s
# Market scan 2026-11-10 09:55 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,395 (+0.3% 24h), ETH $2,101 (-0.2% 24h), SOL $85.46 (-1.2% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.4% (mcap $2.45B, vol $346.20M), pump-fun -1.4% (mcap $964.49M, vol $111.21M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $582.5k | $1.92M | 1.0 d | h24 +13828% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 60* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $52.1k | $142.2k | 21.1 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $77.7k | $663.2k | 1.9 d | h24 +581% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 70* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $89.9k | $1.23M | 10.3 h | h24 +2053% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 78* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $137.9k | $2.88M | 1.2 d | h24 +341% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.28M | $10.03M | 12.5 d | h24 -27% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 42,431 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.56M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 344,454 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.86M | $28.1k | 390.7 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 387,875 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $582.3k | $1.92M | +1% | -21% | +13828% | 0.2x | none flagged (still high risk) | 56 |
| [Rockstar](https://pump.fun/coin/45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump) | `45F77uiNszHeN1tYrecbAbsCL7yyg3GLKWo6TkZepump` | $40.3k | $283.1k | +709% | +709% | +709% | 1.5x | thin liq $40.3k; spike (+709% 1h, +709% 6h); < 1h old | not scored |
| [DERP404](https://pump.fun/coin/FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump) | `FgoLzGV2nVrghVHCWwAh6388iZkcLZSedykJ5trRpump` | $95.1k | $253.5k | +633% | +633% | +633% | 8.7x | spike (+633% 1h, +633% 6h); < 1h old | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $90.6k | $1.25M | -13% | -12% | +2087% | 21.9x | none flagged (still high risk) | 70 |
| [X](https://pump.fun/coin/9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump) | `9VZerdNL1x6EjetDqRnh5bYcdmk1y8sLAGs1ybzGpump` | $32.5k | $167.2k | +159% | +384% | +384% | 22.4x | thin liq $32.5k; spike (+159% 1h, +384% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $38.9k | $246.0k | -19% | -81% | +469% | 40.6x | thin liq $38.9k; churn 41x vol/liq | not scored |

_Timing: total 156s (discovery 71.6s, screen 1.3s, GT prime 0.2s, scoring 82.5s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/144; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
