# Last scan 2026-11-09T09:53:03Z - mode: helius (box heartbeat stale (354 min); budget 70/3000)

```
[fast_scan] 111 candidate mints from 9 source tags; 109 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored CHILL in 72s
[fast_scan] scored ELYSION in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored 0DAY in 82s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored Fartcoin  in 83s
[fast_scan] scored BTC in 93s
# Market scan 2026-11-09 09:53 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,152 (-2.3% 24h), ETH $2,106 (-5.8% 24h), SOL $86.43 (-3.1% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.3% (mcap $2.45B, vol $375.94M), pump-fun -1.0% (mcap $983.60M, vol $132.03M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 31* | CAUTION | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $66.2k | $662.0k | 2.8 d | h24 +117% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 44* | CAUTION | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $75.9k | $842.3k | 1.9 d | h24 +31% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 54* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $69.4k | $806.5k | 2.7 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 70* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.2k | $959.5k | 9.7 h | h24 +2201% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 70* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $96.9k | $1.35M | 18.9 h | h24 +2541% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.25M | $28.80M | 105.7 d | h24 -5% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 425,849 (growth n/a: first sighting) |
| 69* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $7.35M | $113.91M | 752.2 d | h24 -3% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 587,313 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.47M | $39.10M | 500.0 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,696 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [fomo](https://pump.fun/coin/6DQDkup63CskftSsWMVDYo2hzdjjhyLdK4zLir4xpump) | `6DQDkup63CskftSsWMVDYo2hzdjjhyLdK4zLir4xpump` | $56.2k | $533.4k | +214% | +1409% | +1409% | 2.1x | spike (+214% 1h, +1409% 6h) | not scored |
| [BEEPZ](https://dexscreener.com/solana/87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab) | `87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab` | $97.3k | $86.3k | +15% | +958% | +958% | 154.4x | churn 154x vol/liq; spike (+15% 1h, +958% 6h) | not scored |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $96.7k | $1.35M | -12% | -46% | +2541% | 42.5x | churn 42x vol/liq | 70 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.2k | $959.5k | -18% | +7% | +2201% | 11.5x | none flagged (still high risk) | 70 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $49.0k | $374.6k | -19% | -47% | +766% | 29.7x | thin liq $49.0k; churn 30x vol/liq | not scored |
| [BUIDL](https://dexscreener.com/solana/8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2) | `8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2` | $31.6k | $99.6k | +25% | +178% | +178% | 18.5x | thin liq $31.6k | not scored |

_Timing: total 166s (discovery 71.9s, screen 1.1s, GT prime 0.4s, scoring 93.0s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/152; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
