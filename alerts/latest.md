# Last scan 2026-11-23T12:17:50Z - mode: helius (box heartbeat stale (490 min); budget 521/3000)

```
[fast_scan] 111 candidate mints from 9 source tags; 109 with pair data; 29 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored COPIUM in 72s
[fast_scan] scored MINELIUS in 81s
[fast_scan] scored pippin in 82s
[fast_scan] scored KOOP in 83s
[fast_scan] scored CATE in 83s
[fast_scan] scored NOHR in 83s
[fast_scan] scored ROCKET in 84s
[fast_scan] scored MCAT in 85s
[fast_scan] scored TROLL in 72s
# Market scan 2026-11-23 12:17 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,369 (+0.4% 24h), ETH $1,723 (+0.7% 24h), SOL $72.50 (+2.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $1.90B, vol $239.37M), pump-fun +4.5% (mcap $833.35M, vol $146.40M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $65.8k | $553.2k | 2.0 d | h24 -21% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 43* | CAUTION | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $82.8k | $1.23M | 1.9 d | h24 -31% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.7% (+3.9); #11 not checked (+3) |
| 49* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $116.0k | $373.0k | 23.3 h | h24 +259% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/739arFBhh8snVef1UJzaVgmvQaDPm9YtFzQvjgMkY4uj) | `739arFBhh8snVef1UJzaVgmvQaDPm9YtFzQvjgMkY4uj` | $223.4k | $125.3k | 1.7 h | h24 +56% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $58.8k | $627.3k | 14.6 h | h24 +1829% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $335.7k | $19.22M | 14.8 h | h24 +30404% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 1.7% (+9.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.71M | $17.82M | 119.8 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,819 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.43M | $18.03M | 743.7 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,547 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.01M | $22.52M | 843.0 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,607 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $335.1k | $19.22M | +54% | +137% | +30404% | 12.5x | liq/mcap 1.7% | 68 |
| [PumpMeme](https://pump.fun/coin/93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump) | `93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump` | $98.3k | $1.81M | -5% | +150% | +4947% | 12.5x | none flagged (still high risk) | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $86.4k | $1.33M | -11% | -49% | +3358% | 28.6x | churn 29x vol/liq; lopsided buys/sells 3.13 | not scored |
| [FSD v15](https://dexscreener.com/solana/FBfVwpsc8BDgHU4vkXWCLGRTAK4AifYpjcGpX8J9FQkE) | `FBfVwpsc8BDgHU4vkXWCLGRTAK4AifYpjcGpX8J9FQkE` | $76.8k | $77.2k | +405% | +405% | +405% | 42.1x | churn 42x vol/liq; spike (+405% 1h, +405% 6h); < 1h old | not scored |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $58.8k | $627.3k | +25% | +20% | +1829% | 19.5x | none flagged (still high risk) | 57 |
| [OpenIndex](https://pump.fun/coin/FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump) | `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump` | $51.8k | $403.8k | +17% | +53% | +1385% | 57.9x | churn 58x vol/liq | not scored |

_Timing: total 218s (discovery 71.8s, screen 1.2s, GT prime 0.4s, scoring 144.4s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/184; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
