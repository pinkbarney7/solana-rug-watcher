# Last scan 2026-11-24T06:39:05Z - mode: helius (box heartbeat stale (153 min); budget 60/3000)

```
[fast_scan] 114 candidate mints from 10 source tags; 112 with pair data; 21 >= $50,000 liq; 8 pass survivor pre-gates (72s)
[fast_scan] scored ACHI in 71s
[fast_scan] scored CATE in 79s
[fast_scan] scored NVDA in 80s
[fast_scan] scored SuperJense in 80s
[fast_scan] scored TROLL in 81s
[fast_scan] scored ROCKET in 81s
[fast_scan] scored JENSEN in 82s
# Market scan 2026-11-24 06:39 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,421 (-1.5% 24h), ETH $1,700 (-1.1% 24h), SOL $71.68 (+0.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.2% (mcap $1.91B, vol $362.58M), pump-fun +1.8% (mcap $817.26M, vol $115.62M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $77.2k | $709.0k | 2.8 d | h24 -16% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 48* | CAUTION | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $50.7k | $453.1k | 12.8 h | h24 +421% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $169.6k | $110.4k | 1.1 h | h24 +116% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $96.4k | $129.1k | 1.3 h | h24 +191% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.94M | $20.19M | 843.8 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,683 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.99M | $641.9k | 159.0 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,560 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.28M | $86.77B | 120.6 d | h24 +460861% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $99.9k | $1.89M | -14% | +5215% | +5215% | 10.2x | spike (-14% 1h, +5215% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $135.1k | $3.19M | +27% | +2812% | +2812% | 15.3x | liq/mcap 4.2%; spike (+27% 1h, +2812% 6h) | not scored |
| [ORBLUX](https://pump.fun/coin/5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump) | `5KDyvAjSU8HWofZfVnpkdY2N4UM1R2jxUkLupYmgpump` | $20.0k | $81.5k | +924% | +184% | +184% | 13.0x | thin liq $20.0k; spike (+924% 1h, +184% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $35.6k | $117.6k | -11% | -32% | +1458% | 121.8x | thin liq $35.6k; churn 122x vol/liq | not scored |
| [Aircoin](https://pump.fun/coin/ntHUtpTDBYpDknJUHhLRPbdN8GrR3p5PCyvTWwwpump) | `ntHUtpTDBYpDknJUHhLRPbdN8GrR3p5PCyvTWwwpump` | $20.3k | $86.7k | +190% | +190% | +190% | 12.8x | thin liq $20.3k; spike (+190% 1h, +190% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $45.8k | $324.4k | -8% | +64% | +1039% | 45.6x | thin liq $45.8k; churn 46x vol/liq | not scored |

_Timing: total 155s (discovery 70.9s, screen 1.1s, GT prime 0.2s, scoring 82.4s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/147; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
