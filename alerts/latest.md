# Last scan 2026-11-28T02:02:08Z - mode: helius (box heartbeat stale (29 min); budget 495/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 128 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored SPCX in 80s
[fast_scan] scored MEMECARD in 80s
[fast_scan] scored UGOS in 80s
[fast_scan] scored ZEC in 81s
[fast_scan] scored NBA in 81s
[fast_scan] scored Fireball in 82s
[fast_scan] scored GAIB in 121s
[fast_scan] scored FLOAT in 74s
# Market scan 2026-11-28 02:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,158 (-0.7% 24h), ETH $1,669 (-1.7% 24h), SOL $72.13 (+1.0% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.5% (mcap $1.92B, vol $273.74M), pump-fun +4.2% (mcap $814.52M, vol $100.44M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | CAUTION | [GAIB](https://dexscreener.com/solana/2JjmRdQ71UzAUkTCGsFXNEBdqYBAbh9LMzSb8eHnzYJT) | `2JjmRdQ71UzAUkTCGsFXNEBdqYBAbh9LMzSb8eHnzYJT` | $225.4k | $347.5k | 12.1 h | h24 +329% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $51.9k | $502.7k | 11.9 h | h24 +1369% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $317.5k | $16.94M | 2.0 d | h24 +70% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.8); #11 not checked (+3) |
| 57* | SKIP | [NBA](https://pump.fun/coin/AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump) | `AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump` | $56.6k | $594.4k | 9.5 h | h24 +1333% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [MEMECARD](https://pump.fun/coin/8sAxwsNzhRj6LF5npy1HtPir94TzSgP1QaczUmGcpump) | `8sAxwsNzhRj6LF5npy1HtPir94TzSgP1QaczUmGcpump` | $102.9k | $1.78M | 8.7 h | h24 +1514% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $915.3k | $164.94M | 1.2 d | h24 +56% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $419.9k | $2.76M | 30.2 d | h24 -15% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.4% in 45h (now 50,000) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.81M | $14.09M | 184.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.9% in 9h (now 403,506) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.42M | $18.7k | 408.4 d | h24 +7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 9h (now 397,082) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MAYA](https://pump.fun/coin/H2PjSbA2365uxBUJ3EBePSm67AYPuRMgcyswBnrVpump) | `H2PjSbA2365uxBUJ3EBePSm67AYPuRMgcyswBnrVpump` | $93.3k | $1.57M | -34% | +3870% | +3870% | 20.0x | spike (-34% 1h, +3870% 6h) | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $58.7k | $670.2k | +49% | +1945% | +1945% | 9.1x | spike (+49% 1h, +1945% 6h); lopsided buys/sells 4.73 | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $55.9k | $338.1k | -30% | +660% | +660% | 67.2x | churn 67x vol/liq; spike (-30% 1h, +660% 6h) | not scored |
| [MEMECARD](https://pump.fun/coin/8sAxwsNzhRj6LF5npy1HtPir94TzSgP1QaczUmGcpump) | `8sAxwsNzhRj6LF5npy1HtPir94TzSgP1QaczUmGcpump` | $102.5k | $1.78M | +78% | +160% | +1514% | 24.6x | none flagged (still high risk) | 60 |
| [STEADY](https://dexscreener.com/solana/AvvXpCVph4PtJ5urfhetPkdZYh8o4uW7CawUA2MK8hFT) | `AvvXpCVph4PtJ5urfhetPkdZYh8o4uW7CawUA2MK8hFT` | $48.6k | $110.4k | -67% | +440% | +440% | 23.9x | thin liq $48.6k; spike (-67% 1h, +440% 6h) | not scored |
| [NBA](https://pump.fun/coin/AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump) | `AjucUKL3i8wh7SvFL9h5cZbWkd3M9JibLkdvRJKppump` | $56.6k | $594.4k | +29% | -14% | +1333% | 21.0x | none flagged (still high risk) | 57 |

_Timing: total 219s (discovery 71.3s, screen 1.4s, GT prime 0.5s, scoring 145.4s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/178; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
