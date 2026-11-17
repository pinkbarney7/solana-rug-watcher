# Last scan 2026-11-17T06:44:01Z - mode: helius (box heartbeat stale (154 min); budget 110/3000)

```
[fast_scan] 138 candidate mints from 10 source tags; 135 with pair data; 29 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored LEOSTAR in 72s
[fast_scan] scored ZEC in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored GTA in 83s
[fast_scan] scored bul in 83s
[fast_scan] scored HOGE in 85s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-17 06:43 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,292 (-0.5% 24h), ETH $1,817 (+0.3% 24h), SOL $72.17 (+1.6% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $2.04B, vol $326.06M), pump-fun +0.0% (mcap $853.47M, vol $130.79M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $107.2k | $675.8k | 2.1 d | h24 +60% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $62.3k | $124.3k | 4.1 h | h24 +16% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $111.7k | $549.8k | 9.3 h | h24 +1805% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $72.5k | $972.2k | 7.7 h | h24 +3031% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $74.6k | $1.03M | 12.8 h | h24 +3150% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 63* | SKIP | [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $81.6k | $1.18M | 10.7 h | h24 +1293% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #16 Exit liquidity (Jupiter quotes) WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.35M | $7.78M | 663.3 d | h24 -32% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,454 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.05M | $22.4k | 397.6 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,871 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $12.58M | 174.0 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 377,897 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $74.6k | $1.03M | -7% | -4% | +3150% | 13.3x | none flagged (still high risk) | 58 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $72.8k | $978.6k | +17% | -10% | +3052% | 16.3x | none flagged (still high risk) | 58 |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $63.2k | $549.8k | +28% | -34% | +1805% | 77.8x | churn 78x vol/liq | 55 |
| [CHAR](https://pump.fun/coin/9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump) | `9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump` | $36.2k | $218.3k | -6% | +639% | +639% | 42.6x | thin liq $36.2k; churn 43x vol/liq; spike (-6% 1h, +639% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $82.5k | $1.21M | +19% | -13% | +1321% | 26.3x | churn 26x vol/liq | 63 |
| [MELNOK](https://pump.fun/coin/3ig9E5SQKs8RjVn9EuW1YaprjaMd6dEftG63hBcMpump) | `3ig9E5SQKs8RjVn9EuW1YaprjaMd6dEftG63hBcMpump` | $23.5k | $106.4k | +25% | +272% | +272% | 19.7x | thin liq $23.5k; spike (+25% 1h, +272% 6h) | not scored |

_Timing: total 217s (discovery 71.2s, screen 1.3s, GT prime 0.2s, scoring 144.2s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
