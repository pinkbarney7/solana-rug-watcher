# Last scan 2026-11-21T16:54:35Z - mode: helius (box heartbeat stale (5927 min); budget 10/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 121 with pair data; 31 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored win in 78s
[fast_scan] scored PUNANI in 86s
[fast_scan] scored pippin in 87s
[fast_scan] scored VINE in 87s
[fast_scan] scored RIEMANN in 88s
[fast_scan] scored MAYA in 89s
[fast_scan] scored JENSEN in 89s
[fast_scan] scored CoT in 90s
[fast_scan] scored SPCX in 72s
# Market scan 2026-11-21 16:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,032 (+1.0% 24h), ETH $1,683 (+2.5% 24h), SOL $70.55 (+1.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.9% (mcap $1.84B, vol $428.47M), pump-fun +0.6% (mcap $771.98M, vol $143.59M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | CAUTION | [CoT](https://dexscreener.com/solana/5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW) | `5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW` | $65.4k | $982.9k | 19.3 h | h24 +52% | #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [win](https://dexscreener.com/solana/9N6zGSBKeJMcDUt2sk9iQzoawqt2thg2KJv9K5gxDNJX) | `9N6zGSBKeJMcDUt2sk9iQzoawqt2thg2KJv9K5gxDNJX` | $197.1k | $130.8k | 2.1 h | h24 +198% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [RIEMANN](https://pump.fun/coin/dkpuQdjegjU8zcwYrBzYrLW11wvtjwonBsQhjLApump) | `dkpuQdjegjU8zcwYrBzYrLW11wvtjwonBsQhjLApump` | $77.4k | $1.15M | 12.9 h | h24 +1286% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [JENSEN](https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump) | `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump` | $88.4k | $1.33M | 16.9 h | h24 +1306% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [PUNANI](https://pump.fun/coin/2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump) | `2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump` | $98.3k | $1.80M | 12.4 h | h24 +5428% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.5% (+5.4) |
| 66* | SKIP | [MAYA](https://pump.fun/coin/FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump) | `FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump` | $142.1k | $3.82M | 11.8 h | h24 +10455% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 3.7% (+7.5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.47M | $9.20M | 667.7 d | h24 +17% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 8h (now 345,302) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.28M | $16.97M | 741.9 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 15h (now 182,914) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $13.11M | 178.4 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.2% in 8h (now 383,607) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MAYA](https://pump.fun/coin/FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump) | `FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump` | $142.1k | $3.82M | +15% | +24% | +10455% | 11.1x | liq/mcap 3.7% | 66 |
| [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $81.5k | $820.1k | +371% | +1663% | +1663% | 2.0x | spike (+371% 1h, +1663% 6h) | not scored |
| [PUNANI](https://pump.fun/coin/2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump) | `2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump` | $98.3k | $1.80M | -9% | -25% | +5428% | 19.7x | none flagged (still high risk) | 60 |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $93.6k | $1.67M | +178% | +1521% | +1521% | 8.0x | spike (+178% 1h, +1521% 6h) | not scored |
| [PDOG](https://pump.fun/coin/Bmy2XNoysbCCqzqX3CC7DFbHW6FhGJ36MzWD1Wgdpump) | `Bmy2XNoysbCCqzqX3CC7DFbHW6FhGJ36MzWD1Wgdpump` | $13.2k | $34.9k | -10% | -15% | +2313% | 28.4x | thin liq $13.2k; churn 28x vol/liq | not scored |
| [Air](https://dexscreener.com/solana/DdC2S2i6ed7Ld9HJziKcm4hRdMdWERcz74gg9uZUUf3C) | `DdC2S2i6ed7Ld9HJziKcm4hRdMdWERcz74gg9uZUUf3C` | $12.4k | $36.5k | +332% | +332% | +332% | 1.9x | thin liq $12.4k; spike (+332% 1h, +332% 6h); < 1h old | not scored |

_Timing: total 223s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 149.9s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/175; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
