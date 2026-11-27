# Last scan 2026-11-27T04:29:16Z - mode: helius (box heartbeat stale (26 min); budget 467/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 118 with pair data; 26 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 79s
[fast_scan] scored CATE in 86s
[fast_scan] scored PUMPCHAN in 86s
[fast_scan] scored Thanksgivi in 87s
[fast_scan] scored Snowball in 87s
[fast_scan] scored SPCX in 88s
[fast_scan] scored Rizzmas in 89s
# Market scan 2026-11-27 04:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,448 (+0.8% 24h), ETH $1,730 (+1.7% 24h), SOL $72.74 (+2.2% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.6% (mcap $1.91B, vol $279.02M), pump-fun +1.7% (mcap $796.02M, vol $93.48M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $116.9k | $411.4k | 2.0 d | h24 -41% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $95.7k | $614.4k | 1.4 d | h24 +6620% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [Thanksgivi](https://dexscreener.com/solana/4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp) | `4szpC6VF7muZ5rjgxxAjV6r3hQb4BgHPAcJbykjsUGfp` | $216.1k | $163.5k | 1.6 h | h24 +218% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $250.7k | $10.73M | 1.1 d | h24 +717% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.3% (+9.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $232.8k | $699.7k | 1068.4 d | h24 +50% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 1h (now 395,700) |
| 64* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $11.38M | $171.31B | 123.5 d | h24 +2% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.0% (+12); GATES FAILED: rug-funder link; holders +0.3% in 38h (now 438,232) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.59M | $13.87M | 183.9 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.0% in 1h (now 400,869) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $125.6k | $2.72M | -6% | +2400% | +2400% | 24.0x | liq/mcap 4.6%; spike (-6% 1h, +2400% 6h) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $62.7k | $614.4k | -19% | +0% | +6620% | 29.7x | churn 30x vol/liq | 52 |
| [Santaball](https://pump.fun/coin/4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump) | `4obGGXRMVyqpWZr12UzyaBdNkgdYwz2GiY8enmd2pump` | $64.8k | $794.6k | -25% | +2120% | +2120% | 17.5x | spike (-25% 1h, +2120% 6h); lopsided buys/sells 3.72 | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $55.6k | $590.4k | +45% | +1692% | +1692% | 10.9x | spike (+45% 1h, +1692% 6h); lopsided buys/sells 5.55 | not scored |
| [LUMINARE](https://pump.fun/coin/EomygbXHKGwb9bkCatVftQpCVgvBPmgAnMUuwusxpump) | `EomygbXHKGwb9bkCatVftQpCVgvBPmgAnMUuwusxpump` | $23.6k | $116.4k | +285% | +285% | +285% | 9.1x | thin liq $23.6k; spike (+285% 1h, +285% 6h); < 1h old | not scored |
| [LEVER](https://pump.fun/coin/52a6B3qpwGN9daQBTu8kvbXQVgThuiGMJE1mmCEgpump) | `52a6B3qpwGN9daQBTu8kvbXQVgThuiGMJE1mmCEgpump` | $21.4k | $96.8k | +166% | +461% | +229% | 11.6x | thin liq $21.4k; spike (+166% 1h, +461% 6h) | not scored |

_Timing: total 163s (discovery 71.7s, screen 1.6s, GT prime 0.5s, scoring 89.3s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/148; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
