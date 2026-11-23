# Last scan 2026-11-23T09:15:33Z - mode: helius (box heartbeat stale (307 min); budget 266/3000)

```
[fast_scan] 121 candidate mints from 10 source tags; 120 with pair data; 34 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored KOOP in 78s
[fast_scan] scored cateball in 87s
[fast_scan] scored VINE in 89s
[fast_scan] scored Singularity in 89s
[fast_scan] scored ZEC in 89s
[fast_scan] scored NOHR in 90s
[fast_scan] scored ROCKET in 92s
[fast_scan] scored MCAT in 93s
[fast_scan] scored pippin in 72s
# Market scan 2026-11-23 09:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,501 (+3.2% 24h), ETH $1,725 (+2.6% 24h), SOL $72.47 (+4.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +3.4% (mcap $1.90B, vol $240.71M), pump-fun +7.7% (mcap $829.07M, vol $146.40M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $65.5k | $554.9k | 1.9 d | h24 -33% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $88.8k | $515.1k | 2.6 d | h24 +2% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 42* | CAUTION | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $105.1k | $1.99M | 1.7 d | h24 +39% | #3 Liquidity vs market cap WARN (+7); liq/mcap 5.3% (+5.6); #11 not checked (+3) |
| 49* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $120.3k | $389.5k | 20.3 h | h24 +275% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/CyQeKLdAUTmuWwsY8bzq2KeWxv8Rrswu2W4EuKGcvFhK) | `CyQeKLdAUTmuWwsY8bzq2KeWxv8Rrswu2W4EuKGcvFhK` | $232.1k | $131.2k | 2.4 h | h24 +64% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $78.3k | $1.11M | 1.0 d | h24 +1300% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $8.80M | 669.4 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,102 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $17.71M | 743.5 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,539 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.28M | $19.7k | 403.7 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,847 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $310.3k | $16.62M | +27% | +92% | +26281% | 11.4x | liq/mcap 1.9% | not scored |
| [PumpMeme](https://pump.fun/coin/93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump) | `93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump` | $78.4k | $1.17M | -13% | +3158% | +3158% | 12.8x | spike (-13% 1h, +3158% 6h) | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $125.7k | $2.83M | -6% | +10% | +7245% | 16.8x | liq/mcap 4.4%; lopsided buys/sells 3.16 | not scored |
| [PauseAI](https://pump.fun/coin/66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump) | `66wRVXFCn46y6gYD2r55MbBY6hmVD7ueYdTdrF7Lpump` | $11.2k | $23.6k | +51% | +46% | +1562% | 2.1x | thin liq $11.2k | not scored |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $54.7k | $551.5k | -5% | +8% | +1596% | 18.0x | none flagged (still high risk) | not scored |
| [OpenIndex](https://pump.fun/coin/FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump) | `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump` | $48.8k | $362.1k | -4% | +44% | +1232% | 59.9x | thin liq $48.8k; churn 60x vol/liq | not scored |

_Timing: total 224s (discovery 71.4s, screen 1.7s, GT prime 0.4s, scoring 150.2s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/190; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
