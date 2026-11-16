# Last scan 2026-11-16T13:18:16Z - mode: helius (box heartbeat stale (552 min); budget 370/3000)

```
[fast_scan] 119 candidate mints from 9 source tags; 116 with pair data; 28 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored HOGE in 71s
[fast_scan] scored Anthropig in 79s
[fast_scan] scored VINE in 79s
[fast_scan] scored rockstar in 80s
[fast_scan] scored SPCX in 80s
[fast_scan] scored ZEC in 81s
[fast_scan] scored USPR in 81s
# Market scan 2026-11-16 13:18 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,071 (-2.2% 24h), ETH $1,797 (-2.0% 24h), SOL $70.75 (-3.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.2% (mcap $2.01B, vol $337.48M), pump-fun -5.2% (mcap $844.58M, vol $149.08M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $92.3k | $387.1k | 1.3 d | h24 +1344% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [rockstar](https://pump.fun/coin/9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump) | `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump` | $229.6k | $1.11M | 1.1 d | h24 +745% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $66.4k | $813.9k | 19.5 h | h24 +2401% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.09M | $236.83M | 1.6 d | h24 +63% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.58M | $10.92M | 662.5 d | h24 +125% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 344,293 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.34M | $21.3k | 396.9 d | h24 -6% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,931 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.20M | $12.63M | 173.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 376,456 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Anthropig](https://pump.fun/coin/2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump) | `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump` | $66.4k | $813.9k | +2% | -33% | +2401% | 22.0x | none flagged (still high risk) | 58 |
| [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $70.7k | $387.1k | +15% | -1% | +1344% | 48.1x | churn 48x vol/liq | 50 |
| [GTA6](https://pump.fun/coin/AnvhfTgZXdQk3vLmoUxDtYnTb7tpjQkXpFTHDXYFpump) | `AnvhfTgZXdQk3vLmoUxDtYnTb7tpjQkXpFTHDXYFpump` | $37.2k | $279.8k | +219% | +219% | +219% | 12.1x | thin liq $37.2k; spike (+219% 1h, +219% 6h); < 1h old | not scored |
| [DOUG](https://pump.fun/coin/CRKqYn9bnEZaXK6K2uk627szTFjait52RXeY6CEnpump) | `CRKqYn9bnEZaXK6K2uk627szTFjait52RXeY6CEnpump` | $30.7k | $126.4k | +181% | +181% | +181% | 5.2x | thin liq $30.7k; spike (+181% 1h, +181% 6h); < 1h old | not scored |
| [DOUG](https://dexscreener.com/solana/D66FPerv7zKWEYxVLdhKFPYWp8t4PcMu7z8QzdWs2t9k) | `D66FPerv7zKWEYxVLdhKFPYWp8t4PcMu7z8QzdWs2t9k` | $20.2k | $16.9k | +181% | +181% | +181% | 0.2x | thin liq $20.2k; spike (+181% 1h, +181% 6h); lopsided buys/sells 35.00; < 1h old | not scored |
| [VI](https://pump.fun/coin/5wU7osGtkG6NP1Fxqv83mFL4uuDmjvggrkGwuZiYpump) | `5wU7osGtkG6NP1Fxqv83mFL4uuDmjvggrkGwuZiYpump` | $22.2k | $60.5k | +46% | +363% | +223% | 5.2x | thin liq $22.2k; spike (+46% 1h, +363% 6h) | not scored |

_Timing: total 154s (discovery 71.6s, screen 1.1s, GT prime 0.2s, scoring 81.0s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/137; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
