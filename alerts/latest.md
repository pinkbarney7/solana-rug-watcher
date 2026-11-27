# Last scan 2026-11-27T04:47:30Z - mode: helius (box heartbeat stale (44 min); budget 497/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 114 with pair data; 25 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored SPCX in 71s
[fast_scan] scored MPLX in 79s
[fast_scan] scored Snowball in 79s
[fast_scan] scored Thanksgivi in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored BASKET in 82s
[fast_scan] scored Rizzmas in 83s
# Market scan 2026-11-27 04:47 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,493 (+0.8% 24h), ETH $1,735 (+1.9% 24h), SOL $72.84 (+2.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.2% (mcap $1.92B, vol $281.02M), pump-fun +1.9% (mcap $797.97M, vol $93.27M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $116.5k | $407.4k | 2.0 d | h24 -41% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $102.5k | $630.8k | 1.4 d | h24 +7279% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [Thanksgivi](https://dexscreener.com/solana/4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp) | `4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp` | $241.0k | $193.6k | 1.9 h | h24 +276% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $257.5k | $11.30M | 1.1 d | h24 +735% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.3% (+9.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $229.7k | $679.8k | 1068.4 d | h24 +46% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,698 (growth n/a: first sighting) |
| 71* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.01M | $27.61M | 1460.1 d | h24 +15% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,299 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.58M | $13.87M | 183.9 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,841 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $130.3k | $2.93M | +10% | +2588% | +2588% | 23.2x | liq/mcap 4.5%; spike (+10% 1h, +2588% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $63.6k | $630.8k | -3% | +1% | +7279% | 29.6x | churn 30x vol/liq | 52 |
| [Santaball](https://pump.fun/coin/4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump) | `4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump` | $60.4k | $689.0k | -47% | +1825% | +1825% | 19.5x | spike (-47% 1h, +1825% 6h); lopsided buys/sells 3.51 | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $56.2k | $600.4k | +33% | +1723% | +1723% | 11.2x | spike (+33% 1h, +1723% 6h); lopsided buys/sells 5.23 | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $39.2k | $275.8k | +72% | +436% | +805% | 28.2x | thin liq $39.2k; churn 28x vol/liq; spike (+72% 1h, +436% 6h) | not scored |
| [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $50.3k | $308.6k | +39% | +323% | +573% | 2.5x | spike (+39% 1h, +323% 6h) | not scored |

_Timing: total 156s (discovery 71.6s, screen 1.1s, GT prime 0.4s, scoring 83.0s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/147; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
