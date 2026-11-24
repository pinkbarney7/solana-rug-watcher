# Last scan 2026-11-24T21:25:46Z - mode: helius (box heartbeat stale (31 min); budget 514/3000)

```
[fast_scan] 116 candidate mints from 9 source tags; 115 with pair data; 23 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 74s
[fast_scan] scored CATE in 81s
[fast_scan] scored GROKIA in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored pippin in 83s
[fast_scan] scored DONJENSEN in 83s
[fast_scan] scored cateball in 84s
[fast_scan] scored MCAT in 85s
# Market scan 2026-11-24 21:25 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,878 (-2.2% 24h), ETH $1,680 (-2.3% 24h), SOL $69.40 (-4.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -6.0% (mcap $1.79B, vol $327.00M), pump-fun -7.1% (mcap $759.04M, vol $143.77M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $64.2k | $140.0k | 2.4 d | h24 -34% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $66.0k | $777.2k | 2.5 d | h24 +14% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $198.3k | $1.03M | 1.0 d | h24 +489% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $94.7k | $1.71M | 18.9 h | h24 +4692% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |
| 60* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $101.2k | $1.80M | 19.2 h | h24 +1548% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.97M | 121.2 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,865 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.44M | $18.94M | 745.0 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,572 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $3.56M | $12.98M | 181.6 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,464 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Flop](https://dexscreener.com/solana/DCSX5MxQRAYiXEn1X9XuXiHmq87Tza4rJNNL9ETXM65i) | `DCSX5MxQRAYiXEn1X9XuXiHmq87Tza4rJNNL9ETXM65i` | $100.1k | $277.0k | +4119% | +4119% | +4119% | 52.8x | churn 53x vol/liq; spike (+4119% 1h, +4119% 6h); < 1h old | not scored |
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $94.7k | $1.71M | -15% | -5% | +4692% | 19.5x | none flagged (still high risk) | 60 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $93.2k | $1.54M | -39% | -45% | +1310% | 30.9x | churn 31x vol/liq | 60 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $84.3k | $1.01M | +22% | +23% | +1208% | 40.4x | churn 40x vol/liq | 45 |
| [CHRISTMAS](https://pump.fun/coin/6jmhyHEy1rDyYHyRkr1rbVVQnckKpMYWh3zoX7zLpump) | `6jmhyHEy1rDyYHyRkr1rbVVQnckKpMYWh3zoX7zLpump` | $22.8k | $98.0k | +5% | +258% | +258% | 48.2x | thin liq $22.8k; churn 48x vol/liq | not scored |
| [Holders](https://pump.fun/coin/55RwtHpoNB81SgfiNvogeZTMfik2SfMGa5FaxKcXpump) | `55RwtHpoNB81SgfiNvogeZTMfik2SfMGa5FaxKcXpump` | $24.5k | $106.7k | -40% | +207% | +207% | 56.8x | thin liq $24.5k; churn 57x vol/liq | not scored |

_Timing: total 159s (discovery 71.5s, screen 1.7s, GT prime 0.3s, scoring 85.1s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/168; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
