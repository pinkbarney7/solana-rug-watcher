# Last scan 2026-11-09T08:47:29Z - mode: helius (box heartbeat stale (287 min); budget 30/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored 0DAY in 80s
[fast_scan] scored CHILL in 87s
[fast_scan] scored PUSSY in 87s
[fast_scan] scored BAWSAQ in 87s
[fast_scan] scored NVDAx in 89s
[fast_scan] scored BTC in 89s
[fast_scan] scored CATE in 89s
[fast_scan] scored ELYSION in 89s
[fast_scan] scored OTC in 72s
# Market scan 2026-11-09 08:47 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,187 (-2.2% 24h), ETH $2,108 (-5.7% 24h), SOL $86.30 (-3.2% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.0% (mcap $2.43B, vol $365.40M), pump-fun -1.6% (mcap $974.99M, vol $130.33M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $70.7k | $755.5k | 2.8 d | h24 +106% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 54* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $69.3k | $806.5k | 2.6 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 55* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $447.3k | $2.18M | 12.4 h | h24 +1578% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $74.2k | $808.5k | 1.8 d | h24 +48% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |
| 70* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $82.9k | $1.08M | 8.6 h | h24 +2489% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $108.6k | $1.70M | 17.8 h | h24 +3222% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [OTC](https://pump.fun/coin/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | `MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump` | $597.0k | $3.81M | 72.8 d | h24 -25% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 63,892 (growth n/a: first sighting) |
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.25M | $29.04M | 105.7 d | h24 -5% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders 425,839 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.49M | $39.29M | 499.9 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,793 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $108.0k | $1.69M | -28% | -37% | +3200% | 37.1x | churn 37x vol/liq | 71 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $82.9k | $1.08M | +8% | +42% | +2489% | 10.0x | none flagged (still high risk) | 70 |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $277.6k | $2.18M | -18% | -1% | +1578% | 31.3x | churn 31x vol/liq | 55 |
| [BTC](https://dexscreener.com/solana/Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1) | `Big1krPP8QUkgg5fsfEZQmeuwAViNajzAxNhNYvXaSS1` | $33.4k | $151.2k | +185% | +236% | +236% | 5.2x | thin liq $33.4k; spike (+185% 1h, +236% 6h) | not scored |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $52.7k | $433.3k | -15% | -29% | +902% | 26.5x | churn 27x vol/liq | not scored |
| [BUIDL](https://dexscreener.com/solana/8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2) | `8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2` | $31.6k | $101.2k | -24% | +183% | +183% | 17.9x | thin liq $31.6k | not scored |

_Timing: total 225s (discovery 71.6s, screen 1.1s, GT prime 0.4s, scoring 151.8s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/163; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
