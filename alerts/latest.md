# Last scan 2026-11-10T13:11:14Z - mode: helius (box heartbeat stale (549 min); budget 204/3000)

```
[fast_scan] 129 candidate mints from 9 source tags; 125 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BIG in 72s
[fast_scan] scored SPCX in 80s
[fast_scan] scored UODF in 80s
[fast_scan] scored USOE in 81s
[fast_scan] scored AODF in 81s
[fast_scan] scored BIRB in 82s
[fast_scan] scored USPR in 82s
[fast_scan] scored FOTF in 82s
[fast_scan] scored FLOAT in 73s
# Market scan 2026-11-10 13:11 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,256 (-0.8% 24h), ETH $2,095 (-1.3% 24h), SOL $84.79 (-2.1% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.2% (mcap $2.44B, vol $350.45M), pump-fun -4.2% (mcap $955.66M, vol $111.86M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $81.7k | $734.3k | 2.0 d | h24 +597% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 69* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $801.5k | $63.98M | 21.5 h | h24 +108301% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.3% (+10.5) |
| 78* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $123.41M | 22.5 h | h24 +208974% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $121.39M | 22.1 h | h24 +205547% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $878.9k | $76.93M | 23.2 h | h24 +130238% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $745.8k | $55.46M | 21.8 h | h24 +93859% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.19M | $9.13M | 12.6 d | h24 -30% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 42,538 (growth n/a: first sighting) |
| 69* | SKIP | [BIRB](https://dexscreener.com/solana/G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG) | `G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG` | $1.63M | $23.10M | 290.6 d | h24 -13% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 75,398 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.36M | $13.28M | 167.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 346,772 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $123.42M | +1% | +8% | +208982% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.82 | 78 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $121.39M | +1% | +8% | +205547% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.65 | 78 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $878.9k | $76.93M | +3% | +12% | +130238% | 0.6x | liq/mcap 1.1%; lopsided buys/sells 51.74 | 78 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $801.5k | $63.98M | +2% | +12% | +108301% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.56 | 69 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $745.8k | $55.45M | +2% | +14% | +93844% | 0.6x | liq/mcap 1.3%; lopsided buys/sells 58.00 | 78 |
| [UDTF](https://pump.fun/coin/zd2CEvmoaForYWNK9D6kEgrzthiX7cy7FP9n6vnpump) | `zd2CEvmoaForYWNK9D6kEgrzthiX7cy7FP9n6vnpump` | $729.6k | $53.08M | +2% | +14% | +89827% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.82 | not scored |

_Timing: total 218s (discovery 71.7s, screen 1.3s, GT prime 0.2s, scoring 144.8s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/164; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
