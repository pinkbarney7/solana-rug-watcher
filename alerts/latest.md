# Last scan 2026-11-26T10:24:31Z - mode: helius (box heartbeat stale (381 min); budget 277/3000)

```
[fast_scan] 116 candidate mints from 10 source tags; 112 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 80s
[fast_scan] scored FSD V15 in 84s
[fast_scan] scored VINE in 89s
[fast_scan] scored MOODENG in 93s
[fast_scan] scored SPCX in 93s
[fast_scan] scored DOG in 101s
[fast_scan] scored UHI in 109s
# Market scan 2026-11-26 10:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,834 (+3.2% 24h), ETH $1,701 (+3.4% 24h), SOL $70.96 (+4.8% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +7.4% (mcap $1.89B, vol $370.34M), pump-fun +5.2% (mcap $785.91M, vol $143.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $129.8k | $778.3k | 2.6 d | h24 -30% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | $193.0k | $123.0k | 1.4 h | h24 +113% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $210.7k | $121.0k | 1.6 h | h24 +69% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 62* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $81.0k | $1.25M | 11.1 h | h24 +3416% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.33M | 672.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,128 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.86M | $27.91M | 806.7 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,014 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.36M | $13.72M | 183.1 d | h24 +6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,341 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $178.2k | $5.87M | -2% | +424% | +18529% | 14.2x | liq/mcap 3.0%; spike (-2% 1h, +424% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $81.3k | $1.27M | +17% | +25% | +3447% | 10.3x | none flagged (still high risk) | 62 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $36.9k | $235.9k | -13% | +725% | +725% | 38.4x | thin liq $36.9k; churn 38x vol/liq; spike (-13% 1h, +725% 6h) | not scored |
| [STRUCK](https://pump.fun/coin/HN9jRRCKuLNL3oSgNV1MBvd3Krg6TingFntJp1PSpump) | `HN9jRRCKuLNL3oSgNV1MBvd3Krg6TingFntJp1PSpump` | $22.3k | $96.7k | +230% | +230% | +230% | 14.5x | thin liq $22.3k; spike (+230% 1h, +230% 6h); < 1h old | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $46.9k | $408.6k | -8% | -57% | +1058% | 48.1x | thin liq $46.9k; churn 48x vol/liq | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $49.5k | $448.2k | +1% | -25% | +877% | 35.3x | thin liq $49.5k; churn 35x vol/liq | not scored |

_Timing: total 182s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 108.9s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/140; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
