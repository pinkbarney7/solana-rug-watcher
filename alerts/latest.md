# Last scan 2026-11-24T12:20:17Z - mode: helius (box heartbeat stale (494 min); budget 474/3000)

```
[fast_scan] 105 candidate mints from 9 source tags; 102 with pair data; 27 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored GROKIA in 72s
[fast_scan] scored ON in 80s
[fast_scan] scored SPCX in 80s
[fast_scan] scored DONJENSEN in 81s
[fast_scan] scored pippin in 81s
[fast_scan] scored CATE in 82s
[fast_scan] scored ACHI in 82s
[fast_scan] scored COPIUM in 83s
# Market scan 2026-11-24 12:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,188 (-1.8% 24h), ETH $1,695 (-1.5% 24h), SOL $70.52 (-2.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.2% (mcap $1.84B, vol $373.65M), pump-fun -4.8% (mcap $775.21M, vol $132.15M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $67.9k | $787.3k | 1.6 d | h24 +29% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [ON](https://dexscreener.com/solana/3oQ4NUo8Gk7dFgo4nZUT6tNTCf6aHG3b7LfdNzrEbkNZ) | `3oQ4NUo8Gk7dFgo4nZUT6tNTCf6aHG3b7LfdNzrEbkNZ` | $212.8k | $121.1k | 1.8 h | h24 +54% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $151.9k | $145.1k | 7.0 h | h24 +227% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $135.0k | $3.22M | 10.1 h | h24 +2837% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.2% (+7) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $108.0k | $2.22M | 9.8 h | h24 +6125% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.61M | $16.43M | 120.8 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,879 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.37M | $17.84M | 744.7 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,548 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.05M | $12.97M | 181.2 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 23h (now 386,445) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UGOS](https://pump.fun/coin/7MzwkB1sNmpHGh7r19joiwKZ2cPf2iG5m8zsY42Ypump) | `7MzwkB1sNmpHGh7r19joiwKZ2cPf2iG5m8zsY42Ypump` | $881.7k | $155.46M | +526554% | +526554% | +526554% | 0.5x | liq/mcap 0.6%; spike (+526554% 1h, +526554% 6h); < 1h old | not scored |
| [UOF](https://pump.fun/coin/QFT9ifBDvLsCbQkyBfNsAjakFyJakezRW4UViuBpump) | `QFT9ifBDvLsCbQkyBfNsAjakFyJakezRW4UViuBpump` | $285.3k | $16.53M | +55900% | +55900% | +55900% | 0.5x | liq/mcap 1.7%; spike (+55900% 1h, +55900% 6h); < 1h old | not scored |
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $108.5k | $2.24M | +8% | +3% | +6183% | 12.5x | liq/mcap 4.9% | 66 |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $47.8k | $383.1k | +456% | +1310% | +1310% | 25.7x | thin liq $47.8k; churn 26x vol/liq; spike (+456% 1h, +1310% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $135.0k | $3.22M | -8% | +12% | +2837% | 17.3x | liq/mcap 4.2% | 66 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $47.8k | $348.8k | -20% | +16% | +1124% | 52.0x | thin liq $47.8k; churn 52x vol/liq | not scored |

_Timing: total 157s (discovery 71.6s, screen 1.1s, GT prime 0.4s, scoring 83.5s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/158; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
