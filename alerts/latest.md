# Last scan 2026-11-17T04:56:49Z - mode: helius (box heartbeat stale (48 min); budget 390/3000)

```
[fast_scan] 130 candidate mints from 9 source tags; 128 with pair data; 31 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored bul in 74s
[fast_scan] scored SPCX in 81s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored GTA in 82s
[fast_scan] scored BAWSAQ in 82s
[fast_scan] scored ZEC in 83s
[fast_scan] scored VINE in 83s
[fast_scan] scored HOGE in 84s
# Market scan 2026-11-17 04:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,932 (+0.3% 24h), ETH $1,831 (+0.8% 24h), SOL $72.79 (+1.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.4% (mcap $2.06B, vol $309.50M), pump-fun -2.7% (mcap $857.92M, vol $126.74M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $103.8k | $632.0k | 2.0 d | h24 +54% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $85.2k | $199.1k | 2.4 h | h24 +86% | #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $120.8k | $464.7k | 7.5 h | h24 +26% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 58* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $72.0k | $957.0k | 11.0 h | h24 +2919% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $77.0k | $1.05M | 8.9 h | h24 +1139% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.38M | $8.09M | 663.2 d | h24 -28% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,445 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.12M | $22.8k | 397.5 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,939 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $12.63M | 173.9 d | h24 -1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 378,250 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WANTED](https://pump.fun/coin/9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump) | `9jhs5qoJnUFU7AZXbsiD1Q6De6FVsino9Ysw8QU6pump` | $41.4k | $300.5k | +6655% | +525% | +525% | 46.4x | thin liq $41.4k; churn 46x vol/liq; spike (+6655% 1h, +525% 6h) | not scored |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $72.4k | $966.1k | -12% | +3011% | +3011% | 15.1x | spike (-12% 1h, +3011% 6h) | not scored |
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $72.0k | $957.0k | -9% | +32% | +2919% | 12.4x | none flagged (still high risk) | 58 |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $57.7k | $458.1k | -22% | -24% | +1487% | 83.8x | churn 84x vol/liq | 45 |
| [CHAR](https://pump.fun/coin/9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump) | `9k2nqjUrSh9p2ZBnWxNE3QRWYiLocrWZfoDm3Vdxpump` | $32.9k | $182.2k | -24% | +517% | +517% | 42.1x | thin liq $32.9k; churn 42x vol/liq; spike (-24% 1h, +517% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $77.6k | $1.07M | -30% | -42% | +1159% | 26.3x | churn 26x vol/liq | 58 |

_Timing: total 158s (discovery 72.0s, screen 1.3s, GT prime 0.2s, scoring 84.2s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 9/169; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
