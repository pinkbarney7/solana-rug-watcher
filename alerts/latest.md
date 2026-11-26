# Last scan 2026-11-26T05:12:10Z - mode: helius (box heartbeat stale (70 min); budget 0/3000)

```
[fast_scan] 145 candidate mints from 9 source tags; 142 with pair data; 18 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 71s
[fast_scan] scored Grodia in 78s
[fast_scan] scored NORFEATH in 79s
[fast_scan] scored VINE in 79s
[fast_scan] scored SPCX in 79s
[fast_scan] scored FLOAT in 79s
# Market scan 2026-11-26 05:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,919 (+3.0% 24h), ETH $1,700 (+2.5% 24h), SOL $71.12 (+3.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.3% (mcap $1.90B, vol $366.62M), pump-fun +4.2% (mcap $787.18M, vol $133.69M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $159.3k | $685.1k | 1.0 d | h24 +272% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $58.1k | $631.7k | 8.1 h | h24 +1277% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $77.1k | $1.10M | 6.8 h | h24 +3025% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $460.1k | $3.11M | 28.3 d | h24 +23% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 49,793 (growth n/a: first sighting) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.13M | 672.2 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,103 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.73M | 182.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,868 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GOTF](https://pump.fun/coin/91Nahzz8NX1p9dc466RF5me5Q1LGDfY4KjBbyrnmpump) | `91Nahzz8NX1p9dc466RF5me5Q1LGDfY4KjBbyrnmpump` | $715.1k | $102.42M | +346535% | +346535% | +346535% | 0.5x | liq/mcap 0.7%; spike (+346535% 1h, +346535% 6h); < 1h old | not scored |
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $86.5k | $1.47M | +19% | +4574% | +4574% | 7.2x | spike (+19% 1h, +4574% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $74.9k | $1.08M | +0% | +2933% | +2933% | 9.0x | spike (+0% 1h, +2933% 6h) | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $49.7k | $370.9k | +2% | +1177% | +1177% | 78.8x | thin liq $49.7k; churn 79x vol/liq; spike (+2% 1h, +1177% 6h) | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $77.1k | $1.10M | +9% | -1% | +3025% | 25.0x | churn 25x vol/liq | 59 |
| [FRITZ](https://pump.fun/coin/4VMwK3shXxsaMbiJ4qtBMMEgi63riezBSWFHfA6Vpump) | `4VMwK3shXxsaMbiJ4qtBMMEgi63riezBSWFHfA6Vpump` | $21.9k | $101.8k | +240% | +240% | +240% | 9.1x | thin liq $21.9k; spike (+240% 1h, +240% 6h); < 1h old | not scored |

_Timing: total 153s (discovery 71.7s, screen 1.3s, GT prime 0.2s, scoring 79.4s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 6/132; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
