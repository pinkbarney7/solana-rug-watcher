# Last scan 2026-11-27T06:32:51Z - mode: helius (box heartbeat stale (150 min); budget 90/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 116 with pair data; 22 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored SPCX in 69s
[fast_scan] scored PUMPCHAN in 77s
[fast_scan] scored Snowball in 77s
[fast_scan] scored MPLX in 78s
[fast_scan] scored ZEC in 78s
# Market scan 2026-11-27 06:32 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,635 (+1.9% 24h), ETH $1,734 (+2.8% 24h), SOL $72.92 (+3.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.7% (mcap $1.93B, vol $281.49M), pump-fun +1.8% (mcap $798.81M, vol $90.88M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $104.3k | $599.0k | 1.5 d | h24 +3107% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 65* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.6k | $10.36M | 1.2 d | h24 +653% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.4% (+9.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.60M | $13.96M | 183.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 400,772 (growth n/a: first sighting) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.62M | $18.7k | 407.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 396,914 (growth n/a: first sighting) |
| 73* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.01M | $27.64M | 1460.2 d | h24 +17% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders 91,308 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $135.8k | $3.16M | +3% | +2801% | +2801% | 23.2x | liq/mcap 4.3%; spike (+3% 1h, +2801% 6h) | not scored |
| [SpaceXCoin](https://pump.fun/coin/G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump) | `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump` | $70.9k | $930.7k | +14% | +2725% | +2725% | 12.3x | spike (+14% 1h, +2725% 6h); lopsided buys/sells 3.18 | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $62.3k | $602.4k | +2% | +16% | +3371% | 31.1x | churn 31x vol/liq | 52 |
| [PNP](https://dexscreener.com/solana/7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc) | `7KDhKE8SQmGUR6wAp8HJYwBs4S8N9TJ9x7k7AfAQqyjc` | $180.3k | $179.4k | +74% | +487% | +487% | 52.6x | churn 53x vol/liq; spike (+74% 1h, +487% 6h) | not scored |
| [DEXDATA](https://pump.fun/coin/63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump) | `63jDWWFwp25ChLvsofbVRMprRbhiXuWoWVxrwFfypump` | $35.2k | $223.0k | -16% | +138% | +632% | 33.2x | thin liq $35.2k; churn 33x vol/liq | not scored |
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $247.7k | $10.36M | -10% | +15% | +664% | 20.7x | liq/mcap 2.4% | 65 |

_Timing: total 151s (discovery 71.5s, screen 1.2s, GT prime 0.3s, scoring 78.0s for 5 coins, 5 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/105; Helius 429s 65; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
