# Last scan 2026-11-28T09:57:41Z - mode: helius (box heartbeat stale (348 min); budget 240/3000)

```
[fast_scan] 113 candidate mints from 9 source tags; 112 with pair data; 20 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored Fireball in 78s
[fast_scan] scored MoonBoy in 86s
[fast_scan] scored COMM in 87s
[fast_scan] scored VINE in 87s
[fast_scan] scored NIAN in 88s
[fast_scan] scored USFF in 89s
[fast_scan] scored PUMPCHAN in 89s
[fast_scan] scored Rizzmas in 90s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-28 09:57 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,517 (-3.5% 24h), ETH $1,650 (-4.6% 24h), SOL $70.93 (-3.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.3% (mcap $1.84B, vol $347.05M), pump-fun -0.5% (mcap $796.97M, vol $135.64M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $50.6k | $469.2k | 19.8 h | h24 +1271% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [NIAN](https://dexscreener.com/solana/43B7Qd2Xy2Dw2bjEN4kB8APjMegz1yZNSW789YFeAsap) | `43B7Qd2Xy2Dw2bjEN4kB8APjMegz1yZNSW789YFeAsap` | $217.1k | $123.3k | 2.2 h | h24 +71% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [USFF](https://dexscreener.com/solana/2X879XRBj6J4KvnR2qLhSGnVf2rXj9UGmrexj2wR36d6) | `2X879XRBj6J4KvnR2qLhSGnVf2rXj9UGmrexj2wR36d6` | $204.7k | $151.5k | 2.1 h | h24 +196% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [COMM](https://dexscreener.com/solana/3SPuqaCE2tTfTSr5Kn9sNh9J1VQJRtW6yNiEj32Mjh3X) | `3SPuqaCE2tTfTSr5Kn9sNh9J1VQJRtW6yNiEj32Mjh3X` | $171.0k | $119.3k | 1.2 h | h24 +133% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $324.8k | $17.94M | 2.4 d | h24 +76% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #11 not checked (+3) |
| 55* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $97.2k | $534.2k | 13.3 h | h24 +1101% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.0k | $650.9k | 1069.7 d | h24 +4% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,805 (growth n/a: first sighting) |
| 47* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.29M | 674.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,172 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.20M | $165.89B | 124.7 d | h24 +985019% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 439,195 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $80.8k | $1.24M | +5% | +3370% | +3370% | 17.3x | spike (+5% 1h, +3370% 6h) | not scored |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $73.6k | $1.04M | +9% | +55% | +3087% | 11.1x | lopsided buys/sells 3.54 | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $37.6k | $242.0k | -8% | +739% | +739% | 46.1x | thin liq $37.6k; churn 46x vol/liq; spike (-8% 1h, +739% 6h) | not scored |
| [NVIDIA](https://pump.fun/coin/CtvgHuV7MhwypXUg1BfsqSHxvQ7rZdDyS1SiMuempump) | `CtvgHuV7MhwypXUg1BfsqSHxvQ7rZdDyS1SiMuempump` | $23.6k | $121.1k | +311% | +311% | +311% | 4.1x | thin liq $23.6k; spike (+311% 1h, +311% 6h); < 1h old | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $71.7k | $534.2k | +25% | -12% | +1101% | 59.0x | churn 59x vol/liq | 55 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $50.4k | $464.4k | -1% | +14% | +1257% | 31.9x | churn 32x vol/liq | 52 |

_Timing: total 223s (discovery 71.9s, screen 1.2s, GT prime 0.5s, scoring 149.9s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
