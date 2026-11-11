# Last scan 2026-11-11T03:08:46Z - mode: helius (box heartbeat stale (829 min); budget 224/3000)

```
[fast_scan] 148 candidate mints from 10 source tags; 147 with pair data; 40 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored MONTRA in 72s
[fast_scan] scored ACT in 80s
[fast_scan] scored DACITY in 81s
[fast_scan] scored FLOAT in 81s
[fast_scan] scored UODF in 82s
[fast_scan] scored USPR in 82s
[fast_scan] scored BIG in 83s
[fast_scan] scored AODF in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-11 03:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $73,593 (-1.5% 24h), ETH $2,057 (-2.9% 24h), SOL $83.18 (-3.4% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $2.44B, vol $360.51M), pump-fun -2.8% (mcap $944.40M, vol $125.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [MONTRA](https://dexscreener.com/solana/Nm2mzdj1D41m2ndqzJBHVw4VuKTZfoM5CQ39ZQpdVZJ) | `Nm2mzdj1D41m2ndqzJBHVw4VuKTZfoM5CQ39ZQpdVZJ` | $340.8k | $201.1k | 14.8 h | h24 +93% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [DACITY](https://pump.fun/coin/5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump) | `5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump` | $124.0k | $2.44M | 8.1 h | h24 +5785% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.9) |
| 67* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $84.2k | $845.5k | 2.6 d | h24 +77% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 71* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.21M | $146.44M | 1.5 d | h24 +38% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.8% (+11) |
| 71* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.21M | $145.22M | 1.5 d | h24 +34% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.8% (+11) |
| 82* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $896.3k | $136.63M | 20.3 h | h24 +382320% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.27M | $9.05M | 752.7 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 3h (now 136,137) |
| 56* | SKIP | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.08M | $10.69M | 13.2 d | h24 +5% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders +2.2% in 14h (now 43,495) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $9.74M | $107.40B | 107.4 d | h24 +374064% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders +0.1% in 15h (now 426,915) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $896.3k | $136.63M | +1% | +12% | +382320% | 0.8x | liq/mcap 0.7%; lopsided buys/sells 1653.55 | 82 |
| [NIHAO](https://pump.fun/coin/8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump) | `8yLBuP74RnFmjSRS8BGFebvyoTo8uiEjPB71h3Zgpump` | $180.1k | $4.98M | +20% | +10828% | +10828% | 15.5x | liq/mcap 3.6%; spike (+20% 1h, +10828% 6h) | not scored |
| [HOLD](https://pump.fun/coin/4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump) | `4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump` | $97.7k | $1.22M | +67% | +3497% | +3497% | 32.7x | churn 33x vol/liq; spike (+67% 1h, +3497% 6h) | not scored |
| [DACITY](https://pump.fun/coin/5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump) | `5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump` | $124.0k | $2.44M | +20% | +91% | +5785% | 12.6x | none flagged (still high risk) | 60 |
| [mihao](https://pump.fun/coin/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | `4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump` | $387.8k | $14.65M | -6% | +1149% | +2845% | 51.4x | liq/mcap 2.6%; churn 51x vol/liq; spike (-6% 1h, +1149% 6h) | not scored |
| [Koop](https://dexscreener.com/solana/97ModG334B5y6QWAjQqrswSu4hauJnWyrqTUAqLcHojQ) | `97ModG334B5y6QWAjQqrswSu4hauJnWyrqTUAqLcHojQ` | $71.3k | $70.5k | +184% | +789% | +789% | 113.0x | churn 113x vol/liq; spike (+184% 1h, +789% 6h) | not scored |

_Timing: total 217s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 144.2s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/159; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
