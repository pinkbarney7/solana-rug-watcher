# Last scan 2026-11-24T06:19:41Z - mode: helius (box heartbeat stale (133 min); budget 50/3000)

```
[fast_scan] 111 candidate mints from 9 source tags; 108 with pair data; 20 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored SuperELON in 68s
[fast_scan] scored NVDA in 77s
[fast_scan] scored CATE in 77s
[fast_scan] scored TROLL in 78s
[fast_scan] scored ROCKET in 79s
# Market scan 2026-11-24 06:19 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,427 (-2.1% 24h), ETH $1,699 (-1.7% 24h), SOL $71.61 (-0.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.1% (mcap $1.91B, vol $364.37M), pump-fun +1.8% (mcap $817.45M, vol $117.41M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $75.9k | $686.2k | 2.8 d | h24 -21% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/FSZNDcPapEDDLgCbYyMMXh8e5CQTuSbg74kY41Tdc2Qy) | `FSZNDcPapEDDLgCbYyMMXh8e5CQTuSbg74kY41Tdc2Qy` | $203.6k | $113.7k | 1.3 h | h24 +43% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.93M | $19.97M | 843.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,705 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.79M | $643.7k | 159.0 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,599 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.28M | $86.77B | 120.6 d | h24 +455945% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $106.9k | $2.17M | +15% | +5990% | +5990% | 9.4x | liq/mcap 4.9%; spike (+15% 1h, +5990% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $127.9k | $2.87M | +10% | +2519% | +2519% | 16.1x | liq/mcap 4.5%; spike (+10% 1h, +2519% 6h) | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $104.2k | $159.2k | +258% | +258% | +258% | 76.6x | churn 77x vol/liq; spike (+258% 1h, +258% 6h); < 1h old | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.3k | $122.3k | -11% | -19% | +1519% | 119.3x | thin liq $36.3k; churn 119x vol/liq | not scored |
| [ORBLUX](https://pump.fun/coin/5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump) | `5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump` | $21.1k | $91.1k | +218% | +218% | +218% | 9.2x | thin liq $21.1k; spike (+218% 1h, +218% 6h); < 1h old | not scored |
| [yippee](https://pump.fun/coin/3mTQnHtok9wnT7yDA1G9BfMh5xNbyQerYkpfTDyKpump) | `3mTQnHtok9wnT7yDA1G9BfMh5xNbyQerYkpfTDyKpump` | $10.2k | $24.7k | +299% | -14% | -14% | 12.8x | thin liq $10.2k; spike (+299% 1h, -14% 6h) | not scored |

_Timing: total 153s (discovery 71.8s, screen 1.2s, GT prime 0.3s, scoring 79.2s for 5 coins, 5 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/110; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
