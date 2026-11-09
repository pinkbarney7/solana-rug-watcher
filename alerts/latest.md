# Last scan 2026-11-09T10:42:16Z - mode: helius (box heartbeat stale (402 min); budget 90/3000)

```
[fast_scan] 109 candidate mints from 9 source tags; 104 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored ZEC in 72s
[fast_scan] scored ELYSION in 81s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored PUSSY in 82s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored BTC in 94s
[fast_scan] scored 0DAY in 101s
[fast_scan] scored Elysion Pad in 103s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-09 10:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,053 (-2.3% 24h), ETH $2,102 (-5.8% 24h), SOL $85.90 (-3.5% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.4% (mcap $2.45B, vol $378.62M), pump-fun -0.9% (mcap $982.75M, vol $132.34M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | SKIP | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $67.2k | $685.8k | 2.9 d | h24 +106% | sellability gate: Jupiter exit test FAIL: $25: no sell route (HTTP 429); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3) |
| 43* | CAUTION | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $71.2k | $747.8k | 1.9 d | h24 +32% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | SKIP | [Elysion Pad](https://pump.fun/coin/HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump) | `HW2Sz6nNonYCfD59Ng5AeV1xtuU43xu7oktb2PPfpump` | $57.4k | $302.1k | 1.8 d | h24 +224% | sellability gate: Jupiter exit test FAIL: $25: no buy route (HTTP 429); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 55* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $453.1k | $2.17M | 14.3 h | h24 +1570% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $89.6k | $1.26M | 10.5 h | h24 +2913% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $88.1k | $1.13M | 19.7 h | h24 +2095% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.24M | $28.77M | 105.8 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,824 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.14M | $29.6k | 389.7 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 2h (now 387,668) |
| 75* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.46M | $39.32M | 500.0 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: authorities, rug-funder link; holders 398,699 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $64.6k | $362.6k | +461% | +461% | +461% | 0.0x | spike (+461% 1h, +461% 6h); < 1h old | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $89.4k | $1.25M | +24% | +80% | +2897% | 10.8x | none flagged (still high risk) | 58 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $87.9k | $1.13M | -8% | -45% | +2095% | 47.6x | churn 48x vol/liq | 58 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $277.3k | $2.16M | -9% | -20% | +1565% | 31.6x | churn 32x vol/liq | 55 |
| [Scronty ](https://pump.fun/coin/DRQq4oSMeNENScmriRvyGVnm368jr7NJhrRdUZLApump) | `DRQq4oSMeNENScmriRvyGVnm368jr7NJhrRdUZLApump` | $12.6k | $25.3k | +304% | -43% | -43% | 8.7x | thin liq $12.6k; spike (+304% 1h, -43% 6h) | not scored |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $51.1k | $406.0k | +5% | -55% | +839% | 29.5x | churn 30x vol/liq; spike (+5% 1h, -55% 6h) | not scored |

_Timing: total 217s (discovery 71.6s, screen 1.1s, GT prime 0.4s, scoring 143.5s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/183; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
