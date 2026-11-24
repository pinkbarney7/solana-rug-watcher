# Last scan 2026-11-24T10:47:59Z - mode: helius (box heartbeat stale (400 min); budget 304/3000)

```
[fast_scan] 109 candidate mints from 9 source tags; 106 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored NOHR in 72s
[fast_scan] scored pippin in 80s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored GROKIA in 82s
[fast_scan] scored CATE in 82s
[fast_scan] scored ACHI in 83s
[fast_scan] scored ROCKET in 84s
[fast_scan] scored NVDA in 71s
# Market scan 2026-11-24 10:47 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,676 (-2.6% 24h), ETH $1,681 (-2.2% 24h), SOL $70.44 (-2.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.8% (mcap $1.84B, vol $353.20M), pump-fun -4.2% (mcap $775.67M, vol $125.32M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.4k | $771.5k | 3.0 d | h24 +39% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $143.6k | $3.53M | 2.8 d | h24 +116% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.1% (+7.1); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $121.0k | $109.4k | 5.4 h | h24 +146% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $101.1k | $393.0k | 13.7 h | h24 +1280% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.4k | $2.08M | 8.2 h | h24 +5748% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.0% (+6) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $136.4k | $3.30M | 8.5 h | h24 +2910% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.1% (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.61M | $16.55M | 120.8 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,874 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.35M | $17.68M | 744.6 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,546 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.94M | $615.0k | 159.1 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,345 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.4k | $2.08M | -5% | -1% | +5748% | 12.3x | none flagged (still high risk) | 60 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $137.3k | $3.34M | +4% | +25% | +2947% | 16.4x | liq/mcap 4.1% | 66 |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $25.0k | $126.8k | +343% | +343% | +343% | 19.8x | thin liq $25.0k; spike (+343% 1h, +343% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $51.6k | $406.9k | -4% | +16% | +1328% | 47.1x | churn 47x vol/liq | 55 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $27.2k | $73.0k | -30% | -49% | +1069% | 161.3x | thin liq $27.2k; churn 161x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $50.6k | $458.7k | +68% | -39% | +428% | 49.4x | churn 49x vol/liq | not scored |

_Timing: total 216s (discovery 71.6s, screen 1.1s, GT prime 0.2s, scoring 143.1s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
