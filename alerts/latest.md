# Last scan 2026-11-25T05:16:17Z - mode: helius (box heartbeat stale (82 min); budget 10/3000)

```
[fast_scan] 128 candidate mints from 10 source tags; 122 with pair data; 23 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 71s
[fast_scan] scored INJ in 78s
[fast_scan] scored KOOP in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored MCAT in 80s
[fast_scan] scored pippin in 103s
# Market scan 2026-11-25 05:16 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,138 (-2.3% 24h), ETH $1,658 (-2.6% 24h), SOL $68.72 (-4.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.9% (mcap $1.79B, vol $320.41M), pump-fun -5.5% (mcap $762.97M, vol $134.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $57.9k | $112.7k | 2.7 d | h24 -13% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $248.2k | $1.48M | 1.3 d | h24 +266% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $190.0k | $105.1k | 1.0 h | h24 +37% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $18.62M | 745.4 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,577 (growth n/a: first sighting) |
| 56* | SKIP | [INJ](https://dexscreener.com/solana/DRAXGSc7yv1QPAwze4qbF1HVhdwQ9sxt8cSA13ANjnZv) | `DRAXGSc7yv1QPAwze4qbF1HVhdwQ9sxt8cSA13ANjnZv` | $187.16M | $187.54M | 39.6 d | h24 +0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link, exit test; holders 64 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $13.06M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,082 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $87.2k | $1.45M | +125% | +3711% | +3711% | 17.4x | spike (+125% 1h, +3711% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $79.0k | $1.23M | +28% | +3793% | +3793% | 8.5x | spike (+28% 1h, +3793% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $75.2k | $870.8k | -13% | +1430% | +3079% | 44.8x | churn 45x vol/liq; spike (-13% 1h, +1430% 6h) | not scored |
| [FUCKCANCER](https://pump.fun/coin/4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump) | `4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump` | $24.8k | $135.4k | +385% | +385% | +385% | 5.6x | thin liq $24.8k; spike (+385% 1h, +385% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $28.9k | $142.1k | -8% | +425% | +425% | 57.1x | thin liq $28.9k; churn 57x vol/liq; spike (-8% 1h, +425% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $70.4k | $191.9k | +174% | +174% | +174% | 10.9x | spike (+174% 1h, +174% 6h); < 1h old | not scored |

_Timing: total 177s (discovery 71.6s, screen 1.6s, GT prime 0.5s, scoring 102.9s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/132; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
