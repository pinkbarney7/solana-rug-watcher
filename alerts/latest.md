# Last scan 2026-11-24T12:12:18Z - mode: helius (box heartbeat stale (485 min); budget 454/3000)

```
[fast_scan] 106 candidate mints from 10 source tags; 103 with pair data; 23 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored ACHI in 72s
[fast_scan] scored GROKIA in 80s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored ON in 82s
[fast_scan] scored pippin in 83s
[fast_scan] scored COPIUM in 84s
[fast_scan] scored MCAT in 84s
[fast_scan] scored NVDA in 73s
# Market scan 2026-11-24 12:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,230 (-1.8% 24h), ETH $1,698 (-1.4% 24h), SOL $70.67 (-2.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.2% (mcap $1.84B, vol $373.65M), pump-fun -4.8% (mcap $775.21M, vol $132.15M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $76.1k | $184.6k | 2.0 d | h24 -50% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 44* | CAUTION | [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $68.8k | $806.1k | 1.6 d | h24 +28% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [ON](https://dexscreener.com/solana/3oQ4NUo8Gk7dFgo4nZUT6tNTCf6aHG3b7LfdNzrEbkNZ) | `3oQ4NUo8Gk7dFgo4nZUT6tNTCf6aHG3b7LfdNzrEbkNZ` | $210.0k | $118.7k | 1.6 h | h24 +51% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $152.7k | $148.2k | 6.8 h | h24 +234% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $136.8k | $3.29M | 9.9 h | h24 +2906% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.2% (+7) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $108.3k | $2.22M | 9.6 h | h24 +6142% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.60M | 120.8 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,891 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.36M | $17.68M | 744.7 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,548 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.91M | $615.4k | 159.2 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,474 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $108.0k | $2.21M | +7% | +1% | +6110% | 12.5x | liq/mcap 4.9% | 66 |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $41.6k | $293.6k | +371% | +981% | +981% | 27.4x | thin liq $41.6k; churn 27x vol/liq; spike (+371% 1h, +981% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $136.8k | $3.29M | +4% | +12% | +2906% | 17.0x | liq/mcap 4.2% | 66 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $26.5k | $69.4k | +18% | -46% | +1001% | 166.1x | thin liq $26.5k; churn 166x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $46.4k | $328.6k | -16% | +12% | +1053% | 53.4x | thin liq $46.4k; churn 53x vol/liq | not scored |
| [FoolCoin](https://pump.fun/coin/8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump) | `8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump` | $12.5k | $34.5k | +295% | +19% | +19% | 23.9x | thin liq $12.5k; spike (+295% 1h, +19% 6h) | not scored |

_Timing: total 217s (discovery 70.7s, screen 1.1s, GT prime 0.4s, scoring 145.2s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/179; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
