# Last scan 2026-11-09T12:40:35Z - mode: helius (box heartbeat stale (521 min); budget 120/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 72s
[fast_scan] scored PUSSY in 81s
[fast_scan] scored ELYSION in 82s
[fast_scan] scored ZEC in 83s
[fast_scan] scored CATE in 83s
[fast_scan] scored NVDAx in 83s
[fast_scan] scored BTC in 96s
[fast_scan] scored Elysion Pad in 96s
# Market scan 2026-11-09 12:40 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,835 (-1.4% 24h), ETH $2,123 (-5.1% 24h), SOL $86.74 (-3.1% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $2.49B, vol $393.04M), pump-fun +0.5% (mcap $998.21M, vol $134.62M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 37* | CAUTION | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $59.0k | $512.0k | 2.0 d | h24 -33% | #8 Turnover / bot pattern WARN (+4); #11 not checked (+3); #12 not checked (+3) |
| 50* | CAUTION | [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $71.0k | $383.6k | 1.9 d | h24 +452% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.0k | $940.7k | 12.5 h | h24 +2156% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 66* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $68.0k | $663.4k | 21.7 h | h24 +1194% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $507.1k | $2.69M | 16.3 h | h24 +1972% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.29M | $29.93M | 105.8 d | h24 -2% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 425,826 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.24M | $30.0k | 389.8 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,870 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.36M | $38.81M | 500.1 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,592 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $388.0k | $7.55M | +218% | +11570% | +11570% | 0.1x | spike (+218% 1h, +11570% 6h) | not scored |
| [BARRON](https://pump.fun/coin/Aj1udanfFv76FYeg8yALhuUvAgAiFvHkwtRfjrFUpump) | `Aj1udanfFv76FYeg8yALhuUvAgAiFvHkwtRfjrFUpump` | $35.4k | $219.3k | +520% | +520% | +520% | 1.9x | thin liq $35.4k; spike (+520% 1h, +520% 6h); < 1h old | not scored |
| [FULL](https://dexscreener.com/solana/5JwrZF3CKazZnhbtcN4nJr7bUKWVidXtkkT73fj7wR9F) | `5JwrZF3CKazZnhbtcN4nJr7bUKWVidXtkkT73fj7wR9F` | $78.4k | $76.1k | +164% | +819% | +819% | 122.6x | churn 123x vol/liq; spike (+164% 1h, +819% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.0k | $940.7k | +7% | +4% | +2156% | 14.2x | none flagged (still high risk) | 58 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $307.7k | $2.70M | -2% | +0% | +1982% | 29.0x | churn 29x vol/liq | 68 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $67.7k | $663.4k | -16% | -71% | +1194% | 64.4x | churn 64x vol/liq | 66 |

_Timing: total 170s (discovery 71.6s, screen 1.2s, GT prime 0.4s, scoring 96.3s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/152; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
