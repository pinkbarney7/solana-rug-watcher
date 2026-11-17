# Last scan 2026-11-17T08:50:29Z - mode: helius (box heartbeat stale (281 min); budget 200/3000)

```
[fast_scan] 134 candidate mints from 10 source tags; 132 with pair data; 30 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored bul in 73s
[fast_scan] scored GTA in 80s
[fast_scan] scored SPCX in 80s
[fast_scan] scored LEOSTAR in 82s
[fast_scan] scored VINE in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored HOGE in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-17 08:50 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,365 (-0.3% 24h), ETH $1,821 (+0.7% 24h), SOL $72.38 (+1.9% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.7% (mcap $2.04B, vol $320.72M), pump-fun +1.1% (mcap $853.68M, vol $127.34M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $99.4k | $580.4k | 2.2 d | h24 +66% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $65.2k | $136.6k | 6.2 h | h24 +28% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [BAWSAQ](https://dexscreener.com/solana/AHYB7o6eQV9GAERKJzAyeiZj5KHGBhfEiLyq2ftjwvM) | `AHYB7o6eQV9GAERKJzAyeiZj5KHGBhfEiLyq2ftjwvM` | $140.5k | $93.7k | 1.6 h | h24 +147% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $112.7k | $619.3k | 11.4 h | h24 +2046% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $78.2k | $1.12M | 14.9 h | h24 +3439% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $77.6k | $1.10M | 9.8 h | h24 +3458% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.36M | $7.92M | 663.4 d | h24 -28% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,440 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.51M | 113.7 d | h24 +9% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 430,317 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.68M | $12.63M | 174.0 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,368 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $78.2k | $1.12M | -3% | +18% | +3511% | 16.2x | none flagged (still high risk) | 59 |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $77.4k | $1.10M | +15% | +6% | +3369% | 14.2x | none flagged (still high risk) | 59 |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $67.4k | $619.3k | +17% | -22% | +2046% | 74.7x | churn 75x vol/liq | 55 |
| [GTAVI](https://pump.fun/coin/D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump) | `D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump` | $33.8k | $217.1k | +7% | +638% | +638% | 3.8x | thin liq $33.8k; spike (+7% 1h, +638% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $92.6k | $1.50M | +41% | -9% | +1669% | 25.1x | churn 25x vol/liq | not scored |
| [SACK](https://dexscreener.com/solana/N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf) | `N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf` | $139.6k | $109.4k | +112% | +218% | +218% | 48.9x | churn 49x vol/liq; spike (+112% 1h, +218% 6h) | not scored |

_Timing: total 217s (discovery 70.8s, screen 1.3s, GT prime 0.3s, scoring 144.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
