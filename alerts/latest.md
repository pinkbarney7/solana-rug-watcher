# Last scan 2026-11-26T08:29:18Z - mode: helius (box heartbeat stale (266 min); budget 110/3000)

```
[fast_scan] 124 candidate mints from 10 source tags; 119 with pair data; 24 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored BASKET in 73s
[fast_scan] scored UHI in 80s
[fast_scan] scored VINE in 80s
[fast_scan] scored Grodia in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored NORFEATH in 82s
[fast_scan] scored Elonmas in 82s
[fast_scan] scored JIMMY in 83s
[fast_scan] scored MOODENG in 71s
# Market scan 2026-11-26 08:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,645 (+3.0% 24h), ETH $1,689 (+2.9% 24h), SOL $70.92 (+4.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.5% (mcap $1.89B, vol $361.59M), pump-fun +5.0% (mcap $785.80M, vol $144.18M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $188.9k | $926.9k | 1.2 d | h24 -6% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $130.6k | $703.3k | 2.5 d | h24 -35% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $53.1k | $525.1k | 10.0 h | h24 +1388% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [Elonmas](https://dexscreener.com/solana/25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru) | `25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru` | $213.0k | $170.9k | 1.9 h | h24 +235% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 57* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $58.5k | $626.3k | 11.4 h | h24 +1265% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.8k | $1.16M | 9.2 h | h24 +3158% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.33M | 672.3 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,121 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.94M | $29.40M | 806.6 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,906 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.33M | $13.65M | 183.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 394,543 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $189.9k | $6.85M | +165% | +498% | +21632% | 7.1x | liq/mcap 2.8%; spike (+165% 1h, +498% 6h) | not scored |
| [Elonmas](https://dexscreener.com/solana/5z6cgifysmBv4cs2WFa1CHMb691sqzw7vHyj2g7NaQTh) | `5z6cgifysmBv4cs2WFa1CHMb691sqzw7vHyj2g7NaQTh` | $50.6k | $92.8k | +1005% | +1416% | +1416% | 14.6x | spike (+1005% 1h, +1416% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.8k | $1.16M | -7% | +20% | +3158% | 10.2x | none flagged (still high risk) | 59 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $53.1k | $525.1k | -43% | -58% | +1388% | 40.5x | churn 41x vol/liq | 52 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $29.5k | $159.6k | +28% | +458% | +458% | 35.2x | thin liq $29.5k; churn 35x vol/liq; spike (+28% 1h, +458% 6h) | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $16.0k | $54.0k | -22% | +620% | +220% | 17.4x | thin liq $16.0k; spike (-22% 1h, +620% 6h) | not scored |

_Timing: total 217s (discovery 70.9s, screen 1.3s, GT prime 0.3s, scoring 144.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 101; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
