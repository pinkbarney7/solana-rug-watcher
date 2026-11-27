# Last scan 2026-11-27T09:06:10Z - mode: helius (box heartbeat stale (303 min); budget 180/3000)

```
[fast_scan] 118 candidate mints from 10 source tags; 117 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 72s
[fast_scan] scored ALCH in 80s
[fast_scan] scored MOSTO in 81s
[fast_scan] scored Snowball in 81s
[fast_scan] scored ZEC in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored future in 83s
[fast_scan] scored PUMPCHAN in 83s
# Market scan 2026-11-27 09:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,719 (+1.5% 24h), ETH $1,730 (+1.8% 24h), SOL $73.37 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.0% (mcap $1.92B, vol $275.51M), pump-fun +2.4% (mcap $799.41M, vol $91.61M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $150.0k | $892.6k | 1.6 d | h24 +4622% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $202.9k | $137.3k | 1.7 h | h24 +164% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $172.1k | $118.0k | 1.1 h | h24 +124% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $242.7k | $9.90M | 1.3 d | h24 +89% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.5% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $124.7k | $2.64M | 8.4 h | h24 +2320% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.7% (+6.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [ALCH](https://pump.fun/coin/HNg5PYJmtqcmzXrv6S9zP1CDKk5BgDuyFBxbvNApump) | `HNg5PYJmtqcmzXrv6S9zP1CDKk5BgDuyFBxbvNApump` | $2.18M | $29.90M | 729.6 d | h24 +1% | #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 133,056 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.90M | 184.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,839 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.53M | $18.6k | 407.7 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 396,752) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $77.0k | $892.6k | +93% | +35% | +4622% | 27.8x | churn 28x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $124.6k | $2.64M | -5% | -18% | +2320% | 26.7x | liq/mcap 4.7%; churn 27x vol/liq | 66 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $43.4k | $327.4k | +44% | +59% | +975% | 29.2x | thin liq $43.4k; churn 29x vol/liq | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $25.4k | $124.3k | -2% | +286% | +286% | 25.9x | thin liq $25.4k; churn 26x vol/liq | not scored |
| [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $202.8k | $137.0k | +55% | +164% | +164% | 57.5x | churn 58x vol/liq | 53 |
| [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $172.5k | $118.4k | +73% | +125% | +125% | 29.8x | churn 30x vol/liq | 53 |

_Timing: total 156s (discovery 71.4s, screen 1.2s, GT prime 0.4s, scoring 82.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/153; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
