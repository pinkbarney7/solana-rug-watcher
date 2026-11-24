# Last scan 2026-11-24T05:32:53Z - mode: helius (box heartbeat stale (87 min); budget 30/3000)

```
[fast_scan] 116 candidate mints from 10 source tags; 114 with pair data; 17 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored TROLL in 74s
[fast_scan] scored JENSEN in 74s
[fast_scan] scored CATE in 75s
[fast_scan] scored NVDA in 75s
[fast_scan] scored ROCKET in 76s
# Market scan 2026-11-24 05:32 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,579 (-1.3% 24h), ETH $1,705 (-1.5% 24h), SOL $71.60 (-0.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.8% (mcap $1.91B, vol $364.33M), pump-fun +2.5% (mcap $815.85M, vol $117.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $77.2k | $707.6k | 2.7 d | h24 -16% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 59* | SKIP | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $62.2k | $681.1k | 11.7 h | h24 +683% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $17.41M | 120.5 d | h24 -8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,837 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.89M | $20.11M | 843.8 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,706 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $1.80M | $644.2k | 158.9 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,634 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $104.4k | $2.07M | +11% | +5724% | +5724% | 9.2x | spike (+11% 1h, +5724% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $125.6k | $2.76M | +18% | +2419% | +2419% | 16.1x | liq/mcap 4.6%; spike (+18% 1h, +2419% 6h) | not scored |
| [BTC](https://dexscreener.com/solana/47we9WnmawtzZvmzNQKyKCW1853LrErftXzdxaxhEzKs) | `47we9WnmawtzZvmzNQKyKCW1853LrErftXzdxaxhEzKs` | $25.8k | $26.2k | +315% | +508% | +508% | 66.1x | thin liq $25.8k; churn 66x vol/liq; spike (+315% 1h, +508% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $39.0k | $139.9k | +5% | +5% | +1736% | 110.9x | thin liq $39.0k; churn 111x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $48.2k | $361.9k | -14% | -18% | +1170% | 41.8x | thin liq $48.2k; churn 42x vol/liq | not scored |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $51.2k | $468.2k | -35% | -41% | +439% | 45.4x | churn 45x vol/liq | 59 |

_Timing: total 148s (discovery 70.8s, screen 1.2s, GT prime 0.2s, scoring 75.9s for 5 coins, 5 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 39/108; Helius 429s 60; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
