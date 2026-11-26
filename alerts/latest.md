# Last scan 2026-11-26T07:06:45Z - mode: helius (box heartbeat stale (184 min); budget 40/3000)

```
[fast_scan] 139 candidate mints from 9 source tags; 135 with pair data; 23 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored Grodia in 71s
[fast_scan] scored VINE in 79s
[fast_scan] scored MOODENG in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored UHI in 81s
[fast_scan] scored BASKET in 83s
# Market scan 2026-11-26 07:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,504 (+2.3% 24h), ETH $1,687 (+1.8% 24h), SOL $70.68 (+2.9% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +4.6% (mcap $1.88B, vol $362.62M), pump-fun +3.5% (mcap $783.23M, vol $130.48M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $194.3k | $1.03M | 1.1 d | h24 +61% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $134.8k | $668.8k | 2.4 d | h24 -40% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.7k | $1.17M | 7.8 h | h24 +3169% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.8k | $854.6k | 8.7 h | h24 +2322% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.32M | 672.3 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,115 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.89M | $28.79M | 806.6 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,893 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.61M | 183.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 394,361 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $91.5k | $1.65M | +21% | +5127% | +5127% | 7.6x | spike (+21% 1h, +5127% 6h) | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $19.3k | $76.4k | +176% | +969% | +1196% | 13.9x | thin liq $19.3k; spike (+176% 1h, +969% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.7k | $1.17M | +25% | +81% | +3169% | 9.8x | none flagged (still high risk) | 56 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.8k | $854.6k | -3% | -49% | +2322% | 30.3x | churn 30x vol/liq | 58 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $29.4k | $160.7k | +40% | +462% | +462% | 30.5x | thin liq $29.4k; churn 31x vol/liq; spike (+40% 1h, +462% 6h) | not scored |
| [486](https://pump.fun/coin/9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump) | `9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump` | $12.1k | $28.3k | +57% | +469% | +449% | 1.0x | thin liq $12.1k; spike (+57% 1h, +469% 6h) | not scored |

_Timing: total 157s (discovery 71.9s, screen 1.4s, GT prime 0.5s, scoring 82.7s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/148; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
