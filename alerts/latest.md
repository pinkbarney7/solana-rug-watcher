# Last scan 2026-11-21T09:20:18Z - mode: helius (box heartbeat stale (5474 min); budget 0/3000)

```
[fast_scan] 122 candidate mints from 10 source tags; 119 with pair data; 32 >= $50,000 liq; 14 pass survivor pre-gates (73s)
[fast_scan] scored CoT in 71s
[fast_scan] scored win in 78s
[fast_scan] scored JENSEN in 79s
[fast_scan] scored ZEC in 79s
[fast_scan] scored SPCX in 79s
[fast_scan] scored VINE in 80s
# Market scan 2026-11-21 09:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $57,814 (-6.3% 24h), ETH $1,634 (-6.5% 24h), SOL $67.68 (-6.3% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -7.9% (mcap $1.77B, vol $462.02M), pump-fun -6.4% (mcap $746.42M, vol $139.95M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | CAUTION | [CoT](https://dexscreener.com/solana/5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW) | `5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW` | $59.1k | $838.1k | 11.7 h | h24 +29% | #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 53* | SKIP | [win](https://dexscreener.com/solana/5rDMySC3buoNTY6gE6sWzpFzvHfBpP5LGAVpjGCMaijV) | `5rDMySC3buoNTY6gE6sWzpFzvHfBpP5LGAVpjGCMaijV` | $216.0k | $125.1k | 2.4 h | h24 +65% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [JENSEN](https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump) | `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump` | $75.9k | $1.09M | 9.3 h | h24 +1050% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.30M | $6.93M | 667.4 d | h24 -22% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 7h (now 345,182) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.04M | 178.1 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.9% in 79h (now 383,015) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $5.97M | $18.3k | 401.7 d | h24 -13% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 7h (now 393,982) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUNANI](https://pump.fun/coin/2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump) | `2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump` | $120.8k | $2.90M | +4% | +8812% | +8812% | 9.6x | liq/mcap 4.2%; spike (+4% 1h, +8812% 6h) | not scored |
| [MAYA](https://pump.fun/coin/FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump) | `FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump` | $122.4k | $3.01M | -0% | +8214% | +8214% | 8.7x | liq/mcap 4.1%; spike (-0% 1h, +8214% 6h) | not scored |
| [PDOG](https://pump.fun/coin/Bmy2XNoysbCCqzqX3CC7DFbHW6FhGJ36MzWD1Wgdpump) | `Bmy2XNoysbCCqzqX3CC7DFbHW6FhGJ36MzWD1Wgdpump` | $18.6k | $69.2k | +36% | +4686% | +4686% | 16.1x | thin liq $18.6k; spike (+36% 1h, +4686% 6h) | not scored |
| [SI](https://pump.fun/coin/2GiS8L6jzveE7cQ61bjGN6wVn5MS9FcBjarSAMFppump) | `2GiS8L6jzveE7cQ61bjGN6wVn5MS9FcBjarSAMFppump` | $36.7k | $284.2k | -27% | +914% | +914% | 10.1x | thin liq $36.7k; spike (-27% 1h, +914% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump) | `DkHsZ1kjd2Fua8sgKE6PhHhyCdXYscbDVN7mAfiGpump` | $75.7k | $1.09M | +5% | -39% | +1050% | 27.0x | churn 27x vol/liq | 59 |
| [LRS](https://pump.fun/coin/7i8AXjBdKGjGpRo4Ex5aDKUaX55xed5Hrgoww1G9pump) | `7i8AXjBdKGjGpRo4Ex5aDKUaX55xed5Hrgoww1G9pump` | $30.9k | $212.1k | +0% | -4% | +633% | 1.0x | thin liq $30.9k | not scored |

_Timing: total 153s (discovery 71.5s, screen 1.5s, GT prime 0.4s, scoring 79.7s for 6 coins, 6 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/127; Helius 429s 75; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
