# Last scan 2026-11-25T05:24:18Z - mode: helius (box heartbeat stale (91 min); budget 20/3000)

```
[fast_scan] 129 candidate mints from 10 source tags; 123 with pair data; 24 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 78s
[fast_scan] scored pippin in 85s
[fast_scan] scored SPCX in 86s
[fast_scan] scored KOOP in 86s
[fast_scan] scored JIMMY in 86s
[fast_scan] scored MOODENG in 86s
# Market scan 2026-11-25 05:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,169 (-2.3% 24h), ETH $1,659 (-2.7% 24h), SOL $68.68 (-4.3% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.9% (mcap $1.79B, vol $320.41M), pump-fun -5.5% (mcap $762.97M, vol $134.89M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $57.7k | $112.2k | 2.7 d | h24 -13% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $254.7k | $1.66M | 1.3 d | h24 +346% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $194.2k | $107.4k | 1.2 h | h24 +40% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $18.65M | 745.4 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,577 (growth n/a: first sighting) |
| 56* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.77M | $26.32M | 805.5 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 227,488 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $12.96M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,170 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $75.7k | $1.10M | +33% | +2785% | +2785% | 20.3x | spike (+33% 1h, +2785% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $77.9k | $1.20M | +32% | +805% | +3686% | 8.6x | spike (+32% 1h, +805% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $74.6k | $848.7k | -30% | +700% | +2998% | 45.9x | churn 46x vol/liq; spike (-30% 1h, +700% 6h) | not scored |
| [FUCKCANCER](https://pump.fun/coin/4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump) | `4UMErmfmKzDCVmHrwBUbnDnbQnVKVYAcT7X5AdTkpump` | $21.4k | $96.7k | +246% | +246% | +246% | 9.6x | thin liq $21.4k; spike (+246% 1h, +246% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $28.2k | $135.3k | +28% | +400% | +400% | 58.8x | thin liq $28.2k; churn 59x vol/liq; spike (+28% 1h, +400% 6h) | not scored |
| [TIKTOK](https://dexscreener.com/solana/BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57) | `BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57` | $115.6k | $135.4k | +171% | +171% | +171% | 64.4x | churn 64x vol/liq; spike (+171% 1h, +171% 6h); < 1h old | not scored |

_Timing: total 160s (discovery 71.4s, screen 1.4s, GT prime 0.5s, scoring 86.5s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/132; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
