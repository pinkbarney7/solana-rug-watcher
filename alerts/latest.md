# Last scan 2026-11-17T09:05:12Z - mode: helius (box heartbeat stale (296 min); budget 220/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 121 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored bul in 74s
[fast_scan] scored GTA in 81s
[fast_scan] scored ZEC in 81s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored SACK in 83s
[fast_scan] scored LEOSTAR in 83s
[fast_scan] scored HOGE in 83s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-17 09:05 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,280 (-0.3% 24h), ETH $1,818 (+0.7% 24h), SOL $72.38 (+2.2% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.8% (mcap $2.04B, vol $322.41M), pump-fun +1.1% (mcap $853.87M, vol $127.60M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $97.5k | $549.2k | 2.2 d | h24 +48% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $65.7k | $138.6k | 6.5 h | h24 +30% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $107.4k | $557.0k | 11.6 h | h24 +1830% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [SACK](https://dexscreener.com/solana/N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf) | `N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf` | $149.9k | $119.3k | 1.4 h | h24 +247% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $83.9k | $1.29M | 15.1 h | h24 +3958% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $78.1k | $1.12M | 10.0 h | h24 +3499% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.36M | $7.86M | 663.4 d | h24 -28% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,440 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.05M | $22.5k | 397.7 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 391,813) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.68M | $12.63M | 174.0 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,368 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $83.9k | $1.29M | +18% | +18% | +3958% | 13.3x | none flagged (still high risk) | 59 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $78.1k | $1.12M | -3% | +13% | +3499% | 16.3x | none flagged (still high risk) | 59 |
| [GTAVI](https://pump.fun/coin/D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump) | `D7ZkNHN3ESProTmshXRjAgiNjQU7SkUcXHpe13qCpump` | $40.0k | $292.8k | +37% | +896% | +896% | 3.3x | thin liq $40.0k; spike (+37% 1h, +896% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $64.9k | $572.2k | +11% | -37% | +1883% | 78.0x | churn 78x vol/liq | 55 |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $92.4k | $1.49M | +31% | -18% | +1660% | 25.3x | churn 25x vol/liq | not scored |
| [SACK](https://dexscreener.com/solana/N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf) | `N8siSKt4dR7Tz79U1PvukfCSipRikykgFtDF1xx3muf` | $150.5k | $120.0k | +83% | +249% | +249% | 55.9x | churn 56x vol/liq | 56 |

_Timing: total 220s (discovery 72.0s, screen 1.3s, GT prime 0.5s, scoring 145.7s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/180; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
