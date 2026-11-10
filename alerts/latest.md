# Last scan 2026-11-10T12:29:23Z - mode: helius (box heartbeat stale (507 min); budget 120/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 122 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored UODF in 72s
[fast_scan] scored ZEC in 80s
[fast_scan] scored USPR in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored AODF in 82s
[fast_scan] scored USOE in 82s
[fast_scan] scored BIG in 82s
[fast_scan] scored FOTF in 83s
[fast_scan] scored BIRB in 71s
# Market scan 2026-11-10 12:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,308 (-0.4% 24h), ETH $2,092 (-1.3% 24h), SOL $84.75 (-2.0% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.7% (mcap $2.44B, vol $342.40M), pump-fun -2.8% (mcap $955.10M, vol $108.01M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.0k | $794.8k | 2.0 d | h24 +654% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 69* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $874.3k | $76.13M | 22.5 h | h24 +128886% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.1% (+10.6) |
| 78* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.18M | 21.8 h | h24 +206889% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.14M | 21.4 h | h24 +203432% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $794.5k | $62.88M | 20.8 h | h24 +106441% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $739.3k | $54.50M | 21.1 h | h24 +92241% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 57* | SKIP | [BIRB](https://dexscreener.com/solana/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` | $1.63M | $23.43M | 290.5 d | h24 -14% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.1% in 25h (now 75,395) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.40M | $13.55M | 167.2 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 346,718 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.92M | $28.4k | 390.8 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 388,038 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.18M | +1% | +8% | +206889% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.66 | 78 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.14M | +1% | +8% | +203432% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.46 | 78 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $874.5k | $76.17M | +3% | +12% | +128951% | 0.6x | liq/mcap 1.1%; lopsided buys/sells 51.52 | 69 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $794.5k | $62.88M | +2% | +12% | +106441% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.50 | 78 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $739.3k | $54.50M | +2% | +14% | +92241% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.96 | 78 |
| [FAIR](https://dexscreener.com/solana/FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg) | `FairDR2UmRqHxsVPdPcetePCjFaDqVYv3oQX9fcQTpTg` | $41.6k | $282.0k | -17% | +70% | +698% | 35.3x | thin liq $41.6k; churn 35x vol/liq | not scored |

_Timing: total 217s (discovery 71.7s, screen 1.4s, GT prime 0.7s, scoring 143.4s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/159; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
