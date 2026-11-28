# Last scan 2026-11-28T06:41:16Z - mode: helius (box heartbeat stale (153 min); budget 80/3000)

```
[fast_scan] 114 candidate mints from 9 source tags; 113 with pair data; 21 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored UGOS in 79s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored Memeball in 80s
[fast_scan] scored ZEC in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Rizzmas in 82s
# Market scan 2026-11-28 06:41 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,816 (-3.0% 24h), ETH $1,658 (-4.4% 24h), SOL $71.42 (-2.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.1% (mcap $1.86B, vol $321.15M), pump-fun +0.7% (mcap $800.69M, vol $94.82M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $98.4k | $480.6k | 10.0 h | h24 +980% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $329.5k | $18.36M | 2.2 d | h24 +78% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 58* | SKIP | [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $70.0k | $944.8k | 6.2 h | h24 +2783% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $945.2k | $177.67M | 1.4 d | h24 +68% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $219.9k | $633.5k | 1069.5 d | h24 -8% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,808 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.80M | $13.99M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,474 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.35M | $18.3k | 408.6 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 397,085 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $69.0k | $921.8k | -9% | +2470% | +2470% | 15.3x | spike (-9% 1h, +2470% 6h) | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $70.4k | $955.1k | +11% | +169% | +2815% | 10.2x | lopsided buys/sells 3.95 | 58 |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $38.6k | $263.5k | -5% | +814% | +814% | 33.8x | thin liq $38.6k; churn 34x vol/liq; spike (-5% 1h, +814% 6h) | not scored |
| [Split](https://pump.fun/coin/HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump) | `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump` | $32.9k | $151.3k | +235% | +13% | +394% | 50.6x | thin liq $32.9k; churn 51x vol/liq; spike (+235% 1h, +13% 6h) | not scored |
| [FINGART](https://pump.fun/coin/WZVWLfThgm14NN8HRDoyiEeXVvdUDMzGMHUS3VLpump) | `WZVWLfThgm14NN8HRDoyiEeXVvdUDMzGMHUS3VLpump` | $20.2k | $88.9k | +202% | +202% | +202% | 5.5x | thin liq $20.2k; spike (+202% 1h, +202% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $68.2k | $486.5k | -15% | +11% | +994% | 60.8x | churn 61x vol/liq | 54 |

_Timing: total 156s (discovery 71.8s, screen 1.2s, GT prime 0.4s, scoring 82.4s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
