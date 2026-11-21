# Last scan 2026-11-21T02:01:18Z - mode: helius (box heartbeat stale (5035 min); budget 30/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 112 with pair data; 21 >= $50,000 liq; 12 pass survivor pre-gates (72s)
[fast_scan] scored FIONA in 70s
[fast_scan] scored VINE in 77s
[fast_scan] scored ZEC in 77s
[fast_scan] scored pippin in 78s
[fast_scan] scored CoT in 79s
# Market scan 2026-11-21 02:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,897 (-4.3% 24h), ETH $1,621 (-6.7% 24h), SOL $68.63 (-4.7% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.2% (mcap $1.83B, vol $415.36M), pump-fun -2.3% (mcap $780.97M, vol $143.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 43* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $159.0k | $1.01M | 3.3 d | h24 -41% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 51* | CAUTION | [CoT](https://dexscreener.com/solana/5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW) | `5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW` | $59.3k | $829.5k | 4.4 h | h24 +28% | #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.36M | $7.59M | 667.1 d | h24 -11% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 5h (now 345,188) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.36M | $18.35M | 741.2 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 5h (now 182,909) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.46M | $18.5k | 401.4 d | h24 -14% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.4% in 13h (now 393,733) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JENSEN](https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump) | `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump` | $93.3k | $1.66M | -14% | +1648% | +1648% | 16.6x | spike (-14% 1h, +1648% 6h) | not scored |
| [BTC](https://pump.fun/coin/CUfphqswgDK3VP3FX7CiShVCTdGQneFusYRFViABpump) | `CUfphqswgDK3VP3FX7CiShVCTdGQneFusYRFViABpump` | $41.8k | $359.4k | -53% | +962% | +962% | 22.8x | thin liq $41.8k; spike (-53% 1h, +962% 6h) | not scored |
| [LRS](https://pump.fun/coin/7i8AXjBdKGjGpRo4Ex5aDKUaX55xed5Hrgoww1G9pump) | `7i8AXjBdKGjGpRo4Ex5aDKUaX55xed5Hrgoww1G9pump` | $32.6k | $229.2k | -0% | +692% | +692% | 0.9x | thin liq $32.6k; spike (-0% 1h, +692% 6h) | not scored |
| [SBS](https://dexscreener.com/solana/4mE8dPH1RTqQBT5EPim5Ubt2v2wXZ9zgEDDWmL1o1EYu) | `4mE8dPH1RTqQBT5EPim5Ubt2v2wXZ9zgEDDWmL1o1EYu` | $33.3k | $194.1k | +102% | +535% | +535% | 14.0x | thin liq $33.3k; spike (+102% 1h, +535% 6h) | not scored |
| [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $28.4k | $141.6k | -7% | +414% | +414% | 44.9x | thin liq $28.4k; churn 45x vol/liq; spike (-7% 1h, +414% 6h) | not scored |
| [RACIST](https://dexscreener.com/solana/5MTN8FBaLHHxp4tPVFVJLsURFMYYbDhT2eWgv4wuypW7) | `5MTN8FBaLHHxp4tPVFVJLsURFMYYbDhT2eWgv4wuypW7` | $23.2k | $19.8k | +191% | +191% | +191% | 1.0x | thin liq $23.2k; spike (+191% 1h, +191% 6h); < 1h old | not scored |

_Timing: total 152s (discovery 71.2s, screen 1.1s, GT prime 0.4s, scoring 79.4s for 5 coins, 5 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 5/115; Helius 429s 60; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
