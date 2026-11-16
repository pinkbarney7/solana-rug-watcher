# Last scan 2026-11-16T12:15:06Z - mode: helius (box heartbeat stale (489 min); budget 320/3000)

```
[fast_scan] 122 candidate mints from 10 source tags; 119 with pair data; 23 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored HOGE in 71s
[fast_scan] scored gtacoin in 79s
[fast_scan] scored Anthropig in 80s
[fast_scan] scored ZEC in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored USPR in 81s
[fast_scan] scored SPCX in 81s
# Market scan 2026-11-16 12:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,132 (-1.8% 24h), ETH $1,799 (-1.5% 24h), SOL $70.90 (-2.2% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.6% (mcap $2.03B, vol $347.48M), pump-fun -3.6% (mcap $854.28M, vol $154.23M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | SKIP | [gtacoin](https://dexscreener.com/solana/DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK) | `DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK` | $239.1k | $659.3k | 1.8 d | h24 +17% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3) |
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $90.8k | $360.8k | 1.3 d | h24 +708% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $65.8k | $801.7k | 18.5 h | h24 +2363% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.08M | $233.93M | 1.6 d | h24 +67% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.56M | $10.62M | 662.5 d | h24 +116% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,274 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.41M | $21.7k | 396.8 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 4h (now 390,759) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.30M | $12.79M | 173.2 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,436 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $65.1k | $785.2k | +8% | -24% | +2312% | 21.6x | none flagged (still high risk) | 58 |
| [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $112.0k | $1.20M | +51% | +138% | +1234% | 32.7x | churn 33x vol/liq; spike (+51% 1h, +138% 6h) | not scored |
| [1.0](https://pump.fun/coin/42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump) | `42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump` | $28.6k | $147.3k | +19% | +401% | +401% | 33.8x | thin liq $28.6k; churn 34x vol/liq; spike (+19% 1h, +401% 6h) | not scored |
| [ZLUSD](https://pump.fun/coin/DdpwR8QXfnS11HUrSdNmnNvXj3XDMcePoHsWGJrdpump) | `DdpwR8QXfnS11HUrSdNmnNvXj3XDMcePoHsWGJrdpump` | $19.7k | $78.2k | +163% | +163% | +163% | 8.2x | thin liq $19.7k; spike (+163% 1h, +163% 6h); < 1h old | not scored |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $35.3k | $193.2k | -27% | +87% | +573% | 62.5x | thin liq $35.3k; churn 62x vol/liq | not scored |
| [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $68.8k | $367.6k | -20% | -16% | +723% | 49.2x | churn 49x vol/liq | 50 |

_Timing: total 154s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 81.1s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/138; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
