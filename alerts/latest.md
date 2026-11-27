# Last scan 2026-11-27T07:12:35Z - mode: helius (box heartbeat stale (189 min); budget 120/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 115 with pair data; 23 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 69s
[fast_scan] scored Snowball in 78s
[fast_scan] scored SPCX in 78s
[fast_scan] scored CATE in 78s
[fast_scan] scored KAI in 79s
[fast_scan] scored Rizzmas in 80s
# Market scan 2026-11-27 07:12 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,690 (+2.1% 24h), ETH $1,733 (+2.8% 24h), SOL $72.97 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.5% (mcap $1.92B, vol $265.49M), pump-fun +2.3% (mcap $798.39M, vol $94.51M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $95.2k | $539.3k | 1.5 d | h24 +4221% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $245.6k | $10.19M | 1.2 d | h24 +535% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $125.1k | $2.68M | 6.5 h | h24 +2360% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.7% (+6.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.7k | $625.5k | 1068.5 d | h24 +34% | #6 unknown (+3); #7 unknown (+3); #11 not checked (+3); GATES FAILED: rug-funder link |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.70M | $18.27M | 123.6 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 2h (now 438,601) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.90M | 184.0 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 400,725 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $73.2k | $987.4k | +11% | +2897% | +2897% | 12.9x | spike (+11% 1h, +2897% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $58.8k | $537.1k | -16% | -7% | +4204% | 33.3x | churn 33x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $21.8k | $97.2k | +522% | +202% | +202% | 17.9x | thin liq $21.8k; spike (+522% 1h, +202% 6h) | not scored |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $125.2k | $2.68M | -20% | +10% | +2365% | 25.6x | liq/mcap 4.7%; churn 26x vol/liq | 66 |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $213.2k | $231.0k | +49% | +655% | +655% | 59.7x | churn 60x vol/liq; spike (+49% 1h, +655% 6h) | not scored |
| [哈基米](https://dexscreener.com/solana/3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41) | `3HvxhYfVSKMTNPP5LkoZsj9JwPAnjrNxbpzuuoTqbz41` | $167.6k | $114.1k | +117% | +117% | +117% | 27.0x | churn 27x vol/liq; spike (+117% 1h, +117% 6h); < 1h old | not scored |

_Timing: total 153s (discovery 71.8s, screen 1.2s, GT prime 0.5s, scoring 79.7s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/124; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
