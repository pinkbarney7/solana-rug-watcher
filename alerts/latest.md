# Last scan 2026-11-25T04:24:25Z - mode: helius (box heartbeat stale (31 min); budget 524/3000)

```
[fast_scan] 125 candidate mints from 10 source tags; 120 with pair data; 21 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored pippin in 77s
[fast_scan] scored CLAUDIA in 77s
[fast_scan] scored MCAT in 79s
[fast_scan] scored SPCX in 86s
[fast_scan] scored GROKIA in 87s
[fast_scan] scored JIMMY in 87s
# Market scan 2026-11-25 04:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,282 (-1.8% 24h), ETH $1,663 (-2.0% 24h), SOL $69.28 (-3.4% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.5% (mcap $1.79B, vol $320.78M), pump-fun -5.1% (mcap $761.57M, vol $137.44M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $53.7k | $96.6k | 2.6 d | h24 -31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $269.1k | $1.61M | 1.3 d | h24 +355% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $130.3k | $2.95M | 1.1 d | h24 +34% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.4% (+6.7); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $18.50M | 745.3 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,573 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.10M | $74.03B | 49.1 d | h24 -13% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 61,725 (growth n/a: first sighting) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $12.87M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 390,089 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $86.1k | $1.16M | +86% | +5226% | +4126% | 29.8x | churn 30x vol/liq; spike (+86% 1h, +5226% 6h) | not scored |
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $66.9k | $859.9k | -59% | +2157% | +2157% | 21.4x | spike (-59% 1h, +2157% 6h) | not scored |
| [YUMA](https://pump.fun/coin/CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump) | `CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump` | $20.9k | $92.2k | +191% | +207% | +207% | 10.2x | thin liq $20.9k; spike (+191% 1h, +207% 6h) | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $25.3k | $108.8k | -44% | +302% | +302% | 61.4x | thin liq $25.3k; churn 61x vol/liq; spike (-44% 1h, +302% 6h) | not scored |
| [Manlet](https://pump.fun/coin/HyXjbs37EKU1QPKm2MnSQ3YaxNCugdh2W8bktSfYpump) | `HyXjbs37EKU1QPKm2MnSQ3YaxNCugdh2W8bktSfYpump` | $19.3k | $75.1k | +163% | +163% | +163% | 14.2x | thin liq $19.3k; spike (+163% 1h, +163% 6h); < 1h old | not scored |
| [1](https://pump.fun/coin/BWPv5jje9xipZ6V4q855fjiu5e7HiWGNvS5x8c1Mpump) | `BWPv5jje9xipZ6V4q855fjiu5e7HiWGNvS5x8c1Mpump` | $25.4k | $67.5k | +79% | +243% | +243% | 0.8x | thin liq $25.4k | not scored |

_Timing: total 160s (discovery 71.4s, screen 1.5s, GT prime 0.3s, scoring 87.2s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 30/132; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
