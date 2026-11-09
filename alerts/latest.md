# Last scan 2026-11-09T11:56:13Z - mode: helius (box heartbeat stale (476 min); budget 120/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 110 with pair data; 25 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 78s
[fast_scan] scored ELYSION in 87s
[fast_scan] scored BTC in 88s
[fast_scan] scored ZEC in 88s
[fast_scan] scored USDG in 89s
[fast_scan] scored PUSSY in 89s
[fast_scan] scored NVIDIH in 89s
[fast_scan] scored Elysion Pad in 92s
[fast_scan] scored NVDAx in 72s
# Market scan 2026-11-09 11:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,451 (-1.9% 24h), ETH $2,117 (-5.4% 24h), SOL $86.13 (-3.8% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.4% (mcap $2.46B, vol $381.35M), pump-fun -0.7% (mcap $990.43M, vol $129.25M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | CAUTION | [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $66.2k | $388.3k | 1.9 d | h24 +395% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 55* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $59.5k | $523.3k | 1.9 d | h24 -15% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.4k | $959.4k | 11.7 h | h24 +2201% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $56.3k | $488.5k | 11.2 h | h24 +1030% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $499.0k | $2.47M | 15.6 h | h24 +1802% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 70* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $79.9k | $921.6k | 20.9 h | h24 +1697% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 75* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.38M | $39.15M | 500.1 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: authorities, rug-funder link; holders 398,763 (growth n/a: first sighting) |
| 80* | SKIP | [USDG](https://dexscreener.com/solana/2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH) | `2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH` | $25.40M | $10.75M | 619.9 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 1,000,000 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.17M | $29.8k | 389.8 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,657 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $266.1k | $3.94M | +514% | +5997% | +5997% | 0.0x | spike (+514% 1h, +5997% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.4k | $959.4k | -16% | +33% | +2201% | 13.5x | none flagged (still high risk) | 58 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $79.7k | $921.6k | -23% | -50% | +1697% | 53.7x | churn 54x vol/liq | 70 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $295.2k | $2.47M | +15% | -12% | +1802% | 30.0x | churn 30x vol/liq | 68 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $56.3k | $488.5k | +13% | -49% | +1030% | 27.8x | churn 28x vol/liq | 66 |
| [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $58.4k | $388.3k | +36% | +88% | +395% | 13.0x | none flagged (still high risk) | 50 |

_Timing: total 224s (discovery 72.0s, screen 1.1s, GT prime 0.4s, scoring 150.4s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/165; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
