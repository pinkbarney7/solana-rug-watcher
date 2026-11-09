# Last scan 2026-11-09T11:09:30Z - mode: helius (box heartbeat stale (429 min); budget 90/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 115 with pair data; 31 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored 0DAY in 80s
[fast_scan] scored ELYSION in 86s
[fast_scan] scored CATE in 87s
[fast_scan] scored BTC in 87s
[fast_scan] scored Pepetide in 88s
[fast_scan] scored BAWSAQ in 88s
[fast_scan] scored NVDAx in 89s
[fast_scan] scored NVIDIH in 89s
[fast_scan] scored OTC in 72s
# Market scan 2026-11-09 11:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,094 (-2.3% 24h), ETH $2,106 (-5.7% 24h), SOL $85.87 (-3.6% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.6% (mcap $2.44B, vol $377.54M), pump-fun -1.1% (mcap $980.94M, vol $132.68M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [0DAY](https://pump.fun/coin/85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump) | `85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump` | $66.7k | $678.5k | 2.9 d | h24 +77% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 54* | SKIP | [Pepetide](https://dexscreener.com/solana/22JKmY9YZfnQfb3pGYb6hctL5Jyvv3zhL3nQ8oyNuoYp) | `22JKmY9YZfnQfb3pGYb6hctL5Jyvv3zhL3nQ8oyNuoYp` | $167.8k | $417.4k | 1.5 d | h24 +80% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #11 not checked (+3); #12 not checked (+3) |
| 58* | SKIP | [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $88.3k | $1.13M | 20.2 h | h24 +2106% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BTC](https://pump.fun/coin/CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump) | `CZRtwCDJy4cKNvtVwtgGqeEGzLnCDJdTkexgpEsMpump` | $68.0k | $682.9k | 1.9 d | h24 +19% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $53.1k | $437.2k | 10.4 h | h24 +911% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 70* | SKIP | [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $78.8k | $974.5k | 11.0 h | h24 +2237% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [OTC](https://pump.fun/coin/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | `MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump` | $604.3k | $3.80M | 72.9 d | h24 -25% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 2h (now 63,890) |
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.24M | $28.88M | 105.8 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 425,819 (growth n/a: first sighting) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.38M | $39.18M | 500.0 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 398,699 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $96.2k | $817.0k | +502% | +1163% | +1163% | 0.0x | spike (+502% 1h, +1163% 6h) | not scored |
| [GTA 6 Coin](https://pump.fun/coin/9X1X4ho3AYwxoGZZ3UDsbzH9j9UYFWVrPHuUmvUhpump) | `9X1X4ho3AYwxoGZZ3UDsbzH9j9UYFWVrPHuUmvUhpump` | $50.0k | $426.1k | +3% | +1101% | +1101% | 3.4x | spike (+3% 1h, +1101% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $79.6k | $994.5k | +19% | +34% | +2285% | 12.7x | none flagged (still high risk) | 70 |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $88.1k | $1.13M | -18% | -31% | +2106% | 47.7x | churn 48x vol/liq | 58 |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $53.1k | $437.2k | +16% | -43% | +911% | 28.8x | churn 29x vol/liq | 66 |
| [Steve](https://pump.fun/coin/5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump) | `5JHHcudrqibzuc4S9tGgthmfLNoRof4E3KWWGQsrpump` | $21.3k | $79.8k | +39% | +130% | +130% | 11.6x | thin liq $21.3k | not scored |

_Timing: total 224s (discovery 71.5s, screen 1.1s, GT prime 0.4s, scoring 151.4s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/164; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
