# Last scan 2026-11-24T13:05:39Z - mode: helius (box heartbeat stale (538 min); budget 514/3000)

```
[fast_scan] 108 candidate mints from 9 source tags; 105 with pair data; 31 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 80s
[fast_scan] scored GROKIA in 87s
[fast_scan] scored pippin in 87s
[fast_scan] scored DONJENSEN in 88s
[fast_scan] scored ACHI in 88s
[fast_scan] scored ZEC in 88s
[fast_scan] scored JIMMY in 89s
[fast_scan] scored Bullseye in 89s
[fast_scan] scored SPCX in 72s
# Market scan 2026-11-24 13:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,368 (-1.5% 24h), ETH $1,701 (-1.2% 24h), SOL $70.59 (-2.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.3% (mcap $1.83B, vol $377.97M), pump-fun -4.1% (mcap $775.06M, vol $133.95M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $74.6k | $177.0k | 2.0 d | h24 -50% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [Bullseye](https://dexscreener.com/solana/DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe) | `DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe` | $189.3k | $129.7k | 1.5 h | h24 +159% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $84.1k | $408.1k | 16.0 h | h24 +1333% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $157.7k | $145.1k | 7.7 h | h24 +226% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 66* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $110.0k | $2.29M | 10.5 h | h24 +6335% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.8% (+6.2) |
| 67* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $156.4k | $4.29M | 10.8 h | h24 +3815% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 3.6% (+7.6) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.35M | $17.58M | 744.7 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,546 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.09M | $13.15M | 181.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 386,485 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.19M | $18.1k | 404.8 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 8h (now 395,219) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $110.0k | $2.29M | +4% | +16% | +6335% | 12.7x | liq/mcap 4.8% | 66 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $156.4k | $4.29M | +23% | +32% | +3815% | 15.3x | liq/mcap 3.6% | 67 |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $42.5k | $297.3k | -17% | +994% | +994% | 35.5x | thin liq $42.5k; churn 35x vol/liq; spike (-17% 1h, +994% 6h) | not scored |
| [Unemployed](https://pump.fun/coin/FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump) | `FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump` | $24.3k | $118.0k | +322% | +322% | +322% | 15.5x | thin liq $24.3k; spike (+322% 1h, +322% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $52.0k | $409.5k | +21% | +29% | +1337% | 48.2x | churn 48x vol/liq | 55 |
| [cateball](https://pump.fun/coin/4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump) | `4npJ3avxnGhCzKbWQpLrQXAHsjWzKr4JqBsbu5Fspump` | $73.8k | $963.3k | +231% | +115% | -6% | 7.2x | spike (+231% 1h, +115% 6h) | not scored |

_Timing: total 225s (discovery 72.0s, screen 1.1s, GT prime 0.5s, scoring 151.7s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/174; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
