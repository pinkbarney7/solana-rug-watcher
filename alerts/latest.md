# Last scan 2026-11-26T09:14:23Z - mode: helius (box heartbeat stale (312 min); budget 227/3000)

```
[fast_scan] 132 candidate mints from 9 source tags; 128 with pair data; 31 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored SPCX in 77s
[fast_scan] scored MOODENG in 78s
[fast_scan] scored UHI in 78s
[fast_scan] scored BASKET in 79s
[fast_scan] scored NORFEATH in 87s
[fast_scan] scored VINE in 87s
[fast_scan] scored JIMMY in 88s
# Market scan 2026-11-26 09:14 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,827 (+2.8% 24h), ETH $1,700 (+3.2% 24h), SOL $71.04 (+4.9% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.5% (mcap $1.89B, vol $373.59M), pump-fun +4.3% (mcap $784.39M, vol $145.77M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $190.9k | $946.3k | 1.2 d | h24 +14% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $126.5k | $763.2k | 2.5 d | h24 -39% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $49.8k | $455.3k | 12.1 h | h24 +892% | #9 Price momentum FAIL (+14); #4 Liquidity (absolute) WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.3k | $1.12M | 9.9 h | h24 +3034% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.40M | 672.4 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,122 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $28.03M | 806.7 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,015 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.37M | $13.72M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,403 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $172.3k | $5.61M | -17% | +383% | +17711% | 8.9x | liq/mcap 3.1%; spike (-17% 1h, +383% 6h) | not scored |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $41.2k | $295.4k | +97% | +933% | +933% | 30.2x | thin liq $41.2k; churn 30x vol/liq; spike (+97% 1h, +933% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.9k | $1.13M | -3% | -4% | +3075% | 10.6x | none flagged (still high risk) | 59 |
| [HONEY](https://dexscreener.com/solana/4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy) | `4vMsoUT2BWatFweudnQM1xedRLfJgJ7hswhcpz4xgBTy` | $23.9k | $1.55M | +1% | +4% | +2772% | 0.1x | thin liq $23.9k; liq/mcap 1.5% | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $19.6k | $78.9k | +43% | +841% | +369% | 14.0x | thin liq $19.6k; spike (+43% 1h, +841% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $48.7k | $441.0k | -23% | -41% | +1150% | 45.2x | thin liq $48.7k; churn 45x vol/liq | not scored |

_Timing: total 161s (discovery 71.3s, screen 1.6s, GT prime 0.2s, scoring 87.6s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 39/148; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
