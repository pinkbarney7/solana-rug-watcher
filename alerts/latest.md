# Last scan 2026-11-26T06:24:47Z - mode: helius (box heartbeat stale (142 min); budget 30/3000)

```
[fast_scan] 130 candidate mints from 10 source tags; 126 with pair data; 20 >= $50,000 liq; 8 pass survivor pre-gates (72s)
[fast_scan] scored Grodia in 76s
[fast_scan] scored UHI in 76s
[fast_scan] scored VINE in 76s
[fast_scan] scored MOODENG in 77s
[fast_scan] scored miuu in 77s
[fast_scan] scored DOG in 77s
[fast_scan] scored SPCX in 78s
[fast_scan] scored BASKET in 79s
# Market scan 2026-11-26 06:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,382 (+2.1% 24h), ETH $1,683 (+1.6% 24h), SOL $70.63 (+3.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.8% (mcap $1.89B, vol $390.05M), pump-fun +4.2% (mcap $785.43M, vol $152.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $173.7k | $819.0k | 1.1 d | h24 +66% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6) | `FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6` | $224.9k | $128.4k | 2.2 h | h24 +62% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [miuu](https://dexscreener.com/solana/JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew) | `JAeqCAY8zGY6xz6YaWiH2QU8w4CiZoA8GGqLpVo5uMew` | $166.3k | $135.4k | 1.5 h | h24 +242% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 58* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $72.6k | $1.02M | 7.1 h | h24 +2766% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.9k | $861.1k | 8.0 h | h24 +2340% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

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
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $82.5k | $1.35M | -7% | +4180% | +4180% | 8.0x | spike (-7% 1h, +4180% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $73.6k | $1.05M | +3% | +179% | +2841% | 10.2x | none flagged (still high risk) | 58 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $69.2k | $893.3k | -14% | -12% | +2431% | 29.0x | churn 29x vol/liq | 58 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $30.9k | $179.4k | +50% | +528% | +528% | 21.2x | thin liq $30.9k; spike (+50% 1h, +528% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $43.4k | $285.0k | -17% | +107% | +881% | 91.7x | thin liq $43.4k; churn 92x vol/liq | not scored |
| [Elonmas](https://pump.fun/coin/DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump) | `DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump` | $20.4k | $82.2k | +172% | +172% | +172% | 18.2x | thin liq $20.4k; spike (+172% 1h, +172% 6h); < 1h old | not scored |

_Timing: total 151s (discovery 70.6s, screen 1.5s, GT prime 0.2s, scoring 78.7s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 60/157; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
