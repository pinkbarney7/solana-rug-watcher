# Last scan 2026-11-15T07:19:54Z - mode: helius (box heartbeat stale (6841 min); budget 0/3000)

```
[fast_scan] 134 candidate mints from 10 source tags; 133 with pair data; 22 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored CATE in 70s
[fast_scan] scored XTO in 78s
[fast_scan] scored TTWO in 78s
[fast_scan] scored Fartcoin  in 79s
[fast_scan] scored bill in 79s
[fast_scan] scored UODF in 79s
# Market scan 2026-11-15 07:19 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,398 (-4.4% 24h), ETH $1,791 (-5.8% 24h), SOL $70.27 (-6.9% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -8.8% (mcap $2.05B, vol $541.15M), pump-fun -1.7% (mcap $862.53M, vol $134.22M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $164.6k | $718.9k | 11.6 h | h24 +1152% | #9 Price momentum FAIL (+14); #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.04M | $217.22M | 2.8 d | h24 +7% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $1.10M | $244.73M | 1.7 d | h24 +106% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $16.70M | 111.6 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 2h (now 429,421) |
| 56* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $5.91M | $91.35M | 758.1 d | h24 -12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 6.5% (+4.2); GATES FAILED: rug-funder link; holders -0.0% in 141h (now 587,275) |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.02M | $98 | 104.3 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.6% in 11h (now 257,536) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WANTED](https://pump.fun/coin/CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump) | `CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump` | $83.4k | $1.34M | -4% | +3501% | +3501% | 12.1x | spike (-4% 1h, +3501% 6h) | not scored |
| [ZORPO](https://dexscreener.com/solana/M2ZHyvfdmCXpZFie1pVYkNPmXzibyGktKurDBzYWrYn) | `M2ZHyvfdmCXpZFie1pVYkNPmXzibyGktKurDBzYWrYn` | $60.7k | $91.0k | +37% | +1237% | +1237% | 220.0x | churn 220x vol/liq; spike (+37% 1h, +1237% 6h) | not scored |
| [TAIL](https://pump.fun/coin/2tHPtosmh76mmJHeskid7nYUeHjGUQ4ZAYChwdGJpump) | `2tHPtosmh76mmJHeskid7nYUeHjGUQ4ZAYChwdGJpump` | $17.3k | $65.2k | +392% | +142% | +142% | 10.7x | thin liq $17.3k; spike (+392% 1h, +142% 6h) | not scored |
| [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $96.1k | $726.7k | -9% | +53% | +1166% | 41.2x | churn 41x vol/liq | 59 |
| [HYGG](https://pump.fun/coin/HHoDt9mEET28qFFWtUPNTqGcmRQPh3TJChAWHmBopump) | `HHoDt9mEET28qFFWtUPNTqGcmRQPh3TJChAWHmBopump` | $44.1k | $385.7k | -13% | -6% | +1236% | 11.6x | thin liq $44.1k | not scored |
| [DOJE](https://pump.fun/coin/7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump) | `7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump` | $41.3k | $331.9k | -12% | +67% | +885% | 15.1x | thin liq $41.3k | not scored |

_Timing: total 152s (discovery 71.0s, screen 1.3s, GT prime 0.3s, scoring 79.3s for 6 coins, 6 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 6/122; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
