# Last scan 2026-11-17T10:19:36Z - mode: helius (box heartbeat stale (370 min); budget 260/3000)

```
[fast_scan] 121 candidate mints from 9 source tags; 118 with pair data; 29 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored bul in 73s
[fast_scan] scored ZEC in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored HOGE in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored LEOSTAR in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored GTA in 83s
[fast_scan] scored VINE in 71s
# Market scan 2026-11-17 10:19 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,256 (-0.2% 24h), ETH $1,795 (-0.2% 24h), SOL $72.34 (+1.9% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.7% (mcap $2.04B, vol $313.02M), pump-fun +0.9% (mcap $851.37M, vol $131.63M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $101.6k | $573.5k | 2.2 d | h24 +62% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $65.8k | $139.1k | 7.7 h | h24 +30% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $102.3k | $519.9k | 12.9 h | h24 +1701% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $80.4k | $1.13M | 14.2 h | h24 +1231% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $81.6k | $1.21M | 16.4 h | h24 +3726% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $80.8k | $1.19M | 11.3 h | h24 +3734% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.39M | $8.24M | 663.4 d | h24 -22% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,432 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.19M | $22.9k | 397.7 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,848 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.55M | $12.57M | 174.1 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,635 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $80.8k | $1.19M | +18% | -1% | +3734% | 16.1x | none flagged (still high risk) | 59 |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $81.4k | $1.21M | -6% | +10% | +3708% | 14.6x | none flagged (still high risk) | 59 |
| [GCAT](https://dexscreener.com/solana/BPBKGG9G2A44JnB3RMfH6yVfDG5vpUVzkTtY4rjwVjes) | `BPBKGG9G2A44JnB3RMfH6yVfDG5vpUVzkTtY4rjwVjes` | $60.1k | $52.7k | +46% | +666% | +666% | 130.6x | churn 131x vol/liq; spike (+46% 1h, +666% 6h) | not scored |
| [GTAVI](https://pump.fun/coin/D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump) | `D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump` | $35.0k | $248.4k | -15% | +745% | +745% | 4.1x | thin liq $35.0k; spike (-15% 1h, +745% 6h) | not scored |
| [WANTED](https://pump.fun/coin/9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump) | `9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump` | $60.6k | $604.9k | +21% | +408% | +1159% | 42.2x | churn 42x vol/liq; spike (+21% 1h, +408% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $61.9k | $519.9k | -14% | +4% | +1701% | 82.8x | churn 83x vol/liq | 55 |

_Timing: total 218s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 144.9s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/180; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
