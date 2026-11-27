# Last scan 2026-11-27T06:07:38Z - mode: helius (box heartbeat stale (124 min); budget 60/3000)

```
[fast_scan] 123 candidate mints from 9 source tags; 120 with pair data; 24 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 71s
[fast_scan] scored MPLX in 78s
[fast_scan] scored SPCX in 78s
[fast_scan] scored ZEC in 79s
[fast_scan] scored Snowball in 79s
[fast_scan] scored PUMPCHAN in 80s
# Market scan 2026-11-27 06:07 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,707 (+1.9% 24h), ETH $1,739 (+3.2% 24h), SOL $73.03 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.4% (mcap $1.92B, vol $283.62M), pump-fun +1.6% (mcap $797.77M, vol $94.48M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $117.3k | $417.5k | 2.1 d | h24 -45% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $109.1k | $650.0k | 1.5 d | h24 +5759% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.8k | $10.38M | 1.2 d | h24 +650% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.96M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,772 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.66M | $18.9k | 407.6 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 396,921) |
| 73* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.04M | $28.67M | 1460.1 d | h24 +21% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,307 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $135.8k | $3.16M | +13% | +2801% | +2801% | 23.0x | liq/mcap 4.3%; spike (+13% 1h, +2801% 6h) | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $67.7k | $852.3k | +58% | +2487% | +2487% | 12.1x | spike (+58% 1h, +2487% 6h); lopsided buys/sells 3.74 | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $64.8k | $650.0k | +10% | +49% | +5759% | 29.6x | churn 30x vol/liq | 52 |
| [BIAO](https://dexscreener.com/solana/CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN) | `CPbeaozeKGXXvjGEoUqTdmnYrH2d48gq17G1sEFJ1iRN` | $126.7k | $152.6k | +148% | +833% | +833% | 60.1x | churn 60x vol/liq; spike (+148% 1h, +833% 6h) | not scored |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $156.8k | $144.2k | +91% | +371% | +371% | 47.2x | churn 47x vol/liq; spike (+91% 1h, +371% 6h) | not scored |
| [NVIDIA](https://pump.fun/coin/C6oCcRXnB6SEp3Pmi9gL8DHVsoEWR9aaZtf9UGj8pump) | `C6oCcRXnB6SEp3Pmi9gL8DHVsoEWR9aaZtf9UGj8pump` | $21.7k | $99.8k | +228% | +228% | +228% | 5.2x | thin liq $21.7k; spike (+228% 1h, +228% 6h); < 1h old | not scored |

_Timing: total 153s (discovery 71.3s, screen 1.4s, GT prime 0.3s, scoring 79.6s for 6 coins, 6 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/127; Helius 429s 71; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
