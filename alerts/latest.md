# Last scan 2026-11-24T08:20:55Z - mode: helius (box heartbeat stale (254 min); budget 150/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 111 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 71s
[fast_scan] scored SuperELON in 79s
[fast_scan] scored ACHI in 79s
[fast_scan] scored NVDA in 80s
[fast_scan] scored DBR in 80s
[fast_scan] scored pippin in 81s
[fast_scan] scored ROCKET in 82s
# Market scan 2026-11-24 08:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,263 (-1.5% 24h), ETH $1,695 (-1.2% 24h), SOL $71.40 (-0.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $1.88B, vol $348.53M), pump-fun +0.2% (mcap $808.71M, vol $115.92M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $81.8k | $795.1k | 2.9 d | h24 +57% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB) | `BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB` | $210.0k | $117.7k | 1.5 h | h24 +47% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $87.2k | $78.7k | 3.0 h | h24 +77% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $110.3k | $490.0k | 11.2 h | h24 +1620% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.41M | $18.02M | 744.5 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,541 (growth n/a: first sighting) |
| 59* | SKIP | [DBR](https://dexscreener.com/solana/DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5) | `DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5` | $5.36M | $99.97M | 852.7 d | h24 +13% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.6); GATES FAILED: rug-funder link; holders 197,963 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.99M | $643.2k | 159.0 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,467 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $99.2k | $1.87M | -6% | +5148% | +5148% | 11.4x | spike (-6% 1h, +5148% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $127.8k | $2.87M | -5% | +674% | +2519% | 16.7x | liq/mcap 4.5%; spike (-5% 1h, +674% 6h) | not scored |
| [Satoshi](https://pump.fun/coin/DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump) | `DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump` | $20.6k | $81.5k | +634% | +199% | +199% | 22.2x | thin liq $20.6k; spike (+634% 1h, +199% 6h) | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $56.6k | $487.4k | +32% | +130% | +1611% | 40.3x | churn 40x vol/liq | 55 |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $146.9k | $3.65M | +383% | +212% | +86% | 9.8x | liq/mcap 4.0%; spike (+383% 1h, +212% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.3k | $121.9k | -2% | -31% | +1515% | 119.8x | thin liq $36.3k; churn 120x vol/liq | not scored |

_Timing: total 155s (discovery 71.6s, screen 1.1s, GT prime 0.2s, scoring 82.0s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
