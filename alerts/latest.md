# Last scan 2026-11-10T12:22:13Z - mode: helius (box heartbeat stale (499 min); budget 120/3000)

```
[fast_scan] 130 candidate mints from 9 source tags; 123 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (74s)
[fast_scan] scored UODF in 78s
[fast_scan] scored USOE in 87s
[fast_scan] scored SPCX in 87s
[fast_scan] scored AODF in 88s
[fast_scan] scored ZEC in 88s
[fast_scan] scored USPR in 88s
[fast_scan] scored BIG in 89s
[fast_scan] scored FOTF in 89s
[fast_scan] scored MCDx in 72s
# Market scan 2026-11-10 12:22 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,305 (-0.2% 24h), ETH $2,091 (-1.2% 24h), SOL $84.73 (-2.0% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.7% (mcap $2.44B, vol $342.40M), pump-fun -2.8% (mcap $955.10M, vol $108.01M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 68* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $85.4k | $805.2k | 2.0 d | h24 +664% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |
| 69* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $869.0k | $75.22M | 22.4 h | h24 +127340% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.2% (+10.6) |
| 69* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $793.6k | $62.74M | 20.7 h | h24 +106197% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.3% (+10.5) |
| 78* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.00M | 21.7 h | h24 +206578% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $119.96M | 21.3 h | h24 +203126% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $738.4k | $54.36M | 21.0 h | h24 +91996% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [MCDx](https://dexscreener.com/solana/XsqE9cRRpzxcGKDXj1BJ7Xmg4GRhZoyY1KpmGSxAWT2) | `XsqE9cRRpzxcGKDXj1BJ7Xmg4GRhZoyY1KpmGSxAWT2` | $506.5k | $2.42M | 497.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.3% in 6h (now 81,199) |
| 79* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.41M | $13.49M | 167.2 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 346,718 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.90M | $28.5k | 390.8 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 388,005 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.11M | $122.00M | +1% | +8% | +206578% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.67 | 78 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $119.96M | +1% | +8% | +203126% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.43 | 78 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $869.0k | $75.22M | +2% | +11% | +127340% | 0.6x | liq/mcap 1.2%; lopsided buys/sells 51.45 | 69 |
| [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $793.6k | $62.74M | +2% | +12% | +106197% | 0.7x | liq/mcap 1.3%; lopsided buys/sells 57.42 | 69 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $738.4k | $54.36M | +2% | +14% | +91996% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.93 | 78 |
| [CHAINCHOMP131](https://pump.fun/coin/DigVnUDwgbSSWNMNsgzGNw8EQhqwjniPU2EsfD4Wpump) | `DigVnUDwgbSSWNMNsgzGNw8EQhqwjniPU2EsfD4Wpump` | $22.1k | $90.4k | +152% | +152% | +152% | 6.6x | thin liq $22.1k; spike (+152% 1h, +152% 6h); < 1h old | not scored |

_Timing: total 224s (discovery 72.0s, screen 1.8s, GT prime 0.4s, scoring 150.2s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/161; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
