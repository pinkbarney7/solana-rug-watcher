# Last scan 2026-11-24T09:15:03Z - mode: helius (box heartbeat stale (308 min); budget 170/3000)

```
[fast_scan] 112 candidate mints from 9 source tags; 110 with pair data; 27 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored NOHR in 72s
[fast_scan] scored ACHI in 80s
[fast_scan] scored NVDA in 81s
[fast_scan] scored DBR in 82s
[fast_scan] scored GROKIA in 82s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored SuperELON in 83s
[fast_scan] scored ROCKET in 84s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-24 09:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,845 (-2.7% 24h), ETH $1,680 (-2.7% 24h), SOL $70.70 (-2.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.5% (mcap $1.85B, vol $357.89M), pump-fun -3.3% (mcap $782.93M, vol $114.35M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.7k | $740.4k | 2.9 d | h24 +33% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $112.9k | $414.9k | 12.1 h | h24 +138% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB) | `BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB` | $223.4k | $129.6k | 2.4 h | h24 +62% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $97.0k | $86.0k | 3.9 h | h24 +94% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $142.9k | $3.48M | 2.7 d | h24 +79% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.1% (+7.1); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $128.2k | $2.90M | 7.0 h | h24 +2550% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.4% (+6.7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.22M | 120.7 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,822 (growth n/a: first sighting) |
| 59* | SKIP | [DBR](https://dexscreener.com/solana/DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5) | `DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5` | $5.30M | $98.91M | 852.7 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.6); GATES FAILED: rug-funder link; holders 197,960 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.97M | $627.1k | 159.1 d | h24 +17% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,437 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $113.1k | $2.44M | +21% | +124% | +6754% | 10.4x | liq/mcap 4.6% | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $128.2k | $2.91M | +12% | +137% | +2556% | 16.9x | liq/mcap 4.4% | 66 |
| [scamsem](https://pump.fun/coin/4pf9HEnkdN3ihjVbfZg2NwbZkCJyUk4na44oysuWpump) | `4pf9HEnkdN3ihjVbfZg2NwbZkCJyUk4na44oysuWpump` | $27.3k | $120.6k | +346% | +346% | +346% | 16.3x | thin liq $27.3k; spike (+346% 1h, +346% 6h); < 1h old | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $34.8k | $115.1k | -1% | -28% | +1569% | 125.1x | thin liq $34.8k; churn 125x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $53.7k | $442.1k | -9% | +78% | +1452% | 43.6x | churn 44x vol/liq | 45 |
| [CLAUDIO](https://pump.fun/coin/5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump) | `5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump` | $24.8k | $107.7k | +79% | +164% | +21% | 139.3x | thin liq $24.8k; churn 139x vol/liq | not scored |

_Timing: total 216s (discovery 71.6s, screen 1.1s, GT prime 0.3s, scoring 143.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/179; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
