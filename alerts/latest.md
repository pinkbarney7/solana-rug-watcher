# Last scan 2026-11-27T09:28:19Z - mode: helius (box heartbeat stale (325 min); budget 210/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 118 with pair data; 23 >= $50,000 liq; 5 pass survivor pre-gates (73s)
[fast_scan] scored PUMPCHAN in 72s
[fast_scan] scored Snowball in 80s
[fast_scan] scored KAI in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored PETER in 83s
[fast_scan] scored future in 83s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 09:28 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,654 (+1.5% 24h), ETH $1,730 (+1.9% 24h), SOL $73.44 (+3.5% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.3% (mcap $1.93B, vol $258.81M), pump-fun +2.6% (mcap $801.30M, vol $91.07M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $157.3k | $959.1k | 1.6 d | h24 +604% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [PETER](https://dexscreener.com/solana/9p3H9N4sbSTaBe95stavYTH3b4B5gcQUjsJF1BTNCBze) | `9p3H9N4sbSTaBe95stavYTH3b4B5gcQUjsJF1BTNCBze` | $195.2k | $139.2k | 1.8 h | h24 +164% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $226.8k | $160.1k | 2.1 h | h24 +208% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $244.9k | $10.05M | 1.3 d | h24 +79% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 66* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $126.3k | $2.69M | 8.7 h | h24 +2371% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.7% (+6.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $222.8k | $633.4k | 1068.6 d | h24 +27% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 395,720) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.70M | $17.93M | 123.7 d | h24 +7% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 438,645) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.93M | 184.1 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,775 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Kibo](https://dexscreener.com/solana/2Gy6aAgrk4XfxZ38og5pbQPuFa1D41SvYezdPxNKmVoP) | `2Gy6aAgrk4XfxZ38og5pbQPuFa1D41SvYezdPxNKmVoP` | $52.6k | $66.2k | +249% | +1605% | +1605% | 15.2x | spike (+249% 1h, +1605% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $77.2k | $898.9k | +34% | +19% | +4936% | 27.9x | churn 28x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $126.1k | $2.69M | -9% | -6% | +2371% | 26.6x | liq/mcap 4.7%; churn 27x vol/liq | 66 |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $45.1k | $353.1k | +17% | +87% | +1059% | 28.4x | thin liq $45.1k; churn 28x vol/liq | not scored |
| [NIW](https://pump.fun/coin/CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump) | `CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump` | $19.8k | $94.7k | +99% | +226% | +226% | 0.1x | thin liq $19.8k | not scored |
| [future](https://dexscreener.com/solana/6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym) | `6DARe6XUHsxgmF49Fxb3hE4NnnTqfHYHc8ryHUyE5Aym` | $226.9k | $160.1k | +50% | +208% | +208% | 63.8x | churn 64x vol/liq | 56 |

_Timing: total 156s (discovery 71.4s, screen 1.1s, GT prime 0.4s, scoring 83.4s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/158; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
