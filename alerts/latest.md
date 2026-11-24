# Last scan 2026-11-24T09:56:12Z - mode: helius (box heartbeat stale (350 min); budget 264/3000)

```
[fast_scan] 108 candidate mints from 9 source tags; 106 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 74s
[fast_scan] scored DONJENSEN in 80s
[fast_scan] scored CATE in 81s
[fast_scan] scored CLAUDIA in 82s
[fast_scan] scored NOHR in 82s
[fast_scan] scored ROCKET in 82s
[fast_scan] scored ACHI in 83s
[fast_scan] scored NVDA in 83s
# Market scan 2026-11-24 09:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,007 (-2.1% 24h), ETH $1,686 (-2.0% 24h), SOL $70.82 (-1.9% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.5% (mcap $1.85B, vol $362.14M), pump-fun -3.5% (mcap $782.27M, vol $121.94M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.8k | $744.3k | 2.9 d | h24 +38% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $85.8k | $237.1k | 1.9 d | h24 -39% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $142.4k | $3.46M | 2.8 d | h24 +83% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.1% (+7.1); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $113.7k | $106.8k | 4.6 h | h24 +140% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 69* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $110.6k | $2.33M | 7.4 h | h24 +6434% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); #16 Exit liquidity (Jupiter quotes) WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.61M | $16.23M | 120.7 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,835 (growth n/a: first sighting) |
| 67* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.70M | $77.45B | 48.3 d | h24 +792407% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 61,368 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.97M | $625.3k | 159.1 d | h24 +17% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,394 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $110.6k | $2.33M | +6% | +36% | +6434% | 11.0x | liq/mcap 4.8% | 69 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $133.5k | $3.14M | +4% | +984% | +2770% | 16.5x | liq/mcap 4.2%; spike (+4% 1h, +984% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $32.6k | $101.8k | -17% | -31% | +1376% | 133.8x | thin liq $32.6k; churn 134x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $49.6k | $375.6k | -24% | +17% | +1219% | 48.2x | thin liq $49.6k; churn 48x vol/liq | not scored |
| [BLACK](https://dexscreener.com/solana/2f5rwyivxmx38x6DKdb3eqEv3vQf7nQ4mPYRngjac19r) | `2f5rwyivxmx38x6DKdb3eqEv3vQf7nQ4mPYRngjac19r` | $22.6k | $18.2k | +160% | +160% | +160% | 1.9x | thin liq $22.6k; spike (+160% 1h, +160% 6h); < 1h old | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $113.7k | $106.8k | +22% | +140% | +140% | 167.0x | churn 167x vol/liq | 53 |

_Timing: total 156s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 82.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
