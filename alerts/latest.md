# Last scan 2026-11-15T00:00:43Z - mode: helius (box heartbeat stale (6402 min); budget 50/3000)

```
[fast_scan] 136 candidate mints from 10 source tags; 134 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored bill in 70s
[fast_scan] scored XTO in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored CATE in 79s
[fast_scan] scored TROLL in 80s
[fast_scan] scored UODF in 80s
# Market scan 2026-11-15 00:00 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,147 (-6.0% 24h), ETH $1,769 (-8.2% 24h), SOL $70.24 (-10.1% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -12.8% (mcap $2.02B, vol $495.79M), pump-fun -5.4% (mcap $843.85M, vol $130.55M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [bill](https://dexscreener.com/solana/KUtvFkr8Ao6A3YT8V2oZAxs3WtvrmtqU9JAwuEtLb4r) | `KUtvFkr8Ao6A3YT8V2oZAxs3WtvrmtqU9JAwuEtLb4r` | $259.0k | $161.4k | 3.4 h | h24 +136% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.01M | $207.91M | 2.5 d | h24 +4% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $991.3k | $198.21M | 1.4 d | h24 +139% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.61M | $15.11M | 111.3 d | h24 -12% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 4h (now 429,198) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.95M | $22.06M | 834.5 d | h24 -17% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.1% in 114h (now 218,605) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.29M | $12.69M | 171.7 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 4h (now 364,423) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DOJE](https://pump.fun/coin/7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump) | `7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump` | $27.4k | $160.9k | +372% | +372% | +372% | 5.6x | thin liq $27.4k; spike (+372% 1h, +372% 6h); lopsided buys/sells 5.35; < 1h old | not scored |
| [RWA](https://pump.fun/coin/6edJUFSC85CyyLFB1QcCvYu7uzqaD4kV9o5YUPxrpump) | `6edJUFSC85CyyLFB1QcCvYu7uzqaD4kV9o5YUPxrpump` | $26.6k | $153.6k | +346% | +346% | +346% | 3.5x | thin liq $26.6k; spike (+346% 1h, +346% 6h); lopsided buys/sells 5.31; < 1h old | not scored |
| [SWIF](https://pump.fun/coin/Hi6qQHwHBnx9uaxT3KyBxaHaUn4JTAG6ijygQbiopump) | `Hi6qQHwHBnx9uaxT3KyBxaHaUn4JTAG6ijygQbiopump` | $26.0k | $142.8k | +335% | +335% | +335% | 7.2x | thin liq $26.0k; spike (+335% 1h, +335% 6h); lopsided buys/sells 3.38; < 1h old | not scored |
| [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $66.9k | $354.0k | -12% | +517% | +517% | 31.7x | churn 32x vol/liq; spike (-12% 1h, +517% 6h) | not scored |
| [Bear](https://pump.fun/coin/AvRSpY1rPA9iVFxYHc5D5JQW6oU5tjGQZdsW2e5upump) | `AvRSpY1rPA9iVFxYHc5D5JQW6oU5tjGQZdsW2e5upump` | $20.6k | $85.3k | +220% | +220% | +220% | 12.9x | thin liq $20.6k; spike (+220% 1h, +220% 6h); < 1h old | not scored |
| [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $11.4k | $26.0k | +154% | -82% | -95% | 23.0x | thin liq $11.4k; spike (+154% 1h, -82% 6h); dumping -95% 24h; lopsided buys/sells 0.04 | not scored |

_Timing: total 153s (discovery 71.1s, screen 1.3s, GT prime 0.4s, scoring 79.7s for 6 coins, 6 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 6/122; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
