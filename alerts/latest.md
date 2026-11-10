# Last scan 2026-11-10T08:57:56Z - mode: helius (box heartbeat stale (296 min); budget 70/3000)

```
[fast_scan] 126 candidate mints from 9 source tags; 121 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 72s
[fast_scan] scored BIG in 80s
[fast_scan] scored PREDICT in 81s
[fast_scan] scored BORLY in 81s
[fast_scan] scored 现金牛 in 82s
[fast_scan] scored wXRP in 82s
[fast_scan] scored FLOAT in 82s
[fast_scan] scored SPCX in 83s
# Market scan 2026-11-10 08:57 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,561 (+0.2% 24h), ETH $2,114 (-0.3% 24h), SOL $85.69 (-1.2% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $2.47B, vol $349.86M), pump-fun -0.6% (mcap $969.19M, vol $113.81M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $84.9k | $787.0k | 1.8 d | h24 +705% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $579.4k | $1.91M | 23.3 h | h24 +22922% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $98.4k | $1.47M | 9.4 h | h24 +2473% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [现金牛](https://dexscreener.com/solana/MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f) | `MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f` | $357.9k | $207.7k | 2.5 h | h24 +52% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 74* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $171.0k | $2.74M | 1.2 d | h24 +334% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.28M | $10.09M | 12.5 d | h24 -27% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders +0.0% in 1h (now 42,420) |
| 75* | SKIP | [wXRP](https://dexscreener.com/solana/6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2) | `6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2` | $487.7k | $1 | 256.1 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: authorities, rug-funder link, exit test; holders 46,079 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.53M | 167.0 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,433 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $579.3k | $1.91M | -5% | -15% | +22922% | 0.2x | none flagged (still high risk) | 59 |
| [KYTRO](https://dexscreener.com/solana/CBpvPzvQV5Ln6QBFendvrpED1dLimTjVh3yYgmbucfYU) | `CBpvPzvQV5Ln6QBFendvrpED1dLimTjVh3yYgmbucfYU` | $76.9k | $75.5k | +164% | +821% | +821% | 121.2x | churn 121x vol/liq; spike (+164% 1h, +821% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $99.1k | $1.49M | +10% | -20% | +2508% | 19.4x | none flagged (still high risk) | 59 |
| [AMPED](https://pump.fun/coin/yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump) | `yjF8ynR8zcF4umGmFpX2kjG63xBBrXe7rUQjAYBpump` | $24.4k | $108.8k | +208% | +208% | +208% | 2.7x | thin liq $24.4k; spike (+208% 1h, +208% 6h); lopsided buys/sells 3.07; < 1h old | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $39.4k | $254.3k | -80% | -84% | +488% | 37.2x | thin liq $39.4k; churn 37x vol/liq | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $77.7k | $752.7k | +7% | +95% | +670% | 4.6x | none flagged (still high risk) | 55 |

_Timing: total 156s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 82.5s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/143; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
