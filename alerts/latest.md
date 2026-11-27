# Last scan 2026-11-27T05:09:13Z - mode: helius (box heartbeat stale (66 min); budget 0/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 123 with pair data; 27 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 74s
[fast_scan] scored CINU in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Thanksgivi in 81s
[fast_scan] scored Snowball in 82s
[fast_scan] scored PUMPCHAN in 82s
[fast_scan] scored TROLL in 83s
[fast_scan] scored CYBERLEEK in 84s
# Market scan 2026-11-27 05:09 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,444 (+0.9% 24h), ETH $1,734 (+2.0% 24h), SOL $72.80 (+2.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $1.91B, vol $280.68M), pump-fun +1.7% (mcap $796.09M, vol $94.86M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $119.1k | $425.7k | 2.0 d | h24 -37% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $99.0k | $584.9k | 1.5 d | h24 +6744% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [CINU](https://pump.fun/coin/CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump) | `CvXQ9qEriGgTbMWyF8L1U7oqn9ev8A49N1dzNE8cpump` | $51.7k | $321.0k | 7.9 h | h24 +600% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [Thanksgivi](https://dexscreener.com/solana/4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp) | `4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp` | $233.8k | $173.4k | 2.2 h | h24 +237% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $253.4k | $10.95M | 1.2 d | h24 +626% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.3% (+9.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [CYBERLEEK](https://dexscreener.com/solana/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | `ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg` | $299.7k | $1.11M | 103.6 d | h24 -9% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 88h (now 134,788) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.02M | $22.56M | 846.7 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.2% in 69h (now 219,067) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.86M | 183.9 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,841 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $134.1k | $3.09M | +9% | +2738% | +2738% | 22.8x | liq/mcap 4.3%; spike (+9% 1h, +2738% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $60.8k | $576.7k | -7% | +4% | +6648% | 31.1x | churn 31x vol/liq | 52 |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $53.4k | $542.3k | +14% | +1546% | +1546% | 12.3x | spike (+14% 1h, +1546% 6h); lopsided buys/sells 4.88 | not scored |
| [Santaball](https://pump.fun/coin/4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump) | `4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump` | $53.9k | $549.6k | -27% | +1436% | +1436% | 22.5x | spike (-27% 1h, +1436% 6h); lopsided buys/sells 3.39 | not scored |
| [VOLALITY](https://pump.fun/coin/4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump) | `4tPsVjDAqgDjb5TzGazEDMvM2GK2xDvCG2LxpX8opump` | $29.3k | $176.4k | +484% | +484% | +484% | 5.1x | thin liq $29.3k; spike (+484% 1h, +484% 6h); < 1h old | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $35.7k | $229.3k | +20% | +471% | +653% | 31.6x | thin liq $35.7k; churn 32x vol/liq; spike (+20% 1h, +471% 6h) | not scored |

_Timing: total 158s (discovery 71.5s, screen 1.7s, GT prime 0.4s, scoring 84.2s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/164; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
