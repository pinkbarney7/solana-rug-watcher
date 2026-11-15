# Last scan 2026-11-15T04:58:13Z - mode: helius (box heartbeat stale (6700 min); budget 70/3000)

```
[fast_scan] 134 candidate mints from 9 source tags; 133 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored bill in 70s
[fast_scan] scored XTO in 78s
[fast_scan] scored jellyjelly in 78s
[fast_scan] scored CATE in 79s
[fast_scan] scored UODF in 79s
[fast_scan] scored FLOAT in 80s
# Market scan 2026-11-15 04:58 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $65,061 (-3.0% 24h), ETH $1,820 (-4.1% 24h), SOL $71.11 (-5.9% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -8.3% (mcap $2.07B, vol $545.93M), pump-fun +0.6% (mcap $875.04M, vol $140.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $139.7k | $564.8k | 9.2 h | h24 +884% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.04M | $216.85M | 2.7 d | h24 +9% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $1.08M | $233.84M | 1.6 d | h24 +158% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $429.7k | $2.87M | 17.3 d | h24 -10% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +2.8% in 83h (now 45,601) |
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $16.70M | 111.5 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 5h (now 429,364) |
| 51* | SKIP | [jellyjelly](https://pump.fun/coin/FeR8VBqNRSUD5NtXAj2n3j1dAHkZHfyDktKuLXD4pump) | `FeR8VBqNRSUD5NtXAj2n3j1dAHkZHfyDktKuLXD4pump` | $3.61M | $40.37M | 654.2 d | h24 +3% | #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 144,782 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WANTED](https://pump.fun/coin/CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump) | `CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump` | $84.3k | $1.37M | -6% | +3567% | +3567% | 10.3x | spike (-6% 1h, +3567% 6h) | not scored |
| [HYGG](https://pump.fun/coin/HHoDt9mEET28qFFWtUPNTqGcmRQPh3TJChAWHmBopump) | `HHoDt9mEET28qFFWtUPNTqGcmRQPh3TJChAWHmBopump` | $44.7k | $392.3k | +9% | +1259% | +1259% | 10.9x | thin liq $44.7k; spike (+9% 1h, +1259% 6h) | not scored |
| [ニャジラ](https://pump.fun/coin/4qyk1uJexNRNUwfx9J4KKoJ1v5icmZNci42yDzgEpump) | `4qyk1uJexNRNUwfx9J4KKoJ1v5icmZNci42yDzgEpump` | $37.9k | $255.2k | +98% | +882% | +882% | 22.6x | thin liq $37.9k; spike (+98% 1h, +882% 6h) | not scored |
| [DOJE](https://pump.fun/coin/7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump) | `7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump` | $38.9k | $296.0k | +19% | +779% | +779% | 12.8x | thin liq $38.9k; spike (+19% 1h, +779% 6h) | not scored |
| [upcat](https://pump.fun/coin/fQKg71WHx88YaQT8xVM1nMSsTZTz8HkwaK2qAcwpump) | `fQKg71WHx88YaQT8xVM1nMSsTZTz8HkwaK2qAcwpump` | $19.4k | $80.0k | +163% | +163% | +163% | 6.7x | thin liq $19.4k; spike (+163% 1h, +163% 6h); < 1h old | not scored |
| [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $83.8k | $564.8k | -17% | +21% | +884% | 42.1x | churn 42x vol/liq | 55 |

_Timing: total 153s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 80.1s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/127; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
