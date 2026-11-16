# Last scan 2026-11-16T10:52:33Z - mode: helius (box heartbeat stale (406 min); budget 270/3000)

```
[fast_scan] 119 candidate mints from 8 source tags; 116 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored BJB in 72s
[fast_scan] scored Anthropig in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored gtacoin in 82s
[fast_scan] scored Marvin in 82s
[fast_scan] scored rockstar in 82s
[fast_scan] scored HOGE in 83s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-16 10:52 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,502 (-1.6% 24h), ETH $1,805 (-1.3% 24h), SOL $71.42 (-0.8% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.4% (mcap $2.04B, vol $363.74M), pump-fun -3.3% (mcap $853.78M, vol $154.45M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $117.1k | $462.8k | 1.2 d | h24 +845% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [gtacoin](https://dexscreener.com/solana/DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK) | `DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK` | $244.4k | $659.3k | 1.7 d | h24 +17% | #7 Insiders / bundles / LP lock FAIL (+14); #16 Exit liquidity (Jupiter quotes) WARN (+7); #11 not checked (+3) |
| 52* | SKIP | [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $167.0k | $907.6k | 1.0 d | h24 +1997% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $81.0k | $342.9k | 7.2 h | h24 +695% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 57* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $63.9k | $753.0k | 17.1 h | h24 +2213% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $96.0k | $1.70M | 13.7 h | h24 +4209% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.64M | $16.19M | 112.8 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,745 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.60M | $11.08M | 662.4 d | h24 +143% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,277 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.85M | 173.1 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,706 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $4.35M | $28.55M | +1% | +47894002% | +19055759% | 0.0x | spike (+1% 1h, +47894002% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $97.0k | $1.73M | -0% | -4% | +4294% | 18.6x | none flagged (still high risk) | 59 |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $63.9k | $753.0k | -14% | -36% | +2213% | 21.0x | none flagged (still high risk) | 57 |
| [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $96.9k | $907.6k | -2% | +64% | +1997% | 38.9x | churn 39x vol/liq | 52 |
| [1.0](https://pump.fun/coin/42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump) | `42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump` | $22.8k | $103.0k | +242% | +242% | +242% | 18.5x | thin liq $22.8k; spike (+242% 1h, +242% 6h); < 1h old | not scored |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $40.4k | $253.8k | +4% | +110% | +785% | 51.6x | thin liq $40.4k; churn 52x vol/liq | not scored |

_Timing: total 216s (discovery 71.6s, screen 1.1s, GT prime 0.4s, scoring 143.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/169; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
