# Last scan 2026-11-25T11:40:16Z - mode: helius (box heartbeat stale (466 min); budget 283/3000)

```
[fast_scan] 126 candidate mints from 10 source tags; 122 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Jimmies in 71s
[fast_scan] scored BASKET in 79s
[fast_scan] scored pippin in 80s
[fast_scan] scored MOODENG in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored MCAT in 83s
# Market scan 2026-11-25 11:40 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,529 (-2.2% 24h), ETH $1,638 (-3.0% 24h), SOL $67.51 (-3.9% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.3% (mcap $1.77B, vol $324.04M), pump-fun -2.1% (mcap $752.95M, vol $141.38M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $50.5k | $89.1k | 2.9 d | h24 -50% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $199.6k | $1.11M | 1.6 d | h24 +202% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [BASKET](https://dexscreener.com/solana/Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp) | `Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp` | $316.3k | $195.1k | 3.1 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $78.9k | $1.23M | 12.4 h | h24 +3797% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.43M | $8.94M | 671.5 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,051 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.48M | $19.85M | 745.6 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,582 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.80M | $27.53M | 805.8 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,727 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $78.8k | $1.23M | -6% | +10% | +3797% | 11.5x | none flagged (still high risk) | 59 |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $191.4k | $1.86M | -33% | +366% | +2556% | 18.9x | spike (-33% 1h, +366% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $45.1k | $304.8k | -5% | -58% | +1013% | 95.2x | thin liq $45.1k; churn 95x vol/liq | not scored |
| [JaoJiu](https://dexscreener.com/solana/2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy) | `2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy` | $27.4k | $137.9k | -10% | +353% | +353% | 43.3x | thin liq $27.4k; churn 43x vol/liq; spike (-10% 1h, +353% 6h) | not scored |
| [Pompom](https://pump.fun/coin/5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump) | `5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump` | $16.9k | $63.2k | +133% | +133% | +133% | 8.9x | thin liq $16.9k; spike (+133% 1h, +133% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $33.6k | $185.7k | +16% | +39% | +587% | 60.0x | thin liq $33.6k; churn 60x vol/liq | not scored |

_Timing: total 156s (discovery 71.1s, screen 1.4s, GT prime 0.2s, scoring 83.4s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/148; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
