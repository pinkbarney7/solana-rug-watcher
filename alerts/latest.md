# Last scan 2026-11-25T05:02:51Z - mode: helius (box heartbeat stale (69 min); budget 0/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 118 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored CLAUDIA in 76s
[fast_scan] scored pippin in 85s
[fast_scan] scored SPCX in 85s
[fast_scan] scored MCAT in 87s
[fast_scan] scored JIMMY in 87s
# Market scan 2026-11-25 05:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,143 (-1.9% 24h), ETH $1,658 (-2.3% 24h), SOL $68.77 (-3.7% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.2% (mcap $1.79B, vol $322.19M), pump-fun -5.8% (mcap $760.56M, vol $136.75M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $58.2k | $114.2k | 2.7 d | h24 -13% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $249.6k | $1.67M | 1.3 d | h24 +379% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.39M | $18.54M | 745.4 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,580 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.10M | $74.03B | 49.1 d | h24 -12% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 61,695 (growth n/a: first sighting) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $13.01M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 390,082 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $78.6k | $1.22M | +38% | +3764% | +3764% | 8.4x | spike (+38% 1h, +3764% 6h) | not scored |
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $79.9k | $1.23M | +124% | +3115% | +3115% | 18.7x | spike (+124% 1h, +3115% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $76.6k | $903.4k | -5% | +2827% | +3198% | 42.1x | churn 42x vol/liq; spike (-5% 1h, +2827% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $93.4k | $391.5k | +459% | +459% | +459% | 4.8x | spike (+459% 1h, +459% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $26.6k | $121.6k | -6% | +350% | +350% | 61.2x | thin liq $26.6k; churn 61x vol/liq; spike (-6% 1h, +350% 6h) | not scored |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $30.9k | $148.3k | -17% | +30% | +446% | 77.5x | thin liq $30.9k; churn 77x vol/liq | not scored |

_Timing: total 161s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 87.3s for 5 coins, 5 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 5/116; Helius 429s 65; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
