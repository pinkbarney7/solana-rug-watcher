# Last scan 2026-11-26T12:35:32Z - mode: helius (box heartbeat stale (513 min); budget 387/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 116 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored UHI in 70s
[fast_scan] scored pippin in 78s
[fast_scan] scored SPCX in 78s
[fast_scan] scored NORFEATH in 79s
[fast_scan] scored VINE in 79s
[fast_scan] scored JIMMY in 80s
# Market scan 2026-11-26 12:35 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,566 (+3.3% 24h), ETH $1,700 (+3.4% 24h), SOL $70.68 (+4.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +8.0% (mcap $1.89B, vol $336.88M), pump-fun +5.7% (mcap $786.05M, vol $124.10M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $124.1k | $702.2k | 2.6 d | h24 -42% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $52.2k | $492.0k | 15.5 h | h24 +972% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $91.0k | $1.58M | 13.3 h | h24 +4319% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.8% (+5.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.23M | 672.5 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,129 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.37M | $17.78M | 746.7 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 5h (now 182,599) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.74M | 183.2 d | h24 +6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,106 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $229.8k | $9.51M | +17% | +584% | +30073% | 17.1x | liq/mcap 2.4%; spike (+17% 1h, +584% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $91.0k | $1.58M | -2% | +44% | +4319% | 10.7x | none flagged (still high risk) | 59 |
| [Pinky](https://pump.fun/coin/Ag6hKhaYos8a2taqpq1nrqD9B4ArtFN3Nny6tuEZpump) | `Ag6hKhaYos8a2taqpq1nrqD9B4ArtFN3Nny6tuEZpump` | $22.0k | $94.6k | +222% | +222% | +222% | 21.0x | thin liq $22.0k; spike (+222% 1h, +222% 6h); < 1h old | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $44.2k | $360.6k | -24% | -55% | +922% | 54.8x | thin liq $44.2k; churn 55x vol/liq | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $52.2k | $492.0k | -4% | +13% | +972% | 36.7x | churn 37x vol/liq | 52 |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $43.0k | $273.5k | +4% | -13% | +841% | 97.9x | thin liq $43.0k; churn 98x vol/liq | not scored |

_Timing: total 153s (discovery 71.4s, screen 1.1s, GT prime 0.3s, scoring 80.2s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/126; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
