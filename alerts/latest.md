# Last scan 2026-11-19T17:26:42Z - mode: helius (box heartbeat stale (3080 min); budget 20/3000)

```
[fast_scan] 120 candidate mints from 10 source tags; 120 with pair data; 26 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored SHIT in 73s
[fast_scan] scored VINE in 80s
[fast_scan] scored ANT in 81s
[fast_scan] scored pippin in 82s
[fast_scan] scored Mandy in 82s
[fast_scan] scored Leonida in 82s
[fast_scan] scored AI in 83s
[fast_scan] scored GME in 84s
# Market scan 2026-11-19 17:26 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $62,391 (-0.8% 24h), ETH $1,757 (-0.3% 24h), SOL $73.08 (-0.4% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.2% (mcap $1.98B, vol $406.89M), pump-fun +0.4% (mcap $823.39M, vol $142.68M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [SHIT](https://pump.fun/coin/Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump) | `Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump` | $84.0k | $1.10M | 1.7 d | h24 -40% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 50* | CAUTION | [AI](https://dexscreener.com/solana/EE6CRsqqpvHwkCYK8hF15RmNccdq32vdbcQdX4afLoat) | `EE6CRsqqpvHwkCYK8hF15RmNccdq32vdbcQdX4afLoat` | $89.9k | $229.4k | 2.8 h | h24 +88% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 52* | SKIP | [Mandy](https://dexscreener.com/solana/2xCd5qHX5tW6pGUo7zfgHSSAnRjJwPA7Sz1Fu4fWcJjX) | `2xCd5qHX5tW6pGUo7zfgHSSAnRjJwPA7Sz1Fu4fWcJjX` | $59.2k | $290.0k | 1.2 d | h24 +535% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [Leonida](https://pump.fun/coin/9rbKkz2BDQBVgZmrHY6d7PTq2ge91gkpEyE4y9PPpump) | `9rbKkz2BDQBVgZmrHY6d7PTq2ge91gkpEyE4y9PPpump` | $124.8k | $2.57M | 1.7 d | h24 +30% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.9% (+6.2); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [ANT](https://dexscreener.com/solana/8J2VUcwne16c5LeYCSGBagPf32tDSFeGDzmD5B7nfmkY) | `8J2VUcwne16c5LeYCSGBagPf32tDSFeGDzmD5B7nfmkY` | $118.3k | $3.00M | 1.7 d | h24 +199% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 3.9% (+7.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [GME](https://dexscreener.com/solana/8wXtPeU6557ETkp9WHFY1n1EcU6NxDvbAggHGsMYiHsB) | `8wXtPeU6557ETkp9WHFY1n1EcU6NxDvbAggHGsMYiHsB` | $822.0k | $2.21M | 1026.7 d | h24 +9% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 197,161 (growth n/a: first sighting) |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.67M | $11.72M | 665.7 d | h24 +75% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 45h (now 344,446) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.43M | $18.00M | 739.9 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 9h (now 182,685) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [CATMARIO](https://pump.fun/coin/Cc5aMEFwovjGpETSqW64sXLW1NnUbVei8D4TagRcpump) | `Cc5aMEFwovjGpETSqW64sXLW1NnUbVei8D4TagRcpump` | $62.3k | $401.9k | +745% | +745% | +745% | 51.2x | churn 51x vol/liq; spike (+745% 1h, +745% 6h); < 1h old | not scored |
| [MANDY](https://pump.fun/coin/DNZpNGgc25ka2CLJq7dn46urgPCJDsAvH7XHNxFQpump) | `DNZpNGgc25ka2CLJq7dn46urgPCJDsAvH7XHNxFQpump` | $38.3k | $294.2k | +714% | +714% | +714% | 5.0x | thin liq $38.3k; spike (+714% 1h, +714% 6h); lopsided buys/sells 4.38; < 1h old | not scored |
| [GTE](https://pump.fun/coin/7nqA5P4iHvxTpt4WwSeyrdfToVcqxVARCPr96xSDpump) | `7nqA5P4iHvxTpt4WwSeyrdfToVcqxVARCPr96xSDpump` | $57.6k | $610.8k | +447% | +447% | +447% | 17.9x | spike (+447% 1h, +447% 6h); < 1h old | not scored |
| [PIPI](https://pump.fun/coin/6MKD1NkLvWRqdbFtqmgACBwUV5o6GJpZry8HkNgzpump) | `6MKD1NkLvWRqdbFtqmgACBwUV5o6GJpZry8HkNgzpump` | $64.9k | $410.6k | -34% | +868% | +868% | 76.0x | churn 76x vol/liq; spike (-34% 1h, +868% 6h) | not scored |
| [DCTY](https://pump.fun/coin/GD8GhsCv7GHaimi3N5wZU5ZGsZGY3LB6vLN7LgJYpump) | `GD8GhsCv7GHaimi3N5wZU5ZGsZGY3LB6vLN7LgJYpump` | $22.3k | $96.7k | -19% | +949% | +882% | 14.4x | thin liq $22.3k; spike (-19% 1h, +949% 6h) | not scored |
| [scat](https://pump.fun/coin/5EpUkeRekk1uzWKoJz9fyYYA3Vwt6bTtdRNpVtkMpump) | `5EpUkeRekk1uzWKoJz9fyYYA3Vwt6bTtdRNpVtkMpump` | $14.8k | $46.4k | -17% | +28% | +2663% | 8.2x | thin liq $14.8k | not scored |

_Timing: total 157s (discovery 71.1s, screen 1.1s, GT prime 0.4s, scoring 84.3s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/168; Helius 429s 91; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
