# Last scan 2026-11-12T16:16:29Z - mode: helius (box heartbeat stale (3058 min); budget 20/3000)

```
[fast_scan] 121 candidate mints from 10 source tags; 118 with pair data; 24 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored CATE in 81s
[fast_scan] scored updog in 81s
[fast_scan] scored Max in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored PREDICT in 83s
[fast_scan] scored NVDAx in 83s
[fast_scan] scored NOBUSHIBA in 83s
[fast_scan] scored UODF in 84s
# Market scan 2026-11-12 16:16 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $72,046 (-2.9% 24h), ETH $2,022 (-2.7% 24h), SOL $82.05 (-3.4% 24h)
- Fear & Greed: 28 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.8% (mcap $2.34B, vol $354.72M), pump-fun -4.7% (mcap $936.25M, vol $146.87M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [updog](https://pump.fun/coin/77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump) | `77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump` | $92.0k | $524.9k | 21.1 h | h24 +1468% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 64* | SKIP | [NOBUSHIBA](https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump) | `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump` | $87.1k | $1.13M | 1.6 d | h24 +347% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap WARN (+7); #9 Price momentum WARN (+5) |
| 68* | SKIP | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $278.6k | $1.61M | 19.3 h | h24 +4257% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 77* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $1.15M | $228.36M | 2.4 d | h24 +36% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |
| 79* | SKIP | [PREDICT](https://dexscreener.com/solana/7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9) | `7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9` | $146.0k | $4.52M | 1.6 d | h24 +304% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.04M | $22.62M | 109.0 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 9h (now 427,394) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.44M | $13.95M | 169.3 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.2% in 9h (now 358,119) |
| 80* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.35M | $36.72M | 503.3 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +1.8% in 9h (now 414,817) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Huang](https://pump.fun/coin/4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump) | `4FP2GRQS3WYPsZSE2dwaVzqkajrBpHcXyVSTVt83pump` | $59.5k | $497.2k | +47% | +1517% | +1517% | 35.7x | churn 36x vol/liq; spike (+47% 1h, +1517% 6h) | not scored |
| [HUNG](https://pump.fun/coin/4xgqefa5WcdHWKXzqvM9MRJqWYGaHVEUnpUL4Vq5pump) | `4xgqefa5WcdHWKXzqvM9MRJqWYGaHVEUnpUL4Vq5pump` | $72.1k | $434.6k | -41% | +9% | +4453% | 84.7x | churn 85x vol/liq | not scored |
| [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $164.4k | $1.61M | -11% | -18% | +4257% | 338.8x | churn 339x vol/liq | 68 |
| [HUANG](https://pump.fun/coin/7z3QB6D8xge7GzKZCsajvnLt8zqT1SvFonY9vZZmpump) | `7z3QB6D8xge7GzKZCsajvnLt8zqT1SvFonY9vZZmpump` | $26.3k | $123.0k | +261% | +261% | +261% | 8.2x | thin liq $26.3k; spike (+261% 1h, +261% 6h); < 1h old | not scored |
| [LuckyCoin](https://pump.fun/coin/89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump) | `89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump` | $45.2k | $444.6k | +229% | -3% | +627% | 32.1x | thin liq $45.2k; churn 32x vol/liq; spike (+229% 1h, -3% 6h) | not scored |
| [updog](https://pump.fun/coin/77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump) | `77HqxiDCgYfXUsDXDD6YVefPhTTz1Z2n8jX4gTxipump` | $52.9k | $515.5k | -6% | -20% | +1440% | 33.2x | churn 33x vol/liq | 55 |

_Timing: total 156s (discovery 71.2s, screen 1.3s, GT prime 0.4s, scoring 83.5s for 8 coins, 8 newly scored). ~22 Helius credits (smart-money discovery 20). HTTP cache hits 8/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
