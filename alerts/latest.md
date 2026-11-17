# Last scan 2026-11-17T12:39:58Z - mode: helius (box heartbeat stale (510 min); budget 370/3000)

```
[fast_scan] 120 candidate mints from 9 source tags; 117 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored GTA in 72s
[fast_scan] scored ZEC in 81s
[fast_scan] scored LEOSTAR in 81s
[fast_scan] scored bul in 82s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored Millionaires in 83s
[fast_scan] scored VINE in 83s
[fast_scan] scored HOGE in 84s
[fast_scan] scored SPCX in 72s
# Market scan 2026-11-17 12:39 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,838 (+1.2% 24h), ETH $1,814 (+1.1% 24h), SOL $73.35 (+3.7% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.3% (mcap $2.06B, vol $342.17M), pump-fun +0.6% (mcap $857.78M, vol $140.65M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $103.5k | $589.4k | 2.3 d | h24 +62% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $103.1k | $336.2k | 10.1 h | h24 +214% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Millionaires](https://dexscreener.com/solana/12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb) | `12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb` | $115.4k | $74.3k | 1.2 h | h24 +131% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $90.7k | $515.6k | 15.2 h | h24 +1687% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.5k | $1.52M | 18.7 h | h24 +4700% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $86.4k | $1.33M | 13.6 h | h24 +4177% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.38M | $7.94M | 663.5 d | h24 -23% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,406 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.53M | $23.4k | 397.8 d | h24 +9% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,914 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.44M | $12.91M | 174.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,501 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $92.5k | $1.52M | +20% | +46% | +4700% | 14.7x | none flagged (still high risk) | 59 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $86.4k | $1.33M | -1% | +33% | +4177% | 17.3x | none flagged (still high risk) | 59 |
| [GROKIA](https://dexscreener.com/solana/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm) | `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm` | $40.4k | $291.6k | -20% | +782% | +782% | 104.8x | thin liq $40.4k; churn 105x vol/liq; spike (-20% 1h, +782% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $61.6k | $504.3k | -24% | -2% | +1648% | 85.1x | churn 85x vol/liq | 55 |
| [SOYOUARE](https://pump.fun/coin/GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump) | `GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump` | $23.2k | $99.3k | +233% | +233% | +233% | 19.4x | thin liq $23.2k; spike (+233% 1h, +233% 6h); < 1h old | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $57.3k | $565.1k | -43% | -57% | +566% | 47.8x | churn 48x vol/liq | not scored |

_Timing: total 217s (discovery 71.4s, screen 1.1s, GT prime 0.5s, scoring 144.2s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/179; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
