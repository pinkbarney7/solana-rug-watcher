# Last scan 2026-11-20T13:04:07Z - mode: helius (box heartbeat stale (4256 min); budget 0/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 113 with pair data; 29 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored ANT in 78s
[fast_scan] scored SWJ in 86s
[fast_scan] scored MACCA in 87s
[fast_scan] scored LOOSY in 88s
[fast_scan] scored pippin in 88s
[fast_scan] scored FIONA in 89s
[fast_scan] scored ZEC in 89s
[fast_scan] scored SHIT in 90s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-20 13:03 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,601 (-3.5% 24h), ETH $1,741 (-3.5% 24h), SOL $71.24 (-4.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -6.8% (mcap $1.89B, vol $365.70M), pump-fun -5.0% (mcap $788.58M, vol $154.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [SHIT](https://pump.fun/coin/Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump) | `Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump` | $82.7k | $994.6k | 2.6 d | h24 -23% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $342.6k | $2.22M | 2.8 d | h24 +409% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [MACCA](https://dexscreener.com/solana/C5eGEXJZYvXEbKdyvPtasksjGNV4xvMowpKM92bVv47f) | `C5eGEXJZYvXEbKdyvPtasksjGNV4xvMowpKM92bVv47f` | $51.7k | $911.5k | 20.7 h | h24 +123233% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.7% (+5.2) |
| 59* | SKIP | [SWJ](https://pump.fun/coin/gHZhqEnFnitWCJ1MA2i9BzqTReFMhsGmbdL17xypump) | `gHZhqEnFnitWCJ1MA2i9BzqTReFMhsGmbdL17xypump` | $64.2k | $787.9k | 22.0 h | h24 +732% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [LOOSY](https://pump.fun/coin/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump) | `HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump` | $102.9k | $1.94M | 12.0 h | h24 +4771% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.3% (+5.6) |
| 66* | SKIP | [ANT](https://dexscreener.com/solana/ANTBTZQ1EUuTxUs3tfeampxdqTWPHmwyJmcWj4xoAyNe) | `ANTBTZQ1EUuTxUs3tfeampxdqTWPHmwyJmcWj4xoAyNe` | $6.42M | $1.34M | 15.6 d | h24 -10% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.39M | $8.21M | 666.5 d | h24 +26% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.1% in 9h (now 345,156) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.48M | $18.99M | 740.7 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.1% in 9h (now 182,875) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.35M | $19.9k | 400.8 d | h24 -15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 9h (now 392,269) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MACCA](https://dexscreener.com/solana/C5eGEXJZYvXEbKdyvPtasksjGNV4xvMowpKM92bVv47f) | `C5eGEXJZYvXEbKdyvPtasksjGNV4xvMowpKM92bVv47f` | $51.7k | $910.0k | +14% | +97% | +123033% | 3.8x | none flagged (still high risk) | 59 |
| [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $134.7k | $2.21M | -16% | +31% | +6991% | 70.8x | churn 71x vol/liq | 45 |
| [LOOSY](https://pump.fun/coin/HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump) | `HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump` | $102.3k | $1.92M | +16% | +64% | +4715% | 15.2x | none flagged (still high risk) | 60 |
| [XMR](https://dexscreener.com/solana/Bz9A2ZzXbR1QfWEaQTbdW37JN6VdSnFqCGsA3T6LENyt) | `Bz9A2ZzXbR1QfWEaQTbdW37JN6VdSnFqCGsA3T6LENyt` | $34.8k | $41.3k | +462% | +462% | +462% | 11.2x | thin liq $34.8k; spike (+462% 1h, +462% 6h); < 1h old | not scored |
| [AMC ](https://pump.fun/coin/J7bLsZcpkfky92ir8k36Munz91nHKtcDNhDy8d3Qpump) | `J7bLsZcpkfky92ir8k36Munz91nHKtcDNhDy8d3Qpump` | $41.1k | $202.3k | -30% | +378% | +378% | 24.6x | thin liq $41.1k; spike (-30% 1h, +378% 6h) | not scored |
| [SWJ](https://pump.fun/coin/gHZhqEnFnitWCJ1MA2i9BzqTReFMhsGmbdL17xypump) | `gHZhqEnFnitWCJ1MA2i9BzqTReFMhsGmbdL17xypump` | $64.2k | $787.9k | +26% | +23% | +732% | 12.4x | none flagged (still high risk) | 59 |

_Timing: total 224s (discovery 71.4s, screen 1.2s, GT prime 0.6s, scoring 150.5s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/179; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
