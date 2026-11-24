# Last scan 2026-11-24T04:39:32Z - mode: helius (box heartbeat stale (33 min); budget 581/3000)

```
[fast_scan] 124 candidate mints from 10 source tags; 122 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored JINGWA in 72s
[fast_scan] scored JENSEN in 80s
[fast_scan] scored TROLL in 81s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored NVDA in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored USPR in 83s
[fast_scan] scored ROCKET in 84s
# Market scan 2026-11-24 04:39 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,484 (-0.9% 24h), ETH $1,700 (-1.4% 24h), SOL $71.82 (+0.9% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.3% (mcap $1.90B, vol $347.87M), pump-fun +2.0% (mcap $812.05M, vol $114.99M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $75.8k | $685.1k | 2.7 d | h24 -19% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [JINGWA](https://dexscreener.com/solana/ChZzab3vUf5WTkQm2Q13AB9YjY3oCa2JbY2QRVohn8K) | `ChZzab3vUf5WTkQm2Q13AB9YjY3oCa2JbY2QRVohn8K` | $126.0k | $75.5k | 1.7 h | h24 +104% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $69.7k | $402.2k | 7.5 h | h24 +1312% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $63.6k | $711.2k | 10.8 h | h24 +718% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [USPR](https://pump.fun/coin/2LXJm8BfdyJEX1hMPt3D618zheBKLrWe8rBKqQympump) | `2LXJm8BfdyJEX1hMPt3D618zheBKLrWe8rBKqQympump` | $890.1k | $156.84M | 1.0 d | h24 +35% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.6% (+11.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.89M | $19.97M | 843.7 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 15h (now 218,708) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.80M | $645.1k | 158.9 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,427 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.09M | $18.8k | 404.5 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.4% in 19h (now 395,360) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $101.5k | $1.96M | +56% | +5404% | +5404% | 8.9x | spike (+56% 1h, +5404% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $120.6k | $2.55M | +360% | +2232% | +2232% | 16.2x | liq/mcap 4.7%; spike (+360% 1h, +2232% 6h) | not scored |
| [CHIBI](https://dexscreener.com/solana/DoakE72qU5zvcsj9EiKCgCTdQCd5BqG6L1fcQ46MmU7Q) | `DoakE72qU5zvcsj9EiKCgCTdQCd5BqG6L1fcQ46MmU7Q` | $30.0k | $28.2k | +316% | +316% | +316% | 51.3x | thin liq $30.0k; churn 51x vol/liq; spike (+316% 1h, +316% 6h); < 1h old | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $39.4k | $142.2k | -9% | -25% | +1766% | 109.7x | thin liq $39.4k; churn 110x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $50.9k | $402.2k | +30% | +40% | +1312% | 38.5x | churn 39x vol/liq | 55 |
| [CHIBI](https://pump.fun/coin/4ZgqnNi53sRKKegFpYefFjsFE6zQ3T64Xkavcoh7pump) | `4ZgqnNi53sRKKegFpYefFjsFE6zQ3T64Xkavcoh7pump` | $25.5k | $109.9k | +34% | +308% | +308% | 53.1x | thin liq $25.5k; churn 53x vol/liq; spike (+34% 1h, +308% 6h) | not scored |

_Timing: total 157s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 84.2s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/159; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
