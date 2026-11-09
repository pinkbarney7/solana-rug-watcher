# Last scan 2026-11-09T12:09:30Z - mode: helius (box heartbeat stale (489 min); budget 120/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 112 with pair data; 30 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Elysion Pad in 80s
[fast_scan] scored NVDAx in 86s
[fast_scan] scored CATE in 87s
[fast_scan] scored ELYSION in 87s
[fast_scan] scored BAWSAQ in 88s
[fast_scan] scored BTC in 88s
[fast_scan] scored NVIDIH in 88s
[fast_scan] scored PUSSY in 89s
[fast_scan] scored OTC in 72s
# Market scan 2026-11-09 12:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,326 (-2.1% 24h), ETH $2,112 (-5.7% 24h), SOL $86.09 (-4.0% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.6% (mcap $2.46B, vol $385.73M), pump-fun -1.0% (mcap $987.48M, vol $131.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | CAUTION | [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $70.0k | $392.7k | 1.9 d | h24 +408% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 55* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $58.5k | $507.2k | 2.0 d | h24 -22% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $51.5k | $409.7k | 11.4 h | h24 +847% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $512.7k | $2.70M | 15.8 h | h24 +1978% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 69* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $70.6k | $721.3k | 21.2 h | h24 +1306% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 70* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.2k | $953.9k | 12.0 h | h24 +2187% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [OTC](https://pump.fun/coin/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | `MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump` | $606.6k | $3.79M | 72.9 d | h24 -26% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 63,883) |
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.26M | $29.43M | 105.8 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,827 (growth n/a: first sighting) |
| 75* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.35M | $38.79M | 500.1 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: authorities, rug-funder link; holders 398,763 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [NADF](https://pump.fun/coin/mBhCpHkVei7zgYQngY1ok36zGSqmzDFgiqwxjjTpump) | `mBhCpHkVei7zgYQngY1ok36zGSqmzDFgiqwxjjTpump` | $232.1k | $8.99M | +25052% | +25052% | +25052% | 0.5x | liq/mcap 2.6%; spike (+25052% 1h, +25052% 6h); lopsided buys/sells 59.50; < 1h old | not scored |
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $355.0k | $6.37M | +680% | +9745% | +9745% | 0.0x | spike (+680% 1h, +9745% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.2k | $953.9k | -4% | +12% | +2187% | 13.7x | none flagged (still high risk) | 70 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $309.3k | $2.72M | +25% | -2% | +1992% | 28.8x | churn 29x vol/liq | 68 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $70.3k | $721.3k | -36% | -64% | +1306% | 61.1x | churn 61x vol/liq | 69 |
| [BANK](https://pump.fun/coin/HA9JHZn8S8VhtGtHtQcDVoLFBAssFPce9VthA2Pgpump) | `HA9JHZn8S8VhtGtHtQcDVoLFBAssFPce9VthA2Pgpump` | $30.0k | $122.8k | +154% | +154% | +154% | 5.8x | thin liq $30.0k; spike (+154% 1h, +154% 6h); < 1h old | not scored |

_Timing: total 224s (discovery 71.8s, screen 1.1s, GT prime 0.3s, scoring 151.1s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/163; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
