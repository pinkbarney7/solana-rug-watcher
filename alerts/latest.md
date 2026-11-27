# Last scan 2026-11-27T08:57:42Z - mode: helius (box heartbeat stale (294 min); budget 170/3000)

```
[fast_scan] 118 candidate mints from 10 source tags; 117 with pair data; 24 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored KAI in 78s
[fast_scan] scored CATE in 86s
[fast_scan] scored PUMPCHAN in 86s
[fast_scan] scored SuperFIONA in 87s
[fast_scan] scored SPCX in 87s
[fast_scan] scored future in 88s
[fast_scan] scored Rizzmas in 89s
# Market scan 2026-11-27 08:57 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,703 (+1.4% 24h), ETH $1,730 (+2.0% 24h), SOL $73.27 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.0% (mcap $1.92B, vol $275.51M), pump-fun +2.4% (mcap $799.41M, vol $91.61M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7) | `8kXyaKo95LDMq2ZyNqdKzwnoRXVYWYoioNrZuBgNuwX7` | $239.2k | $139.9k | 2.9 h | h24 +72% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $195.0k | $130.1k | 1.6 h | h24 +150% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $242.9k | $9.92M | 1.3 d | h24 +91% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $123.7k | $2.59M | 8.2 h | h24 +2282% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.8% (+6.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $221.2k | $626.7k | 1068.6 d | h24 +25% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,722 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.82M | 123.7 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,634 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.88M | 184.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,839 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $77.2k | $902.8k | +103% | +43% | +5159% | 27.3x | churn 27x vol/liq; spike (+103% 1h, +43% 6h) | not scored |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $123.5k | $2.59M | -13% | -12% | +2282% | 26.8x | liq/mcap 4.8%; churn 27x vol/liq | 66 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $42.4k | $315.4k | +27% | +82% | +935% | 29.5x | thin liq $42.4k; churn 29x vol/liq | not scored |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $24.7k | $118.8k | -26% | +269% | +269% | 26.4x | thin liq $24.7k; churn 26x vol/liq | not scored |
| [MOSTO](https://dexscreener.com/solana/3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo) | `3UPbAqDetbPp8dVbBm8qXtV27zvVnedZryterN8rGtAo` | $166.1k | $112.2k | +113% | +113% | +113% | 26.7x | churn 27x vol/liq; spike (+113% 1h, +113% 6h); < 1h old | not scored |
| [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $195.0k | $130.1k | +59% | +150% | +150% | 54.4x | churn 54x vol/liq | 53 |

_Timing: total 162s (discovery 71.5s, screen 1.4s, GT prime 0.5s, scoring 89.0s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/142; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
