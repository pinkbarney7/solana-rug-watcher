# Last scan 2026-11-24T21:16:47Z - mode: helius (box heartbeat stale (23 min); budget 514/3000)

```
[fast_scan] 120 candidate mints from 9 source tags; 119 with pair data; 23 >= $50,000 liq; 11 pass survivor pre-gates (74s)
[fast_scan] scored JIMMY in 73s
[fast_scan] scored CATE in 81s
[fast_scan] scored cateball in 82s
[fast_scan] scored DONJENSEN in 82s
[fast_scan] scored pippin in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored GROKIA in 83s
[fast_scan] scored MCAT in 83s
# Market scan 2026-11-24 21:16 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,700 (-2.6% 24h), ETH $1,673 (-3.0% 24h), SOL $69.20 (-4.9% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -6.0% (mcap $1.79B, vol $327.00M), pump-fun -7.1% (mcap $759.04M, vol $143.77M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $63.7k | $137.9k | 2.3 d | h24 -41% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $66.4k | $788.1k | 2.5 d | h24 +20% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $188.2k | $1.03M | 1.0 d | h24 +491% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $95.9k | $1.75M | 18.7 h | h24 +4827% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.5% (+5.4) |
| 60* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $101.8k | $1.84M | 19.0 h | h24 +1582% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.5% (+5.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.91M | 121.2 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 8h (now 436,865) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.44M | $18.89M | 745.0 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 8h (now 182,572) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $3.56M | $13.01M | 181.6 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +1.0% in 8h (now 390,464) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Flop](https://dexscreener.com/solana/DCSX5MxQRAYiXEn1X9XuXiHmq87Tza4rJNNL9ETXM65i) | `DCSX5MxQRAYiXEn1X9XuXiHmq87Tza4rJNNL9ETXM65i` | $86.5k | $219.3k | +3240% | +3240% | +3240% | 48.2x | churn 48x vol/liq; spike (+3240% 1h, +3240% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $86.7k | $1.06M | +32% | +25% | +5368% | 40.1x | churn 40x vol/liq | 45 |
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $95.9k | $1.75M | -13% | -4% | +4827% | 19.2x | none flagged (still high risk) | 60 |
| [CrimeCat](https://dexscreener.com/solana/YrdaNSJMZ8wkiVaRbUeGdMwQDsfnku9TaNdPumCgAfB) | `YrdaNSJMZ8wkiVaRbUeGdMwQDsfnku9TaNdPumCgAfB` | $11.5k | $19.8k | +350% | +376% | +312% | 1.9x | thin liq $11.5k; spike (+350% 1h, +376% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $101.8k | $1.84M | -35% | -24% | +1582% | 28.1x | churn 28x vol/liq | 60 |
| [CHRISTMAS](https://pump.fun/coin/6jmhyHEy1rDyYHyRkr1rbVVQnckKpMYWh3zoX7zLpump) | `6jmhyHEy1rDyYHyRkr1rbVVQnckKpMYWh3zoX7zLpump` | $23.6k | $104.3k | +0% | +281% | +281% | 46.6x | thin liq $23.6k; churn 47x vol/liq | not scored |

_Timing: total 157s (discovery 71.6s, screen 2.1s, GT prime 0.2s, scoring 83.2s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/168; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
