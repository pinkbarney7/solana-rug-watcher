# Last scan 2026-11-25T04:21:19Z - mode: helius (box heartbeat stale (28 min); budget 524/3000)

```
[fast_scan] 125 candidate mints from 10 source tags; 120 with pair data; 21 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored GROKIA in 70s
[fast_scan] scored SPCX in 78s
[fast_scan] scored CLAUDIA in 79s
[fast_scan] scored pippin in 80s
[fast_scan] scored JIMMY in 80s
[fast_scan] scored MCAT in 82s
# Market scan 2026-11-25 04:21 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,302 (-1.8% 24h), ETH $1,662 (-2.1% 24h), SOL $69.24 (-3.4% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.8% (mcap $1.78B, vol $318.95M), pump-fun -5.2% (mcap $760.49M, vol $134.17M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $53.7k | $96.6k | 2.6 d | h24 -31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $269.1k | $1.61M | 1.3 d | h24 +355% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $133.4k | $3.09M | 1.1 d | h24 +51% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.3% (+6.8); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.40M | $18.50M | 745.3 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 182,573) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.10M | $74.03B | 49.1 d | h24 -13% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders +0.6% in 18h (now 61,725) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $12.96M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders -0.1% in 7h (now 390,089) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $80.8k | $1.03M | +61% | +8558% | +3650% | 31.3x | churn 31x vol/liq; spike (+61% 1h, +8558% 6h) | not scored |
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $63.1k | $768.2k | -65% | +1916% | +1916% | 22.6x | spike (-65% 1h, +1916% 6h) | not scored |
| [YUMA](https://pump.fun/coin/CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump) | `CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump` | $23.4k | $114.6k | +282% | +282% | +282% | 8.5x | thin liq $23.4k; spike (+282% 1h, +282% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $28.4k | $138.2k | -19% | +411% | +411% | 53.8x | thin liq $28.4k; churn 54x vol/liq; spike (-19% 1h, +411% 6h) | not scored |
| [Manlet](https://pump.fun/coin/6LuwyvmTMyJiQRZQPneZCfr2gehSSAvQbMWgXCjopump) | `6LuwyvmTMyJiQRZQPneZCfr2gehSSAvQbMWgXCjopump` | $43.3k | $231.5k | +46% | +357% | +357% | 1.0x | thin liq $43.3k; spike (+46% 1h, +357% 6h) | not scored |
| [Manlet](https://pump.fun/coin/HyXjbs37EKU1QPKm2MnSQ3YaxNCugdh2W8bktSfYpump) | `HyXjbs37EKU1QPKm2MnSQ3YaxNCugdh2W8bktSfYpump` | $17.3k | $62.9k | +120% | +120% | +120% | 14.4x | thin liq $17.3k; spike (+120% 1h, +120% 6h); < 1h old | not scored |

_Timing: total 155s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 81.7s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/132; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
