# Last scan 2026-11-13T02:41:44Z - mode: helius (box heartbeat stale (3683 min); budget 62/3000)

```
[fast_scan] 140 candidate mints from 10 source tags; 139 with pair data; 28 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored Max in 74s
[fast_scan] scored STONK in 80s
[fast_scan] scored updog in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored UODF in 82s
[fast_scan] scored USPR in 82s
[fast_scan] scored NOBUSHIBA in 83s
[fast_scan] scored NVDAx in 83s
# Market scan 2026-11-13 02:41 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $70,349 (-4.7% 24h), ETH $1,996 (-2.9% 24h), SOL $80.56 (-3.4% 24h)
- Fear & Greed: 20 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.5% (mcap $2.33B, vol $333.32M), pump-fun -5.0% (mcap $911.43M, vol $132.70M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 43* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $262.5k | $1.86M | 1.2 d | h24 -3% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [NOBUSHIBA](https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump) | `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump` | $51.9k | $401.3k | 2.1 d | h24 -4% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 61* | SKIP | [updog](https://pump.fun/coin/77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump) | `77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump` | $74.8k | $432.1k | 1.3 d | h24 +300% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 67* | SKIP | [USPR](https://dexscreener.com/solana/SnaNyd3KgXZJafzvM3EdhpKkcQrTaBAb3qBybL9pYLy) | `SnaNyd3KgXZJafzvM3EdhpKkcQrTaBAb3qBybL9pYLy` | $287.0k | $161.5k | 9.4 h | h24 +52% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |
| 77* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $1.20M | $251.09M | 2.8 d | h24 +31% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [STONK](https://dexscreener.com/solana/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | `6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx` | $3.23M | $34.55M | 112.3 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 4h (now 334,083) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.97M | $22.17M | 109.4 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 4h (now 427,885) |
| 80* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.71M | $36.75M | 503.7 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +3.1% in 10h (now 427,740) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [fomo](https://pump.fun/coin/2DNJD5r854fcv71BpLuRdpjppNAaLBXxRQhrSAybpump) | `2DNJD5r854fcv71BpLuRdpjppNAaLBXxRQhrSAybpump` | $61.3k | $677.7k | +167% | +1927% | +1927% | 1.5x | spike (+167% 1h, +1927% 6h) | not scored |
| [AI](https://pump.fun/coin/2T56GBrvcyeWWyhUAzsTFW4AcFag1nr7xyzrtZn7pump) | `2T56GBrvcyeWWyhUAzsTFW4AcFag1nr7xyzrtZn7pump` | $78.5k | $626.5k | -11% | +993% | +993% | 53.5x | churn 54x vol/liq; spike (-11% 1h, +993% 6h) | not scored |
| [GTAINU](https://pump.fun/coin/AY2P2J79jdLWib4yYwMDApCmq9GorZhddDXerca3pump) | `AY2P2J79jdLWib4yYwMDApCmq9GorZhddDXerca3pump` | $45.1k | $363.4k | +48% | +919% | +919% | 8.7x | thin liq $45.1k; spike (+48% 1h, +919% 6h) | not scored |
| [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $47.2k | $320.8k | -6% | +778% | +778% | 56.5x | thin liq $47.2k; churn 57x vol/liq; spike (-6% 1h, +778% 6h) | not scored |
| [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $59.5k | $561.8k | +23% | +669% | +669% | 21.1x | spike (+23% 1h, +669% 6h) | not scored |
| [THRONG](https://pump.fun/coin/FQbUZry4SJTzxS1GxAeZGLW2ngzDnwxv3XDNVXa4pump) | `FQbUZry4SJTzxS1GxAeZGLW2ngzDnwxv3XDNVXa4pump` | $33.6k | $202.2k | +0% | +504% | +504% | 17.3x | thin liq $33.6k; spike (+0% 1h, +504% 6h) | not scored |

_Timing: total 156s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 82.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/148; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
