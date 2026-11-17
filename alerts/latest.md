# Last scan 2026-11-17T13:06:20Z - mode: helius (box heartbeat stale (538 min); budget 400/3000)

```
[fast_scan] 114 candidate mints from 9 source tags; 111 with pair data; 27 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 78s
[fast_scan] scored SPCX in 86s
[fast_scan] scored Millionaires in 87s
[fast_scan] scored ZEC in 87s
[fast_scan] scored VINE in 88s
[fast_scan] scored GTA in 89s
[fast_scan] scored HOGE in 89s
[fast_scan] scored bul in 91s
# Market scan 2026-11-17 13:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,983 (+1.3% 24h), ETH $1,822 (+1.2% 24h), SOL $73.60 (+4.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.7% (mcap $2.06B, vol $332.57M), pump-fun +2.1% (mcap $858.80M, vol $137.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $103.2k | $594.7k | 2.3 d | h24 +45% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $90.6k | $252.8k | 10.5 h | h24 +136% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [Millionaires](https://dexscreener.com/solana/12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb) | `12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb` | $118.8k | $70.0k | 1.6 h | h24 +118% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $91.5k | $570.6k | 15.7 h | h24 +1877% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.1k | $1.50M | 19.2 h | h24 +4632% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.38M | $7.91M | 663.5 d | h24 -21% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,395 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.55M | $23.5k | 397.8 d | h24 +10% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 392,499 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.47M | $12.91M | 174.2 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,501 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.1k | $1.50M | +19% | +46% | +4632% | 15.1x | none flagged (still high risk) | 59 |
| [GROKIA](https://dexscreener.com/solana/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm) | `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm` | $44.8k | $352.3k | -12% | +965% | +965% | 98.2x | thin liq $44.8k; churn 98x vol/liq; spike (-12% 1h, +965% 6h) | not scored |
| [SOYOUARE](https://pump.fun/coin/GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump) | `GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump` | $22.3k | $92.7k | +379% | +211% | +211% | 25.0x | thin liq $22.3k; spike (+379% 1h, +211% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $65.8k | $570.6k | -1% | +12% | +1877% | 80.0x | churn 80x vol/liq | 55 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $43.6k | $342.4k | -75% | -69% | +1003% | 40.7x | thin liq $43.6k; churn 41x vol/liq | not scored |
| [RYANAIR](https://dexscreener.com/solana/9WcYJegbsMSzvtFUEGmJoGhZjCGBEcKqXpdkNDoMR5pN) | `9WcYJegbsMSzvtFUEGmJoGhZjCGBEcKqXpdkNDoMR5pN` | $13.9k | $41.8k | +183% | +50% | +50% | 7.6x | thin liq $13.9k; spike (+183% 1h, +50% 6h) | not scored |

_Timing: total 164s (discovery 71.9s, screen 1.1s, GT prime 0.4s, scoring 90.7s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/163; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
