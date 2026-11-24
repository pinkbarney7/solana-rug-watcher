# Last scan 2026-11-24T12:35:47Z - mode: helius (box heartbeat stale (509 min); budget 484/3000)

```
[fast_scan] 105 candidate mints from 9 source tags; 102 with pair data; 23 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored ACHI in 72s
[fast_scan] scored Bullseye in 81s
[fast_scan] scored GROKIA in 81s
[fast_scan] scored MCAT in 82s
[fast_scan] scored DONJENSEN in 82s
[fast_scan] scored pippin in 83s
[fast_scan] scored CATE in 83s
[fast_scan] scored NVDA in 83s
# Market scan 2026-11-24 12:35 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,189 (-1.7% 24h), ETH $1,696 (-1.3% 24h), SOL $70.49 (-2.4% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.5% (mcap $1.83B, vol $372.06M), pump-fun -5.0% (mcap $773.81M, vol $132.80M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $76.6k | $187.8k | 2.0 d | h24 -49% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [Bullseye](https://dexscreener.com/solana/DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe) | `DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe` | $160.0k | $102.4k | 1.0 h | h24 +105% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $158.0k | $153.0k | 7.2 h | h24 +244% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $136.7k | $3.30M | 10.3 h | h24 +2910% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.1% (+7) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.0k | $2.18M | 10.0 h | h24 +6010% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.36M | 120.8 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,879 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.35M | $17.64M | 744.7 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,547 (growth n/a: first sighting) |
| 66* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.91M | $614.4k | 159.2 d | h24 +16% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 46,458 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $45.6k | $345.2k | +892% | +1171% | +1171% | 30.2x | thin liq $45.6k; churn 30x vol/liq; spike (+892% 1h, +1171% 6h) | not scored |
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $107.7k | $2.20M | +3% | +13% | +6089% | 12.7x | liq/mcap 4.9% | 66 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $136.1k | $3.27M | -7% | +2% | +2886% | 17.2x | liq/mcap 4.2% | 66 |
| [Unemployed](https://pump.fun/coin/FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump) | `FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump` | $23.5k | $115.4k | +302% | +302% | +302% | 12.1x | thin liq $23.5k; spike (+302% 1h, +302% 6h); < 1h old | not scored |
| [SHHFT](https://dexscreener.com/solana/GqMg4TRt5U5HRK6oeZYwCF1Jz7Ym9MSzWSoFCtFsbzf6) | `GqMg4TRt5U5HRK6oeZYwCF1Jz7Ym9MSzWSoFCtFsbzf6` | $26.6k | $106.9k | +268% | +268% | +268% | 5.6x | thin liq $26.6k; spike (+268% 1h, +268% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $48.8k | $362.7k | -6% | +9% | +1173% | 51.1x | thin liq $48.8k; churn 51x vol/liq | not scored |

_Timing: total 156s (discovery 71.5s, screen 1.2s, GT prime 0.4s, scoring 82.9s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/158; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
