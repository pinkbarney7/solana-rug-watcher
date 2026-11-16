# Last scan 2026-11-16T08:05:41Z - mode: helius (box heartbeat stale (240 min); budget 140/3000)

```
[fast_scan] 130 candidate mints from 8 source tags; 126 with pair data; 27 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored USPR in 71s
[fast_scan] scored ZEC in 79s
[fast_scan] scored SPCX in 80s
[fast_scan] scored Anthropig in 80s
[fast_scan] scored BJB in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored HOGE in 82s
# Market scan 2026-11-16 08:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,936 (+1.6% 24h), ETH $1,818 (+2.2% 24h), SOL $71.32 (+2.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.5% (mcap $2.05B, vol $372.01M), pump-fun +0.4% (mcap $856.64M, vol $156.72M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $108.6k | $339.3k | 1.1 d | h24 +165% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 59* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $79.5k | $1.17M | 14.3 h | h24 +3497% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $99.4k | $1.84M | 10.9 h | h24 +4561% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.05M | $220.82M | 1.4 d | h24 +85% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.63M | $11.58M | 662.3 d | h24 +162% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,215 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.63M | $22.1k | 396.6 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 63h (now 390,822) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.96M | 173.0 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 375,656 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $4.02M | $28.44M | +35345139% | +18978340% | +18978340% | 0.0x | spike (+35345139% 1h, +18978340% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $98.5k | $1.81M | -1% | +1% | +4476% | 17.0x | none flagged (still high risk) | 60 |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $68.4k | $508.5k | +28% | +1080% | +1080% | 36.8x | churn 37x vol/liq; spike (+28% 1h, +1080% 6h) | not scored |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $78.2k | $1.14M | +4% | +7% | +3389% | 15.2x | none flagged (still high risk) | 59 |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $41.3k | $273.3k | -9% | +95% | +853% | 43.1x | thin liq $41.3k; churn 43x vol/liq | not scored |
| [BLOB](https://pump.fun/coin/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump) | `8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump` | $286.8k | $12.01M | +38% | +172% | +198% | 8.0x | liq/mcap 2.4% | not scored |

_Timing: total 155s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 82.2s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/143; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
