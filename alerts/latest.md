# Last scan 2026-11-25T12:15:46Z - mode: helius (box heartbeat stale (502 min); budget 313/3000)

```
[fast_scan] 123 candidate mints from 10 source tags; 119 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 71s
[fast_scan] scored VINE in 79s
[fast_scan] scored BASKET in 80s
[fast_scan] scored MOODENG in 81s
[fast_scan] scored Jimmies in 81s
[fast_scan] scored pippin in 81s
[fast_scan] scored JIMMY in 81s
# Market scan 2026-11-25 12:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,490 (-2.9% 24h), ETH $1,639 (-3.4% 24h), SOL $67.60 (-4.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.3% (mcap $1.76B, vol $309.73M), pump-fun -3.3% (mcap $747.05M, vol $126.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $191.3k | $1.06M | 1.6 d | h24 +225% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [BASKET](https://dexscreener.com/solana/Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp) | `Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp` | $316.4k | $195.2k | 3.7 h | h24 +95% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $340.9k | $1.45M | 7.6 h | h24 +1974% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $85.1k | $1.43M | 13.0 h | h24 +4407% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $9.28M | 671.5 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,051 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.48M | $19.77M | 745.7 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,579 (growth n/a: first sighting) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.80M | $27.26M | 805.8 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,739 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $85.5k | $1.44M | +18% | -5% | +4450% | 11.5x | none flagged (still high risk) | 59 |
| [Pompom](https://pump.fun/coin/5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump) | `5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump` | $27.8k | $153.8k | +480% | +480% | +480% | 15.4x | thin liq $27.8k; spike (+480% 1h, +480% 6h); < 1h old | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $169.3k | $1.45M | -33% | +251% | +1974% | 22.1x | none flagged (still high risk) | 55 |
| [JaoJiu](https://dexscreener.com/solana/2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy) | `2UyrvgCRXiEwiKRVk96gs6B4myrBHZAfcLyMVLE8vSCy` | $28.8k | $150.6k | +21% | +394% | +394% | 42.3x | thin liq $28.8k; churn 42x vol/liq; spike (+21% 1h, +394% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $43.0k | $277.5k | +2% | -60% | +913% | 100.2x | thin liq $43.0k; churn 100x vol/liq | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $31.9k | $167.0k | -21% | -2% | +518% | 63.8x | thin liq $31.9k; churn 64x vol/liq | not scored |

_Timing: total 154s (discovery 71.4s, screen 1.4s, GT prime 0.3s, scoring 81.3s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/143; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
