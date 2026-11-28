# Last scan 2026-11-28T11:23:03Z - mode: helius (box heartbeat stale (434 min); budget 344/3000)

```
[fast_scan] 116 candidate mints from 10 source tags; 114 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored MoonBoy in 80s
[fast_scan] scored Rizzmas in 82s
[fast_scan] scored BITCOINU in 88s
[fast_scan] scored Optimus in 98s
[fast_scan] scored USD2 in 108s
[fast_scan] scored Mojave in 108s
[fast_scan] scored CATE in 80s
# Market scan 2026-11-28 11:22 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,222 (-3.8% 24h), ETH $1,647 (-4.5% 24h), SOL $70.74 (-3.4% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.7% (mcap $1.83B, vol $357.90M), pump-fun -0.5% (mcap $793.55M, vol $145.74M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [Optimus](https://dexscreener.com/solana/3b71UijUNK5iVRCAeBRorB4A8Y3qErdAhMcoTX28gXS6) | `3b71UijUNK5iVRCAeBRorB4A8Y3qErdAhMcoTX28gXS6` | $201.0k | $137.3k | 1.8 h | h24 +172% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 47* | CAUTION | [USD2](https://dexscreener.com/solana/7Hdb2CicU2eMs3Q4CRQUs8P6eesk81i1qeVrujJAZ3en) | `7Hdb2CicU2eMs3Q4CRQUs8P6eesk81i1qeVrujJAZ3en` | $174.7k | $101.8k | 1.7 h | h24 +102% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 47* | CAUTION | [Mojave](https://dexscreener.com/solana/3kzBSsT32SyWx8QyGihmbena8v1w2mW7cCWtwHnwx2WW) | `3kzBSsT32SyWx8QyGihmbena8v1w2mW7cCWtwHnwx2WW` | $171.2k | $119.6k | 1.2 h | h24 +133% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $322.2k | $17.69M | 2.4 d | h24 +68% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $158.4k | $819.2k | 14.7 h | h24 +1742% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 62* | SKIP | [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $77.2k | $1.14M | 6.6 h | h24 +3064% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.3k | $653.8k | 1069.7 d | h24 +4% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,811 (growth n/a: first sighting) |
| 64* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.20M | $165.89B | 20785.5 d | h24 -2% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 439,200 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.84M | $13.99M | 20785.5 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 4h (now 403,544) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $77.2k | $1.14M | -6% | +6% | +3064% | 19.4x | none flagged (still high risk) | 62 |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $72.5k | $1.02M | -8% | +18% | +3001% | 11.8x | lopsided buys/sells 3.33 | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $90.1k | $819.2k | +27% | +62% | +1742% | 49.1x | churn 49x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $58.8k | $627.0k | +23% | +50% | +1732% | 28.9x | churn 29x vol/liq | not scored |
| [SPSC](https://pump.fun/coin/EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump) | `EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump` | $29.0k | $166.6k | +52% | +485% | +485% | 19.4x | thin liq $29.0k; spike (+52% 1h, +485% 6h) | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $44.5k | $333.1k | +10% | +222% | +1055% | 40.8x | thin liq $44.5k; churn 41x vol/liq | not scored |

_Timing: total 224s (discovery 71.7s, screen 1.1s, GT prime 0.4s, scoring 150.3s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/181; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
