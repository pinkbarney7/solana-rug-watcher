# Last scan 2026-11-26T11:01:12Z - mode: helius (box heartbeat stale (418 min); budget 287/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 110 with pair data; 21 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored DOG in 70s
[fast_scan] scored VINE in 79s
[fast_scan] scored SPCX in 79s
[fast_scan] scored UHI in 80s
[fast_scan] scored JIMMY in 80s
[fast_scan] scored Anthropic in 97s
[fast_scan] scored MOODENG in 105s
# Market scan 2026-11-26 11:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,444 (+2.9% 24h), ETH $1,693 (+3.1% 24h), SOL $70.52 (+4.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.9% (mcap $1.89B, vol $355.28M), pump-fun +4.4% (mcap $781.99M, vol $129.85M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $126.1k | $737.6k | 2.6 d | h24 -34% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 47* | SKIP | [Anthropic](https://dexscreener.com/solana/8Di9FbUApRwpaEoTBh8xdDtqeq5nhn6mbyXetbLiDanA) | `8Di9FbUApRwpaEoTBh8xdDtqeq5nhn6mbyXetbLiDanA` | $194.3k | $146.4k | 1.6 h | h24 +187% | sellability gate: Jupiter exit test FAIL: $25: no sell route (No routes found); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $225.1k | $131.3k | 2.2 h | h24 +83% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $84.3k | $1.37M | 11.7 h | h24 +3727% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.88M | $28.66M | 806.7 d | h24 -2% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.6% (+4.1); #6 unknown (+3); GATES FAILED: rug-funder link |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.15M | 672.4 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,126 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.66M | 183.1 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,262 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $195.4k | $7.02M | +38% | +361% | +22168% | 15.8x | liq/mcap 2.8%; spike (+38% 1h, +361% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $84.3k | $1.37M | +19% | +23% | +3727% | 10.3x | none flagged (still high risk) | 59 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $38.5k | $256.9k | +8% | +799% | +799% | 38.0x | thin liq $38.5k; churn 38x vol/liq; spike (+8% 1h, +799% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $49.2k | $450.5k | +3% | -62% | +1177% | 46.6x | thin liq $49.2k; churn 47x vol/liq | not scored |
| [konnichiwa](https://pump.fun/coin/HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump) | `HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump` | $19.3k | $79.2k | +172% | +172% | +172% | 14.2x | thin liq $19.3k; spike (+172% 1h, +172% 6h); < 1h old | not scored |
| [486](https://pump.fun/coin/9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump) | `9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump` | $13.1k | $32.9k | +39% | +199% | +539% | 1.6x | thin liq $13.1k | not scored |

_Timing: total 178s (discovery 71.8s, screen 1.1s, GT prime 0.4s, scoring 105.1s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/148; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
