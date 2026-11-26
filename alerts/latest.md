# Last scan 2026-11-26T06:11:42Z - mode: helius (box heartbeat stale (129 min); budget 30/3000)

```
[fast_scan] 127 candidate mints from 8 source tags; 125 with pair data; 19 >= $50,000 liq; 8 pass survivor pre-gates (85s)
[fast_scan] scored BASKET in 72s
[fast_scan] scored VINE in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored DOG in 79s
[fast_scan] scored MOODENG in 79s
[fast_scan] scored Grodia in 80s
# Market scan 2026-11-26 06:11 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,582 (+2.6% 24h), ETH $1,687 (+2.0% 24h), SOL $70.74 (+3.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.9% (mcap $1.89B, vol $391.05M), pump-fun +4.5% (mcap $786.98M, vol $150.94M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $169.2k | $759.5k | 1.1 d | h24 +117% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6) | `FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6` | $222.1k | $126.5k | 2.0 h | h24 +60% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $68.2k | $868.4k | 7.7 h | h24 +2361% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.21M | 672.2 d | h24 -0% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,108 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $29.10M | 806.5 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,882 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.65M | 182.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,939 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $82.7k | $1.35M | -8% | +4192% | +4192% | 7.9x | spike (-8% 1h, +4192% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $71.6k | $993.4k | -9% | +304% | +2684% | 10.3x | spike (-9% 1h, +304% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $44.0k | $292.6k | -22% | +907% | +907% | 90.2x | thin liq $44.0k; churn 90x vol/liq; spike (-22% 1h, +907% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $68.2k | $868.4k | -22% | -20% | +2361% | 29.3x | churn 29x vol/liq | 58 |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $24.2k | $117.3k | +370% | +310% | +310% | 24.1x | thin liq $24.2k; spike (+370% 1h, +310% 6h) | not scored |
| [Elonmas](https://pump.fun/coin/DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump) | `DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump` | $21.7k | $99.9k | +231% | +231% | +231% | 13.7x | thin liq $21.7k; spike (+231% 1h, +231% 6h); < 1h old | not scored |

_Timing: total 167s (discovery 83.3s, screen 1.4s, GT prime 3.3s, scoring 79.5s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 6/127; Helius 429s 80; DEX Screener ok._
_Source gaps: gt_top_tx: gave up after 3 tries (ReadTimeout: HTTPSConnectionPool(host='api.geckoterminal.com', port=443): Read timed out. (read timeout=20))_

_Full reports: out/<mint>.md (+ .json)_
```
