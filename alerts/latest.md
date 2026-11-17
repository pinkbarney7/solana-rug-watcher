# Last scan 2026-11-17T06:37:10Z - mode: helius (box heartbeat stale (148 min); budget 100/3000)

```
[fast_scan] 129 candidate mints from 9 source tags; 126 with pair data; 29 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored LEOSTAR in 72s
[fast_scan] scored BAWSAQ in 80s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored ZEC in 82s
[fast_scan] scored GTA in 82s
[fast_scan] scored HOGE in 82s
[fast_scan] scored SPCX in 83s
[fast_scan] scored bul in 84s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-17 06:37 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,527 (-0.1% 24h), ETH $1,827 (+0.8% 24h), SOL $72.61 (+2.3% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.3% (mcap $2.04B, vol $323.91M), pump-fun +0.5% (mcap $854.80M, vol $128.65M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $105.7k | $654.5k | 2.1 d | h24 +49% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $70.4k | $157.0k | 4.0 h | h24 +47% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $108.5k | $445.6k | 9.2 h | h24 +1444% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $72.7k | $971.3k | 7.6 h | h24 +3028% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $76.2k | $1.07M | 12.7 h | h24 +3271% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $87.1k | $1.34M | 10.5 h | h24 +1476% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.36M | $7.86M | 663.3 d | h24 -35% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,442 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.07M | $22.6k | 397.6 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,871 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $12.69M | 173.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 377,897 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $76.2k | $1.07M | +2% | -0% | +3271% | 12.9x | none flagged (still high risk) | 58 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $71.9k | $951.7k | +15% | -2% | +2965% | 16.4x | none flagged (still high risk) | 58 |
| [CHAR](https://pump.fun/coin/9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump) | `9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump` | $38.7k | $247.3k | +15% | +737% | +737% | 39.6x | thin liq $38.7k; churn 40x vol/liq; spike (+15% 1h, +737% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $56.5k | $440.7k | +12% | -38% | +1427% | 86.4x | churn 86x vol/liq | 55 |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $86.3k | $1.31M | +11% | -12% | +1445% | 25.0x | churn 25x vol/liq | 59 |
| [FROGE](https://pump.fun/coin/GkMfy66mLHzyXFKBw4feG8dXtoXuphQVSJQYMQb4pump) | `GkMfy66mLHzyXFKBw4feG8dXtoXuphQVSJQYMQb4pump` | $19.8k | $46.8k | +231% | -17% | -17% | 6.9x | thin liq $19.8k; spike (+231% 1h, -17% 6h) | not scored |

_Timing: total 217s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 144.2s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 12/180; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
