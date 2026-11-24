# Last scan 2026-11-24T10:12:19Z - mode: helius (box heartbeat stale (365 min); budget 274/3000)

```
[fast_scan] 112 candidate mints from 10 source tags; 110 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored NOHR in 78s
[fast_scan] scored GROKIA in 86s
[fast_scan] scored NVDA in 87s
[fast_scan] scored CATE in 88s
[fast_scan] scored MCAT in 88s
[fast_scan] scored DONJENSEN in 88s
[fast_scan] scored ACHI in 89s
[fast_scan] scored ROCKET in 90s
[fast_scan] scored CLAUDIA in 72s
# Market scan 2026-11-24 10:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,942 (-2.3% 24h), ETH $1,684 (-2.2% 24h), SOL $70.68 (-2.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.1% (mcap $1.83B, vol $351.62M), pump-fun -3.9% (mcap $779.34M, vol $123.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.3k | $770.7k | 2.9 d | h24 +42% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $82.1k | $214.7k | 1.9 d | h24 -48% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $143.7k | $3.53M | 2.8 d | h24 +82% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.1% (+7.1); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $121.8k | $119.0k | 4.8 h | h24 +168% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $102.6k | $2.01M | 7.6 h | h24 +5542% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.9) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $140.1k | $3.47M | 7.9 h | h24 +3065% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.0% (+7.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.56M | 120.7 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,835 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.74M | $620.0k | 159.1 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,388 (growth n/a: first sighting) |
| 67* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.76M | $77.92B | 48.4 d | h24 +793973% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 61,375 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $102.6k | $2.01M | -15% | +19% | +5542% | 12.1x | none flagged (still high risk) | 60 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $140.1k | $3.47M | +19% | +87% | +3065% | 15.8x | liq/mcap 4.0% | 66 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $49.6k | $375.8k | -18% | -2% | +1219% | 48.5x | thin liq $49.6k; churn 48x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $25.2k | $63.4k | -45% | -53% | +819% | 173.2x | thin liq $25.2k; churn 173x vol/liq | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $121.8k | $119.0k | +44% | +168% | +168% | 162.0x | churn 162x vol/liq | 53 |
| [CLAUDIO](https://pump.fun/coin/5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump) | `5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump` | $29.9k | $153.2k | +32% | +214% | +71% | 116.5x | thin liq $29.9k; churn 116x vol/liq | not scored |

_Timing: total 223s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 149.7s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/179; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
