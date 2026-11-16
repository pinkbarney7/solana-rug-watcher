# Last scan 2026-11-16T09:07:48Z - mode: helius (box heartbeat stale (302 min); budget 180/3000)

```
[fast_scan] 127 candidate mints from 8 source tags; 124 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored DADOG in 72s
[fast_scan] scored BJB in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored USPR in 82s
[fast_scan] scored Anthropig in 83s
[fast_scan] scored CATE in 83s
[fast_scan] scored HOGE in 84s
# Market scan 2026-11-16 09:07 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,318 (-2.0% 24h), ETH $1,797 (-1.4% 24h), SOL $70.67 (-1.3% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.9% (mcap $2.03B, vol $366.56M), pump-fun -1.7% (mcap $847.16M, vol $155.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $113.2k | $370.2k | 1.2 d | h24 +385% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $74.4k | $1.03M | 15.3 h | h24 +3069% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $95.9k | $1.72M | 12.0 h | h24 +4262% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.05M | $222.89M | 1.5 d | h24 +77% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 73* | SKIP | [DADOG](https://dexscreener.com/solana/6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY) | `6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY` | $834.2k | $842.3k | 11.6 h | h24 +839% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.60M | $15.69M | 112.7 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,736 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.58M | $10.89M | 662.4 d | h24 +142% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,273 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.86M | 173.1 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 375,633 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $3.96M | $28.24M | -1% | +12557987% | +18847528% | 0.0x | spike (-1% 1h, +12557987% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.0k | $1.73M | -11% | -9% | +4274% | 17.9x | none flagged (still high risk) | 60 |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $74.4k | $1.03M | -5% | +2% | +3069% | 16.8x | none flagged (still high risk) | 58 |
| [Huang](https://pump.fun/coin/42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump) | `42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump` | $14.9k | $36.7k | +552% | +352% | -4% | 17.6x | thin liq $14.9k; spike (+552% 1h, +352% 6h) | not scored |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $62.9k | $428.6k | -16% | +894% | +894% | 41.3x | churn 41x vol/liq; spike (-16% 1h, +894% 6h) | not scored |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $41.3k | $270.2k | -6% | +59% | +842% | 48.4x | thin liq $41.3k; churn 48x vol/liq | not scored |

_Timing: total 157s (discovery 71.9s, screen 1.3s, GT prime 0.3s, scoring 83.8s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/157; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
