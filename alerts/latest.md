# Last scan 2026-11-24T05:10:16Z - mode: helius (box heartbeat stale (64 min); budget 0/3000)

```
[fast_scan] 122 candidate mints from 10 source tags; 120 with pair data; 23 >= $50,000 liq; 6 pass survivor pre-gates (72s)
[fast_scan] scored JINGWA in 78s
[fast_scan] scored NVDA in 78s
[fast_scan] scored CATE in 86s
[fast_scan] scored JIMMY in 87s
[fast_scan] scored JENSEN in 88s
[fast_scan] scored TROLL in 88s
[fast_scan] scored ROCKET in 88s
# Market scan 2026-11-24 05:10 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,440 (-1.2% 24h), ETH $1,701 (-1.4% 24h), SOL $71.70 (+0.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.4% (mcap $1.90B, vol $363.99M), pump-fun +2.2% (mcap $813.66M, vol $117.47M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $76.0k | $686.0k | 2.7 d | h24 -16% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [JINGWA](https://dexscreener.com/solana/ChZzab3vUf5WTkQm2Q13AB9YjY3oCa2JbY2QRVohn8K) | `ChZzab3vUf5WTkQm2Q13AB9YjY3oCa2JbY2QRVohn8K` | $138.6k | $81.5k | 2.2 h | h24 +120% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $69.1k | $382.7k | 8.1 h | h24 +1244% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $58.7k | $608.0k | 11.4 h | h24 +599% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.67M | $17.22M | 120.5 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,837 (growth n/a: first sighting) |
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.88M | $19.88M | 843.7 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,711 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.80M | $643.9k | 158.9 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,453 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $102.3k | $1.99M | +19% | +5493% | +5493% | 9.3x | spike (+19% 1h, +5493% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $118.2k | $2.46M | +35% | +2145% | +2145% | 16.7x | liq/mcap 4.8%; spike (+35% 1h, +2145% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $38.2k | $134.1k | -2% | +2% | +1660% | 113.3x | thin liq $38.2k; churn 113x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $50.0k | $388.4k | +1% | +23% | +1263% | 40.0x | churn 40x vol/liq | 55 |
| [Ponder](https://dexscreener.com/solana/6xKLxVZfUUsh7txi2NwhWovBYKBb6KvpGinTBtRhZq83) | `6xKLxVZfUUsh7txi2NwhWovBYKBb6KvpGinTBtRhZq83` | $147.1k | $103.5k | +133% | +133% | +133% | 28.2x | churn 28x vol/liq; spike (+133% 1h, +133% 6h); < 1h old | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $58.6k | $608.0k | +6% | -20% | +599% | 39.4x | churn 39x vol/liq | 59 |

_Timing: total 161s (discovery 71.1s, screen 1.3s, GT prime 0.3s, scoring 87.9s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/143; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
