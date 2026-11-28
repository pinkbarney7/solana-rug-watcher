# Last scan 2026-11-28T04:38:38Z - mode: helius (box heartbeat stale (30 min); budget 525/3000)

```
[fast_scan] 128 candidate mints from 9 source tags; 126 with pair data; 21 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored SPCX in 70s
[fast_scan] scored UGOS in 79s
[fast_scan] scored MoonBoy in 79s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored CATE in 80s
[fast_scan] scored Rizzmas in 82s
[fast_scan] scored MoonBoy in 88s
# Market scan 2026-11-28 04:38 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,968 (-2.4% 24h), ETH $1,663 (-3.9% 24h), SOL $71.59 (-1.7% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.5% (mcap $1.90B, vol $254.93M), pump-fun +1.8% (mcap $807.62M, vol $96.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [MoonBoy](https://dexscreener.com/solana/APzXPGGfnXQgabrt9tCyXdBFLCgwKRdkminNjFfXmQV) | `APzXPGGfnXQgabrt9tCyXdBFLCgwKRdkminNjFfXmQV` | $93.9k | $54.5k | 1.1 h | h24 +38% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $319.9k | $17.31M | 2.1 d | h24 +53% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $112.0k | $570.7k | 8.0 h | h24 +1183% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $932.4k | $172.60M | 1.3 d | h24 +63% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.4k | $634.9k | 1069.4 d | h24 -8% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,801 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.65M | $17.24M | 124.5 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 439,199 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.80M | $14.11M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,392 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $58.9k | $675.3k | -8% | +1961% | +1961% | 11.0x | spike (-8% 1h, +1961% 6h); lopsided buys/sells 4.29 | not scored |
| [RICE](https://pump.fun/coin/3rVr2RBzEXXKf1cVvZ6HBvFg2XmBK4iMgZv9q9q4pump) | `3rVr2RBzEXXKf1cVvZ6HBvFg2XmBK4iMgZv9q9q4pump` | $26.2k | $122.7k | +232% | +232% | +232% | 17.1x | thin liq $26.2k; spike (+232% 1h, +232% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $72.8k | $555.3k | -5% | +95% | +1149% | 55.1x | churn 55x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $48.6k | $439.6k | +14% | -43% | +1184% | 27.1x | thin liq $48.6k; churn 27x vol/liq | not scored |
| [Frogger](https://pump.fun/coin/GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump) | `GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump` | $20.1k | $77.8k | +160% | +160% | +160% | 7.3x | thin liq $20.1k; spike (+160% 1h, +160% 6h); < 1h old | not scored |
| [PRISMEICE](https://pump.fun/coin/8N6WF11pLUUeUu8b1HbnDJHTzyL4bbr8YRdPS6Znpump) | `8N6WF11pLUUeUu8b1HbnDJHTzyL4bbr8YRdPS6Znpump` | $22.0k | $99.3k | +61% | +233% | +233% | 20.6x | thin liq $22.0k | not scored |

_Timing: total 161s (discovery 71.7s, screen 1.4s, GT prime 0.3s, scoring 87.9s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/143; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
