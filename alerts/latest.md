# Last scan 2026-11-26T06:21:57Z - mode: helius (box heartbeat stale (139 min); budget 30/3000)

```
[fast_scan] 130 candidate mints from 10 source tags; 126 with pair data; 19 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored UHI in 72s
[fast_scan] scored miuu in 81s
[fast_scan] scored Grodia in 81s
[fast_scan] scored VINE in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored DOG in 83s
[fast_scan] scored MOODENG in 83s
[fast_scan] scored BASKET in 83s
# Market scan 2026-11-26 06:21 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,360 (+2.0% 24h), ETH $1,682 (+1.4% 24h), SOL $70.60 (+2.8% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.8% (mcap $1.89B, vol $390.05M), pump-fun +4.2% (mcap $785.43M, vol $152.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $173.7k | $819.0k | 1.1 d | h24 +66% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6) | `FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6` | $224.9k | $128.4k | 2.1 h | h24 +62% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [miuu](https://dexscreener.com/solana/JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew) | `JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew` | $166.3k | $135.4k | 1.5 h | h24 +242% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 58* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $72.6k | $1.02M | 7.1 h | h24 +2766% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.9k | $861.1k | 7.9 h | h24 +2340% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.18M | 672.3 d | h24 +0% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,108 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.89M | $28.74M | 806.5 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,888 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.25M | $13.63M | 182.9 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,935 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $83.5k | $1.38M | +11% | +4282% | +4282% | 7.9x | spike (+11% 1h, +4282% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $72.6k | $1.02M | -13% | +234% | +2766% | 10.3x | none flagged (still high risk) | 58 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.9k | $861.1k | -17% | -22% | +2340% | 29.6x | churn 30x vol/liq | 58 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $29.2k | $163.1k | +140% | +471% | +471% | 21.7x | thin liq $29.2k; spike (+140% 1h, +471% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $43.8k | $290.4k | -21% | +233% | +900% | 90.8x | thin liq $43.8k; churn 91x vol/liq | not scored |
| [miuu](https://dexscreener.com/solana/JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew) | `JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew` | $166.3k | $135.4k | +83% | +242% | +242% | 41.0x | churn 41x vol/liq | 56 |

_Timing: total 156s (discovery 71.2s, screen 1.4s, GT prime 0.4s, scoring 83.4s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/159; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
