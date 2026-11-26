# Last scan 2026-11-26T05:40:09Z - mode: helius (box heartbeat stale (97 min); budget 20/3000)

```
[fast_scan] 147 candidate mints from 9 source tags; 144 with pair data; 18 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored SPCX in 68s
[fast_scan] scored VINE in 77s
[fast_scan] scored Grodia in 77s
[fast_scan] scored MOODENG in 95s
[fast_scan] scored NORFEATH in 102s
[fast_scan] scored BASKET in 103s
# Market scan 2026-11-26 05:40 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,949 (+3.2% 24h), ETH $1,700 (+2.8% 24h), SOL $71.28 (+4.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.4% (mcap $1.90B, vol $372.67M), pump-fun +4.4% (mcap $788.65M, vol $133.20M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 42* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $163.7k | $735.7k | 1.0 d | h24 +103% | #8 Turnover / bot pattern WARN (+4); #6 unknown (+3); #7 unknown (+3) |
| 56* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $53.3k | $531.0k | 8.6 h | h24 +1057% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $70.3k | $915.6k | 7.2 h | h24 +2495% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.10M | 672.2 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,105 (growth n/a: first sighting) |
| 50* | CAUTION | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $28.84M | 806.4 d | h24 +11% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.6% (+4.1); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.25M | $13.72M | 182.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,939 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $84.8k | $1.41M | +7% | +4374% | +4374% | 7.6x | spike (+7% 1h, +4374% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $77.7k | $1.16M | +20% | +701% | +3153% | 9.1x | spike (+20% 1h, +701% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $48.2k | $347.1k | -28% | +1095% | +1095% | 81.8x | thin liq $48.2k; churn 82x vol/liq; spike (-28% 1h, +1095% 6h) | not scored |
| [MONEY](https://pump.fun/coin/DeACAbp2GMzapB6Z2K8qdkTZupmNbKc6EZx9bnbCpump) | `DeACAbp2GMzapB6Z2K8qdkTZupmNbKc6EZx9bnbCpump` | $73.2k | $945.1k | +25% | +870% | +870% | 27.6x | churn 28x vol/liq; spike (+25% 1h, +870% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $70.3k | $915.6k | -22% | -48% | +2495% | 27.9x | churn 28x vol/liq | 58 |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $55.0k | $565.7k | -1% | -16% | +1133% | 24.1x | none flagged (still high risk) | 56 |

_Timing: total 177s (discovery 71.7s, screen 1.3s, GT prime 0.3s, scoring 103.3s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/126; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
