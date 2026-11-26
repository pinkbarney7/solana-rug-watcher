# Last scan 2026-11-26T05:01:55Z - mode: helius (box heartbeat stale (59 min); budget 433/3000)

```
[fast_scan] 145 candidate mints from 9 source tags; 142 with pair data; 19 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 71s
[fast_scan] scored NORFEATH in 78s
[fast_scan] scored SPCX in 78s
[fast_scan] scored VINE in 79s
[fast_scan] scored Grodia in 79s
[fast_scan] scored FLOAT in 81s
# Market scan 2026-11-26 05:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,836 (+2.8% 24h), ETH $1,699 (+2.5% 24h), SOL $71.00 (+3.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.4% (mcap $1.90B, vol $372.11M), pump-fun +4.3% (mcap $787.31M, vol $134.28M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $155.3k | $647.9k | 1.0 d | h24 +85% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 57* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $59.5k | $663.3k | 7.9 h | h24 +1346% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $79.9k | $1.18M | 6.6 h | h24 +3254% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $453.7k | $3.07M | 28.3 d | h24 +22% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 49,789 (growth n/a: first sighting) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.11M | 672.2 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,103 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.73M | 182.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,868 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $87.7k | $1.52M | +23% | +4709% | +4709% | 7.0x | spike (+23% 1h, +4709% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $75.1k | $1.09M | -3% | +2961% | +2961% | 8.8x | spike (-3% 1h, +2961% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $54.2k | $440.6k | +11% | +1417% | +1417% | 72.0x | churn 72x vol/liq; spike (+11% 1h, +1417% 6h) | not scored |
| [call.fun](https://dexscreener.com/solana/ABdHxVMR3TgUvJdgNJpcV7HM4qjKDuZCMmmaqWdj2fBF) | `ABdHxVMR3TgUvJdgNJpcV7HM4qjKDuZCMmmaqWdj2fBF` | $21.4k | $28.8k | +573% | +573% | +573% | 2.3x | thin liq $21.4k; spike (+573% 1h, +573% 6h); lopsided buys/sells 4.27; < 1h old | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $79.9k | $1.18M | +10% | -1% | +3254% | 24.0x | none flagged (still high risk) | 59 |
| [TEEETHY](https://pump.fun/coin/BbC8hVHJ2bo6xFcGh2X6zcMiv1T1rznQd3qWoxXApump) | `BbC8hVHJ2bo6xFcGh2X6zcMiv1T1rznQd3qWoxXApump` | $21.6k | $101.0k | +208% | +243% | +243% | 6.6x | thin liq $21.6k; spike (+208% 1h, +243% 6h) | not scored |

_Timing: total 154s (discovery 71.7s, screen 1.5s, GT prime 0.5s, scoring 80.7s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 6/132; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
