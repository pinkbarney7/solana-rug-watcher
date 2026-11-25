# Last scan 2026-11-25T14:55:44Z - mode: helius (box heartbeat stale (21 min); budget 363/3000)

```
[fast_scan] 123 candidate mints from 10 source tags; 117 with pair data; 24 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 78s
[fast_scan] scored 4CHAN in 87s
[fast_scan] scored BASKET in 87s
[fast_scan] scored JIMMY in 89s
[fast_scan] scored MOODENG in 90s
[fast_scan] scored pippin in 91s
[fast_scan] scored SPCX in 91s
[fast_scan] scored Jimmies in 91s
# Market scan 2026-11-25 14:55 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $57,480 (-4.8% 24h), ETH $1,616 (-4.6% 24h), SOL $66.34 (-5.0% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.1% (mcap $1.74B, vol $316.23M), pump-fun -4.7% (mcap $729.85M, vol $138.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $228.7k | $1.61M | 1.7 d | h24 +101% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [BASKET](https://dexscreener.com/solana/Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp) | `Gs7MYTzyrKFktBQyiXriRcyFC4gxsR8C7W9E64Fatyp` | $309.8k | $189.7k | 6.4 h | h24 +90% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $250.8k | $1.09M | 10.3 h | h24 +1453% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $70.7k | $385.3k | 17.0 h | h24 +1307% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $73.4k | $1.08M | 15.6 h | h24 +3323% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.34M | $18.54M | 745.8 d | h24 -0% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 182,579) |
| 59* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.75M | $26.31M | 805.9 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders -0.0% in 2h (now 227,712) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.39M | $12.95M | 182.3 d | h24 -11% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders +0.0% in 8h (now 390,277) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $73.6k | $1.09M | -24% | -8% | +3341% | 13.9x | none flagged (still high risk) | 59 |
| [Pompom](https://pump.fun/coin/5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump) | `5EmvWDizkpjAXbcfCcVq69w1id8GaLzi4LLwtuSgpump` | $38.7k | $260.2k | +16% | +882% | +882% | 45.7x | thin liq $38.7k; churn 46x vol/liq; spike (+16% 1h, +882% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $145.4k | $1.09M | -33% | +24% | +1457% | 29.2x | churn 29x vol/liq | 55 |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $50.1k | $369.3k | +13% | +11% | +1248% | 91.1x | churn 91x vol/liq | 56 |
| [MONEYGO](https://pump.fun/coin/5Go8ByHzd9vvdBHhqFnxxgU2SRDfTv5XXMLjBnvrpump) | `5Go8ByHzd9vvdBHhqFnxxgU2SRDfTv5XXMLjBnvrpump` | $21.2k | $104.2k | +149% | +149% | +149% | 10.5x | thin liq $21.2k; spike (+149% 1h, +149% 6h); lopsided buys/sells 6.71; < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $36.1k | $214.0k | +16% | +40% | +691% | 59.0x | thin liq $36.1k; churn 59x vol/liq | not scored |

_Timing: total 164s (discovery 71.2s, screen 1.4s, GT prime 0.3s, scoring 90.8s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 11/159; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
