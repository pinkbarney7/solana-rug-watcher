# Last scan 2026-11-26T09:38:13Z - mode: helius (box heartbeat stale (336 min); budget 237/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 112 with pair data; 20 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored Sol in 72s
[fast_scan] scored UHI in 81s
[fast_scan] scored VINE in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored BASKET in 82s
[fast_scan] scored Grodia in 82s
[fast_scan] scored MOODENG in 83s
[fast_scan] scored JIMMY in 84s
# Market scan 2026-11-26 09:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,725 (+3.2% 24h), ETH $1,699 (+3.7% 24h), SOL $70.92 (+5.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +7.2% (mcap $1.89B, vol $345.86M), pump-fun +4.9% (mcap $783.58M, vol $125.82M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $184.2k | $901.9k | 1.2 d | h24 -24% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $134.0k | $829.9k | 2.5 d | h24 -26% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [Sol](https://dexscreener.com/solana/8KsuTdpbgLZq3S2DMSaab9x18waZY2e6yaHrWDtf8AUr) | `8KsuTdpbgLZq3S2DMSaab9x18waZY2e6yaHrWDtf8AUr` | $167.3k | $115.0k | 1.1 h | h24 +125% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $50.6k | $475.5k | 11.2 h | h24 +1247% | #9 Price momentum FAIL (+14); #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $74.9k | $1.08M | 10.3 h | h24 +2916% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.23M | 672.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,124 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $28.01M | 806.7 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,015 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.34M | $13.71M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,412 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $169.0k | $5.37M | -36% | +365% | +16947% | 11.0x | liq/mcap 3.1%; spike (-36% 1h, +365% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $74.9k | $1.08M | -5% | -7% | +2916% | 11.0x | none flagged (still high risk) | 59 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $39.7k | $272.6k | +42% | +854% | +854% | 33.5x | thin liq $39.7k; churn 33x vol/liq; spike (+42% 1h, +854% 6h) | not scored |
| [YEE](https://dexscreener.com/solana/9G47JD7gUQ1Yv3BbDqCWAzuJWkN4smbmZjL6eozMGwBF) | `9G47JD7gUQ1Yv3BbDqCWAzuJWkN4smbmZjL6eozMGwBF` | $33.7k | $47.1k | +391% | +391% | +391% | 5.3x | thin liq $33.7k; spike (+391% 1h, +391% 6h); < 1h old | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $20.6k | $86.1k | +66% | +418% | +457% | 13.5x | thin liq $20.6k; spike (+66% 1h, +418% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $50.6k | $475.5k | -17% | -40% | +1247% | 43.8x | churn 44x vol/liq | 56 |

_Timing: total 158s (discovery 71.9s, screen 1.1s, GT prime 0.4s, scoring 84.2s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/163; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
