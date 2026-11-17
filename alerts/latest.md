# Last scan 2026-11-17T07:30:52Z - mode: helius (box heartbeat stale (201 min); budget 140/3000)

```
[fast_scan] 136 candidate mints from 10 source tags; 133 with pair data; 33 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored HOGE in 74s
[fast_scan] scored Bones in 80s
[fast_scan] scored BAWSAQ in 81s
[fast_scan] scored ZEC in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored GTA in 82s
[fast_scan] scored LEOSTAR in 83s
[fast_scan] scored bul in 84s
[fast_scan] scored VINE in 72s
# Market scan 2026-11-17 07:30 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,644 (+0.0% 24h), ETH $1,830 (+1.0% 24h), SOL $72.88 (+2.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.3% (mcap $2.05B, vol $327.31M), pump-fun +0.5% (mcap $857.30M, vol $131.52M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $102.9k | $628.4k | 2.1 d | h24 +67% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $61.0k | $118.8k | 4.9 h | h24 +11% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $103.4k | $534.0k | 10.1 h | h24 +1750% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [Bones](https://dexscreener.com/solana/1Q5LFbfP8SLDQrEKq7arfa4tPN1Yh3zatKDGxZXWNfp) | `1Q5LFbfP8SLDQrEKq7arfa4tPN1Yh3zatKDGxZXWNfp` | $152.7k | $123.9k | 1.4 h | h24 +265% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 58* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $74.0k | $1.00M | 13.6 h | h24 +3067% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $82.0k | $1.22M | 8.5 h | h24 +3837% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.39M | $8.14M | 663.3 d | h24 -33% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,447 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.14M | $22.8k | 397.6 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,867 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.70M | $12.61M | 174.0 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 378,991 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $81.9k | $1.22M | +25% | +36% | +3830% | 15.0x | none flagged (still high risk) | 59 |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $74.0k | $1.00M | -5% | -12% | +3067% | 13.9x | none flagged (still high risk) | 58 |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $62.6k | $534.0k | +21% | -26% | +1750% | 79.2x | churn 79x vol/liq | 55 |
| [CHAR](https://pump.fun/coin/9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump) | `9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump` | $30.6k | $155.8k | -50% | +427% | +427% | 52.0x | thin liq $30.6k; churn 52x vol/liq; spike (-50% 1h, +427% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $77.5k | $1.05M | -17% | -29% | +1144% | 28.8x | churn 29x vol/liq | not scored |
| [Bones](https://dexscreener.com/solana/1Q5LFbfP8SLDQrEKq7arfa4tPN1Yh3zatKDGxZXWNfp) | `1Q5LFbfP8SLDQrEKq7arfa4tPN1Yh3zatKDGxZXWNfp` | $152.7k | $123.9k | +82% | +265% | +265% | 55.3x | churn 55x vol/liq | 56 |

_Timing: total 219s (discovery 71.4s, screen 1.4s, GT prime 0.3s, scoring 145.9s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 11/180; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
