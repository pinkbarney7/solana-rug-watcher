# Last scan 2026-11-10T12:48:46Z - mode: helius (box heartbeat stale (526 min); budget 174/3000)

```
[fast_scan] 133 candidate mints from 10 source tags; 128 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (64s)
[fast_scan] scored FOTF in 72s
[fast_scan] scored USPR in 80s
[fast_scan] scored AODF in 81s
[fast_scan] scored UODF in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored USOE in 82s
[fast_scan] scored BIRB in 83s
[fast_scan] scored BIG in 83s
[fast_scan] scored Dacity in 73s
# Market scan 2026-11-10 12:48 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,117 (-0.8% 24h), ETH $2,085 (-1.8% 24h), SOL $84.64 (-2.3% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.3% (mcap $2.44B, vol $342.53M), pump-fun -4.3% (mcap $954.57M, vol $110.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.0k | $793.5k | 2.0 d | h24 +652% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 69* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.80M | 22.1 h | h24 +207936% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 69* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.61M | 21.8 h | h24 +204223% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 69* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $742.0k | $54.89M | 21.4 h | h24 +92902% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.4% (+10.4) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $876.1k | $76.44M | 22.9 h | h24 +129406% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $797.2k | $63.30M | 21.1 h | h24 +107142% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [Dacity](https://pump.fun/coin/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | `nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump` | $828.9k | $9.52M | 30.1 d | h24 +10% | #3 Liquidity vs market cap WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.6% in 6h (now 68,907) |
| 69* | SKIP | [BIRB](https://dexscreener.com/solana/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` | $1.63M | $23.35M | 290.6 d | h24 -13% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 75,396 (growth n/a: first sighting) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.39M | $13.40M | 167.2 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 346,772 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.80M | +1% | +8% | +207936% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.83 | 69 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $120.61M | +1% | +8% | +204223% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.53 | 69 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $876.1k | $76.44M | +3% | +12% | +129406% | 0.6x | liq/mcap 1.1%; lopsided buys/sells 51.59 | 78 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $797.2k | $63.30M | +2% | +12% | +107142% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.57 | 78 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $742.0k | $54.89M | +2% | +14% | +92902% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 58.03 | 69 |
| [USDP](https://pump.fun/coin/viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump) | `viJdzhnv1eMDGV42NBc7CchjYSbnKuuQvpiKuuYpump` | $716.4k | $51.18M | +2% | +13% | +86618% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.83 | not scored |

_Timing: total 210s (discovery 63.0s, screen 1.3s, GT prime 0.5s, scoring 145.0s for 9 coins, 9 newly scored). ~30 Helius credits (smart-money discovery 30). HTTP cache hits 9/164; Helius 429s 97; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
