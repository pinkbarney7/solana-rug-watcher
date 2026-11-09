# Last scan 2026-11-09T08:38:49Z - mode: helius (box heartbeat stale (279 min); budget 20/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 27 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 72s
[fast_scan] scored PUSSY in 81s
[fast_scan] scored BTC in 81s
[fast_scan] scored ELYSION in 81s
[fast_scan] scored CHILL in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored NVDAx in 83s
[fast_scan] scored 0DAY in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-09 08:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,147 (-2.2% 24h), ETH $2,107 (-5.7% 24h), SOL $86.25 (-3.1% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.0% (mcap $2.43B, vol $365.40M), pump-fun -1.6% (mcap $974.99M, vol $130.33M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $451.1k | $2.14M | 12.3 h | h24 +1544% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $71.4k | $770.2k | 2.8 d | h24 +73% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3) |
| 56* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $83.9k | $1.11M | 8.5 h | h24 +2556% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $115.2k | $1.92M | 17.7 h | h24 +3646% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $73.4k | $791.3k | 1.8 d | h24 +41% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $68.6k | $790.1k | 2.6 d | h24 +8% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.25M | $28.98M | 105.7 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,839 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.18M | $29.8k | 389.7 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,715 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.49M | $39.17M | 499.9 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,793 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $115.0k | $1.92M | -15% | -29% | +3646% | 34.7x | churn 35x vol/liq | 59 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $83.0k | $1.08M | +23% | +48% | +2499% | 9.9x | none flagged (still high risk) | 56 |
| [BTC](https://dexscreener.com/solana/Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1) | `Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1` | $35.0k | $166.1k | +269% | +269% | +269% | 4.4x | thin liq $35.0k; spike (+269% 1h, +269% 6h); < 1h old | not scored |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $272.7k | $2.11M | -18% | -4% | +1523% | 31.9x | churn 32x vol/liq | 52 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $53.5k | $447.9k | -11% | -23% | +936% | 26.0x | churn 26x vol/liq | not scored |
| [OI](https://dexscreener.com/solana/BuNTjuiSXzJyppo3dSwQjfr6ssqBnZRi6tQsKvrxyDmV) | `BuNTjuiSXzJyppo3dSwQjfr6ssqBnZRi6tQsKvrxyDmV` | $21.1k | $16.4k | +142% | +142% | +142% | 7.4x | thin liq $21.1k; spike (+142% 1h, +142% 6h); lopsided buys/sells 3.01; < 1h old | not scored |

_Timing: total 217s (discovery 71.4s, screen 1.1s, GT prime 0.3s, scoring 144.0s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/158; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
