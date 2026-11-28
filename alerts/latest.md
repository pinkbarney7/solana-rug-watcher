# Last scan 2026-11-28T05:56:57Z - mode: helius (box heartbeat stale (109 min); budget 40/3000)

```
[fast_scan] 121 candidate mints from 10 source tags; 120 with pair data; 24 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored USOI in 77s
[fast_scan] scored SPCX in 86s
[fast_scan] scored PUMPCHAN in 86s
[fast_scan] scored MoonBoy in 86s
[fast_scan] scored CATE in 87s
[fast_scan] scored UGOS in 88s
[fast_scan] scored Rizzmas in 89s
# Market scan 2026-11-28 05:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,737 (-3.1% 24h), ETH $1,654 (-4.9% 24h), SOL $71.19 (-2.6% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.8% (mcap $1.84B, vol $271.23M), pump-fun +0.2% (mcap $797.86M, vol $93.49M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $101.3k | $514.1k | 9.3 h | h24 +1056% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $316.3k | $17.02M | 2.2 d | h24 +67% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.8); #11 not checked (+3) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $935.3k | $174.88M | 1.4 d | h24 +66% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $774.2k | $119.90M | 1.4 d | h24 +18% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $219.4k | $633.5k | 1069.5 d | h24 -11% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,807 (growth n/a: first sighting) |
| 64* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.31M | $169.24B | 124.6 d | h24 -4% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 439,204 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.81M | $13.99M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,582 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $83.8k | $1.37M | +121% | +3709% | +3709% | 11.3x | spike (+121% 1h, +3709% 6h) | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $67.1k | $875.0k | +8% | +2570% | +2570% | 10.4x | spike (+8% 1h, +2570% 6h); lopsided buys/sells 4.09 | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $42.9k | $336.8k | +185% | +1068% | +1068% | 22.8x | thin liq $42.9k; spike (+185% 1h, +1068% 6h) | not scored |
| [Split](https://pump.fun/coin/HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump) | `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump` | $21.1k | $65.7k | +227% | -49% | +115% | 75.7x | thin liq $21.1k; churn 76x vol/liq; spike (+227% 1h, -49% 6h) | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $69.8k | $510.7k | +13% | -5% | +1048% | 58.9x | churn 59x vol/liq | 54 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $46.3k | $400.5k | +1% | -44% | +1070% | 29.8x | thin liq $46.3k; churn 30x vol/liq | not scored |

_Timing: total 162s (discovery 71.4s, screen 1.6s, GT prime 0.3s, scoring 88.7s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/143; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
