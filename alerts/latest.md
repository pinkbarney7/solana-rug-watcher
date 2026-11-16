# Last scan 2026-11-16T12:55:01Z - mode: helius (box heartbeat stale (529 min); budget 350/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 117 with pair data; 28 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored ZEC in 71s
[fast_scan] scored rockstar in 79s
[fast_scan] scored VINE in 80s
[fast_scan] scored HOGE in 80s
[fast_scan] scored USPR in 81s
[fast_scan] scored Anthropig in 81s
[fast_scan] scored SPCX in 81s
# Market scan 2026-11-16 12:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,138 (-2.0% 24h), ETH $1,797 (-1.9% 24h), SOL $70.66 (-2.8% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.0% (mcap $2.02B, vol $354.80M), pump-fun -4.9% (mcap $847.38M, vol $152.31M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $91.4k | $369.2k | 1.3 d | h24 +1136% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $231.3k | $1.19M | 1.1 d | h24 +1263% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $64.4k | $769.3k | 19.1 h | h24 +2264% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.08M | $235.30M | 1.6 d | h24 +64% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.52M | $10.18M | 662.5 d | h24 +110% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,285 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.29M | $21.2k | 396.8 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,931 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.20M | $12.70M | 173.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,456 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $64.4k | $769.3k | +1% | -30% | +2264% | 22.3x | none flagged (still high risk) | 58 |
| [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $111.4k | $1.19M | +32% | +154% | +1149% | 33.7x | churn 34x vol/liq | 52 |
| [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $68.9k | $369.2k | -16% | -13% | +1136% | 49.2x | churn 49x vol/liq | 50 |
| [DOUG](https://pump.fun/coin/CRKqYn9bnEZaXK6K2uk627szTFjait52RXeY6CEnpump) | `CRKqYn9bnEZaXK6K2uk627szTFjait52RXeY6CEnpump` | $28.9k | $121.2k | +159% | +159% | +159% | 2.5x | thin liq $28.9k; spike (+159% 1h, +159% 6h); < 1h old | not scored |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $39.5k | $240.4k | +34% | +18% | +738% | 57.0x | thin liq $39.5k; churn 57x vol/liq | not scored |
| [1.0](https://pump.fun/coin/42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump) | `42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump` | $23.3k | $99.7k | -48% | +239% | +239% | 45.4x | thin liq $23.3k; churn 45x vol/liq | not scored |

_Timing: total 154s (discovery 71.4s, screen 1.1s, GT prime 0.3s, scoring 81.2s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/137; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
