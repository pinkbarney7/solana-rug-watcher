# Last scan 2026-11-23T08:22:16Z - mode: helius (box heartbeat stale (254 min); budget 206/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 117 with pair data; 32 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored Singularity in 74s
[fast_scan] scored cateball in 81s
[fast_scan] scored cCAT in 82s
[fast_scan] scored NOHR in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored ZEC in 83s
[fast_scan] scored MCAT in 85s
[fast_scan] scored ROCKET in 85s
[fast_scan] scored pippin in 72s
# Market scan 2026-11-23 08:22 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,161 (+3.2% 24h), ETH $1,715 (+2.6% 24h), SOL $71.97 (+3.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +4.2% (mcap $1.89B, vol $242.56M), pump-fun +8.2% (mcap $824.10M, vol $136.22M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $62.4k | $507.1k | 1.9 d | h24 -40% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $89.5k | $525.1k | 2.5 d | h24 -13% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 42* | CAUTION | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $103.9k | $1.95M | 1.7 d | h24 +54% | #3 Liquidity vs market cap WARN (+7); liq/mcap 5.3% (+5.6); #11 not checked (+3) |
| 49* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $113.9k | $337.0k | 19.4 h | h24 +224% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 53* | SKIP | [cCAT](https://dexscreener.com/solana/GV9KAJn6xkTvxYP8snyU13Dw7NNWakVddnzmRqd8Lrj) | `GV9KAJn6xkTvxYP8snyU13Dw7NNWakVddnzmRqd8Lrj` | $129.0k | $85.1k | 1.1 h | h24 +118% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $78.6k | $1.12M | 23.2 h | h24 +3646% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $8.77M | 669.3 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,105 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.37M | $17.59M | 743.5 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,537 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.24M | $19.5k | 403.6 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 3h (now 393,842) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $283.3k | $13.96M | +28% | +83% | +22054% | 12.2x | liq/mcap 2.0% | not scored |
| [PumpMeme](https://pump.fun/coin/93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump) | `93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump` | $80.9k | $1.25M | -13% | +3395% | +3395% | 11.6x | spike (-13% 1h, +3395% 6h) | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $128.6k | $2.99M | -3% | +4% | +7642% | 16.1x | liq/mcap 4.3%; lopsided buys/sells 3.26 | not scored |
| [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $78.6k | $1.12M | +7% | -37% | +3646% | 17.6x | none flagged (still high risk) | 59 |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $57.8k | $620.5k | +4% | -12% | +1808% | 16.2x | none flagged (still high risk) | not scored |
| [PauseAI](https://pump.fun/coin/66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump) | `66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump` | $10.9k | $22.6k | +45% | +46% | +1492% | 2.2x | thin liq $10.9k; spike (+45% 1h, +46% 6h) | not scored |

_Timing: total 218s (discovery 71.3s, screen 1.1s, GT prime 0.4s, scoring 145.6s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/189; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
