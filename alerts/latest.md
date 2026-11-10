# Last scan 2026-11-10T08:44:56Z - mode: helius (box heartbeat stale (282 min); budget 70/3000)

```
[fast_scan] 129 candidate mints from 9 source tags; 124 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (74s)
[fast_scan] scored 现金牛 in 78s
[fast_scan] scored BORLY in 86s
[fast_scan] scored MILES in 87s
[fast_scan] scored PREDICT in 87s
[fast_scan] scored SPCX in 88s
[fast_scan] scored BIG in 88s
[fast_scan] scored HODLER in 89s
[fast_scan] scored ZEC in 89s
[fast_scan] scored wXRP in 64s
# Market scan 2026-11-10 08:44 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,502 (+0.4% 24h), ETH $2,111 (+0.1% 24h), SOL $85.60 (-0.9% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.0% (mcap $2.47B, vol $335.83M), pump-fun -0.6% (mcap $969.66M, vol $113.21M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $52.9k | $143.3k | 19.9 h | h24 -7% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 53* | SKIP | [现金牛](https://dexscreener.com/solana/MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f) | `MsAn4UwaZFc8Nb8EEqG5MtBRTmV4acZ5QogzQ8AWa4f` | $355.5k | $207.8k | 2.2 h | h24 +52% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $94.1k | $1.35M | 9.1 h | h24 +2256% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.7k | $803.2k | 1.8 d | h24 +710% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 71* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $571.0k | $1.89M | 23.1 h | h24 +22690% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 74* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $168.8k | $2.72M | 1.2 d | h24 +347% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 65* | SKIP | [wXRP](https://dexscreener.com/solana/6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2) | `6UpQcMAb5xMzxc7ZfPaVMgx3KqsvKZdT5U718BzD5We2` | $487.8k | $1 | 256.1 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,099 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.56M | 167.0 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 344,433 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.88M | $28.2k | 390.7 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.0% in 17h (now 387,895) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $570.8k | $1.89M | -6% | -15% | +22690% | 0.2x | none flagged (still high risk) | 71 |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $94.5k | $1.36M | +3% | -28% | +2277% | 20.2x | none flagged (still high risk) | 59 |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $31.2k | $154.6k | +59% | +582% | +218% | 14.7x | thin liq $31.2k; spike (+59% 1h, +582% 6h) | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $44.2k | $317.8k | -76% | -79% | +635% | 32.7x | thin liq $44.2k; churn 33x vol/liq | not scored |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $36.0k | $204.1k | -10% | +139% | +478% | 38.4x | thin liq $36.0k; churn 38x vol/liq | not scored |
| [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $80.3k | $803.2k | +18% | +63% | +710% | 4.5x | none flagged (still high risk) | 68 |

_Timing: total 216s (discovery 72.0s, screen 1.6s, GT prime 0.3s, scoring 142.1s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/159; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
