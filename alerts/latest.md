# Last scan 2026-11-24T07:17:31Z - mode: helius (box heartbeat stale (191 min); budget 110/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 113 with pair data; 27 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored ACHI in 72s
[fast_scan] scored SuperJense in 81s
[fast_scan] scored ACHI in 81s
[fast_scan] scored NVDA in 81s
[fast_scan] scored TROLL in 82s
[fast_scan] scored CATE in 83s
[fast_scan] scored ROCKET in 85s
[fast_scan] scored JENSEN in 86s
# Market scan 2026-11-24 07:17 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,386 (-1.7% 24h), ETH $1,698 (-1.6% 24h), SOL $71.73 (-0.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.4% (mcap $1.90B, vol $363.39M), pump-fun +1.5% (mcap $816.29M, vol $114.95M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.8k | $774.2k | 2.8 d | h24 +2% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 48* | CAUTION | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $52.2k | $480.1k | 13.5 h | h24 +452% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $205.6k | $143.6k | 1.7 h | h24 +181% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $93.3k | $108.4k | 1.9 h | h24 +144% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/CTBuzBkKqjyXthSHNWcN9tKTsJ1PY15HnT7pZfTpwfC) | `CTBuzBkKqjyXthSHNWcN9tKTsJ1PY15HnT7pZfTpwfC` | $105.6k | $60.7k | 1.3 h | h24 +62% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.94M | $20.16M | 843.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,713 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $2.00M | $645.4k | 159.0 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,482 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.27M | $87.19B | 120.6 d | h24 +463707% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $98.6k | $1.84M | -15% | +5073% | +5073% | 10.8x | spike (-15% 1h, +5073% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $139.6k | $3.41M | +14% | +3011% | +3011% | 14.9x | liq/mcap 4.1%; spike (+14% 1h, +3011% 6h) | not scored |
| [JIMMY](https://dexscreener.com/solana/DmCzraz35Ah3WQbpJLtSw6dUZSYggTAhzFwiT8zbngRW) | `DmCzraz35Ah3WQbpJLtSw6dUZSYggTAhzFwiT8zbngRW` | $30.1k | $34.5k | +491% | +491% | +491% | 17.9x | thin liq $30.1k; spike (+491% 1h, +491% 6h); < 1h old | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $37.0k | $126.1k | +4% | -15% | +1570% | 117.3x | thin liq $37.0k; churn 117x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $47.2k | $343.8k | +18% | +61% | +1107% | 44.8x | thin liq $47.2k; churn 45x vol/liq | not scored |
| [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $205.7k | $143.6k | +58% | +181% | +181% | 57.3x | churn 57x vol/liq | 53 |

_Timing: total 159s (discovery 71.7s, screen 1.2s, GT prime 0.4s, scoring 85.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
