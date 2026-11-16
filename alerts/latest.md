# Last scan 2026-11-16T11:14:39Z - mode: helius (box heartbeat stale (428 min); budget 270/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 115 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored HOGE in 72s
[fast_scan] scored rockstar in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored BJB in 81s
[fast_scan] scored gtacoin in 82s
[fast_scan] scored Marvin in 82s
[fast_scan] scored Anthropig in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-16 11:14 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,608 (-1.3% 24h), ETH $1,811 (-0.8% 24h), SOL $71.81 (-0.3% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.2% (mcap $2.04B, vol $362.68M), pump-fun -3.1% (mcap $855.48M, vol $152.16M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | SKIP | [gtacoin](https://dexscreener.com/solana/DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK) | `DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK` | $242.4k | $659.3k | 1.8 d | h24 +17% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3) |
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $107.8k | $477.8k | 1.3 d | h24 +823% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $156.6k | $827.7k | 1.0 d | h24 +1965% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $73.3k | $294.9k | 7.5 h | h24 +584% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 57* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $63.7k | $743.1k | 17.4 h | h24 +2183% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.7k | $1.72M | 14.1 h | h24 +4246% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.64M | $16.31M | 112.8 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,745 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.57M | $10.65M | 662.5 d | h24 +133% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,277 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.74M | 173.1 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,563 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $4.35M | $28.55M | +1% | +39071715% | +19055759% | 0.0x | spike (+1% 1h, +39071715% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.0k | $1.69M | -3% | -9% | +4182% | 19.0x | none flagged (still high risk) | 59 |
| [1.0](https://pump.fun/coin/42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump) | `42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump` | $27.8k | $138.9k | +373% | +373% | +373% | 23.5x | thin liq $27.8k; spike (+373% 1h, +373% 6h); < 1h old | not scored |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $63.7k | $743.1k | -18% | -31% | +2183% | 21.3x | none flagged (still high risk) | 57 |
| [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $92.2k | $821.9k | -11% | +76% | +1950% | 40.6x | churn 41x vol/liq | 52 |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $40.5k | $252.1k | -5% | +173% | +778% | 52.4x | thin liq $40.5k; churn 52x vol/liq | not scored |

_Timing: total 216s (discovery 71.3s, screen 1.1s, GT prime 0.3s, scoring 143.8s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/169; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
