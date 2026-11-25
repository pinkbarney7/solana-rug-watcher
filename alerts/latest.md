# Last scan 2026-11-25T05:39:17Z - mode: helius (box heartbeat stale (105 min); budget 30/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 118 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 77s
[fast_scan] scored CATE in 85s
[fast_scan] scored pippin in 85s
[fast_scan] scored SPCX in 85s
[fast_scan] scored JIMMY in 86s
# Market scan 2026-11-25 05:39 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,079 (-2.6% 24h), ETH $1,656 (-3.0% 24h), SOL $68.51 (-4.5% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.7% (mcap $1.79B, vol $322.80M), pump-fun -6.2% (mcap $761.85M, vol $138.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $57.8k | $112.9k | 2.7 d | h24 -23% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $246.7k | $1.54M | 1.4 d | h24 +355% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.57M | $16.51M | 121.6 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 436,951) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.39M | $18.60M | 745.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,577 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $13.04M | 181.9 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,170 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $77.0k | $1.14M | +4% | +2896% | +2896% | 20.2x | spike (+4% 1h, +2896% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $74.5k | $1.10M | -1% | +540% | +3378% | 9.1x | spike (-1% 1h, +540% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $67.8k | $698.7k | -52% | +323% | +2451% | 52.3x | churn 52x vol/liq; spike (-52% 1h, +323% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $91.8k | $336.2k | +380% | +380% | +380% | 10.1x | spike (+380% 1h, +380% 6h); < 1h old | not scored |
| [FUCKCANCER](https://pump.fun/coin/4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump) | `4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump` | $24.5k | $124.1k | +356% | +356% | +356% | 11.1x | thin liq $24.5k; spike (+356% 1h, +356% 6h); < 1h old | not scored |
| [TIKTOK](https://dexscreener.com/solana/BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57) | `BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57` | $141.1k | $184.9k | +149% | +271% | +271% | 68.6x | churn 69x vol/liq; spike (+149% 1h, +271% 6h) | not scored |

_Timing: total 159s (discovery 71.8s, screen 1.4s, GT prime 0.4s, scoring 85.5s for 5 coins, 5 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 5/116; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
