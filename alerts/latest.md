# Last scan 2026-11-28T05:37:02Z - mode: helius (box heartbeat stale (89 min); budget 30/3000)

```
[fast_scan] 120 candidate mints from 9 source tags; 119 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored UGOS in 77s
[fast_scan] scored MoonBoy in 86s
[fast_scan] scored CATE in 86s
[fast_scan] scored USOI in 87s
[fast_scan] scored PUMPCHAN in 88s
[fast_scan] scored Rizzmas in 88s
[fast_scan] scored neet in 90s
# Market scan 2026-11-28 05:36 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,736 (-3.3% 24h), ETH $1,656 (-5.2% 24h), SOL $71.32 (-2.7% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.1% (mcap $1.86B, vol $278.23M), pump-fun +0.6% (mcap $800.94M, vol $96.21M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $320.4k | $17.39M | 2.2 d | h24 +20% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $106.0k | $540.1k | 9.0 h | h24 +1114% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $937.1k | $174.77M | 1.3 d | h24 +65% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 67* | SKIP | [USOI](https://pump.fun/coin/HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump) | `HQs4Zd8w1jGR72o43iP58U43QtDdTTUE3Dq9Dv4dpump` | $776.7k | $120.16M | 1.4 d | h24 +18% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.1k | $640.6k | 1069.5 d | h24 -9% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,807 (growth n/a: first sighting) |
| 43* | CAUTION | [neet](https://pump.fun/coin/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | `Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump` | $1.78M | $19.30M | 580.2 d | h24 -7% | #3 Liquidity vs market cap WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 129,107) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.65M | $17.34M | 124.6 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 439,202) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $83.4k | $1.35M | +3672% | +3672% | +3672% | 10.4x | spike (+3672% 1h, +3672% 6h); < 1h old | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $66.2k | $848.0k | +27% | +2488% | +2488% | 10.4x | spike (+27% 1h, +2488% 6h); lopsided buys/sells 4.13 | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $31.6k | $183.0k | +534% | +534% | +534% | 21.5x | thin liq $31.6k; spike (+534% 1h, +534% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $71.9k | $540.1k | -6% | +16% | +1114% | 57.0x | churn 57x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $47.3k | $416.0k | -6% | -35% | +1115% | 28.8x | thin liq $47.3k; churn 29x vol/liq | not scored |
| [Zhaki](https://pump.fun/coin/2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump) | `2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump` | $34.5k | $203.1k | +53% | +100% | +570% | 45.2x | thin liq $34.5k; churn 45x vol/liq | not scored |

_Timing: total 163s (discovery 71.8s, screen 1.1s, GT prime 0.3s, scoring 89.6s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
