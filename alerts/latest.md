# Last scan 2026-11-09T09:18:36Z - mode: helius (box heartbeat stale (320 min); budget 40/3000)

```
[fast_scan] 114 candidate mints from 9 source tags; 112 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored BTC in 80s
[fast_scan] scored BAWSAQ in 87s
[fast_scan] scored CHILL in 87s
[fast_scan] scored NVDAx in 87s
[fast_scan] scored ERA in 88s
[fast_scan] scored 0DAY in 89s
[fast_scan] scored ELYSION in 89s
[fast_scan] scored Fartcoin  in 89s
# Market scan 2026-11-09 09:18 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,387 (-1.9% 24h), ETH $2,117 (-5.2% 24h), SOL $86.72 (-2.7% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.0% (mcap $2.45B, vol $380.69M), pump-fun -0.9% (mcap $984.00M, vol $133.53M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 43* | CAUTION | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $71.7k | $752.2k | 1.8 d | h24 +26% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $69.2k | $719.5k | 2.8 d | h24 +93% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $81.9k | $1.05M | 9.1 h | h24 +2412% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $68.8k | $792.5k | 2.7 d | h24 +9% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 70* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $93.7k | $1.27M | 18.3 h | h24 +2373% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [ERA](https://dexscreener.com/solana/2fthhjkV9nmezZCPgpx1w4SRW2fZSASe7fpDhfpLpatr) | `2fthhjkV9nmezZCPgpx1w4SRW2fZSASe7fpDhfpLpatr` | $102.49M | $102.70M | 110.8 d | h24 -0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 33 (growth n/a: first sighting) |
| 69* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $7.35M | $113.64M | 752.1 d | h24 -3% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 587,317 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.49M | $39.23M | 500.0 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,696 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BEEPZ](https://dexscreener.com/solana/87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab) | `87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab` | $87.8k | $83.9k | +82% | +927% | +927% | 133.9x | churn 134x vol/liq; spike (+82% 1h, +927% 6h) | not scored |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $93.5k | $1.27M | -53% | -48% | +2373% | 43.4x | churn 43x vol/liq | 70 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $82.5k | $1.06M | -1% | +41% | +2451% | 10.6x | none flagged (still high risk) | 58 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $49.9k | $387.2k | -14% | -39% | +795% | 28.6x | thin liq $49.9k; churn 29x vol/liq | not scored |
| [BUIDL](https://dexscreener.com/solana/8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2) | `8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2` | $32.0k | $102.8k | +16% | +187% | +187% | 18.0x | thin liq $32.0k | not scored |
| [GPU](https://pump.fun/coin/EFYdWBh6hQJLduR4QYnLNKLMq93PLqjjU5WwhNPgpump) | `EFYdWBh6hQJLduR4QYnLNKLMq93PLqjjU5WwhNPgpump` | $14.6k | $31.3k | +87% | -27% | -27% | 49.0x | thin liq $14.6k; churn 49x vol/liq | not scored |

_Timing: total 162s (discovery 71.6s, screen 1.2s, GT prime 0.5s, scoring 89.0s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/149; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
