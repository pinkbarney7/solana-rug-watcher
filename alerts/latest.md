# Last scan 2026-11-17T01:06:17Z - mode: helius (box heartbeat stale (21 min); budget 370/3000)

```
[fast_scan] 146 candidate mints from 10 source tags; 140 with pair data; 27 >= $50,000 liq; 12 pass survivor pre-gates (65s)
[fast_scan] scored SPCX in 71s
[fast_scan] scored BAWSAQ in 80s
[fast_scan] scored GTA6 in 80s
[fast_scan] scored USPR in 80s
[fast_scan] scored USOE in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored CATE in 82s
# Market scan 2026-11-17 01:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,582 (-0.3% 24h), ETH $1,813 (+0.2% 24h), SOL $71.47 (-0.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.6% (mcap $2.02B, vol $320.39M), pump-fun -5.0% (mcap $846.63M, vol $125.37M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [GTA6](https://dexscreener.com/solana/JqWFgttDRXeP49F6iYc4eVK88D1PonNEmKcQwkLwENN) | `JqWFgttDRXeP49F6iYc4eVK88D1PonNEmKcQwkLwENN` | $137.6k | $90.1k | 1.1 h | h24 +106% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [BAWSAQ](https://dexscreener.com/solana/55jDZh5aM1H3rYxc4Z8mndGUXNj35jvBan6SkDoqNoS) | `55jDZh5aM1H3rYxc4Z8mndGUXNj35jvBan6SkDoqNoS` | $132.6k | $89.2k | 1.4 h | h24 +141% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $1.19M | $282.58M | 2.1 d | h24 +46% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.4% (+11.5) |
| 67* | SKIP | [USOE](https://pump.fun/coin/9ywBZUXaPhjtxwVbjdq9SJJoXuTTRx5BmqK5wnb8pump) | `9ywBZUXaPhjtxwVbjdq9SJJoXuTTRx5BmqK5wnb8pump` | $449.3k | $40.10M | 1.4 d | h24 +46% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 1.1% (+10.7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.65M | $16.31M | 113.4 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 13h (now 430,210) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.39M | $8.34M | 663.0 d | h24 -21% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 12h (now 344,452) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.54M | $12.54M | 173.7 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.0% in 12h (now 376,608) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AGI](https://dexscreener.com/solana/CUmQsPuWxK97tYYWV44qhHXEu69oM4nj3CpYBTw796ea) | `CUmQsPuWxK97tYYWV44qhHXEu69oM4nj3CpYBTw796ea` | $25.6k | $95.8k | +4504% | +4504% | +4504% | 4.2x | thin liq $25.6k; spike (+4504% 1h, +4504% 6h); < 1h old | not scored |
| [LEOSTAR](https://pump.fun/coin/2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump) | `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump` | $77.6k | $1.15M | +11% | +3592% | +3592% | 9.3x | spike (+11% 1h, +3592% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $82.5k | $1.00M | +81% | +3377% | +3377% | 44.0x | churn 44x vol/liq; spike (+81% 1h, +3377% 6h) | not scored |
| [BAWSAQ](https://pump.fun/coin/D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump) | `D9EcoQZeAytCrF1kQFSpRNpoPhibJUvJcmRHXhubpump` | $99.0k | $1.79M | +35% | +2009% | +2009% | 16.0x | spike (+35% 1h, +2009% 6h) | not scored |
| [LUCIA](https://pump.fun/coin/27Ggmg2ZmaehHX7L5vZqCeTRoQmPaBtR5vqvaRLbpump) | `27Ggmg2ZmaehHX7L5vZqCeTRoQmPaBtR5vqvaRLbpump` | $23.0k | $111.5k | +184% | +184% | +184% | 17.9x | thin liq $23.0k; spike (+184% 1h, +184% 6h); lopsided buys/sells 4.18; < 1h old | not scored |
| [ETF](https://pump.fun/coin/Gg5aWvfucyMwihDzyfCEaLgyeeNE2dkob2LTwWfHpump) | `Gg5aWvfucyMwihDzyfCEaLgyeeNE2dkob2LTwWfHpump` | $37.1k | $252.8k | +37% | -0% | +728% | 27.1x | thin liq $37.1k; churn 27x vol/liq | not scored |

_Timing: total 147s (discovery 63.4s, screen 1.3s, GT prime 0.4s, scoring 81.6s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/138; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
