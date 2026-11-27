# Last scan 2026-11-27T03:36:54Z - mode: helius (box heartbeat stale (22 min); budget 457/3000)

```
[fast_scan] 117 candidate mints from 9 source tags; 113 with pair data; 22 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored Snowball in 72s
[fast_scan] scored SuperFIONA in 80s
[fast_scan] scored TOGI in 81s
[fast_scan] scored PUMPCHAN in 82s
[fast_scan] scored ZEC in 82s
[fast_scan] scored BASKET in 83s
[fast_scan] scored SPCX in 83s
[fast_scan] scored Rizzmas in 84s
# Market scan 2026-11-27 03:36 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,588 (+1.5% 24h), ETH $1,730 (+2.1% 24h), SOL $73.03 (+2.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.0% (mcap $1.92B, vol $283.08M), pump-fun +1.8% (mcap $796.72M, vol $94.82M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $112.1k | $384.1k | 2.0 d | h24 -48% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $102.5k | $677.1k | 1.4 d | h24 +5675% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/UgVBFEstTHmbxKcFMDKZnsuh5oTmuQ1AgRSvKD4RoPC) | `UgVBFEstTHmbxKcFMDKZnsuh5oTmuQ1AgRSvKD4RoPC` | $224.5k | $127.0k | 1.8 h | h24 +60% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [TOGI](https://dexscreener.com/solana/6aHvrZ99fXBDRiVNYsuVERXzCeeMdzF9fjvefx1UjR83) | `6aHvrZ99fXBDRiVNYsuVERXzCeeMdzF9fjvefx1UjR83` | $192.0k | $135.2k | 1.7 h | h24 +161% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $255.2k | $11.09M | 1.1 d | h24 +834% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.3% (+9.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $233.7k | $703.1k | 1068.4 d | h24 +52% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,691 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.50M | $13.92M | 183.8 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +1.3% in 13h (now 400,775) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.54M | $18.5k | 407.5 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.5% in 13h (now 396,987) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Santaball](https://pump.fun/coin/4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump) | `4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump` | $73.6k | $1.03M | +57% | +2772% | +2772% | 12.8x | spike (+57% 1h, +2772% 6h); lopsided buys/sells 3.72 | not scored |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $127.1k | $2.79M | +1% | +2460% | +2460% | 23.3x | liq/mcap 4.6%; spike (+1% 1h, +2460% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $65.9k | $677.1k | +32% | +30% | +5675% | 27.6x | churn 28x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $49.1k | $464.5k | +204% | +1310% | +1310% | 10.4x | thin liq $49.1k; spike (+204% 1h, +1310% 6h); lopsided buys/sells 6.21 | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $31.6k | $182.6k | -14% | +1609% | +499% | 33.5x | thin liq $31.6k; churn 34x vol/liq; spike (-14% 1h, +1609% 6h) | not scored |
| [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $40.7k | $211.6k | +3% | +362% | +362% | 2.6x | thin liq $40.7k; spike (+3% 1h, +362% 6h) | not scored |

_Timing: total 157s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 84.3s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
