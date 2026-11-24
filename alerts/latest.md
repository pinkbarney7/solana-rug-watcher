# Last scan 2026-11-24T08:53:05Z - mode: helius (box heartbeat stale (287 min); budget 160/3000)

```
[fast_scan] 114 candidate mints from 10 source tags; 111 with pair data; 27 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 74s
[fast_scan] scored NVDA in 80s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored ACHI in 82s
[fast_scan] scored pippin in 82s
[fast_scan] scored CATE in 83s
[fast_scan] scored ROCKET in 83s
[fast_scan] scored GROKIA in 83s
# Market scan 2026-11-24 08:53 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,420 (-1.6% 24h), ETH $1,699 (-1.3% 24h), SOL $71.48 (-1.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $1.88B, vol $360.09M), pump-fun -0.4% (mcap $806.32M, vol $115.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.7k | $740.6k | 2.9 d | h24 +43% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $115.9k | $488.1k | 11.8 h | h24 +180% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $95.8k | $86.8k | 3.5 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $129.3k | $2.93M | 6.6 h | h24 +2577% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.4% (+6.7) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.4k | $2.18M | 6.3 h | h24 +6031% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $17.98M | 744.5 d | h24 +0% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,540 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.99M | $639.7k | 159.1 d | h24 +20% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,455 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.24M | $85.07B | 120.7 d | h24 +476710% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,801 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.4k | $2.18M | +13% | +298% | +6031% | 10.8x | liq/mcap 4.9% | 66 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $129.3k | $2.93M | +10% | +139% | +2577% | 16.7x | liq/mcap 4.4% | 66 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $57.0k | $493.0k | +13% | +65% | +1631% | 40.7x | churn 41x vol/liq | 45 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.3k | $122.4k | +1% | -30% | +1675% | 119.9x | thin liq $36.3k; churn 120x vol/liq | not scored |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $143.4k | $3.48M | +251% | +209% | +82% | 10.0x | liq/mcap 4.1%; spike (+251% 1h, +209% 6h) | not scored |
| [CLAUDIO](https://pump.fun/coin/5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump) | `5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump` | $23.0k | $92.8k | +52% | +165% | +4% | 149.6x | thin liq $23.0k; churn 150x vol/liq | not scored |

_Timing: total 156s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 82.9s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
