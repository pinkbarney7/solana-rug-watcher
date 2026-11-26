# Last scan 2026-11-26T13:11:58Z - mode: helius (box heartbeat stale (549 min); budget 437/3000)

```
[fast_scan] 121 candidate mints from 9 source tags; 118 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored UHI in 71s
[fast_scan] scored pippin in 79s
[fast_scan] scored HYPER in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored NORFEATH in 81s
[fast_scan] scored BASKET in 81s
[fast_scan] scored SPCX in 81s
# Market scan 2026-11-26 13:11 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,778 (+3.7% 24h), ETH $1,706 (+3.7% 24h), SOL $70.93 (+4.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +8.3% (mcap $1.89B, vol $338.79M), pump-fun +5.8% (mcap $786.18M, vol $125.37M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $163.5k | $717.2k | 1.4 d | h24 -46% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $50.4k | $452.5k | 16.1 h | h24 +886% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $87.1k | $1.44M | 13.9 h | h24 +3928% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 80* | SKIP | [HYPER](https://dexscreener.com/solana/DYJgMJWR4wEfdcifuYrdJFfW1V44BvS7N7DgQh9qukxi) | `DYJgMJWR4wEfdcifuYrdJFfW1V44BvS7N7DgQh9qukxi` | $84.1k | $204.11M | 7.8 d | h24 -32% | #2 Authorities / extensions FAIL (+40); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.24M | 672.5 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,126 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.38M | $17.79M | 746.7 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,594 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.53M | $13.78M | 183.2 d | h24 +7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,599 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $227.2k | $9.17M | +17% | +471% | +29008% | 19.7x | liq/mcap 2.5%; spike (+17% 1h, +471% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $87.5k | $1.45M | -11% | +24% | +3963% | 11.7x | none flagged (still high risk) | 59 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $43.2k | $341.4k | +3% | -60% | +868% | 57.1x | thin liq $43.2k; churn 57x vol/liq | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $40.0k | $236.9k | -34% | -34% | +715% | 105.8x | thin liq $40.0k; churn 106x vol/liq | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $51.4k | $470.7k | +2% | +4% | +926% | 40.9x | churn 41x vol/liq | 52 |
| [SEXYANIMAL](https://pump.fun/coin/9hTjkeV6TqqXZEXZZdjXzaFSBqgbC9pCeWaGDfBbpump) | `9hTjkeV6TqqXZEXZZdjXzaFSBqgbC9pCeWaGDfBbpump` | $23.9k | $126.4k | +2% | +317% | +317% | 0.5x | thin liq $23.9k; spike (+2% 1h, +317% 6h); lopsided buys/sells 7.95 | not scored |

_Timing: total 155s (discovery 72.0s, screen 1.3s, GT prime 0.3s, scoring 81.3s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/143; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
