# Last scan 2026-11-26T06:45:02Z - mode: helius (box heartbeat stale (162 min); budget 30/3000)

```
[fast_scan] 132 candidate mints from 9 source tags; 129 with pair data; 23 >= $50,000 liq; 10 pass survivor pre-gates (74s)
[fast_scan] scored Grodia in 72s
[fast_scan] scored pippin in 80s
[fast_scan] scored UHI in 81s
[fast_scan] scored VINE in 82s
[fast_scan] scored DOG in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored JIMMY in 83s
[fast_scan] scored BASKET in 91s
# Market scan 2026-11-26 06:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,421 (+2.2% 24h), ETH $1,685 (+1.7% 24h), SOL $70.72 (+3.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.3% (mcap $1.89B, vol $365.90M), pump-fun +3.8% (mcap $785.88M, vol $132.91M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $129.6k | $623.2k | 2.4 d | h24 -47% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 42* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $179.1k | $902.5k | 1.1 d | h24 +67% | #8 Turnover / bot pattern WARN (+4); #6 unknown (+3); #7 unknown (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6) | `FS7VE3wTpvbkB5j3t6vGYL8k3DnqnHrSdY4vJnkKFvG6` | $232.5k | $133.2k | 2.5 h | h24 +68% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.6k | $1.13M | 7.4 h | h24 +3074% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 62* | SKIP | [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $69.1k | $887.4k | 8.3 h | h24 +2415% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #16 Exit liquidity (Jupiter quotes) WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.25M | 672.3 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,113 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.45M | $18.59M | 746.4 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 2h (now 182,594) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.24M | $13.61M | 183.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 393,935 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $91.2k | $1.64M | +17% | +5092% | +5092% | 7.5x | spike (+17% 1h, +5092% 6h) | not scored |
| [wizardcat](https://pump.fun/coin/6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump) | `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump` | $23.4k | $111.5k | +297% | +1382% | +2002% | 9.7x | thin liq $23.4k; spike (+297% 1h, +1382% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $76.6k | $1.13M | -6% | +107% | +3074% | 9.9x | none flagged (still high risk) | 56 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $69.1k | $887.4k | +1% | -37% | +2415% | 29.4x | churn 29x vol/liq | 62 |
| [486](https://pump.fun/coin/9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump) | `9tVxVhKDmWLsG29CcfsAhLfgcZEkvemjB8TUDb4Wpump` | $11.6k | $26.3k | +78% | +429% | +410% | 1.0x | thin liq $11.6k; spike (+78% 1h, +429% 6h) | not scored |
| [Elonmas](https://pump.fun/coin/6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump) | `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump` | $28.1k | $149.2k | +24% | +422% | +422% | 28.0x | thin liq $28.1k; churn 28x vol/liq; spike (+24% 1h, +422% 6h) | not scored |

_Timing: total 167s (discovery 71.9s, screen 1.7s, GT prime 2.3s, scoring 91.0s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/163; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
