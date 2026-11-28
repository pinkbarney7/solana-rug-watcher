# Last scan 2026-11-28T11:05:45Z - mode: helius (box heartbeat stale (415 min); budget 270/3000)

```
[fast_scan] 115 candidate mints from 10 source tags; 114 with pair data; 26 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored NIAN in 80s
[fast_scan] scored PUMPCHAN in 89s
[fast_scan] scored Rizzmas in 91s
[fast_scan] scored BITCOINU in 107s
[fast_scan] scored DOG in 108s
[fast_scan] scored Optimus in 178s
[fast_scan] scored MoonBoy in 185s
[fast_scan] scored CATE in 105s
[fast_scan] scored VINE in 224s
# Market scan 2026-11-28 11:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,214 (-3.8% 24h), ETH $1,645 (-4.8% 24h), SOL $70.68 (-3.5% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.3% (mcap $1.84B, vol $355.14M), pump-fun -0.4% (mcap $793.91M, vol $139.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [DOG](https://dexscreener.com/solana/9ug1ZrRRA62yA24LbTLN1pSbwL1vvNK6mXc2gvgYmpBg) | `9ug1ZrRRA62yA24LbTLN1pSbwL1vvNK6mXc2gvgYmpBg` | $185.4k | $146.4k | 2.6 h | h24 +85% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 47* | CAUTION | [Optimus](https://dexscreener.com/solana/3b71UijUNK5iVRCAeBRorB4A8Y3qErdAhMcoTX28gXS6) | `3b71UijUNK5iVRCAeBRorB4A8Y3qErdAhMcoTX28gXS6` | $183.0k | $120.8k | 1.5 h | h24 +139% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #6 unknown (+3) |
| 53* | SKIP | [NIAN](https://dexscreener.com/solana/43B7Qd2Xy2Dw2bjEN4kB8APjMegz1yZNSW789YFeAsap) | `43B7Qd2Xy2Dw2bjEN4kB8APjMegz1yZNSW789YFeAsap` | $237.3k | $140.2k | 3.4 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 54* | SKIP | [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $124.6k | $724.2k | 14.4 h | h24 +1528% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $324.0k | $17.89M | 2.4 d | h24 +67% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.8% (+9.8); #6 unknown (+3) |
| 62* | SKIP | [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $78.5k | $1.17M | 6.3 h | h24 +3171% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.1k | $653.4k | 1069.7 d | h24 +4% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,811 (growth n/a: first sighting) |
| 50* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.30M | 674.5 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #18 Wash trading (recent swaps) WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 345,170) |
| 64* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.20M | $165.89B | 20785.5 d | h24 -2% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders 439,194 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BITCOINU](https://pump.fun/coin/ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump) | `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump` | $78.5k | $1.17M | -6% | +81% | +3171% | 18.9x | none flagged (still high risk) | 62 |
| [Memeball](https://pump.fun/coin/9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump) | `9G9Ssh55SZEoniFjMrMefug9fBy67bUvHzWAxb5Ypump` | $73.2k | $1.04M | +2% | +32% | +3061% | 11.6x | lopsided buys/sells 3.37 | not scored |
| [MoonBoy](https://pump.fun/coin/GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump) | `GXjSWDoMQkDEbhon9ALxz8chUUsVKg3x8V3NajjDpump` | $83.7k | $715.8k | +30% | +73% | +1509% | 51.9x | churn 52x vol/liq | 54 |
| [Fireball](https://pump.fun/coin/B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump) | `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump` | $55.2k | $554.5k | +29% | +36% | +1520% | 30.3x | churn 30x vol/liq | not scored |
| [WLFI](https://pump.fun/coin/HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump) | `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump` | $42.7k | $308.9k | +29% | +158% | +971% | 42.1x | thin liq $42.7k; churn 42x vol/liq | not scored |
| [SPSC](https://pump.fun/coin/EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump) | `EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump` | $27.3k | $149.1k | +31% | +423% | +423% | 20.3x | thin liq $27.3k; spike (+31% 1h, +423% 6h) | not scored |

_Timing: total 296s (discovery 71.1s, screen 1.1s, GT prime 0.3s, scoring 223.8s for 9 coins, 9 newly scored). ~74 Helius credits (smart-money discovery 20). HTTP cache hits 11/200; Helius 429s 130; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
