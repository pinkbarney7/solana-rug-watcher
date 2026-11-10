# Last scan 2026-11-10T10:54:07Z - mode: helius (box heartbeat stale (411 min); budget 110/3000)

```
[fast_scan] 120 candidate mints from 9 source tags; 117 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored AODF in 72s
[fast_scan] scored MILES in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BORLY in 81s
[fast_scan] scored PREDICT in 82s
[fast_scan] scored BIG in 82s
[fast_scan] scored UODF in 83s
[fast_scan] scored ZEC in 83s
[fast_scan] scored FLOAT in 73s
# Market scan 2026-11-10 10:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,110 (+0.0% 24h), ETH $2,086 (-1.0% 24h), SOL $84.47 (-1.7% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.2% (mcap $2.44B, vol $345.33M), pump-fun -1.9% (mcap $958.05M, vol $112.43M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $53.5k | $149.2k | 22.0 h | h24 -3% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 58* | SKIP | [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $86.3k | $1.14M | 11.3 h | h24 +1905% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.7k | $808.9k | 1.9 d | h24 +667% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 69* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $119.85M | 20.2 h | h24 +202933% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $858.5k | $73.43M | 21.0 h | h24 +124298% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $145.4k | $2.92M | 1.3 d | h24 +297% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.25M | $9.93M | 12.5 d | h24 -27% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,441 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.49M | 167.1 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 345,358 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.85M | $28.2k | 390.8 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 388,011 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $119.87M | +1% | +8% | +202977% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.38 | 69 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $858.5k | $73.43M | +2% | +11% | +124298% | 0.6x | liq/mcap 1.2%; lopsided buys/sells 50.89 | 78 |
| [KYTRO](https://dexscreener.com/solana/8AsTXdTAcBpzkwU7uK9NR5LQXrF5rjiqvRA8k73hc8Lz) | `8AsTXdTAcBpzkwU7uK9NR5LQXrF5rjiqvRA8k73hc8Lz` | $72.2k | $68.2k | +196% | +739% | +739% | 121.0x | churn 121x vol/liq; spike (+196% 1h, +739% 6h) | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $86.3k | $1.14M | -6% | -18% | +1905% | 23.5x | none flagged (still high risk) | 58 |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $38.7k | $243.6k | +14% | +29% | +589% | 36.6x | thin liq $38.7k; churn 37x vol/liq | not scored |
| [OnlyCats](https://pump.fun/coin/BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump) | `BAftaSb1HVqBn5723w72WLcXU7YASSgmVxQxJJAJpump` | $38.6k | $244.7k | +1% | -81% | +466% | 41.8x | thin liq $38.6k; churn 42x vol/liq | not scored |

_Timing: total 219s (discovery 71.8s, screen 1.1s, GT prime 0.4s, scoring 145.2s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/163; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
