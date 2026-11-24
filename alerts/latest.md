# Last scan 2026-11-24T08:08:11Z - mode: helius (box heartbeat stale (242 min); budget 150/3000)

```
[fast_scan] 112 candidate mints from 9 source tags; 110 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored SuperELON in 71s
[fast_scan] scored ACHI in 79s
[fast_scan] scored NVDA in 80s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored DBR in 81s
[fast_scan] scored ROCKET in 81s
[fast_scan] scored pippin in 81s
# Market scan 2026-11-24 08:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,346 (-1.6% 24h), ETH $1,696 (-1.4% 24h), SOL $71.42 (-0.8% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.5% (mcap $1.89B, vol $344.26M), pump-fun +0.3% (mcap $809.59M, vol $109.67M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $81.8k | $795.3k | 2.9 d | h24 +69% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB) | `BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB` | $203.9k | $113.5k | 1.3 h | h24 +42% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $88.3k | $83.6k | 2.8 h | h24 +88% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $108.7k | $497.4k | 11.0 h | h24 +1646% | #9 Price momentum FAIL (+14); #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.42M | $18.20M | 744.5 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,543 (growth n/a: first sighting) |
| 59* | SKIP | [DBR](https://dexscreener.com/solana/DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5) | `DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5` | $5.37M | $100.26M | 852.7 d | h24 +13% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.6); GATES FAILED: rug-funder link; holders 197,963 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $2.00M | $643.4k | 159.0 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,474 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $100.8k | $1.93M | +4% | +5323% | +5323% | 11.1x | spike (+4% 1h, +5323% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $123.5k | $2.68M | -16% | +2347% | +2347% | 17.2x | liq/mcap 4.6%; spike (-16% 1h, +2347% 6h) | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $57.4k | $500.3k | +61% | +133% | +1656% | 39.4x | churn 39x vol/liq | 59 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $35.5k | $116.6k | -7% | -28% | +1444% | 122.6x | thin liq $35.5k; churn 123x vol/liq | not scored |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $136.5k | $3.17M | +319% | +180% | +42% | 9.9x | liq/mcap 4.3%; spike (+319% 1h, +180% 6h) | not scored |
| [Satoshi](https://pump.fun/coin/DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump) | `DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump` | $20.6k | $81.5k | +199% | +199% | +199% | 20.0x | thin liq $20.6k; spike (+199% 1h, +199% 6h); < 1h old | not scored |

_Timing: total 155s (discovery 71.9s, screen 1.2s, GT prime 0.4s, scoring 81.4s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
