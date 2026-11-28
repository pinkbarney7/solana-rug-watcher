# Last scan 2026-11-28T11:42:38Z - mode: helius (box heartbeat stale (453 min); budget 374/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 110 with pair data; 17 >= $50,000 liq; 5 pass survivor pre-gates (73s)
[fast_scan] scored UGOS in 71s
[fast_scan] scored CATE in 80s
[fast_scan] scored MoonBoy in 81s
[fast_scan] scored Memeball in 81s
[fast_scan] scored Rizzmas in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored USD2 in 90s
[fast_scan] scored BITCOINU in 106s
[fast_scan] scored mihao in 77s
# Market scan 2026-11-28 11:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,130 (-4.2% 24h), ETH $1,644 (-4.8% 24h), SOL $70.76 (-3.4% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.9% (mcap $1.83B, vol $358.96M), pump-fun -0.2% (mcap $794.13M, vol $143.95M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | SKIP | [USD2](https://dexscreener.com/solana/7Hdb2CicU2eMs3Q4CRQUs8P6eesk81i1qeVrujJAZ3en) | `7Hdb2CicU2eMs3Q4CRQUs8P6eesk81i1qeVrujJAZ3en` | $184.8k | $107.3k | 2.0 h | h24 +112% | sellability gate: Jupiter exit test FAIL: $25: no sell route (No routes found); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $323.4k | $17.80M | 2.4 d | h24 +55% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $162.2k | $793.1k | 15.0 h | h24 +1683% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $78.2k | $1.18M | 11.2 h | h24 +3490% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 62* | SKIP | [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $75.0k | $1.07M | 6.9 h | h24 +2882% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [UGOS](https://pump.fun/coin/FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump) | `FTF6S5GJvnBMcKALHZFP5Lbg9DeEEqtdrVBBraUYpump` | $970.7k | $189.21M | 1.6 d | h24 +56% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [mihao](https://pump.fun/coin/4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump) | `4CxjZyMNoF1p6eXHXHv1TWpS2X47CuUmLwtGe18spump` | $601.1k | $5.55M | 20785.5 d | h24 -4% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 2h (now 76,715) |
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $223.6k | $661.4k | 1069.7 d | h24 +9% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,811 (growth n/a: first sighting) |
| 64* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.20M | $165.89B | 20785.5 d | h24 -1% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 439,200 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $77.9k | $1.17M | +6% | +35% | +3460% | 11.3x | lopsided buys/sells 3.29 | 59 |
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $75.0k | $1.07M | -6% | -2% | +2885% | 20.3x | none flagged (still high risk) | 62 |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $88.2k | $793.1k | +32% | +38% | +1683% | 50.6x | churn 51x vol/liq | 55 |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $43.6k | $320.9k | +8% | +16% | +1012% | 42.3x | thin liq $43.6k; churn 42x vol/liq | not scored |
| [Vicewire](https://dexscreener.com/solana/viCEWiReoWxwmRRfGmWmpP1FFdB8Jm8PzZChVJ9dvg6) | `viCEWiReoWxwmRRfGmWmpP1FFdB8Jm8PzZChVJ9dvg6` | $28.8k | $150.1k | +39% | +250% | +379% | 35.4x | thin liq $28.8k; churn 35x vol/liq | not scored |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $31.4k | $184.2k | -61% | -56% | +438% | 55.2x | thin liq $31.4k; churn 55x vol/liq | not scored |

_Timing: total 221s (discovery 71.6s, screen 1.1s, GT prime 0.3s, scoring 147.8s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/180; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
