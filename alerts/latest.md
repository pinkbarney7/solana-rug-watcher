# Last scan 2026-11-10T23:45:38Z - mode: helius (box heartbeat stale (626 min); budget 204/3000)

```
[fast_scan] 134 candidate mints from 11 source tags; 132 with pair data; 37 >= $50,000 liq; 14 pass survivor pre-gates (72s)
[fast_scan] scored BIG in 72s
[fast_scan] scored UODF in 80s
[fast_scan] scored ZEC in 81s
[fast_scan] scored ACT in 81s
[fast_scan] scored AODF in 82s
[fast_scan] scored UODF in 82s
[fast_scan] scored MONTRA in 83s
[fast_scan] scored USPR in 83s
[fast_scan] scored CYBERLEEK in 73s
# Market scan 2026-11-10 23:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $73,685 (-1.9% 24h), ETH $2,050 (-3.8% 24h), SOL $83.17 (-3.9% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.7% (mcap $2.43B, vol $368.57M), pump-fun -4.4% (mcap $941.52M, vol $120.76M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $96.5k | $1.11M | 2.5 d | h24 +430% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #9 Price momentum WARN (+5) |
| 67* | SKIP | [MONTRA](https://dexscreener.com/solana/Nm2mzdj1D41m2ndqzJBHVw4VuKTZfoM5CQ39ZQpdVZJ) | `Nm2mzdj1D41m2ndqzJBHVw4VuKTZfoM5CQ39ZQpdVZJ` | $308.5k | $183.2k | 11.4 h | h24 +76% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 71* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.18M | $137.80M | 1.4 d | h24 +35% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.9% (+11) |
| 71* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.18M | $139.42M | 1.4 d | h24 +35% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.8% (+11) |
| 71* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $950.7k | $89.95M | 1.4 d | h24 +52% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.1% (+10.7) |
| 75* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $858.8k | $125.68M | 16.9 h | h24 +351683% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [CYBERLEEK](https://dexscreener.com/solana/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | `ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg` | $426.4k | $2.09M | 87.4 d | h24 +31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 132,205 (growth n/a: first sighting) |
| 52* | SKIP | [ACT](https://pump.fun/coin/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` | $1.29M | $9.45M | 752.5 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 15h (now 136,137) |
| 80* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.52M | $25.9k | 391.3 d | h24 -9% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.3% in 11h (now 389,391) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $858.9k | $125.69M | +1% | +11% | +351706% | 0.8x | liq/mcap 0.7%; lopsided buys/sells 1411.61 | 75 |
| [DACITY](https://pump.fun/coin/5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump) | `5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump` | $104.1k | $1.76M | +1% | +4144% | +4144% | 10.9x | spike (+1% 1h, +4144% 6h) | not scored |
| [mihao](https://pump.fun/coin/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | `4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump` | $307.4k | $10.43M | +324% | +710% | +2162% | 28.8x | liq/mcap 2.9%; churn 29x vol/liq; spike (+324% 1h, +710% 6h) | not scored |
| [BULLHARIS](https://pump.fun/coin/6mwuYnY3fHdxed9GnrdY5BkXhJwMi1uz39MPsYUcpump) | `6mwuYnY3fHdxed9GnrdY5BkXhJwMi1uz39MPsYUcpump` | $53.2k | $495.2k | +0% | +1336% | +1336% | 5.8x | spike (+0% 1h, +1336% 6h) | not scored |
| [HOLD](https://pump.fun/coin/4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump) | `4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump` | $40.2k | $237.9k | -38% | +603% | +603% | 34.2x | thin liq $40.2k; churn 34x vol/liq; spike (-38% 1h, +603% 6h) | not scored |
| [MOMO](https://pump.fun/coin/488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump) | `488SaFq6wHF2z2k6NLSD3PtoSkXDNZaPkJwxze11pump` | $45.9k | $137.9k | +23% | +30% | +1100% | 5.1x | thin liq $45.9k | not scored |

_Timing: total 218s (discovery 71.1s, screen 1.4s, GT prime 0.4s, scoring 144.8s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/164; Helius 429s 101; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
