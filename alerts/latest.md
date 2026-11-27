# Last scan 2026-11-27T05:17:57Z - mode: helius (box heartbeat stale (75 min); budget 10/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 120 with pair data; 25 >= $50,000 liq; 6 pass survivor pre-gates (72s)
[fast_scan] scored Thanksgivi in 71s
[fast_scan] scored SPCX in 79s
[fast_scan] scored CATE in 80s
[fast_scan] scored Snowball in 81s
[fast_scan] scored PUMPCHAN in 81s
[fast_scan] scored Rizzmas in 82s
[fast_scan] scored BASKET in 82s
# Market scan 2026-11-27 05:17 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,633 (+1.3% 24h), ETH $1,741 (+2.6% 24h), SOL $73.04 (+2.7% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $1.91B, vol $280.68M), pump-fun +1.7% (mcap $796.09M, vol $94.86M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $119.7k | $429.5k | 2.0 d | h24 -39% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $97.4k | $547.8k | 1.5 d | h24 +5673% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $264.1k | $11.85M | 1.2 d | h24 +719% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.2% (+9.3) |
| 67* | SKIP | [Thanksgivi](https://dexscreener.com/solana/4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp) | `4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp` | $140.2k | $28.8k | 2.4 h | h24 -44% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $231.1k | $686.1k | 1068.5 d | h24 +47% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,698 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.73M | $18.74M | 123.5 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 438,378) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.90M | 183.9 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,808 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $134.6k | $3.11M | +15% | +2753% | +2753% | 22.8x | liq/mcap 4.3%; spike (+15% 1h, +2753% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $59.2k | $546.0k | -9% | +7% | +5663% | 32.0x | churn 32x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $54.8k | $570.1k | +14% | +1631% | +1631% | 12.1x | spike (+14% 1h, +1631% 6h); lopsided buys/sells 4.81 | not scored |
| [VOLALITY](https://pump.fun/coin/4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump) | `4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump` | $32.0k | $205.8k | +581% | +581% | +581% | 6.4x | thin liq $32.0k; spike (+581% 1h, +581% 6h); < 1h old | not scored |
| [BIAO](https://dexscreener.com/solana/CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN) | `CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN` | $81.6k | $77.0k | +371% | +371% | +371% | 43.7x | churn 44x vol/liq; spike (+371% 1h, +371% 6h); < 1h old | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $35.3k | $223.7k | +20% | +527% | +634% | 32.2x | thin liq $35.3k; churn 32x vol/liq; spike (+20% 1h, +527% 6h) | not scored |

_Timing: total 155s (discovery 70.9s, screen 1.4s, GT prime 0.3s, scoring 82.3s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/148; Helius 429s 81; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
