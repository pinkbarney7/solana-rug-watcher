# Last scan 2026-11-09T09:38:14Z - mode: helius (box heartbeat stale (338 min); budget 60/3000)

```
[fast_scan] 114 candidate mints from 10 source tags; 112 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored CHILL in 72s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored ELYSION in 82s
[fast_scan] scored 0DAY in 82s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored NVIDIH in 83s
[fast_scan] scored BTC in 86s
[fast_scan] scored Fartcoin  in 73s
# Market scan 2026-11-09 09:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,238 (-2.1% 24h), ETH $2,108 (-5.6% 24h), SOL $86.70 (-2.8% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.2% (mcap $2.44B, vol $372.59M), pump-fun -1.1% (mcap $982.43M, vol $131.52M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 43* | CAUTION | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $74.1k | $802.4k | 1.8 d | h24 +33% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 54* | SKIP | [CHILL](https://pump.fun/coin/9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump) | `9RZeokzHNXoRyJkWDFdvcQTAzUhKpXm7RrqkUM3Fpump` | $69.4k | $806.9k | 2.7 d | h24 +14% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 56* | SKIP | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $69.3k | $724.6k | 2.8 d | h24 +102% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $81.1k | $1.03M | 9.4 h | h24 +2365% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $50.4k | $394.4k | 8.9 h | h24 +812% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 70* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $89.0k | $1.14M | 18.6 h | h24 +2131% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 56* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $7.34M | $113.70M | 752.1 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 6.5% (+4.2); GATES FAILED: rug-funder link; holders 587,317 (growth n/a: first sighting) |
| 66* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.26M | $8.70M | 750.9 d | h24 -19% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link, exit test; holders 136,086 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.47M | $38.97M | 500.0 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,696 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BEEPZ](https://dexscreener.com/solana/87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab) | `87w7DHmnbAoB1t7VtR33Fy4bUbJu3R82w7g8mENyBtab` | $93.2k | $85.6k | +39% | +949% | +949% | 144.7x | churn 145x vol/liq; spike (+39% 1h, +949% 6h) | not scored |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $88.8k | $1.14M | -41% | -56% | +2131% | 46.0x | churn 46x vol/liq | 70 |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $81.0k | $1.03M | -7% | +45% | +2362% | 10.9x | none flagged (still high risk) | 58 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $50.4k | $394.4k | -12% | -41% | +812% | 28.6x | churn 29x vol/liq | 66 |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $22.9k | $92.0k | +74% | +166% | +166% | 6.5x | thin liq $22.9k | not scored |
| [BUIDL](https://dexscreener.com/solana/8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2) | `8MuTFfgeFCYa7BKMkKzRbxPLjgdEZFfHtNM2XWSfdtH2` | $30.8k | $93.7k | -10% | +162% | +162% | 18.9x | thin liq $30.8k | not scored |

_Timing: total 218s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 145.0s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/165; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
