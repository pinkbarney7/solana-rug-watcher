# Last scan 2026-11-28T06:20:38Z - mode: helius (box heartbeat stale (132 min); budget 70/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 118 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored MoonBoy in 72s
[fast_scan] scored USOI in 80s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored SPCX in 83s
[fast_scan] scored UGOS in 83s
[fast_scan] scored Rizzmas in 84s
[fast_scan] scored Snowball in 85s
# Market scan 2026-11-28 06:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,716 (-3.4% 24h), ETH $1,656 (-4.8% 24h), SOL $71.28 (-2.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.4% (mcap $1.83B, vol $290.63M), pump-fun +0.1% (mcap $796.62M, vol $95.26M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $77.5k | $411.4k | 2.5 d | h24 -33% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $99.0k | $473.3k | 9.7 h | h24 +964% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $328.0k | $18.26M | 2.2 d | h24 +76% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $939.9k | $176.24M | 1.4 d | h24 +67% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $776.8k | $120.48M | 1.4 d | h24 +18% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.2k | $637.0k | 1069.5 d | h24 -8% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,808 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.32M | $169.24B | 124.6 d | h24 +965614% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 439,204 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.80M | $13.98M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,582 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $70.4k | $959.5k | +10% | +2828% | +2828% | 10.1x | spike (+10% 1h, +2828% 6h); lopsided buys/sells 4.01 | not scored |
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $69.9k | $949.8k | -7% | +2548% | +2548% | 14.7x | spike (-7% 1h, +2548% 6h) | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $39.5k | $275.6k | +175% | +855% | +855% | 30.2x | thin liq $39.5k; churn 30x vol/liq; spike (+175% 1h, +855% 6h) | not scored |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $47.4k | $418.6k | +0% | -38% | +1123% | 29.5x | thin liq $47.4k; churn 30x vol/liq | not scored |
| [Split](https://pump.fun/coin/HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump) | `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump` | $23.3k | $78.7k | +208% | -29% | +157% | 69.5x | thin liq $23.3k; churn 69x vol/liq; spike (+208% 1h, -29% 6h) | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $67.2k | $473.3k | -8% | +0% | +964% | 61.5x | churn 61x vol/liq | 54 |

_Timing: total 158s (discovery 71.4s, screen 1.2s, GT prime 0.4s, scoring 85.1s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
