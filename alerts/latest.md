# Last scan 2026-11-27T09:13:22Z - mode: helius (box heartbeat stale (310 min); budget 190/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 117 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (72s)
[fast_scan] scored PUMPCHAN in 72s
[fast_scan] scored ALCH in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored MOSTO in 81s
[fast_scan] scored TROLL in 82s
[fast_scan] scored KAI in 82s
[fast_scan] scored future in 82s
[fast_scan] scored Snowball in 83s
# Market scan 2026-11-27 09:13 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,745 (+1.5% 24h), ETH $1,731 (+1.8% 24h), SOL $73.43 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.3% (mcap $1.93B, vol $263.15M), pump-fun +2.6% (mcap $800.99M, vol $89.49M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $149.8k | $848.5k | 1.6 d | h24 +4229% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $210.0k | $143.6k | 1.8 h | h24 +176% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $178.3k | $124.2k | 1.2 h | h24 +135% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $243.4k | $9.94M | 1.3 d | h24 +77% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $122.8k | $2.55M | 8.5 h | h24 +2241% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.8% (+6.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [ALCH](https://pump.fun/coin/HNg5PYJmtqcmzXrv6S9zP1CDKk5BgDuyFBxbvNApump) | `HNg5PYJmtqcmzXrv6S9zP1CDKk5BgDuyFBxbvNApump` | $2.18M | $29.91M | 729.6 d | h24 +1% | #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 133,056 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.03M | $22.50M | 846.9 d | h24 +0% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 4h (now 219,057) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.90M | 184.1 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,839 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $74.9k | $848.5k | +79% | +22% | +4229% | 28.7x | churn 29x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $122.6k | $2.55M | -10% | -15% | +2241% | 27.2x | liq/mcap 4.8%; churn 27x vol/liq | 66 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $45.8k | $365.6k | +51% | +60% | +1100% | 27.9x | thin liq $45.8k; churn 28x vol/liq | not scored |
| [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $210.0k | $143.6k | +54% | +176% | +176% | 59.6x | churn 60x vol/liq | 53 |
| [APE](https://dexscreener.com/solana/3JV8jfHTXs75yQ7nYPmaqnhvBVtE8QhrCWBH5qXZZFG2) | `3JV8jfHTXs75yQ7nYPmaqnhvBVtE8QhrCWBH5qXZZFG2` | $23.9k | $17.9k | +126% | +126% | +126% | 6.7x | thin liq $23.9k; spike (+126% 1h, +126% 6h); < 1h old | not scored |
| [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $178.4k | $124.2k | +61% | +135% | +135% | 32.0x | churn 32x vol/liq | 53 |

_Timing: total 155s (discovery 70.9s, screen 1.1s, GT prime 0.4s, scoring 82.7s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/153; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
