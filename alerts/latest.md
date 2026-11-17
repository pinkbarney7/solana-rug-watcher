# Last scan 2026-11-17T09:24:42Z - mode: helius (box heartbeat stale (315 min); budget 220/3000)

```
[fast_scan] 83 candidate mints from 7 source tags; 81 with pair data; 28 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored GTA in 72s
[fast_scan] scored LEOSTAR in 81s
[fast_scan] scored bul in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored WANTED in 83s
[fast_scan] scored SPCX in 83s
[fast_scan] scored HOGE in 83s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-17 09:24 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,180 (-0.0% 24h), ETH $1,810 (+0.8% 24h), SOL $72.11 (+2.2% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.3% (mcap $2.03B, vol $303.33M), pump-fun +0.7% (mcap $850.66M, vol $126.26M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $99.2k | $584.1k | 2.2 d | h24 +56% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $66.2k | $141.4k | 6.8 h | h24 +32% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $114.2k | $593.3k | 12.0 h | h24 +1956% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $74.6k | $1.02M | 10.4 h | h24 +3195% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $82.2k | $1.24M | 15.4 h | h24 +3804% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [WANTED](https://pump.fun/coin/9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump) | `9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump` | $53.8k | $463.9k | 7.1 h | h24 +866% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.37M | $8.05M | 663.4 d | h24 -26% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,436 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.02M | $22.4k | 397.7 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,813 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.65M | $12.83M | 174.1 d | h24 -3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,390 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $82.2k | $1.24M | +17% | +17% | +3804% | 13.8x | none flagged (still high risk) | 59 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $74.6k | $1.02M | -11% | -3% | +3195% | 17.2x | none flagged (still high risk) | 58 |
| [GTAVI](https://pump.fun/coin/D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump) | `D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump` | $37.8k | $268.4k | +39% | +812% | +812% | 3.7x | thin liq $37.8k; spike (+39% 1h, +812% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $66.0k | $593.3k | +9% | -33% | +1956% | 76.9x | churn 77x vol/liq | 55 |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $92.0k | $1.48M | +8% | -21% | +1647% | 25.6x | churn 26x vol/liq | not scored |
| [WANTED](https://pump.fun/coin/9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump) | `9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump` | $52.7k | $463.9k | +47% | -46% | +866% | 47.3x | churn 47x vol/liq | 60 |

_Timing: total 217s (discovery 71.4s, screen 0.9s, GT prime 0.5s, scoring 144.4s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/178; Helius 429s 105; DEX Screener ok._
_Source gaps: gt_new: gave up after 3 tries (HTTP 429); gt_pumpswap_vol: gave up after 3 tries (HTTP 429)_

_Full reports: out/<mint>.md (+ .json)_
```
