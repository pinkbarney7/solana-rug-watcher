# Last scan 2026-11-16T08:58:04Z - mode: helius (box heartbeat stale (292 min); budget 180/3000)

```
[fast_scan] 125 candidate mints from 8 source tags; 122 with pair data; 26 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored HOGE in 73s
[fast_scan] scored VINE in 80s
[fast_scan] scored USPR in 81s
[fast_scan] scored DADOG in 81s
[fast_scan] scored Anthropig in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored BJB in 82s
[fast_scan] scored SPCX in 82s
# Market scan 2026-11-16 08:58 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,473 (-0.5% 24h), ETH $1,807 (+0.3% 24h), SOL $70.92 (+0.3% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.7% (mcap $2.04B, vol $368.63M), pump-fun -1.4% (mcap $849.80M, vol $158.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $109.4k | $341.0k | 1.2 d | h24 +423% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $76.3k | $1.08M | 15.2 h | h24 +3219% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.4k | $1.73M | 11.8 h | h24 +4288% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.06M | $223.55M | 1.5 d | h24 +79% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 73* | SKIP | [DADOG](https://dexscreener.com/solana/6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY) | `6FHTxbq7SQgHumeppwBvCZNj8161dNUuQHAVm8Sq6MdY` | $834.2k | $842.3k | 11.4 h | h24 +839% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.62M | $15.89M | 112.7 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,736 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.58M | $10.94M | 662.4 d | h24 +145% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,262 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.95M | 173.0 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 375,633 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $3.98M | $28.39M | -0% | +13316139% | +18946304% | 0.0x | spike (-0% 1h, +13316139% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.4k | $1.73M | -7% | -12% | +4288% | 17.8x | none flagged (still high risk) | 60 |
| [Huang](https://pump.fun/coin/42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump) | `42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump` | $16.3k | $42.8k | +661% | +408% | +12% | 14.9x | thin liq $16.3k; spike (+661% 1h, +408% 6h) | not scored |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $68.3k | $504.8k | -12% | +1071% | +1071% | 37.8x | churn 38x vol/liq; spike (-12% 1h, +1071% 6h) | not scored |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $76.3k | $1.08M | -8% | -1% | +3219% | 16.3x | none flagged (still high risk) | 58 |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $40.6k | $259.4k | -12% | +39% | +804% | 48.9x | thin liq $40.6k; churn 49x vol/liq | not scored |

_Timing: total 156s (discovery 71.7s, screen 1.3s, GT prime 0.2s, scoring 82.2s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/157; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
