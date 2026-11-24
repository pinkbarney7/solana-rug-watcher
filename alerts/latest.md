# Last scan 2026-11-24T10:27:33Z - mode: helius (box heartbeat stale (380 min); budget 284/3000)

```
[fast_scan] 110 candidate mints from 9 source tags; 108 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored GROKIA in 72s
[fast_scan] scored DOG in 81s
[fast_scan] scored ACHI in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored NOHR in 82s
[fast_scan] scored NVDA in 83s
[fast_scan] scored DONJENSEN in 83s
[fast_scan] scored ROCKET in 83s
[fast_scan] scored CLAUDIA in 72s
# Market scan 2026-11-24 10:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,904 (-2.3% 24h), ETH $1,685 (-2.0% 24h), SOL $70.75 (-2.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.0% (mcap $1.84B, vol $355.75M), pump-fun -4.0% (mcap $778.75M, vol $127.47M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.3k | $770.7k | 2.9 d | h24 +42% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/HHHBrDuje8KVMrw3G9PHrh3P5HN2Pvj2akykhdSRBRAg) | `HHHBrDuje8KVMrw3G9PHrh3P5HN2Pvj2akykhdSRBRAg` | $193.7k | $107.5k | 1.1 h | h24 +36% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $144.3k | $3.55M | 2.8 d | h24 +95% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.1% (+7.1); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $120.1k | $111.9k | 5.1 h | h24 +152% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.3k | $2.07M | 7.9 h | h24 +5719% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.0% (+6) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $143.1k | $3.61M | 8.2 h | h24 +3196% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.0% (+7.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.65M | 120.8 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,835 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.74M | $621.5k | 159.1 d | h24 +16% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,372 (growth n/a: first sighting) |
| 67* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.84M | $78.60B | 48.4 d | h24 +814197% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 61,362 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.3k | $2.07M | -8% | +2% | +5719% | 12.2x | none flagged (still high risk) | 60 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $143.1k | $3.61M | +24% | +63% | +3196% | 15.6x | liq/mcap 4.0% | 66 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $27.2k | $72.7k | -34% | -45% | +1090% | 160.8x | thin liq $27.2k; churn 161x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $49.1k | $368.9k | -8% | +7% | +1195% | 49.1x | thin liq $49.1k; churn 49x vol/liq | not scored |
| [Rockstar](https://pump.fun/coin/3T9e85d5yZMxSYZWGVaq95MoQrPoeGMchRohWaqFpump) | `3T9e85d5yZMxSYZWGVaq95MoQrPoeGMchRohWaqFpump` | $18.8k | $76.6k | +135% | +169% | +169% | 3.1x | thin liq $18.8k; spike (+135% 1h, +169% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $51.2k | $467.5k | +68% | -30% | +438% | 48.7x | churn 49x vol/liq | not scored |

_Timing: total 217s (discovery 71.7s, screen 1.3s, GT prime 0.4s, scoring 143.9s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
