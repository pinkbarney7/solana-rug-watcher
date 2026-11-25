# Last scan 2026-11-25T09:18:48Z - mode: helius (box heartbeat stale (325 min); budget 183/3000)

```
[fast_scan] 116 candidate mints from 10 source tags; 111 with pair data; 20 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 73s
[fast_scan] scored Jimmies in 79s
[fast_scan] scored MOODENG in 80s
[fast_scan] scored BOOBS in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored MANIFEST in 84s
[fast_scan] scored JIMMY in 84s
# Market scan 2026-11-25 09:18 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,050 (-1.3% 24h), ETH $1,643 (-2.2% 24h), SOL $67.57 (-4.3% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.0% (mcap $1.78B, vol $323.23M), pump-fun -4.3% (mcap $755.42M, vol $136.17M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $53.3k | $98.8k | 2.8 d | h24 -50% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $229.3k | $1.21M | 1.5 d | h24 +221% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $78.6k | $1.23M | 10.0 h | h24 +3773% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $102.1k | $1.98M | 8.9 h | h24 +5108% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.8) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MANIFEST](https://pump.fun/coin/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | `BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump` | $206.0k | $1.81M | 195.7 d | h24 -25% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 66,304 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.42M | $8.80M | 671.4 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,070 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.79M | $27.09M | 805.7 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders -0.0% in 2h (now 227,593) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $102.1k | $1.98M | +12% | -24% | +5108% | 18.4x | none flagged (still high risk) | 60 |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $78.6k | $1.22M | -2% | +72% | +3770% | 11.2x | none flagged (still high risk) | 59 |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $129.4k | $849.5k | -8% | +1113% | +1113% | 19.4x | spike (-8% 1h, +1113% 6h) | not scored |
| [JaoJiu](https://dexscreener.com/solana/2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy) | `2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy` | $34.7k | $223.0k | +47% | +632% | +632% | 25.6x | thin liq $34.7k; churn 26x vol/liq; spike (+47% 1h, +632% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $47.5k | $341.0k | +13% | -45% | +1145% | 87.6x | thin liq $47.5k; churn 88x vol/liq | not scored |
| [HELIORA](https://pump.fun/coin/96qfge1RkUWhSsv8i9V4QZFANGypKEe1u7pzCDGGpump) | `96qfge1RkUWhSsv8i9V4QZFANGypKEe1u7pzCDGGpump` | $17.3k | $61.1k | +124% | +124% | +124% | 30.9x | thin liq $17.3k; churn 31x vol/liq; spike (+124% 1h, +124% 6h); < 1h old | not scored |

_Timing: total 158s (discovery 71.7s, screen 1.2s, GT prime 0.5s, scoring 84.3s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/152; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
