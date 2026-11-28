# Last scan 2026-11-28T06:08:30Z - mode: helius (box heartbeat stale (120 min); budget 50/3000)

```
[fast_scan] 120 candidate mints from 10 source tags; 119 with pair data; 23 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored ZEC in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored USOI in 79s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored UGOS in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored Rizzmas in 82s
# Market scan 2026-11-28 06:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,666 (-3.3% 24h), ETH $1,653 (-5.0% 24h), SOL $71.15 (-2.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.0% (mcap $1.84B, vol $286.02M), pump-fun -0.0% (mcap $795.85M, vol $95.36M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $99.5k | $497.8k | 9.5 h | h24 +1019% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $317.2k | $17.11M | 2.2 d | h24 +66% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.9% (+9.8); #11 not checked (+3) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $936.7k | $175.39M | 1.4 d | h24 +66% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $774.8k | $120.09M | 1.4 d | h24 +18% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $219.6k | $634.3k | 1069.5 d | h24 -8% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,807 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.80M | $13.99M | 184.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 403,582 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.29M | $18.1k | 408.6 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.0% in 4h (now 397,090) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $68.8k | $919.2k | +15% | +2705% | +2705% | 10.2x | spike (+15% 1h, +2705% 6h); lopsided buys/sells 4.04 | not scored |
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $68.6k | $917.9k | -29% | +2459% | +2459% | 14.6x | spike (-29% 1h, +2459% 6h) | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $38.0k | $251.8k | +211% | +773% | +773% | 29.3x | thin liq $38.0k; churn 29x vol/liq; spike (+211% 1h, +773% 6h) | not scored |
| [Split](https://pump.fun/coin/HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump) | `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump` | $24.9k | $89.0k | +282% | -31% | +191% | 64.7x | thin liq $24.9k; churn 65x vol/liq; spike (+282% 1h, -31% 6h) | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $70.6k | $520.5k | +8% | +23% | +1070% | 58.4x | churn 58x vol/liq | 54 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $45.3k | $384.2k | -8% | -43% | +1023% | 30.6x | thin liq $45.3k; churn 31x vol/liq | not scored |

_Timing: total 154s (discovery 71.0s, screen 1.1s, GT prime 0.4s, scoring 81.6s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/142; Helius 429s 81; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
