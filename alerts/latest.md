# Last scan 2026-11-26T08:16:32Z - mode: helius (box heartbeat stale (253 min); budget 100/3000)

```
[fast_scan] 126 candidate mints from 10 source tags; 121 with pair data; 22 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored UHI in 72s
[fast_scan] scored Grodia in 80s
[fast_scan] scored Elonmas in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored JIMMY in 84s
[fast_scan] scored BASKET in 85s
[fast_scan] scored NORFEATH in 105s
[fast_scan] scored MOODENG in 88s
# Market scan 2026-11-26 08:16 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,599 (+3.1% 24h), ETH $1,689 (+3.1% 24h), SOL $70.88 (+4.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.4% (mcap $1.89B, vol $365.16M), pump-fun +4.9% (mcap $784.97M, vol $149.60M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $191.2k | $948.5k | 1.2 d | h24 +2% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $127.0k | $660.1k | 2.5 d | h24 -38% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [Elonmas](https://dexscreener.com/solana/25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru) | `25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru` | $204.8k | $162.0k | 1.7 h | h24 +218% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 57* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $55.8k | $580.1k | 9.8 h | h24 +1544% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $78.2k | $1.18M | 8.9 h | h24 +3197% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $58.2k | $626.2k | 11.2 h | h24 +1265% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.25M | 672.3 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,121 (growth n/a: first sighting) |
| 50* | CAUTION | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.94M | $29.36M | 806.6 d | h24 +11% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.6% (+4.1); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.28M | $13.65M | 183.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 394,543 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $189.2k | $6.80M | +296% | +568% | +21485% | 6.9x | liq/mcap 2.8%; spike (+296% 1h, +568% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $78.2k | $1.18M | +2% | +32% | +3197% | 10.1x | none flagged (still high risk) | 59 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $55.8k | $580.1k | -30% | -56% | +1544% | 38.3x | churn 38x vol/liq | 57 |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $16.3k | $55.9k | +1% | +704% | +180% | 17.2x | thin liq $16.3k; spike (+1% 1h, +704% 6h) | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $58.2k | $626.2k | +47% | +26% | +1265% | 25.6x | churn 26x vol/liq | 60 |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $45.0k | $302.5k | -14% | -63% | +941% | 90.4x | thin liq $45.0k; churn 90x vol/liq | not scored |

_Timing: total 234s (discovery 71.4s, screen 1.4s, GT prime 0.6s, scoring 160.6s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/181; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
