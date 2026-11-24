# Last scan 2026-11-24T11:42:19Z - mode: helius (box heartbeat stale (455 min); budget 414/3000)

```
[fast_scan] 111 candidate mints from 10 source tags; 107 with pair data; 24 >= $50,000 liq; 12 pass survivor pre-gates (72s)
[fast_scan] scored ACHI in 72s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored GROKIA in 82s
[fast_scan] scored NOHR in 82s
[fast_scan] scored ROCKET in 83s
[fast_scan] scored TRON-USDT in 83s
[fast_scan] scored MCAT in 86s
[fast_scan] scored USDT-ERC20 in 87s
[fast_scan] scored pippin in 72s
# Market scan 2026-11-24 11:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,851 (-2.5% 24h), ETH $1,689 (-2.2% 24h), SOL $70.28 (-3.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.6% (mcap $1.83B, vol $364.77M), pump-fun -5.4% (mcap $770.57M, vol $124.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $77.9k | $728.0k | 3.0 d | h24 +28% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $74.2k | $176.7k | 1.9 d | h24 -50% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $135.9k | $124.6k | 6.3 h | h24 +180% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $145.6k | $3.64M | 2.8 d | h24 +125% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.0% (+7.2); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $142.5k | $3.59M | 9.4 h | h24 +3181% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.0% (+7.2) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $105.9k | $2.14M | 9.1 h | h24 +5918% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [TRON-USDT](https://dexscreener.com/solana/JEJBCQ451WSHS73vzVH843qSvWySWudXfuC3hANnbr6L) | `JEJBCQ451WSHS73vzVH843qSvWySWudXfuC3hANnbr6L` | $209.71M | $210.07M | 24.7 d | h24 +0% | #7 unknown (+3); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 61 (growth n/a: first sighting) |
| 38* | CAUTION | [USDT-ERC20](https://dexscreener.com/solana/WXxZMqHEPsbA91HYuAvtGM4eh5d2LC5tjqEktXVjbs6) | `WXxZMqHEPsbA91HYuAvtGM4eh5d2LC5tjqEktXVjbs6` | $209.71M | $210.07M | 24.7 d | h24 -0% | #7 unknown (+3); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 58 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.36M | $17.79M | 744.6 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,548 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $106.1k | $2.15M | +4% | -2% | +5944% | 12.5x | liq/mcap 4.9% | 66 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $143.0k | $3.62M | +8% | +40% | +3203% | 16.2x | liq/mcap 4.0% | 66 |
| [FoolCoin](https://pump.fun/coin/8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump) | `8RKV9GyNmhQAVaKVEYK9tBMWkJy7BAJ5JpXAsSV8pump` | $13.0k | $37.5k | +502% | +30% | +30% | 22.1x | thin liq $13.0k; spike (+502% 1h, +30% 6h) | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $48.6k | $362.3k | -10% | +11% | +1172% | 50.7x | thin liq $48.6k; churn 51x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $25.9k | $66.6k | -1% | -49% | +926% | 169.6x | thin liq $25.9k; churn 170x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $48.5k | $421.7k | +7% | -15% | +385% | 52.0x | thin liq $48.5k; churn 52x vol/liq | not scored |

_Timing: total 216s (discovery 71.0s, screen 1.2s, GT prime 0.3s, scoring 143.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/189; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
