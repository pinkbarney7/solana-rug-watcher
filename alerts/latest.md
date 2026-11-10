# Last scan 2026-11-10T12:37:18Z - mode: helius (box heartbeat stale (514 min); budget 120/3000)

```
[fast_scan] 136 candidate mints from 10 source tags; 131 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored ZEC in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored USPR in 82s
[fast_scan] scored USOE in 82s
[fast_scan] scored UODF in 83s
[fast_scan] scored FOTF in 90s
[fast_scan] scored BIRB in 69s
[fast_scan] scored AODF in 166s
[fast_scan] scored BIG in 182s
# Market scan 2026-11-10 12:37 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,158 (-0.9% 24h), ETH $2,088 (-1.7% 24h), SOL $84.61 (-2.4% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.5% (mcap $2.44B, vol $351.45M), pump-fun -2.8% (mcap $955.58M, vol $112.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $82.7k | $751.1k | 2.0 d | h24 +612% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 69* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.43M | 22.0 h | h24 +207312% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $875.5k | $76.34M | 22.7 h | h24 +129242% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $795.4k | $63.02M | 20.9 h | h24 +106668% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $740.3k | $54.64M | 21.2 h | h24 +92474% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 79* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.33M | 21.6 h | h24 +203757% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 57* | SKIP | [BIRB](https://dexscreener.com/solana/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` | $1.63M | $23.37M | 290.5 d | h24 -13% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 75,395 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.92M | $28.5k | 390.8 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 388,038 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.40M | $13.44M | 167.2 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 346,718 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.43M | +1% | +8% | +207312% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.79 | 69 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.33M | +1% | +8% | +203757% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.49 | 79 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $875.5k | $76.34M | +3% | +12% | +129242% | 0.6x | liq/mcap 1.1%; lopsided buys/sells 51.58 | 78 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $795.4k | $63.02M | +2% | +12% | +106668% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.53 | 78 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $740.3k | $54.64M | +2% | +14% | +92474% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.99 | 78 |
| [USDP](https://pump.fun/coin/viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump) | `viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump` | $715.0k | $50.98M | +2% | +13% | +86274% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.80 | not scored |

_Timing: total 255s (discovery 71.1s, screen 1.3s, GT prime 0.3s, scoring 181.9s for 9 coins, 9 newly scored). ~54 Helius credits (smart-money discovery 20). HTTP cache hits 9/175; Helius 429s 113; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
