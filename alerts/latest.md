# Last scan 2026-11-09T08:15:51Z - mode: helius (box heartbeat stale (256 min); budget 10/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 110 with pair data; 24 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored 0DAY in 73s
[fast_scan] scored PUSSY in 80s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored CHILL in 81s
[fast_scan] scored ZEC in 82s
[fast_scan] scored BTC in 82s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored ELYSION in 83s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-09 08:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $73,818 (-2.7% 24h), ETH $2,092 (-6.4% 24h), SOL $85.63 (-3.9% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.9% (mcap $2.40B, vol $370.63M), pump-fun -2.5% (mcap $966.52M, vol $127.02M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $70.7k | $763.0k | 2.7 d | h24 +68% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 55* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $438.9k | $2.13M | 11.9 h | h24 +1541% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $74.1k | $813.4k | 1.8 d | h24 +61% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $67.9k | $782.5k | 2.6 d | h24 +3% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 70* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $79.6k | $1.01M | 8.1 h | h24 +2316% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $131.1k | $2.50M | 17.3 h | h24 +4782% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.23M | $28.73M | 105.7 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,838 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.08M | $29.3k | 389.6 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 387,738 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.47M | $38.97M | 499.9 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,752 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $130.9k | $2.50M | +15% | -8% | +4782% | 30.1x | churn 30x vol/liq | 71 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $79.6k | $1.01M | +12% | +60% | +2316% | 10.1x | none flagged (still high risk) | 70 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $274.1k | $2.15M | -18% | -10% | +1555% | 31.5x | churn 32x vol/liq | 55 |
| [牛逼](https://pump.fun/coin/e2GPNPFQ3b12UEbfwLNcARFdu3jZoPnjDUMTbsnpump) | `e2GPNPFQ3b12UEbfwLNcARFdu3jZoPnjDUMTbsnpump` | $24.3k | $110.2k | +210% | +210% | +210% | 0.2x | thin liq $24.3k; spike (+210% 1h, +210% 6h); < 1h old | not scored |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $53.9k | $456.6k | -5% | -5% | +956% | 25.4x | churn 25x vol/liq | not scored |
| [BTC](https://dexscreener.com/solana/Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1) | `Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1` | $24.8k | $91.3k | +96% | +96% | +96% | 4.3x | thin liq $24.8k; < 1h old | not scored |

_Timing: total 218s (discovery 71.6s, screen 1.1s, GT prime 0.5s, scoring 144.8s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/164; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
