# Last scan 2026-11-26T06:53:52Z - mode: helius (box heartbeat stale (171 min); budget 30/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 128 with pair data; 21 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored DOG in 78s
[fast_scan] scored Grodia in 87s
[fast_scan] scored UHI in 87s
[fast_scan] scored MOODENG in 88s
[fast_scan] scored VINE in 89s
[fast_scan] scored Santa Clau in 89s
[fast_scan] scored SPCX in 89s
[fast_scan] scored JIMMY in 89s
# Market scan 2026-11-26 06:53 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,411 (+2.1% 24h), ETH $1,684 (+1.5% 24h), SOL $70.56 (+2.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.3% (mcap $1.89B, vol $365.90M), pump-fun +3.8% (mcap $785.88M, vol $132.91M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $129.9k | $660.8k | 2.4 d | h24 -47% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6) | `FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6` | $234.6k | $135.2k | 2.7 h | h24 +71% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Santa Clau](https://dexscreener.com/solana/BooKBEXvcj1A71JQJzYWebDHBSXvKZ3FjhALSdFyVUva) | `BooKBEXvcj1A71JQJzYWebDHBSXvKZ3FjhALSdFyVUva` | $173.5k | $116.9k | 1.1 h | h24 +131% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $78.8k | $1.20M | 7.6 h | h24 +3262% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.3k | $845.1k | 8.4 h | h24 +2295% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.28M | 672.3 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,113 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.89M | $28.82M | 806.6 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,887 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.61M | 183.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 394,361 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $90.5k | $1.62M | +12% | +5034% | +5034% | 7.6x | spike (+12% 1h, +5034% 6h) | not scored |
| [ELONCOIN](https://dexscreener.com/solana/CyKTZ2bg1VyUkjyMvABrMgSK3yksM7N2GZd6UY9rbh3U) | `CyKTZ2bg1VyUkjyMvABrMgSK3yksM7N2GZd6UY9rbh3U` | $33.3k | $182.5k | +1068% | +1068% | +1068% | 0.8x | thin liq $33.3k; spike (+1068% 1h, +1068% 6h); lopsided buys/sells 3.34; < 1h old | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $21.7k | $95.9k | +264% | +1174% | +1718% | 11.2x | thin liq $21.7k; spike (+264% 1h, +1174% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $78.8k | $1.20M | +2% | +110% | +3262% | 9.6x | none flagged (still high risk) | 56 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $67.3k | $845.1k | -6% | -51% | +2295% | 30.3x | churn 30x vol/liq | 58 |
| [486](https://pump.fun/coin/9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump) | `9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump` | $12.3k | $29.0k | +81% | +484% | +464% | 1.0x | thin liq $12.3k; spike (+81% 1h, +484% 6h) | not scored |

_Timing: total 163s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 89.4s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/159; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
