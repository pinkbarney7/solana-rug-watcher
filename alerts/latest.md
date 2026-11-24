# Last scan 2026-11-24T05:30:05Z - mode: helius (box heartbeat stale (84 min); budget 30/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 17 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored ROCKET in 70s
[fast_scan] scored CATE in 77s
[fast_scan] scored NVDA in 77s
[fast_scan] scored TROLL in 78s
[fast_scan] scored JENSEN in 78s
# Market scan 2026-11-24 05:30 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,580 (-1.3% 24h), ETH $1,705 (-1.4% 24h), SOL $71.64 (+0.1% 24h)
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
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $102.8k | $2.01M | +5% | +5552% | +5552% | 9.4x | spike (+5% 1h, +5552% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $131.5k | $3.04M | +27% | +2672% | +2672% | 15.4x | liq/mcap 4.3%; spike (+27% 1h, +2672% 6h) | not scored |
| [BTC](https://dexscreener.com/solana/47we9WnmawtzZvmzNQKyKCW1853LrErftXzdxaxhEzKs) | `47we9WnmawtzZvmzNQKyKCW1853LrErftXzdxaxhEzKs` | $28.7k | $33.2k | +295% | +669% | +669% | 56.6x | thin liq $28.7k; churn 57x vol/liq; spike (+295% 1h, +669% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $38.8k | $138.4k | +3% | +8% | +1717% | 111.6x | thin liq $38.8k; churn 112x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $48.5k | $366.6k | +1% | -19% | +1187% | 41.5x | thin liq $48.5k; churn 42x vol/liq | not scored |
| [Spidercow](https://pump.fun/coin/9oxUBRyk9EXfQHMchya45p3xsF2fbNzzDUNKzEfKpump) | `9oxUBRyk9EXfQHMchya45p3xsF2fbNzzDUNKzEfKpump` | $18.6k | $68.8k | +132% | +132% | +132% | 16.1x | thin liq $18.6k; spike (+132% 1h, +132% 6h); < 1h old | not scored |

_Timing: total 151s (discovery 71.1s, screen 1.1s, GT prime 0.3s, scoring 78.0s for 5 coins, 5 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 5/110; Helius 429s 60; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
