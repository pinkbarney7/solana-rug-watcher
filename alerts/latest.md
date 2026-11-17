# Last scan 2026-11-17T12:54:14Z - mode: helius (box heartbeat stale (525 min); budget 400/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 115 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored GTA in 72s
[fast_scan] scored Millionaires in 81s
[fast_scan] scored LEOSTAR in 81s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored bul in 83s
[fast_scan] scored HOGE in 85s
[fast_scan] scored SPCX in 72s
# Market scan 2026-11-17 12:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,870 (+1.1% 24h), ETH $1,819 (+1.2% 24h), SOL $73.60 (+4.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +3.0% (mcap $2.07B, vol $338.41M), pump-fun +2.0% (mcap $857.60M, vol $135.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $105.3k | $613.4k | 2.3 d | h24 +69% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $106.3k | $348.8k | 10.3 h | h24 +226% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Millionaires](https://dexscreener.com/solana/12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb) | `12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb` | $116.7k | $71.0k | 1.4 h | h24 +121% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $94.0k | $553.1k | 15.5 h | h24 +1817% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.4k | $1.51M | 18.9 h | h24 +4657% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $94.9k | $1.58M | 13.8 h | h24 +5003% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.37M | $7.85M | 663.5 d | h24 -23% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,395 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.54M | $23.4k | 397.8 d | h24 +11% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 392,499 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.48M | $12.89M | 174.2 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,501 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $94.9k | $1.58M | +23% | +52% | +5003% | 17.1x | none flagged (still high risk) | 59 |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.8k | $1.52M | +21% | +51% | +4702% | 14.8x | none flagged (still high risk) | 59 |
| [GROKIA](https://dexscreener.com/solana/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm) | `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm` | $45.3k | $361.2k | -10% | +992% | +992% | 96.1x | thin liq $45.3k; churn 96x vol/liq; spike (-10% 1h, +992% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $66.2k | $577.5k | -2% | +18% | +1901% | 79.3x | churn 79x vol/liq | 55 |
| [SOYOUARE](https://pump.fun/coin/GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump) | `GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump` | $23.3k | $101.0k | +239% | +239% | +239% | 21.6x | thin liq $23.3k; spike (+239% 1h, +239% 6h); < 1h old | not scored |
| [WANTED](https://pump.fun/coin/9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump) | `9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump` | $42.6k | $295.1k | -41% | +24% | +514% | 64.6x | thin liq $42.6k; churn 65x vol/liq | not scored |

_Timing: total 218s (discovery 72.1s, screen 1.1s, GT prime 0.2s, scoring 144.1s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/179; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
