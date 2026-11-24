# Last scan 2026-11-24T06:58:55Z - mode: helius (box heartbeat stale (172 min); budget 80/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 115 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored ROCKET in 79s
[fast_scan] scored ACHI in 86s
[fast_scan] scored TROLL in 87s
[fast_scan] scored JENSEN in 87s
[fast_scan] scored NVDA in 87s
[fast_scan] scored SuperJense in 88s
[fast_scan] scored CATE in 88s
# Market scan 2026-11-24 06:58 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,482 (-1.5% 24h), ETH $1,700 (-1.3% 24h), SOL $71.86 (-0.1% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.6% (mcap $1.91B, vol $363.12M), pump-fun +1.8% (mcap $818.61M, vol $114.47M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.5k | $768.6k | 2.8 d | h24 -10% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 48* | CAUTION | [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $53.1k | $495.9k | 13.2 h | h24 +470% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $187.7k | $126.5k | 1.4 h | h24 +148% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $95.6k | $119.8k | 1.6 h | h24 +170% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.94M | $20.19M | 843.8 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders 218,683 (growth n/a: first sighting) |
| 68* | SKIP | [NVDA](https://dexscreener.com/solana/NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv) | `NVDAVuiB7hwd3m5Wa1JuHNovPaPG6BH1QNztbKFxNjv` | $2.00M | $645.0k | 159.0 d | h24 +22% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 46,511 (growth n/a: first sighting) |
| 71* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $4.29M | $87.19B | 120.6 d | h24 +464368% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); GATES FAILED: rug-funder link; holders 436,804 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $105.0k | $2.08M | -5% | +5747% | +5747% | 9.9x | spike (-5% 1h, +5747% 6h) | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $133.8k | $3.13M | +12% | +2754% | +2754% | 15.5x | liq/mcap 4.3%; spike (+12% 1h, +2754% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $36.7k | $124.2k | -7% | -29% | +1545% | 118.3x | thin liq $36.7k; churn 118x vol/liq | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $46.0k | $326.1k | +21% | +68% | +1045% | 45.8x | thin liq $46.0k; churn 46x vol/liq | not scored |
| [SuperJense](https://dexscreener.com/solana/2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J) | `2eRz2GUQozCxFdmjdjYG7FUY3U3WSB2FfPrxJWR4Lu8J` | $187.3k | $125.8k | +64% | +146% | +146% | 50.7x | churn 51x vol/liq | 53 |
| [JENSEN](https://pump.fun/coin/HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump) | `HKiMA2mKQHU2cjfZ4Kbmru5GBGCauSNqPtpu8cfmpump` | $53.0k | $495.9k | +6% | -28% | +470% | 45.0x | churn 45x vol/liq | 48 |

_Timing: total 161s (discovery 71.4s, screen 1.5s, GT prime 0.2s, scoring 87.7s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/147; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
