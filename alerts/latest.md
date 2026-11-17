# Last scan 2026-11-17T12:46:27Z - mode: helius (box heartbeat stale (517 min); budget 380/3000)

```
[fast_scan] 126 candidate mints from 10 source tags; 123 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored HOGE in 73s
[fast_scan] scored ZEC in 80s
[fast_scan] scored GTA in 81s
[fast_scan] scored Millionaires in 81s
[fast_scan] scored LEOSTAR in 82s
[fast_scan] scored VINE in 82s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored bul in 83s
[fast_scan] scored SPCX in 71s
# Market scan 2026-11-17 12:46 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,892 (+1.3% 24h), ETH $1,817 (+1.3% 24h), SOL $73.48 (+4.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +3.0% (mcap $2.07B, vol $338.41M), pump-fun +2.0% (mcap $857.60M, vol $135.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $104.1k | $596.7k | 2.3 d | h24 +65% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $102.0k | $327.8k | 10.2 h | h24 +206% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [Millionaires](https://dexscreener.com/solana/12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb) | `12Xt9B42H3MkyYosmPffPjNK36v5pPwXhNuaFyDA3QFb` | $116.6k | $73.4k | 1.3 h | h24 +128% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $90.7k | $514.0k | 15.3 h | h24 +1681% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $89.0k | $1.41M | 18.8 h | h24 +4344% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 59* | SKIP | [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $89.1k | $1.41M | 13.7 h | h24 +4432% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.38M | $7.93M | 663.5 d | h24 -22% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 344,406 (growth n/a: first sighting) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.55M | $23.5k | 397.8 d | h24 +10% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 392,499 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.43M | $12.97M | 174.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 380,501 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $90.4k | $1.45M | +11% | +42% | +4464% | 15.1x | none flagged (still high risk) | 59 |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $89.1k | $1.41M | +9% | +44% | +4432% | 16.8x | none flagged (still high risk) | 59 |
| [GROKIA](https://dexscreener.com/solana/A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm) | `A4zQMT7ZFC2mM8fZDDQEqCs5bLFifA9XhDAJtHc3Lzbm` | $46.1k | $379.9k | -2% | +1048% | +1048% | 92.3x | thin liq $46.1k; churn 92x vol/liq; spike (-2% 1h, +1048% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $62.3k | $514.0k | -19% | -1% | +1681% | 84.2x | churn 84x vol/liq | 55 |
| [SOYOUARE](https://pump.fun/coin/GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump) | `GbGzZQugMJtZnhcnNyHUamXg2xGZw4C4RWy1uSvVpump` | $23.5k | $99.8k | +235% | +235% | +235% | 20.1x | thin liq $23.5k; spike (+235% 1h, +235% 6h); < 1h old | not scored |
| [BLG](https://dexscreener.com/solana/DKDktvVnv1Bg1MCnUGdn1FTgHLGb6twejRVD9rVTQ2kt) | `DKDktvVnv1Bg1MCnUGdn1FTgHLGb6twejRVD9rVTQ2kt` | $15.5k | $13.2k | +168% | +168% | +168% | 2.4x | thin liq $15.5k; spike (+168% 1h, +168% 6h); < 1h old | not scored |

_Timing: total 217s (discovery 70.7s, screen 1.4s, GT prime 0.2s, scoring 144.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/180; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
