# Last scan 2026-11-16T11:09:26Z - mode: helius (box heartbeat stale (422 min); budget 270/3000)

```
[fast_scan] 114 candidate mints from 8 source tags; 111 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Marvin in 72s
[fast_scan] scored Anthropig in 80s
[fast_scan] scored rockstar in 81s
[fast_scan] scored HOGE in 82s
[fast_scan] scored BJB in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored gtacoin in 83s
[fast_scan] scored VINE in 83s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-16 11:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,555 (-1.4% 24h), ETH $1,810 (-1.0% 24h), SOL $71.71 (-0.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.2% (mcap $2.04B, vol $362.68M), pump-fun -3.1% (mcap $855.48M, vol $152.16M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | SKIP | [gtacoin](https://dexscreener.com/solana/DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK) | `DSKM3d518BBaQShSKqaqZcG1XMRf81UFB6a1eavhSTNK` | $243.0k | $659.3k | 1.8 d | h24 +17% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3) |
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $108.3k | $476.5k | 1.3 d | h24 +873% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $162.9k | $835.0k | 1.0 d | h24 +2193% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $73.7k | $295.4k | 7.4 h | h24 +585% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 57* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $62.2k | $710.1k | 17.4 h | h24 +2082% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $95.9k | $1.69M | 14.0 h | h24 +4174% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.7% (+5.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.64M | $16.23M | 112.8 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,745 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.56M | $10.56M | 662.5 d | h24 +131% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,277 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.35M | $12.72M | 173.1 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,563 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $4.35M | $28.55M | +1% | +39071715% | +19055759% | 0.0x | spike (+1% 1h, +39071715% 6h) | not scored |
| [UODF](https://pump.fun/coin/Xr799tXRyGdfXwRXRnhtxqDgKbbRCWgmSm5GTMLpump) | `Xr799tXRyGdfXwRXRnhtxqDgKbbRCWgmSm5GTMLpump` | $859.8k | $145.19M | +482918% | +482918% | +482918% | 0.5x | liq/mcap 0.6%; spike (+482918% 1h, +482918% 6h); < 1h old | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $95.5k | $1.67M | -3% | -9% | +4140% | 19.0x | none flagged (still high risk) | 59 |
| [1.0](https://pump.fun/coin/42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump) | `42t61wPi41TwWtpqBVgZN1V4hjiKwZBKwq27xME9pump` | $31.0k | $175.4k | +497% | +497% | +497% | 20.1x | thin liq $31.0k; spike (+497% 1h, +497% 6h); < 1h old | not scored |
| [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $93.5k | $845.0k | -7% | +68% | +2220% | 40.2x | churn 40x vol/liq | 52 |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $62.2k | $710.1k | -21% | -35% | +2082% | 21.8x | none flagged (still high risk) | 57 |

_Timing: total 218s (discovery 72.1s, screen 1.1s, GT prime 0.6s, scoring 144.1s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/169; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
