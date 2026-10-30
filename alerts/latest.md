# Last scan 2026-10-30T19:12:30Z

```
[fast_scan] 129 candidate mints from 10 source tags; 124 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (10s)
[fast_scan] scored HYPE in 51s
[fast_scan] scored ZEC in 60s
[fast_scan] scored USDG in 65s
[fast_scan] scored GTA6 in 66s
[fast_scan] scored UDTF in 71s
[fast_scan] scored HI in 72s
[fast_scan] scored HYPERCHAN in 73s
# Market scan 2026-10-30 19:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $76,437 (-5.3% 24h), ETH $2,230 (-4.1% 24h), SOL $94.27 (-6.0% 24h)
- Fear & Greed: 30 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -7.7% (mcap $2.72B, vol $682.73M), pump-fun -8.2% (mcap $1.02B, vol $180.01M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 70 | SKIP | [HI](https://pump.fun/coin/3w2TvVmTrtq4kSkoFVrTFQgz6MX7ThzDVrx9r5c3pump) | `3w2TvVmTrtq4kSkoFVrTFQgz6MX7ThzDVrx9r5c3pump` | $157.0k | $892.2k | 1.1 d | h24 -21% | #15 Known rug-funder link FAIL (+32); #19 Same operator as other coins FAIL (+18); #13 Creator wallet WARN (+9) |
| 77 | SKIP | [HYPERCHAN](https://pump.fun/coin/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump) | `3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump` | $136.0k | $2.42M | 15.8 h | h24 +4962% | #14 Common-funder clusters FAIL (+16); #9 Price momentum FAIL (+14); linked launch group took 93% (+14) |
| 82 | SKIP | [UDTF](https://pump.fun/coin/9D51oXUyHGrLdabvXiJHRPc5UhW9Py14z3g6TTw7pump) | `9D51oXUyHGrLdabvXiJHRPc5UhW9Py14z3g6TTw7pump` | $421.3k | $26.78M | 22.5 h | h24 +64924% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 86 | SKIP | [GTA6](https://dexscreener.com/solana/4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz) | `4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz` | $613.6k | $13.30M | 85.2 d | h24 -17% | #15 Known rug-funder link FAIL (+32); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 79 | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.18M | $30.0k | 380.1 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 378,932 (growth n/a: first sighting) |
| 87 | SKIP | [HYPE](https://dexscreener.com/solana/98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g) | `98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g` | $9.59M | $64.97M | 385.1 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #15 Known rug-funder link FAIL (+32); #16 Exit liquidity (Jupiter quotes) FAIL (+24); GATES FAILED: authorities, rug-funder link, exit test; holders 209,441 (growth n/a: first sighting) |
| 88 | SKIP | [USDG](https://dexscreener.com/solana/2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH) | `2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH` | $24.11M | $10.75M | 610.2 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #11 Helius top holders FAIL (+18); GATES FAILED: authorities, rug-funder link, same operator as a rug, exit test, top holders concentrated; holders 1,000,000 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [UDTF](https://pump.fun/coin/9D51oXUyHGrLdabvXiJHRPc5UhW9Py14z3g6TTw7pump) | `9D51oXUyHGrLdabvXiJHRPc5UhW9Py14z3g6TTw7pump` | $421.4k | $26.78M | +2% | +12% | +64934% | 7.6x | liq/mcap 1.6% | 82 |
| [HYPERCHAN](https://pump.fun/coin/3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump) | `3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump` | $133.8k | $2.34M | +39% | +11% | +4806% | 27.2x | churn 27x vol/liq | 77 |
| [AgenC](https://pump.fun/coin/DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump) | `DDG8rjV3TViCqKRQED2QZq4MEaE1uqXgEiosBNpapump` | $53.9k | $416.4k | +709% | +709% | +709% | 24.6x | spike (+709% 1h, +709% 6h); < 1h old | not scored |
| [HI](https://dexscreener.com/solana/Byf7PwqFnqbhXBzt18YXhPcGr4aw65Zdk9FNXgzBTyW4) | `Byf7PwqFnqbhXBzt18YXhPcGr4aw65Zdk9FNXgzBTyW4` | $75.6k | $111.6k | +32% | +1130% | +1130% | 234.9x | churn 235x vol/liq; spike (+32% 1h, +1130% 6h) | not scored |
| [BTC](https://pump.fun/coin/ra4qZ68oPFuEhHR5hMRpUsGH5riMbRBuMyW68r3pump) | `ra4qZ68oPFuEhHR5hMRpUsGH5riMbRBuMyW68r3pump` | $28.0k | $126.9k | +221% | +221% | +221% | 8.0x | thin liq $28.0k; spike (+221% 1h, +221% 6h); < 1h old | not scored |
| [TYGR](https://pump.fun/coin/5wCqCq6jbppuTocMeq6zd4UywAm64L1QNNxvEDAHpump) | `5wCqCq6jbppuTocMeq6zd4UywAm64L1QNNxvEDAHpump` | $44.6k | $229.5k | +2% | +426% | +426% | 40.5x | thin liq $44.6k; churn 40x vol/liq; spike (+2% 1h, +426% 6h) | not scored |

_Timing: total 84s (discovery 9.0s, screen 1.4s, GT prime 1.3s, scoring 72.6s for 7 coins, 7 newly scored). ~2756 Helius credits (smart-money discovery 30). HTTP cache hits 9/749; Helius 429s 73; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
