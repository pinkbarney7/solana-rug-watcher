# Last scan 2026-11-25T06:37:34Z - mode: helius (box heartbeat stale (164 min); budget 40/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 118 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored 4CHAN in 72s
[fast_scan] scored CHUCK in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored KOOP in 82s
[fast_scan] scored pippin in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored JIMMY in 83s
[fast_scan] scored MCAT in 85s
# Market scan 2026-11-25 06:37 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,005 (-2.3% 24h), ETH $1,655 (-2.6% 24h), SOL $68.62 (-4.3% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.2% (mcap $1.80B, vol $310.82M), pump-fun -6.3% (mcap $760.97M, vol $138.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $54.1k | $98.5k | 2.7 d | h24 -36% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $228.4k | $1.27M | 1.4 d | h24 +291% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $222.5k | $127.9k | 2.4 h | h24 +67% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $151.1k | $580.3k | 8.7 h | h24 +2019% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $145.0k | $159.1k | 1.8 h | h24 +222% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.47M | $9.30M | 671.3 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,014 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.41M | $18.78M | 745.4 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,578 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.17M | $12.92M | 181.9 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,217 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $84.7k | $1.41M | +29% | +502% | +4357% | 9.2x | spike (+29% 1h, +502% 6h) | not scored |
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $88.4k | $1.49M | +36% | +340% | +3808% | 18.6x | spike (+36% 1h, +340% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $119.1k | $705.3k | +110% | +907% | +907% | 12.2x | spike (+110% 1h, +907% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $61.6k | $580.3k | -18% | +90% | +2019% | 60.3x | churn 60x vol/liq | 56 |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $33.3k | $185.1k | +31% | +584% | +584% | 51.9x | thin liq $33.3k; churn 52x vol/liq; spike (+31% 1h, +584% 6h) | not scored |
| [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $145.7k | $160.3k | +68% | +224% | +224% | 96.7x | churn 97x vol/liq | 56 |

_Timing: total 158s (discovery 71.9s, screen 1.3s, GT prime 0.4s, scoring 84.6s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/164; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
