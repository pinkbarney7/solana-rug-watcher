# Last scan 2026-11-12T07:42:18Z - mode: helius (box heartbeat stale (2544 min); budget 0/3000)

```
[fast_scan] 136 candidate mints from 11 source tags; 134 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored Max in 71s
[fast_scan] scored UODF in 79s
[fast_scan] scored PREDICT in 79s
[fast_scan] scored CATE in 80s
[fast_scan] scored AIB in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored NVDAx in 81s
# Market scan 2026-11-12 07:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $73,540 (-0.3% 24h), ETH $2,050 (-0.5% 24h), SOL $82.88 (+0.1% 24h)
- Fear & Greed: 28 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.8% (mcap $2.38B, vol $350.30M), pump-fun +2.0% (mcap $953.46M, vol $173.47M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $380.6k | $2.36M | 10.8 h | h24 +6287% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $1.09M | $203.77M | 2.0 d | h24 +41% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 68* | SKIP | [AIB](https://pump.fun/coin/AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump) | `AJFnmpiF4VTKeqEWtwBUarib5zKKbXcs594UyrMHpump` | $55.1k | $481.9k | 6.4 h | h24 +775% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 74* | SKIP | [PREDICT](https://dexscreener.com/solana/7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9) | `7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9` | $165.9k | $2.97M | 1.3 d | h24 +355% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.06M | $22.79M | 108.6 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 427,413) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.75M | $13.42M | 169.0 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.4% in 7h (now 357,490) |
| 80* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.07M | $35.62M | 502.9 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +1.7% in 50h (now 407,666) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $197.8k | $2.36M | -33% | -30% | +6287% | 275.0x | churn 275x vol/liq | 55 |
| [updog](https://pump.fun/coin/77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump) | `77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump` | $68.7k | $764.4k | +4% | +1312% | +2183% | 19.6x | spike (+4% 1h, +1312% 6h) | not scored |
| [:3](https://pump.fun/coin/FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump) | `FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump` | $29.7k | $137.0k | -14% | +31% | +3848% | 22.3x | thin liq $29.7k | not scored |
| [LuckyCoin](https://pump.fun/coin/89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump) | `89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump` | $49.0k | $461.7k | -11% | -42% | +1253% | 24.8x | thin liq $49.0k | not scored |
| [NOBUSHIBA](https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump) | `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump` | $113.0k | $1.93M | +23% | +398% | +492% | 10.3x | spike (+23% 1h, +398% 6h) | not scored |
| [mihao](https://pump.fun/coin/966YHiVdAkkFH8dPxPqNEyLQeTVQrhBwcaoqv4cppump) | `966YHiVdAkkFH8dPxPqNEyLQeTVQrhBwcaoqv4cppump` | $23.0k | $102.2k | +197% | +197% | +197% | 0.3x | thin liq $23.0k; spike (+197% 1h, +197% 6h); < 1h old | not scored |

_Timing: total 153s (discovery 70.7s, screen 1.3s, GT prime 0.3s, scoring 80.9s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/131; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
