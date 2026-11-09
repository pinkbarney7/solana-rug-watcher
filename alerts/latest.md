# Last scan 2026-11-09T16:08:40Z - mode: helius (box heartbeat stale (25 min); budget 140/3000)

```
[fast_scan] 112 candidate mints from 9 source tags; 110 with pair data; 26 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored NVDAx in 68s
[fast_scan] scored SPCX in 76s
[fast_scan] scored ZEC in 77s
[fast_scan] scored MYWAY in 77s
# Market scan 2026-11-09 16:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $75,342 (-0.9% 24h), ETH $2,144 (-4.3% 24h), SOL $87.69 (-2.2% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.2% (mcap $2.52B, vol $415.08M), pump-fun +1.1% (mcap $1.00B, vol $138.26M)

## Cleanest on real liquidity (younger than 3 days)
Top 1 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 37* | CAUTION | [MYWAY](https://pump.fun/coin/tx41eAXzN6jHH22LSgF7eSxpTNvJXwcbrcGsbDrpump) | `tx41eAXzN6jHH22LSgF7eSxpTNvJXwcbrcGsbDrpump` | $63.2k | $612.7k | 1.1 d | h24 +141% | #8 Turnover / bot pattern WARN (+4); #11 not checked (+3); #12 not checked (+3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.67M | $14.18M | 166.3 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 343,021 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $10.26M | $29.9k | 390.0 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders -0.0% in 3h (now 387,773) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.53M | $38.99M | 500.2 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.1% in 3h (now 398,911) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $441.1k | $8.80M | -10% | +6383% | +13499% | 0.1x | spike (-10% 1h, +6383% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump) | `H2ZViwA4dwxHd3bctARCUDUqTwTqfVrbmKQMrwBmpump` | $89.1k | $1.19M | +164% | +43% | +2762% | 15.3x | spike (+164% 1h, +43% 6h) | not scored |
| [NVIDIH](https://pump.fun/coin/3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump) | `3mPaWq3s4MoF7mXLHPo3N9ueRjG4oRQVPqnHTJLkpump` | $31.9k | $156.2k | +18% | -60% | +261% | 57.9x | thin liq $31.9k; churn 58x vol/liq | not scored |
| [AMD](https://pump.fun/coin/DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump) | `DDmGnuvroxVrb7CSyjYcezFU8gnAfhKasg4ZZezmpump` | $65.6k | $321.0k | +40% | +182% | +38% | 6.2x | none flagged (still high risk) | not scored |
| [ELYSION](https://pump.fun/coin/AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump) | `AWaBBNoVuwQ22B8Y5nEtLne2uEfk8UaYEFws7vT7pump` | $28.7k | $123.3k | -25% | -91% | -93% | 106.2x | thin liq $28.7k; churn 106x vol/liq; dumping -93% 24h | not scored |
| [MAX](https://dexscreener.com/solana/2WznTTxHejRYZWMfUBv349StrMiwaTZeaEPmtzXfLoat) | `2WznTTxHejRYZWMfUBv349StrMiwaTZeaEPmtzXfLoat` | $45.1k | $46.2k | -69% | -69% | -69% | 23.1x | thin liq $45.1k; dumping -69% 24h; < 1h old | not scored |

_Timing: total 151s (discovery 72.0s, screen 1.1s, GT prime 0.4s, scoring 77.1s for 4 coins, 4 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 4/90; Helius 429s 60; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
