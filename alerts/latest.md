# Last scan 2026-11-24T11:45:49Z - mode: helius (box heartbeat stale (459 min); budget 434/3000)

```
[fast_scan] 108 candidate mints from 10 source tags; 105 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored ACHI in 71s
[fast_scan] scored GROKIA in 79s
[fast_scan] scored CATE in 80s
[fast_scan] scored NOHR in 80s
[fast_scan] scored NVDA in 81s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored pippin in 81s
# Market scan 2026-11-24 11:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,806 (-2.6% 24h), ETH $1,688 (-2.2% 24h), SOL $70.22 (-3.3% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.6% (mcap $1.83B, vol $364.77M), pump-fun -5.4% (mcap $770.57M, vol $124.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $139.8k | $130.9k | 6.4 h | h24 +195% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $146.7k | $3.69M | 2.9 d | h24 +124% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.0% (+7.2); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $146.6k | $3.80M | 9.5 h | h24 +3373% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 3.9% (+7.4) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.4k | $2.20M | 9.2 h | h24 +6088% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.60M | $16.31M | 120.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 436,891) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.35M | $17.77M | 744.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,545 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.91M | $619.1k | 159.2 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders +0.0% in 1h (now 46,346) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.4k | $2.20M | +7% | +0% | +6088% | 12.4x | liq/mcap 4.9% | 66 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $146.6k | $3.80M | +13% | +41% | +3373% | 15.8x | liq/mcap 3.9% | 66 |
| [FoolCoin](https://pump.fun/coin/8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump) | `8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump` | $14.0k | $42.9k | +534% | +48% | +48% | 20.7x | thin liq $14.0k; spike (+534% 1h, +48% 6h) | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $49.9k | $381.6k | -6% | +18% | +1240% | 49.4x | thin liq $49.9k; churn 49x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $26.4k | $68.7k | -6% | -47% | +958% | 166.6x | thin liq $26.4k; churn 167x vol/liq | not scored |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $146.7k | $3.69M | +4% | +265% | +119% | 8.7x | liq/mcap 4.0% | 56 |

_Timing: total 154s (discovery 71.4s, screen 1.1s, GT prime 0.5s, scoring 81.2s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/137; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
