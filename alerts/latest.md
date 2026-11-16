# Last scan 2026-11-16T09:30:35Z - mode: helius (box heartbeat stale (324 min); budget 180/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 119 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored Marvin in 72s
[fast_scan] scored Anthropig in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BJB in 81s
[fast_scan] scored USPR in 82s
[fast_scan] scored VINE in 82s
[fast_scan] scored FiveM in 82s
[fast_scan] scored HOGE in 84s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-16 09:30 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,307 (-2.0% 24h), ETH $1,798 (-1.8% 24h), SOL $70.76 (-1.9% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.9% (mcap $2.03B, vol $347.87M), pump-fun -1.7% (mcap $846.80M, vol $152.69M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $116.0k | $416.9k | 1.2 d | h24 +360% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Marvin](https://dexscreener.com/solana/CuKub87k6z2Uu9xY7bV9sifaoMi4dW7CZSoRcQogDgM) | `CuKub87k6z2Uu9xY7bV9sifaoMi4dW7CZSoRcQogDgM` | $151.2k | $96.5k | 1.5 h | h24 +110% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [FiveM](https://pump.fun/coin/2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump) | `2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump` | $57.8k | $633.2k | 9.1 h | h24 +1599% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $69.7k | $905.0k | 15.7 h | h24 +2681% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $98.5k | $1.81M | 12.3 h | h24 +4494% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.4% (+5.5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.06M | $224.29M | 1.5 d | h24 +74% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.61M | $15.68M | 112.7 d | h24 -10% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 429,737 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.57M | $10.84M | 662.4 d | h24 +137% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,273 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.45M | $12.81M | 173.1 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,060 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAG](https://pump.fun/coin/Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump) | `Ed87eQeDX8yFscuNRgNRSZf7TpEwgNjdRfMxhtGppump` | $3.96M | $28.26M | -0% | +14340155% | +18860876% | 0.0x | spike (-0% 1h, +14340155% 6h) | not scored |
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $98.5k | $1.81M | +9% | -3% | +4494% | 17.7x | none flagged (still high risk) | 60 |
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $68.8k | $882.4k | -21% | -29% | +2611% | 18.5x | none flagged (still high risk) | 58 |
| [Marvin](https://pump.fun/coin/HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump) | `HkRQ6Qcadi5yuoNpZdA1Q7yVF3r7LdEmAw1aKkSxpump` | $59.0k | $377.6k | -25% | +776% | +776% | 44.9x | churn 45x vol/liq; spike (-25% 1h, +776% 6h) | not scored |
| [Huang](https://pump.fun/coin/42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump) | `42Fyyi97PSgdnoaskbHDHFsCFR6hr5DtwK3hKTzXpump` | $11.7k | $23.8k | +330% | +244% | -38% | 23.7x | thin liq $11.7k; spike (+330% 1h, +244% 6h) | not scored |
| [FiveM](https://pump.fun/coin/2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump) | `2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump` | $57.8k | $633.2k | +5% | +83% | +1599% | 13.8x | none flagged (still high risk) | 57 |

_Timing: total 217s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 144.1s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/175; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
