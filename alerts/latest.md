# Last scan 2026-11-17T04:41:28Z - mode: helius (box heartbeat stale (33 min); budget 390/3000)

```
[fast_scan] 134 candidate mints from 10 source tags; 131 with pair data; 30 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored GTA in 73s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored SPCX in 83s
[fast_scan] scored ZEC in 83s
[fast_scan] scored bul in 83s
[fast_scan] scored BAWSAQ in 85s
[fast_scan] scored HOGE in 86s
# Market scan 2026-11-17 04:41 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,922 (+0.0% 24h), ETH $1,829 (+0.4% 24h), SOL $72.72 (+1.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.9% (mcap $2.05B, vol $308.02M), pump-fun -3.1% (mcap $854.08M, vol $126.80M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $97.3k | $551.0k | 2.0 d | h24 +37% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $107.0k | $314.7k | 2.1 h | h24 +194% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $119.1k | $441.1k | 7.3 h | h24 +19% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $71.8k | $953.7k | 10.7 h | h24 +2909% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $76.6k | $1.04M | 8.6 h | h24 +1128% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.38M | $8.01M | 663.2 d | h24 -29% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 4h (now 344,445) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.10M | $22.7k | 397.5 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.3% in 15h (now 391,939) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.61M | $12.59M | 173.9 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.4% in 4h (now 378,250) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $75.9k | $1.06M | +1% | +3323% | +3323% | 14.2x | spike (+1% 1h, +3323% 6h) | not scored |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $71.5k | $945.5k | -23% | +31% | +2883% | 12.3x | none flagged (still high risk) | 58 |
| [CHAR](https://pump.fun/coin/9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump) | `9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump` | $36.3k | $221.3k | +202% | +649% | +649% | 37.4x | thin liq $36.3k; churn 37x vol/liq; spike (+202% 1h, +649% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $56.7k | $444.5k | -40% | +36% | +1440% | 84.9x | churn 85x vol/liq | 45 |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $76.6k | $1.04M | -41% | -38% | +1128% | 26.4x | churn 26x vol/liq | 58 |
| [MELNOK](https://pump.fun/coin/3ig9E5SQKs8RjVn9EuW1YaprjaMd6dEftG63hBcMpump) | `3ig9E5SQKs8RjVn9EuW1YaprjaMd6dEftG63hBcMpump` | $25.6k | $130.2k | +33% | +355% | +355% | 9.3x | thin liq $25.6k; spike (+33% 1h, +355% 6h) | not scored |

_Timing: total 158s (discovery 71.2s, screen 1.3s, GT prime 0.3s, scoring 85.5s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/169; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
