# Last scan 2026-11-14T16:00:03Z - mode: helius (box heartbeat stale (5920 min); budget 20/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 131 with pair data; 32 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Max in 74s
[fast_scan] scored UODF in 81s
[fast_scan] scored XTO in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored FOOD in 82s
[fast_scan] scored VTC in 82s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored AMC in 83s
[fast_scan] scored TTWO in 71s
# Market scan 2026-11-14 15:59 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $65,598 (-4.4% 24h), ETH $1,836 (-4.8% 24h), SOL $73.70 (-7.5% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -8.6% (mcap $2.15B, vol $352.87M), pump-fun -5.1% (mcap $882.07M, vol $114.26M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $243.9k | $1.90M | 2.8 d | h24 -2% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $124.6k | $618.3k | 1.8 d | h24 -46% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 54* | SKIP | [VTC](https://pump.fun/coin/3tjPCXfx3KrgMY53yo7pa67D2QQZMbLTRaqQckJmpump) | `3tjPCXfx3KrgMY53yo7pa67D2QQZMbLTRaqQckJmpump` | $82.2k | $706.6k | 19.5 h | h24 +32% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.04M | $208.13M | 2.2 d | h24 +14% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $121.5k | $2.64M | 21.3 h | h24 +6515% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.6% (+6.5) |
| 67* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $918.0k | $162.06M | 1.1 d | h24 +101% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.66M | $15.75M | 111.0 d | h24 -13% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 13h (now 428,883) |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.45M | $98 | 103.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +4.1% in 6h (now 254,988) |
| 72* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.29M | $35.26M | 505.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders -0.1% in 6h (now 431,932) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AMC](https://pump.fun/coin/HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump) | `HWya5CpQiQWLnJfJVRDF9o8AHaUPnPMRa3vfQRczpump` | $121.5k | $2.64M | +12% | -28% | +6515% | 19.9x | liq/mcap 4.6% | 66 |
| [FLAG](https://dexscreener.com/solana/FvQHUAqNV4U8X559sFmjqSm6juzprVJLxgimNrKDaray) | `FvQHUAqNV4U8X559sFmjqSm6juzprVJLxgimNrKDaray` | $54.1k | $563.1k | +12% | +1713% | +1713% | 0.6x | spike (+12% 1h, +1713% 6h) | not scored |
| [ASTRALIS](https://pump.fun/coin/DWsutTNJSjG5mkhGsPevvT8xbRtVYQBLZdxqxm2Upump) | `DWsutTNJSjG5mkhGsPevvT8xbRtVYQBLZdxqxm2Upump` | $28.6k | $131.0k | +750% | +159% | +336% | 57.4x | thin liq $28.6k; churn 57x vol/liq; spike (+750% 1h, +159% 6h) | not scored |
| [ROCKY](https://pump.fun/coin/D8ezSnpTQDH3dMnkr4ZNK59uoYmXFU3G7fQrQkGXpump) | `D8ezSnpTQDH3dMnkr4ZNK59uoYmXFU3G7fQrQkGXpump` | $12.9k | $29.1k | +330% | +184% | +262% | 5.3x | thin liq $12.9k; spike (+330% 1h, +184% 6h) | not scored |
| [GTA$](https://pump.fun/coin/6Nh9cmDoQvd2FvjNm44VmTwbyiKtxgmM7SCuhREhpump) | `6Nh9cmDoQvd2FvjNm44VmTwbyiKtxgmM7SCuhREhpump` | $57.4k | $325.0k | -18% | +549% | +549% | 37.5x | churn 38x vol/liq; spike (-18% 1h, +549% 6h) | not scored |
| [Snoopy](https://dexscreener.com/solana/7mEhH5gsuwPeBC9n9C2XQJdXinWhKGfNhrt4r8db47Cn) | `7mEhH5gsuwPeBC9n9C2XQJdXinWhKGfNhrt4r8db47Cn` | $66.2k | $665.0k | +82% | +403% | +613% | 19.9x | spike (+82% 1h, +403% 6h) | not scored |

_Timing: total 218s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 145.0s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/180; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
