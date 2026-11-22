# Last scan 2026-11-22T01:55:55Z - mode: helius (box heartbeat stale (6469 min); budget 30/3000)

```
[fast_scan] 124 candidate mints from 11 source tags; 122 with pair data; 23 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored Singularity in 71s
[fast_scan] scored AODT in 78s
[fast_scan] scored VINE in 78s
[fast_scan] scored pippin in 79s
[fast_scan] scored FIONA in 79s
[fast_scan] scored SPCX in 79s
# Market scan 2026-11-22 01:55 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,064 (+2.0% 24h), ETH $1,685 (+3.9% 24h), SOL $70.25 (+2.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.9% (mcap $1.84B, vol $376.84M), pump-fun -0.8% (mcap $770.32M, vol $132.15M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $93.9k | $488.0k | 1.2 d | h24 +258% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $88.4k | $1.62M | 1.0 d | h24 +69% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.5% (+5.4) |
| 67* | SKIP | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $3.12M | $6.06B | 4.3 d | h24 +1026899% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.1% (+11.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.47M | $9.19M | 668.1 d | h24 +21% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 4h (now 345,290) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.28M | $17.07M | 742.2 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 4h (now 182,896) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.25M | $13.12M | 178.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 4h (now 385,457) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MANDY](https://pump.fun/coin/3JqV4LuKVqzCpWsDAsBnTLg2mKik22hLeyyPyfW3pump) | `3JqV4LuKVqzCpWsDAsBnTLg2mKik22hLeyyPyfW3pump` | $42.8k | $378.4k | +880% | +880% | +880% | 8.2x | thin liq $42.8k; spike (+880% 1h, +880% 6h); lopsided buys/sells 4.74; < 1h old | not scored |
| [RIZZMAS3](https://pump.fun/coin/BQcV4Ryfu9bZK8egAF89AhkojdJqAaDt4xTFwUQ2pump) | `BQcV4Ryfu9bZK8egAF89AhkojdJqAaDt4xTFwUQ2pump` | $31.8k | $172.2k | +24% | +534% | +534% | 40.1x | thin liq $31.8k; churn 40x vol/liq; spike (+24% 1h, +534% 6h) | not scored |
| [STREETS](https://pump.fun/coin/82mseLFauphc2yutbaDGgViahquJ1jGVLpyof99xpump) | `82mseLFauphc2yutbaDGgViahquJ1jGVLpyof99xpump` | $57.7k | $636.9k | +5% | +458% | +458% | 22.4x | spike (+5% 1h, +458% 6h) | not scored |
| [RIZZMAS](https://pump.fun/coin/6J3ApVu8dSLg1TJjBLWSTgmnvJXcH2YyF2iDC48Fpump) | `6J3ApVu8dSLg1TJjBLWSTgmnvJXcH2YyF2iDC48Fpump` | $20.5k | $82.8k | +181% | +181% | +181% | 25.5x | thin liq $20.5k; churn 26x vol/liq; spike (+181% 1h, +181% 6h); < 1h old | not scored |
| [Elf](https://dexscreener.com/solana/FQtsgCcssPBZiuWsxaafrqATDKEhwWh4uzjdwfuqDEq5) | `FQtsgCcssPBZiuWsxaafrqATDKEhwWh4uzjdwfuqDEq5` | $24.6k | $25.3k | +167% | +167% | +167% | 3.9x | thin liq $24.6k; spike (+167% 1h, +167% 6h); < 1h old | not scored |
| [GRAUDIA](https://pump.fun/coin/B1oGtkaVAVZkdtWV7SXrHnFkcWC1Kd45sYpy6RYTpump) | `B1oGtkaVAVZkdtWV7SXrHnFkcWC1Kd45sYpy6RYTpump` | $23.9k | $121.9k | +35% | +295% | +295% | 7.6x | thin liq $23.9k | not scored |

_Timing: total 152s (discovery 70.8s, screen 1.3s, GT prime 0.4s, scoring 79.2s for 6 coins, 6 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 6/127; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
