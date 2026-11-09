# Last scan 2026-11-09T12:27:13Z - mode: helius (box heartbeat stale (507 min); budget 120/3000)

```
[fast_scan] 109 candidate mints from 9 source tags; 107 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 72s
[fast_scan] scored ZEC in 80s
[fast_scan] scored NVDAx in 81s
[fast_scan] scored PUSSY in 81s
[fast_scan] scored ELYSION in 82s
[fast_scan] scored Elysion Pad in 82s
[fast_scan] scored BTC in 82s
[fast_scan] scored NVIDIH in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-09 12:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,586 (-1.7% 24h), ETH $2,120 (-5.2% 24h), SOL $86.48 (-3.4% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $2.48B, vol $386.20M), pump-fun -0.3% (mcap $994.09M, vol $130.20M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $59.9k | $527.8k | 2.0 d | h24 -25% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $80.0k | $991.8k | 12.3 h | h24 +2278% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 61* | SKIP | [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $68.4k | $347.9k | 1.9 d | h24 +381% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $51.3k | $404.5k | 11.7 h | h24 +835% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $512.2k | $2.74M | 16.1 h | h24 +2010% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 69* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $74.2k | $790.8k | 21.5 h | h24 +1442% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.23M | $29.55M | 105.8 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,827 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.23M | $30.0k | 389.8 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 387,870 (growth n/a: first sighting) |
| 75* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.39M | $38.70M | 500.1 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: authorities, rug-funder link; holders 398,763 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $433.7k | $8.48M | +285% | +13000% | +13000% | 0.1x | spike (+285% 1h, +13000% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $80.0k | $991.8k | +3% | +20% | +2278% | 13.7x | none flagged (still high risk) | 58 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $309.7k | $2.74M | +19% | +5% | +2011% | 28.8x | churn 29x vol/liq | 68 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $73.3k | $777.0k | -12% | -64% | +1415% | 59.2x | churn 59x vol/liq | 69 |
| [BANK](https://pump.fun/coin/HA9JHZn8S8VhtGtHtQcDVoLFBAssFPce9VthA2Pgpump) | `HA9JHZn8S8VhtGtHtQcDVoLFBAssFPce9VthA2Pgpump` | $34.9k | $150.5k | +223% | +223% | +223% | 9.0x | thin liq $34.9k; spike (+223% 1h, +223% 6h); < 1h old | not scored |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $51.3k | $404.5k | -5% | -44% | +835% | 31.3x | churn 31x vol/liq | 66 |

_Timing: total 217s (discovery 71.7s, screen 1.1s, GT prime 0.4s, scoring 143.6s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/158; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
