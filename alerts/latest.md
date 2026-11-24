# Last scan 2026-11-24T08:48:05Z - mode: helius (box heartbeat stale (282 min); budget 160/3000)

```
[fast_scan] 111 candidate mints from 9 source tags; 108 with pair data; 27 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored ROCKET in 73s
[fast_scan] scored ACHI in 80s
[fast_scan] scored GROKIA in 80s
[fast_scan] scored pippin in 80s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored NVDA in 81s
# Market scan 2026-11-24 08:48 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,174 (-2.0% 24h), ETH $1,694 (-1.6% 24h), SOL $71.29 (-1.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $1.88B, vol $360.09M), pump-fun -0.4% (mcap $806.32M, vol $115.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.8k | $741.1k | 2.9 d | h24 +40% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $93.5k | $83.7k | 3.5 h | h24 +88% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $116.9k | $543.8k | 11.7 h | h24 +1809% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $133.2k | $3.11M | 6.5 h | h24 +2740% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.3% (+6.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.41M | $18.07M | 744.5 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,540 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.99M | $640.1k | 159.1 d | h24 +20% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,453 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.23M | $85.07B | 120.7 d | h24 +476710% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 436,801) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.5k | $2.07M | +1% | +334% | +5712% | 11.1x | spike (+1% 1h, +334% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $133.2k | $3.11M | +14% | +237% | +2740% | 16.1x | liq/mcap 4.3% | 66 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $59.9k | $540.5k | +11% | +79% | +1798% | 38.7x | churn 39x vol/liq | 55 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.4k | $123.0k | -1% | -28% | +1683% | 119.6x | thin liq $36.4k; churn 120x vol/liq | not scored |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $144.1k | $3.52M | +257% | +224% | +102% | 10.0x | liq/mcap 4.1%; spike (+257% 1h, +224% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $44.0k | $346.7k | -28% | -60% | +299% | 55.4x | thin liq $44.0k; churn 55x vol/liq | not scored |

_Timing: total 155s (discovery 71.9s, screen 1.1s, GT prime 0.4s, scoring 81.4s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
