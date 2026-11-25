# Last scan 2026-11-25T13:23:57Z - mode: helius (box heartbeat stale (570 min); budget 343/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 118 with pair data; 25 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 71s
[fast_scan] scored pippin in 79s
[fast_scan] scored BASKET in 79s
[fast_scan] scored VINE in 79s
[fast_scan] scored MOODENG in 80s
[fast_scan] scored Jimmies in 80s
[fast_scan] scored JIMMY in 80s
# Market scan 2026-11-25 13:23 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,609 (-2.4% 24h), ETH $1,645 (-2.6% 24h), SOL $67.65 (-3.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.9% (mcap $1.75B, vol $317.04M), pump-fun -3.1% (mcap $746.01M, vol $140.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $231.3k | $1.59M | 1.7 d | h24 +312% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [BASKET](https://dexscreener.com/solana/Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp) | `Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp` | $317.1k | $195.6k | 4.8 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $268.5k | $1.23M | 8.7 h | h24 +1650% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $86.3k | $1.47M | 14.1 h | h24 +4532% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.45M | $9.21M | 671.5 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,043 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.46M | $19.54M | 745.7 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,581 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.78M | $26.71M | 805.8 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,731 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $86.3k | $1.47M | -3% | +41% | +4534% | 11.6x | none flagged (still high risk) | 59 |
| [Pompom](https://pump.fun/coin/5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump) | `5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump` | $43.8k | $320.8k | +60% | +1111% | +1111% | 31.0x | thin liq $43.8k; churn 31x vol/liq; spike (+60% 1h, +1111% 6h) | not scored |
| [SLITHEEN](https://pump.fun/coin/2ajAnFA8UKpeYbWSoEwobGQrLvdUUmjipjpongMepump) | `2ajAnFA8UKpeYbWSoEwobGQrLvdUUmjipjpongMepump` | $11.1k | $29.4k | +300% | +1145% | -0% | 18.7x | thin liq $11.1k; spike (+300% 1h, +1145% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $155.5k | $1.23M | -24% | +89% | +1650% | 25.6x | churn 26x vol/liq | 55 |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $45.4k | $304.0k | +8% | -18% | +1010% | 97.0x | thin liq $45.4k; churn 97x vol/liq | not scored |
| [JaoJiu](https://dexscreener.com/solana/2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy) | `2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy` | $27.6k | $135.4k | +25% | +122% | +344% | 49.4x | thin liq $27.6k; churn 49x vol/liq | not scored |

_Timing: total 154s (discovery 71.7s, screen 1.4s, GT prime 0.4s, scoring 80.1s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 22/143; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
