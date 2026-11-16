# Last scan 2026-11-16T08:33:25Z - mode: helius (box heartbeat stale (267 min); budget 160/3000)

```
[fast_scan] 128 candidate mints from 8 source tags; 124 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored DADOG in 72s
[fast_scan] scored VINE in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Anthropig in 81s
[fast_scan] scored USPR in 82s
[fast_scan] scored CATE in 83s
[fast_scan] scored BJB in 83s
[fast_scan] scored HOGE in 84s
# Market scan 2026-11-16 08:33 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,505 (+0.0% 24h), ETH $1,805 (+0.6% 24h), SOL $70.68 (+0.2% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.4% (mcap $2.03B, vol $351.93M), pump-fun -0.6% (mcap $847.95M, vol $154.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $109.9k | $341.4k | 1.1 d | h24 +299% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $78.4k | $1.14M | 14.8 h | h24 +3418% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $94.4k | $1.67M | 11.4 h | h24 +4123% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.7% (+5.2) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.05M | $221.03M | 1.4 d | h24 +80% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 73* | SKIP | [DADOG](https://dexscreener.com/solana/6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY) | `6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY` | $834.2k | $842.3k | 11.0 h | h24 +839% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $15.91M | 112.7 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,728 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.60M | $11.26M | 662.3 d | h24 +151% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,262 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.34M | $12.86M | 173.0 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 375,656 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $3.96M | $28.26M | -1% | +18863546% | +18863546% | 0.0x | spike (-1% 1h, +18863546% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $94.4k | $1.67M | -10% | -14% | +4123% | 18.1x | none flagged (still high risk) | 59 |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $69.5k | $520.3k | +24% | +1107% | +1107% | 36.8x | churn 37x vol/liq; spike (+24% 1h, +1107% 6h) | not scored |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $78.4k | $1.14M | -3% | +10% | +3418% | 15.5x | none flagged (still high risk) | 59 |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $43.4k | $293.4k | -28% | +37% | +922% | 43.9x | thin liq $43.4k; churn 44x vol/liq | not scored |
| [DADOG](https://dexscreener.com/solana/6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY) | `6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY` | $834.2k | $842.3k | +0% | +0% | +839% | 0.0x | lopsided buys/sells 275.00 | 73 |

_Timing: total 157s (discovery 71.8s, screen 1.5s, GT prime 0.2s, scoring 83.9s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/157; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
