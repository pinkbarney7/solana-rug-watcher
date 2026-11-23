# Last scan 2026-11-23T12:08:56Z - mode: helius (box heartbeat stale (481 min); budget 511/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 32 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored NOHR in 74s
[fast_scan] scored CATE in 80s
[fast_scan] scored pippin in 81s
[fast_scan] scored KOOP in 82s
[fast_scan] scored MCAT in 82s
[fast_scan] scored COPIUM in 83s
[fast_scan] scored ROCKET in 85s
[fast_scan] scored SIDOOR in 86s
[fast_scan] scored TROLL in 72s
# Market scan 2026-11-23 12:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,305 (+0.4% 24h), ETH $1,722 (+0.8% 24h), SOL $72.47 (+2.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $1.90B, vol $239.37M), pump-fun +4.5% (mcap $833.35M, vol $146.40M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $66.8k | $570.6k | 2.0 d | h24 -30% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 43* | CAUTION | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $93.1k | $1.55M | 1.9 d | h24 -12% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.0% (+4.8); #11 not checked (+3) |
| 43* | CAUTION | [SIDOOR](https://dexscreener.com/solana/zcRvzm7gAfYGde8gRwaSYxNryL47SjLVUQLAf1bdoor) | `zcRvzm7gAfYGde8gRwaSYxNryL47SjLVUQLAf1bdoor` | $55.4k | $389.2k | 1.6 d | h24 +82% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 49* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $116.3k | $373.7k | 23.2 h | h24 +260% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 57* | SKIP | [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $60.9k | $671.9k | 14.4 h | h24 +1966% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [KOOP](https://dexscreener.com/solana/1324nw49dNWMiBCYL1pGJFo49m4xJqusxgjaVW367LGF) | `1324nw49dNWMiBCYL1pGJFo49m4xJqusxgjaVW367LGF` | $256.7k | $163.3k | 1.1 h | h24 +86% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.72M | $17.91M | 119.8 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,819 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.41M | $17.88M | 743.7 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,547 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.01M | $22.40M | 843.0 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 3h (now 218,607) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $323.0k | $17.90M | +32% | +99% | +28320% | 12.3x | liq/mcap 1.8% | not scored |
| [PumpMeme](https://pump.fun/coin/93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump) | `93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump` | $100.1k | $1.88M | +33% | +84% | +5133% | 12.2x | none flagged (still high risk) | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $90.6k | $1.47M | +12% | -43% | +3701% | 27.1x | churn 27x vol/liq; lopsided buys/sells 3.14 | not scored |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $60.9k | $671.9k | +43% | +66% | +1966% | 18.7x | none flagged (still high risk) | 57 |
| [PauseAI](https://pump.fun/coin/66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump) | `66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump` | $11.2k | $23.7k | +3% | +49% | +1572% | 2.1x | thin liq $11.2k | not scored |
| [Lotus Cat](https://dexscreener.com/solana/96uYiGanjXefBsHDmKZPzrx13Af31SpV3wEyQuCwXuHn) | `96uYiGanjXefBsHDmKZPzrx13Af31SpV3wEyQuCwXuHn` | $54.5k | $48.7k | +220% | +236% | +236% | 8.3x | spike (+220% 1h, +236% 6h) | not scored |

_Timing: total 219s (discovery 71.5s, screen 1.3s, GT prime 0.4s, scoring 145.5s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/189; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
