# Last scan 2026-11-25T13:21:00Z - mode: helius (box heartbeat stale (567 min); budget 343/3000)

```
[fast_scan] 125 candidate mints from 10 source tags; 120 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 78s
[fast_scan] scored MOODENG in 87s
[fast_scan] scored VINE in 87s
[fast_scan] scored JIMMY in 88s
[fast_scan] scored Jimmies in 88s
[fast_scan] scored BASKET in 89s
[fast_scan] scored pippin in 89s
[fast_scan] scored MCAT in 90s
# Market scan 2026-11-25 13:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,700 (-2.0% 24h), ETH $1,646 (-2.3% 24h), SOL $67.76 (-3.0% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.9% (mcap $1.75B, vol $317.04M), pump-fun -3.1% (mcap $746.01M, vol $140.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $50.3k | $87.5k | 3.0 d | h24 -47% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $232.0k | $1.59M | 1.7 d | h24 +316% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [BASKET](https://dexscreener.com/solana/Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp) | `Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp` | $317.1k | $195.6k | 4.8 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $276.4k | $1.32M | 8.7 h | h24 +1784% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $86.3k | $1.46M | 14.1 h | h24 +4509% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $9.24M | 671.5 d | h24 +12% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,043 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.46M | $19.54M | 745.7 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,581 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.78M | $26.58M | 805.8 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,731 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $86.3k | $1.46M | -6% | +46% | +4518% | 11.6x | none flagged (still high risk) | 59 |
| [Pompom](https://pump.fun/coin/5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump) | `5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump` | $44.6k | $336.6k | +81% | +1170% | +1170% | 29.5x | thin liq $44.6k; churn 30x vol/liq; spike (+81% 1h, +1170% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $161.6k | $1.32M | -15% | +145% | +1784% | 24.6x | none flagged (still high risk) | 55 |
| [JaoJiu](https://dexscreener.com/solana/2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy) | `2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy` | $28.8k | $146.7k | +36% | +290% | +381% | 47.2x | thin liq $28.8k; churn 47x vol/liq | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $42.8k | $271.1k | -3% | -30% | +890% | 102.6x | thin liq $42.8k; churn 103x vol/liq | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $30.2k | $149.2k | -20% | -36% | +452% | 68.5x | thin liq $30.2k; churn 68x vol/liq | not scored |

_Timing: total 164s (discovery 71.4s, screen 1.5s, GT prime 0.3s, scoring 90.3s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/164; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
