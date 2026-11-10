# Last scan 2026-11-10T13:02:00Z - mode: helius (box heartbeat stale (539 min); budget 204/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 123 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored AODF in 72s
[fast_scan] scored FOTF in 80s
[fast_scan] scored BIRB in 81s
[fast_scan] scored BIG in 81s
[fast_scan] scored USPR in 82s
[fast_scan] scored USOE in 83s
[fast_scan] scored SPCX in 83s
[fast_scan] scored UODF in 83s
[fast_scan] scored FLOAT in 73s
# Market scan 2026-11-10 13:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,297 (-0.7% 24h), ETH $2,095 (-1.3% 24h), SOL $84.86 (-2.1% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.2% (mcap $2.44B, vol $350.45M), pump-fun -4.2% (mcap $955.66M, vol $111.86M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $81.1k | $721.8k | 2.0 d | h24 +585% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 69* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $123.17M | 22.4 h | h24 +208570% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 69* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $742.5k | $54.97M | 21.6 h | h24 +93030% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.4% (+10.4) |
| 78* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $121.14M | 22.0 h | h24 +205127% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $877.9k | $76.75M | 23.1 h | h24 +129936% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $800.6k | $63.84M | 21.4 h | h24 +108063% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.20M | $9.14M | 12.6 d | h24 -31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.2% in 1h (now 42,531) |
| 69* | SKIP | [BIRB](https://dexscreener.com/solana/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` | $1.63M | $22.98M | 290.6 d | h24 -14% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 75,396 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.37M | $13.34M | 167.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 346,772 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $123.17M | +1% | +8% | +208570% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.86 | 69 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $121.12M | +1% | +8% | +205098% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.60 | 78 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $877.8k | $76.75M | +3% | +12% | +129929% | 0.6x | liq/mcap 1.1%; lopsided buys/sells 51.70 | 78 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $800.6k | $63.84M | +2% | +12% | +108063% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.56 | 78 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $742.6k | $54.98M | +2% | +14% | +93043% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 58.00 | 69 |
| [USDP](https://pump.fun/coin/viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump) | `viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump` | $717.7k | $51.37M | +2% | +12% | +86925% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.86 | not scored |

_Timing: total 219s (discovery 71.9s, screen 1.3s, GT prime 0.4s, scoring 145.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/164; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
