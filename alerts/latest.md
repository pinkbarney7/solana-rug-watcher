# Last scan 2026-11-10T08:37:04Z - mode: helius (box heartbeat stale (274 min); budget 60/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 128 with pair data; 27 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BIG in 72s
[fast_scan] scored HODLER in 80s
[fast_scan] scored 现金牛 in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored OnlyCats in 82s
[fast_scan] scored MILES in 83s
[fast_scan] scored BORLY in 83s
[fast_scan] scored wXRP in 72s
# Market scan 2026-11-10 08:37 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,584 (+0.6% 24h), ETH $2,111 (+0.1% 24h), SOL $85.63 (-0.8% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.0% (mcap $2.47B, vol $335.83M), pump-fun -0.6% (mcap $969.66M, vol $113.21M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $52.9k | $143.3k | 19.8 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.0k | $790.3k | 1.8 d | h24 +697% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 59* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $589.4k | $1.96M | 23.0 h | h24 +23499% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [现金牛](https://dexscreener.com/solana/MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f) | `MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f` | $353.0k | $206.4k | 2.1 h | h24 +51% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 71* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $94.7k | $1.36M | 9.0 h | h24 +2287% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $92.8k | $1.36M | 8.5 h | h24 +3044% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 65* | SKIP | [wXRP](https://dexscreener.com/solana/6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2) | `6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2` | $488.2k | $1 | 256.1 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,125 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.37M | $10.24M | 751.9 d | h24 +19% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders 136,111 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.41M | $13.57M | 167.0 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,322 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $589.2k | $1.96M | -2% | -13% | +23499% | 0.1x | none flagged (still high risk) | 59 |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $92.8k | $1.36M | -2% | +0% | +3044% | 15.1x | none flagged (still high risk) | 71 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $94.6k | $1.36M | +13% | -33% | +2283% | 20.1x | none flagged (still high risk) | 71 |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $31.9k | $162.4k | +93% | +538% | +175% | 14.8x | thin liq $31.9k; spike (+93% 1h, +538% 6h) | not scored |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $37.2k | $217.7k | -5% | +222% | +516% | 37.2x | thin liq $37.2k; churn 37x vol/liq | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $79.6k | $790.3k | +10% | +69% | +697% | 4.5x | none flagged (still high risk) | 55 |

_Timing: total 217s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 144.0s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/161; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
