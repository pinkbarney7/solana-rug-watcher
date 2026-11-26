# Last scan 2026-11-26T09:46:03Z - mode: helius (box heartbeat stale (343 min); budget 237/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 111 with pair data; 19 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored NORFEATH in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored MOODENG in 80s
[fast_scan] scored UHI in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored JIMMY in 83s
[fast_scan] scored BASKET in 84s
# Market scan 2026-11-26 09:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,851 (+3.4% 24h), ETH $1,702 (+3.9% 24h), SOL $71.09 (+5.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +7.2% (mcap $1.89B, vol $345.86M), pump-fun +4.9% (mcap $783.58M, vol $125.82M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $185.1k | $884.2k | 1.2 d | h24 -21% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $133.7k | $819.9k | 2.5 d | h24 -26% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $50.4k | $464.9k | 12.7 h | h24 +913% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.1k | $1.11M | 10.5 h | h24 +3009% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.27M | 672.4 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,124 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $28.02M | 806.7 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,015 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.36M | $13.73M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,412 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $177.2k | $5.87M | +27% | +400% | +18516% | 11.2x | liq/mcap 3.0%; spike (+27% 1h, +400% 6h) | not scored |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $41.5k | $296.8k | +69% | +938% | +938% | 32.5x | thin liq $41.5k; churn 33x vol/liq; spike (+69% 1h, +938% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $75.3k | $1.09M | -4% | -6% | +2942% | 11.0x | none flagged (still high risk) | 59 |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $22.1k | $98.4k | +63% | +615% | +482% | 12.5x | thin liq $22.1k; spike (+63% 1h, +615% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $44.3k | $365.8k | -46% | -62% | +937% | 50.2x | thin liq $44.3k; churn 50x vol/liq | not scored |
| [HONEY](https://dexscreener.com/solana/4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy) | `4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy` | $24.7k | $1.61M | +5% | +8% | +1272% | 0.1x | thin liq $24.7k; liq/mcap 1.5% | not scored |

_Timing: total 157s (discovery 71.8s, screen 1.1s, GT prime 0.1s, scoring 83.6s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
