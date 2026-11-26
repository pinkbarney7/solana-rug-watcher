# Last scan 2026-11-26T04:51:05Z - mode: helius (box heartbeat stale (48 min); budget 433/3000)

```
[fast_scan] 144 candidate mints from 9 source tags; 141 with pair data; 19 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored Grodia in 70s
[fast_scan] scored VINE in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored BASKET in 79s
[fast_scan] scored NORFEATH in 79s
[fast_scan] scored FLOAT in 81s
# Market scan 2026-11-26 04:51 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,966 (+3.3% 24h), ETH $1,703 (+2.9% 24h), SOL $71.15 (+3.8% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.7% (mcap $1.90B, vol $381.04M), pump-fun +4.5% (mcap $788.97M, vol $155.15M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $161.1k | $692.5k | 1.0 d | h24 +391% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $56.9k | $607.8k | 7.8 h | h24 +1225% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $75.6k | $1.06M | 6.4 h | h24 +2911% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $456.1k | $3.10M | 28.3 d | h24 +23% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +9.2% in 264h (now 49,787) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.07M | 672.2 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,103 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.73M | 182.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,615 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $83.1k | $1.36M | +11% | +4221% | +4221% | 7.0x | spike (+11% 1h, +4221% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $72.0k | $1.00M | -14% | +2713% | +2713% | 9.0x | spike (-14% 1h, +2713% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $55.2k | $454.5k | -1% | +1464% | +1464% | 70.6x | churn 71x vol/liq; spike (-1% 1h, +1464% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $75.6k | $1.06M | -4% | -8% | +2911% | 25.2x | churn 25x vol/liq | 58 |
| [call.fun](https://dexscreener.com/solana/ABdHxVMR3TgUvJdgNJpcV7HM4qjKDuZCMmmaqWdj2fBF) | `ABdHxVMR3TgUvJdgNJpcV7HM4qjKDuZCMmmaqWdj2fBF` | $16.3k | $16.7k | +291% | +291% | +291% | 2.4x | thin liq $16.3k; spike (+291% 1h, +291% 6h); lopsided buys/sells 3.92; < 1h old | not scored |
| [TEEETHY](https://pump.fun/coin/BbC8hVHJ2bo6xFcGh2X6zcMiv1T1rznQd3qWoxXApump) | `BbC8hVHJ2bo6xFcGh2X6zcMiv1T1rznQd3qWoxXApump` | $21.9k | $104.2k | +254% | +254% | +254% | 5.5x | thin liq $21.9k; spike (+254% 1h, +254% 6h); < 1h old | not scored |

_Timing: total 154s (discovery 71.7s, screen 1.3s, GT prime 0.4s, scoring 80.8s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 6/132; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
