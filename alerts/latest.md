# Last scan 2026-11-24T07:50:58Z - mode: helius (box heartbeat stale (224 min); budget 130/3000)

```
[fast_scan] 112 candidate mints from 9 source tags; 110 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored ROCKET in 73s
[fast_scan] scored DBR in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored JENSEN in 82s
[fast_scan] scored NVDA in 82s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored ACHI in 82s
[fast_scan] scored SuperELON in 83s
# Market scan 2026-11-24 07:50 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,404 (-1.7% 24h), ETH $1,699 (-1.3% 24h), SOL $71.51 (-0.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $1.90B, vol $347.75M), pump-fun -1.0% (mcap $811.21M, vol $112.67M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $81.1k | $782.1k | 2.8 d | h24 +72% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 48* | CAUTION | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $52.5k | $486.2k | 14.0 h | h24 +459% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB) | `BjnedHtjNn2MeXopH5RHckbkoHyRaRMQrd7qMw93FZB` | $195.3k | $108.3k | 1.0 h | h24 +36% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $85.9k | $83.4k | 2.5 h | h24 +88% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $81.2k | $453.3k | 10.7 h | h24 +1491% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [DBR](https://dexscreener.com/solana/DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5) | `DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5` | $5.37M | $100.11M | 852.7 d | h24 +13% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.6); GATES FAILED: rug-funder link; holders 197,958 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $2.00M | $643.4k | 159.0 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,494 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.25M | $85.88B | 120.6 d | h24 +470703% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,795 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $102.9k | $2.01M | +5% | +5539% | +5539% | 10.7x | spike (+5% 1h, +5539% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $122.6k | $2.64M | -15% | +2308% | +2308% | 17.3x | liq/mcap 4.6%; spike (-15% 1h, +2308% 6h) | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $54.6k | $456.6k | +36% | +132% | +1503% | 39.8x | churn 40x vol/liq | 55 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.8k | $125.3k | -2% | -23% | +1560% | 118.0x | thin liq $36.8k; churn 118x vol/liq | not scored |
| [Satoshi](https://pump.fun/coin/DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump) | `DXkCsXhXeh2xTfQ8Um8dicQcwseTfuHvDwriTcJLpump` | $19.0k | $76.1k | +163% | +163% | +163% | 15.0x | thin liq $19.0k; spike (+163% 1h, +163% 6h); < 1h old | not scored |
| [CLAUDIO](https://pump.fun/coin/5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump) | `5St93zSNQvWxK22Cj5mJBXcjUNNB452h5uNmrttSpump` | $19.3k | $66.8k | +86% | -96% | -25% | 177.7x | thin liq $19.3k; churn 178x vol/liq | not scored |

_Timing: total 156s (discovery 71.9s, screen 1.1s, GT prime 0.5s, scoring 82.6s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/163; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
