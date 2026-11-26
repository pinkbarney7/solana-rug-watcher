# Last scan 2026-11-26T08:52:48Z - mode: helius (box heartbeat stale (288 min); budget 140/3000)

```
[fast_scan] 123 candidate mints from 10 source tags; 118 with pair data; 22 >= $50,000 liq; 9 pass survivor pre-gates (10s)
[fast_scan] scored MOODENG in 109s
[fast_scan] scored BASKET in 119s
[fast_scan] scored UHI in 145s
[fast_scan] scored JIMMY in 181s
[fast_scan] scored Grodia in 188s
[fast_scan] scored NORFEATH in 204s
[fast_scan] scored SPCX in 213s
[fast_scan] scored VINE in 249s
# Market scan 2026-11-26 08:52 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,700 (+2.4% 24h), ETH $1,690 (+2.5% 24h), SOL $70.89 (+4.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.4% (mcap $1.89B, vol $372.83M), pump-fun +4.2% (mcap $783.67M, vol $148.26M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $195.3k | $958.4k | 1.2 d | h24 +6% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $127.3k | $768.2k | 2.5 d | h24 -34% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 54* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $50.3k | $466.0k | 11.8 h | h24 +916% | #9 Price momentum FAIL (+14); #18 Wash trading (recent swaps) WARN (+7); #5 Token / pool age WARN (+5) |
| 57* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $62.9k | $731.5k | 10.4 h | h24 +1973% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.3k | $1.12M | 9.5 h | h24 +3036% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.27M | 672.4 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,122 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $28.13M | 806.6 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,913 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.64M | 183.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,403 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $163.4k | $5.07M | -31% | +324% | +15979% | 9.2x | liq/mcap 3.2%; spike (-31% 1h, +324% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.5k | $1.13M | +1% | +1% | +3053% | 10.5x | none flagged (still high risk) | 59 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $33.2k | $197.9k | +93% | +592% | +592% | 32.9x | thin liq $33.2k; churn 33x vol/liq; spike (+93% 1h, +592% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $62.9k | $731.5k | -12% | +10% | +1973% | 34.5x | churn 34x vol/liq | 57 |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $17.4k | $62.9k | +28% | +573% | +460% | 15.9x | thin liq $17.4k; spike (+28% 1h, +573% 6h) | not scored |
| [Elonmas](https://dexscreener.com/solana/25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru) | `25WMvnpEqe1t5E3DdT8Fc5CtqycmJV24n2ZTakGfz6ru` | $160.4k | $204.8k | +49% | +301% | +301% | 64.6x | churn 65x vol/liq; spike (+49% 1h, +301% 6h) | not scored |

_Timing: total 275s (discovery 9.0s, screen 1.4s, GT prime 15.0s, scoring 249.2s for 8 coins, 8 newly scored). ~87 Helius credits (smart-money discovery 40). HTTP cache hits 0/189; Helius 429s 98; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
