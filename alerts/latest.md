# Last scan 2026-11-17T08:27:21Z - mode: helius (box heartbeat stale (258 min); budget 180/3000)

```
[fast_scan] 135 candidate mints from 10 source tags; 133 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 72s
[fast_scan] scored LEOSTAR in 81s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored bul in 82s
[fast_scan] scored GTA in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored SPCX in 83s
[fast_scan] scored HOGE in 84s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-17 08:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,536 (-0.1% 24h), ETH $1,829 (+1.2% 24h), SOL $72.64 (+2.6% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.3% (mcap $2.05B, vol $327.03M), pump-fun +0.3% (mcap $856.48M, vol $133.31M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $96.8k | $549.2k | 2.1 d | h24 +68% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $68.1k | $148.2k | 5.9 h | h24 +39% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [BAWSAQ](https://dexscreener.com/solana/AHYB7o6eQV9GAERKJzAyeiZj5KHGBhfEiLyq2ftjwvM) | `AHYB7o6eQV9GAERKJzAyeiZj5KHGBhfEiLyq2ftjwvM` | $135.2k | $93.9k | 1.2 h | h24 +147% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $99.0k | $543.8k | 11.0 h | h24 +1784% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $78.2k | $1.12M | 14.5 h | h24 +3427% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $78.7k | $1.13M | 9.4 h | h24 +3540% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.37M | $7.99M | 663.3 d | h24 -25% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,442 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.73M | $17.74M | 113.7 d | h24 +11% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 430,317 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.69M | $12.66M | 174.0 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 379,910 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $78.7k | $1.13M | -7% | -7% | +3540% | 15.9x | none flagged (still high risk) | 59 |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $78.2k | $1.12M | +12% | +12% | +3427% | 13.8x | none flagged (still high risk) | 59 |
| [cepump](https://pump.fun/coin/DQRNzNt2QRbLj9iPDRGDBNxCN6skYdne7Qxv819Bpump) | `DQRNzNt2QRbLj9iPDRGDBNxCN6skYdne7Qxv819Bpump` | $25.5k | $126.8k | +518% | +340% | +340% | 10.9x | thin liq $25.5k; spike (+518% 1h, +340% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $63.4k | $546.5k | +2% | -41% | +1794% | 79.0x | churn 79x vol/liq | 55 |
| [GTAVI](https://pump.fun/coin/D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump) | `D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump` | $33.4k | $209.2k | +22% | +611% | +611% | 3.8x | thin liq $33.4k; spike (+22% 1h, +611% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $85.1k | $1.27M | +19% | -7% | +1393% | 27.0x | churn 27x vol/liq | not scored |

_Timing: total 217s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 144.2s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/180; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
