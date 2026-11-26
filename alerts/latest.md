# Last scan 2026-11-26T07:12:49Z - mode: helius (box heartbeat stale (190 min); budget 40/3000)

```
[fast_scan] 143 candidate mints from 10 source tags; 139 with pair data; 20 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored Grodia in 70s
[fast_scan] scored UHI in 79s
[fast_scan] scored VINE in 80s
[fast_scan] scored JIMMY in 80s
[fast_scan] scored BASKET in 82s
[fast_scan] scored SPCX in 88s
[fast_scan] scored MOODENG in 112s
# Market scan 2026-11-26 07:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,439 (+1.9% 24h), ETH $1,686 (+1.4% 24h), SOL $70.78 (+2.8% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +4.6% (mcap $1.88B, vol $362.62M), pump-fun +3.5% (mcap $783.23M, vol $130.48M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $196.9k | $1.01M | 1.1 d | h24 +114% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $135.8k | $667.5k | 2.4 d | h24 -43% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.6k | $1.16M | 7.9 h | h24 +3154% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.0k | $833.3k | 8.8 h | h24 +2261% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.31M | 672.3 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,115 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.89M | $28.90M | 806.6 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,893 (growth n/a: first sighting) |
| 66* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.61M | 166.6 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #6 unknown (+3); #7 unknown (+3); GATES FAILED: authorities, rug-funder link |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UBR](https://pump.fun/coin/rZfj79VG6ubQaqpaAPhqih6iKaE9GddpmLqRqjhpump) | `rZfj79VG6ubQaqpaAPhqih6iKaE9GddpmLqRqjhpump` | $932.3k | $175.42M | -1% | +590148% | +590148% | 0.5x | liq/mcap 0.5%; spike (-1% 1h, +590148% 6h) | not scored |
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $89.9k | $1.59M | +19% | +4945% | +4945% | 7.8x | spike (+19% 1h, +4945% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.6k | $1.16M | +20% | +49% | +3154% | 9.9x | none flagged (still high risk) | 56 |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $17.2k | $62.0k | +111% | +767% | +959% | 16.0x | thin liq $17.2k; spike (+111% 1h, +767% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.0k | $833.3k | +2% | -47% | +2261% | 30.8x | churn 31x vol/liq | 58 |
| [486](https://pump.fun/coin/9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump) | `9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump` | $11.9k | $27.3k | +41% | +450% | +430% | 1.0x | thin liq $11.9k; spike (+41% 1h, +450% 6h) | not scored |

_Timing: total 185s (discovery 71.1s, screen 1.6s, GT prime 0.2s, scoring 112.1s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/146; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
