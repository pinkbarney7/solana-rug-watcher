# Last scan 2026-11-24T06:11:21Z - mode: helius (box heartbeat stale (125 min); budget 40/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 113 with pair data; 19 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored SuperELON in 69s
[fast_scan] scored TROLL in 77s
[fast_scan] scored CATE in 77s
[fast_scan] scored NVDA in 78s
[fast_scan] scored ROCKET in 79s
# Market scan 2026-11-24 06:11 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,405 (-2.0% 24h), ETH $1,699 (-1.7% 24h), SOL $71.53 (-0.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.1% (mcap $1.91B, vol $364.37M), pump-fun +1.8% (mcap $817.45M, vol $117.41M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $75.1k | $672.9k | 2.8 d | h24 -22% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [SuperELON](https://dexscreener.com/solana/FSZNDcPapEDDLgCbYyMMXh8e5CQTuSbg74kY41Tdc2Qy) | `FSZNDcPapEDDLgCbYyMMXh8e5CQTuSbg74kY41Tdc2Qy` | $199.1k | $111.1k | 1.1 h | h24 +40% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $17.31M | 120.6 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.93M | $20.09M | 843.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,705 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.79M | $644.0k | 159.0 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,610 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.3k | $2.19M | +15% | +6047% | +6047% | 9.3x | liq/mcap 4.9%; spike (+15% 1h, +6047% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $129.2k | $2.93M | +22% | +2575% | +2575% | 15.9x | liq/mcap 4.4%; spike (+22% 1h, +2575% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $37.3k | $128.5k | -6% | -21% | +1603% | 116.1x | thin liq $37.3k; churn 116x vol/liq | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $182.0k | $146.3k | +229% | +229% | +229% | 39.1x | churn 39x vol/liq; spike (+229% 1h, +229% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $42.9k | $286.7k | -22% | +22% | +906% | 48.2x | thin liq $42.9k; churn 48x vol/liq | not scored |
| [ORBLUX](https://pump.fun/coin/5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump) | `5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump` | $18.8k | $73.7k | +157% | +157% | +157% | 8.8x | thin liq $18.8k; spike (+157% 1h, +157% 6h); < 1h old | not scored |

_Timing: total 152s (discovery 71.5s, screen 1.1s, GT prime 0.4s, scoring 79.3s for 5 coins, 5 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 5/110; Helius 429s 65; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
