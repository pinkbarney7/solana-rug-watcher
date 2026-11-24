# Last scan 2026-11-24T06:45:59Z - mode: helius (box heartbeat stale (159 min); budget 80/3000)

```
[fast_scan] 110 candidate mints from 9 source tags; 108 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored ACHI in 71s
[fast_scan] scored TROLL in 79s
[fast_scan] scored CATE in 80s
[fast_scan] scored SuperJense in 81s
[fast_scan] scored NVDA in 81s
[fast_scan] scored JENSEN in 81s
[fast_scan] scored ROCKET in 83s
# Market scan 2026-11-24 06:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,411 (-1.6% 24h), ETH $1,700 (-1.2% 24h), SOL $71.65 (-0.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.5% (mcap $1.91B, vol $366.26M), pump-fun +1.6% (mcap $817.18M, vol $118.02M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.0k | $724.0k | 2.8 d | h24 -14% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 48* | CAUTION | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $52.6k | $489.7k | 12.9 h | h24 +463% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $175.2k | $115.5k | 1.2 h | h24 +126% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $95.7k | $124.9k | 1.4 h | h24 +181% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.94M | $20.18M | 843.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,683 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.99M | $643.2k | 159.0 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,529 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.27M | $86.77B | 120.6 d | h24 +460861% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $98.3k | $1.83M | -16% | +5052% | +5052% | 10.5x | spike (-16% 1h, +5052% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $131.0k | $3.01M | +11% | +2646% | +2646% | 15.8x | liq/mcap 4.4%; spike (+11% 1h, +2646% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.3k | $122.3k | -6% | -29% | +1519% | 119.4x | thin liq $36.3k; churn 119x vol/liq | not scored |
| [Aircoin](https://pump.fun/coin/ntHUtpTDBYpDknJUHhLRPbdN8GrR3p5PCyvTWwwpump) | `ntHUtpTDBYpDknJUHhLRPbdN8GrR3p5PCyvTWwwpump` | $21.6k | $96.3k | +222% | +222% | +222% | 14.0x | thin liq $21.6k; spike (+222% 1h, +222% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $46.3k | $331.9k | +2% | +108% | +1065% | 45.3x | thin liq $46.3k; churn 45x vol/liq | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $96.5k | $127.0k | +24% | +186% | +186% | 97.4x | churn 97x vol/liq | 53 |

_Timing: total 156s (discovery 71.8s, screen 1.2s, GT prime 0.2s, scoring 82.9s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
