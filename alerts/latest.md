# Last scan 2026-11-22T22:29:38Z - mode: helius (box heartbeat stale (7702 min); budget 40/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 124 with pair data; 34 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored Singularity in 74s
[fast_scan] scored XNR in 81s
[fast_scan] scored cateball in 81s
[fast_scan] scored VINE in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored ROCKET in 83s
[fast_scan] scored AODT in 83s
[fast_scan] scored UCASH in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-22 22:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,760 (+0.9% 24h), ETH $1,712 (+1.7% 24h), SOL $70.08 (-0.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $1.85B, vol $238.31M), pump-fun +1.3% (mcap $784.17M, vol $99.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 40* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $83.0k | $855.7k | 1.4 d | h24 -8% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $113.7k | $653.6k | 2.1 d | h24 +73% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [XNR](https://dexscreener.com/solana/3PR537YCsjrDGfkaX8EfAYwLPSHa7FaX4MvH9kdDqMkh) | `3PR537YCsjrDGfkaX8EfAYwLPSHa7FaX4MvH9kdDqMkh` | $195.3k | $109.3k | 1.2 h | h24 +40% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UCASH](https://pump.fun/coin/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | `7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump` | $79.8k | $1.17M | 11.2 h | h24 +2360% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 65* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $105.6k | $2.31M | 1.9 d | h24 +52% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 4.6% (+6.5) |
| 66* | SKIP | [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $108.2k | $2.19M | 13.4 h | h24 +7216% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.44M | $8.84M | 668.9 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 5h (now 345,115) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $17.92M | 119.3 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.9% in 49h (now 436,273) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.26M | $13.16M | 179.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.3% in 5h (now 387,980) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MINELIUS](https://pump.fun/coin/E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump) | `E9rWKjVhHMxQkxfREr7Li8Yy46rVcWiWHoKVQAe9pump` | $196.4k | $7.11M | +11184% | +11184% | +11184% | 10.4x | liq/mcap 2.8%; spike (+11184% 1h, +11184% 6h); < 1h old | not scored |
| [FSDV15](https://pump.fun/coin/3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump) | `3BcJ4SSCfbxDMrWcUDucyCWxMjmy4M2ECCtvxu86pump` | $70.0k | $972.4k | +2420% | +2420% | +2420% | 10.5x | spike (+2420% 1h, +2420% 6h); lopsided buys/sells 3.01; < 1h old | not scored |
| [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $108.2k | $2.19M | +7% | +231% | +7216% | 10.1x | liq/mcap 4.9% | 66 |
| [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $39.6k | $319.9k | +884% | +884% | +884% | 8.0x | thin liq $39.6k; spike (+884% 1h, +884% 6h); < 1h old | not scored |
| [OpenIndex](https://pump.fun/coin/FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump) | `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump` | $53.6k | $473.3k | +24% | +1641% | +1641% | 41.9x | churn 42x vol/liq; spike (+24% 1h, +1641% 6h) | not scored |
| [UCASH](https://pump.fun/coin/7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump) | `7cFiqdT46zs7ooHWLFiLSaSQKLMibtokh9dBinsspump` | $79.4k | $1.16M | -2% | +61% | +2333% | 22.2x | none flagged (still high risk) | 59 |

_Timing: total 219s (discovery 71.3s, screen 1.7s, GT prime 0.5s, scoring 145.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
