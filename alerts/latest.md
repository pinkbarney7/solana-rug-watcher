# Last scan 2026-11-28T04:44:41Z - mode: helius (box heartbeat stale (37 min); budget 525/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 131 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored MoonBoy in 79s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored UGOS in 81s
[fast_scan] scored Rizzmas in 81s
# Market scan 2026-11-28 04:44 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,986 (-2.5% 24h), ETH $1,663 (-4.2% 24h), SOL $71.59 (-1.8% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.5% (mcap $1.90B, vol $254.93M), pump-fun +1.8% (mcap $807.62M, vol $96.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [MoonBoy](https://dexscreener.com/solana/APzXPGGfnXQgabrt9tCyXdBFLCgwKRdkminNjFfXmQV) | `APzXPGGfnXQgabrt9tCyXdBFLCgwKRdkminNjFfXmQV` | $97.5k | $58.4k | 1.2 h | h24 +48% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $321.9k | $17.53M | 2.1 d | h24 +57% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $104.7k | $492.0k | 8.1 h | h24 +1006% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $933.0k | $172.86M | 1.3 d | h24 +64% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.4k | $634.9k | 1069.4 d | h24 -7% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,801 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.65M | $17.24M | 124.5 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 439,199 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.80M | $14.08M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,392 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $55.2k | $593.9k | -24% | +1712% | +1712% | 11.8x | spike (-24% 1h, +1712% 6h); lopsided buys/sells 4.28 | not scored |
| [RICE](https://pump.fun/coin/3rVr2RBzEXXKf1cVvZ6HBvFg2XmBK4iMgZv9q9q4pump) | `3rVr2RBzEXXKf1cVvZ6HBvFg2XmBK4iMgZv9q9q4pump` | $28.5k | $156.9k | +324% | +324% | +324% | 17.4x | thin liq $28.5k; spike (+324% 1h, +324% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $68.4k | $492.0k | -9% | +98% | +1006% | 58.8x | churn 59x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $48.4k | $435.5k | +8% | -43% | +1172% | 27.4x | thin liq $48.4k; churn 27x vol/liq | not scored |
| [Frogger](https://pump.fun/coin/GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump) | `GGatn9GfrvRgFMFZy9ZSaTsKmpwnzCTogmocLHCjpump` | $18.3k | $70.9k | +137% | +137% | +137% | 10.2x | thin liq $18.3k; spike (+137% 1h, +137% 6h); < 1h old | not scored |
| [Zhaki](https://pump.fun/coin/2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump) | `2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump` | $30.3k | $158.7k | +10% | +70% | +424% | 49.9x | thin liq $30.3k; churn 50x vol/liq | not scored |

_Timing: total 154s (discovery 71.5s, screen 1.4s, GT prime 0.2s, scoring 81.0s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/143; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
