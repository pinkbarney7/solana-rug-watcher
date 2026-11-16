# Last scan 2026-11-16T08:51:17Z - mode: helius (box heartbeat stale (285 min); budget 160/3000)

```
[fast_scan] 130 candidate mints from 9 source tags; 127 with pair data; 26 >= $50,000 liq; 12 pass survivor pre-gates (72s)
[fast_scan] scored DADOG in 72s
[fast_scan] scored CATE in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored HOGE in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored BJB in 82s
[fast_scan] scored Anthropig in 83s
[fast_scan] scored USPR in 83s
# Market scan 2026-11-16 08:51 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,575 (-0.2% 24h), ETH $1,810 (+0.6% 24h), SOL $71.07 (+0.6% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.7% (mcap $2.04B, vol $368.63M), pump-fun -1.4% (mcap $849.80M, vol $158.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $111.4k | $353.3k | 1.2 d | h24 +267% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $77.2k | $1.11M | 15.1 h | h24 +3299% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.2k | $1.72M | 11.7 h | h24 +4267% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.06M | $223.06M | 1.5 d | h24 +80% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 73* | SKIP | [DADOG](https://dexscreener.com/solana/6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY) | `6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY` | $834.2k | $842.3k | 11.3 h | h24 +839% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $16.02M | 112.7 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,736 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.58M | $10.98M | 662.4 d | h24 +147% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,262 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.34M | $12.84M | 173.0 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 375,633 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $3.98M | $28.38M | -0% | +30780325% | +18938295% | 0.0x | spike (-0% 1h, +30780325% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.2k | $1.72M | -3% | -20% | +4266% | 17.8x | none flagged (still high risk) | 60 |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $68.8k | $511.2k | +5% | +1086% | +1086% | 37.5x | churn 37x vol/liq; spike (+5% 1h, +1086% 6h) | not scored |
| [Huang](https://pump.fun/coin/42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump) | `42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump` | $16.1k | $41.7k | +634% | +403% | +9% | 14.7x | thin liq $16.1k; spike (+634% 1h, +403% 6h) | not scored |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $77.2k | $1.11M | -9% | -1% | +3299% | 16.0x | none flagged (still high risk) | 59 |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $42.0k | $278.5k | -23% | +52% | +871% | 47.1x | thin liq $42.0k; churn 47x vol/liq | not scored |

_Timing: total 155s (discovery 71.1s, screen 1.3s, GT prime 0.3s, scoring 82.7s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/157; Helius 429s 91; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
