# Last scan 2026-11-09T09:05:26Z - mode: helius (box heartbeat stale (305 min); budget 40/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 113 with pair data; 28 >= $50,000 liq; 11 pass survivor pre-gates (74s)
[fast_scan] scored 0DAY in 74s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored NVDAx in 81s
[fast_scan] scored ELYSION in 82s
[fast_scan] scored CHILL in 82s
[fast_scan] scored BTC in 83s
[fast_scan] scored NVIDIH in 83s
[fast_scan] scored ZEC in 83s
[fast_scan] scored Fartcoin  in 73s
# Market scan 2026-11-09 09:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,489 (-1.8% 24h), ETH $2,121 (-5.2% 24h), SOL $86.87 (-2.6% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.4% (mcap $2.44B, vol $373.02M), pump-fun -1.3% (mcap $980.04M, vol $132.57M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $69.5k | $730.1k | 2.8 d | h24 +110% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $85.6k | $1.14M | 8.9 h | h24 +2640% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $93.2k | $1.25M | 18.1 h | h24 +2341% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $75.1k | $822.4k | 1.8 d | h24 +43% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $50.3k | $393.6k | 8.3 h | h24 +810% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $69.7k | $810.8k | 2.7 d | h24 +9% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $7.32M | $112.67M | 752.1 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 6.5% (+4.2); GATES FAILED: rug-funder link; holders 587,075 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.27M | $30.4k | 389.7 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,699 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.49M | $39.41M | 500.0 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,793 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BEEPZ](https://dexscreener.com/solana/87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab) | `87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab` | $81.4k | $79.1k | +122% | +869% | +869% | 123.9x | churn 124x vol/liq; spike (+122% 1h, +869% 6h) | not scored |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $94.1k | $1.28M | -49% | -60% | +2400% | 42.9x | churn 43x vol/liq | 58 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $85.6k | $1.14M | +12% | +43% | +2640% | 10.0x | none flagged (still high risk) | 58 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $50.3k | $393.6k | -22% | -33% | +810% | 28.1x | churn 28x vol/liq | 66 |
| [BTC](https://dexscreener.com/solana/Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1) | `Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1` | $29.4k | $118.7k | +57% | +164% | +164% | 6.6x | thin liq $29.4k | not scored |
| [BUIDL](https://dexscreener.com/solana/8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2) | `8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2` | $33.3k | $112.2k | +5% | +214% | +214% | 17.3x | thin liq $33.3k | not scored |

_Timing: total 220s (discovery 71.9s, screen 1.7s, GT prime 0.5s, scoring 146.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/163; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
