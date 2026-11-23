# Last scan 2026-11-23T08:04:59Z - mode: helius (box heartbeat stale (237 min); budget 186/3000)

```
[fast_scan] 120 candidate mints from 10 source tags; 119 with pair data; 32 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored MCAT in 74s
[fast_scan] scored cateball in 80s
[fast_scan] scored NOHR in 81s
[fast_scan] scored pippin in 81s
[fast_scan] scored KOOP in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored Singularity in 85s
[fast_scan] scored ROCKET in 85s
[fast_scan] scored AVA in 72s
# Market scan 2026-11-23 08:04 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,384 (+3.9% 24h), ETH $1,721 (+3.4% 24h), SOL $71.93 (+4.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +4.1% (mcap $1.89B, vol $242.60M), pump-fun +8.0% (mcap $822.38M, vol $134.30M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $58.6k | $451.1k | 1.8 d | h24 -47% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $93.3k | $529.9k | 2.5 d | h24 -6% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 49* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $117.6k | $360.6k | 19.1 h | h24 +247% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 51* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $115.7k | $2.43M | 1.7 d | h24 +87% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.8% (+6.3); #11 not checked (+3) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/CyQeKLdAUTmuWwsY8bzq2KeWxv8Rrswu2W4EuKGcvFhK) | `CyQeKLdAUTmuWwsY8bzq2KeWxv8Rrswu2W4EuKGcvFhK` | $202.7k | $112.6k | 1.2 h | h24 +41% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $76.6k | $1.07M | 23.0 h | h24 +3466% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [AVA](https://pump.fun/coin/DKu9kykSfbN5LBfFXtNNDPaX35o4Fv6vJ9FKk7pZpump) | `DKu9kykSfbN5LBfFXtNNDPaX35o4Fv6vJ9FKk7pZpump` | $931.7k | $6.71M | 739.6 d | h24 +24% | #6 Top-10 holders (excl. pools/programs) FAIL (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 112,247 (growth n/a: first sighting) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $8.78M | 669.3 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,106 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.35M | $17.37M | 743.5 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,538 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $273.0k | $12.99M | +27% | +55% | +20526% | 12.6x | liq/mcap 2.1% | not scored |
| [PumpMeme](https://pump.fun/coin/93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump) | `93uamrbDerKbUh8MSjNF1wDtxYvEUD1CS9BcHn1apump` | $84.3k | $1.36M | -7% | +3706% | +3706% | 10.9x | spike (-7% 1h, +3706% 6h) | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $129.4k | $3.03M | -7% | +14% | +7745% | 15.9x | liq/mcap 4.3%; lopsided buys/sells 3.30 | not scored |
| [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $76.6k | $1.07M | -10% | -38% | +3466% | 18.0x | none flagged (still high risk) | 58 |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $55.7k | $577.5k | -1% | -16% | +1676% | 16.5x | none flagged (still high risk) | not scored |
| [UCASH](https://pump.fun/coin/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | `7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump` | $57.5k | $559.7k | -21% | -69% | +1076% | 56.2x | churn 56x vol/liq | not scored |

_Timing: total 218s (discovery 71.2s, screen 1.1s, GT prime 0.5s, scoring 145.4s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/184; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
