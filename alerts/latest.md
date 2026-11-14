# Last scan 2026-11-14T20:20:45Z - mode: helius (box heartbeat stale (6182 min); budget 30/3000)

```
[fast_scan] 131 candidate mints from 10 source tags; 131 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored USPR in 78s
[fast_scan] scored UODF in 87s
[fast_scan] scored TTWO in 88s
[fast_scan] scored CATE in 89s
[fast_scan] scored SPCX in 89s
[fast_scan] scored Max in 89s
[fast_scan] scored XTO in 89s
[fast_scan] scored JENSEN in 90s
# Market scan 2026-11-14 20:20 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $65,498 (-5.1% 24h), ETH $1,826 (-6.5% 24h), SOL $71.83 (-10.6% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -12.9% (mcap $2.05B, vol $421.88M), pump-fun -6.8% (mcap $857.34M, vol $115.32M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $214.9k | $1.38M | 3.0 d | h24 -32% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JENSEN](https://pump.fun/coin/B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump) | `B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump` | $55.2k | $525.9k | 19.4 h | h24 +494% | #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $1.02M | $207.90M | 2.3 d | h24 +6% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.5% (+11.4); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [UODF](https://pump.fun/coin/39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump) | `39rS82a9nNnBuDdoJHGFti2CHQaZvLtauQzzUkERpump` | $959.1k | $181.68M | 1.3 d | h24 +117% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 75* | SKIP | [USPR](https://pump.fun/coin/4B71G7FRC6v2DjJW8rQB62ewJ8Kv8vh5KV6oV4fRpump) | `4B71G7FRC6v2DjJW8rQB62ewJ8Kv8vh5KV6oV4fRpump` | $897.4k | $159.67M | 16.2 h | h24 +511300% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.63M | $15.79M | 111.2 d | h24 -15% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 4h (now 429,033) |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.35M | $98 | 103.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.4% in 4h (now 255,890) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.19M | $12.68M | 171.5 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.9% in 11h (now 364,064) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [USPR](https://pump.fun/coin/4B71G7FRC6v2DjJW8rQB62ewJ8Kv8vh5KV6oV4fRpump) | `4B71G7FRC6v2DjJW8rQB62ewJ8Kv8vh5KV6oV4fRpump` | $897.5k | $159.71M | +3% | +30% | +511428% | 0.6x | liq/mcap 0.6%; lopsided buys/sells 197.39 | 75 |
| [DOGCOIN](https://pump.fun/coin/46sup1Mc1AdQPpikrdNLUjmzSgZcEYdV3pk8XPPXpump) | `46sup1Mc1AdQPpikrdNLUjmzSgZcEYdV3pk8XPPXpump` | $24.8k | $118.3k | +277% | +334% | +334% | 15.3x | thin liq $24.8k; spike (+277% 1h, +334% 6h) | not scored |
| [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $46.1k | $217.0k | +266% | +266% | +266% | 13.0x | thin liq $46.1k; spike (+266% 1h, +266% 6h); < 1h old | not scored |
| [elchef](https://pump.fun/coin/3VkUe5T9uAuU6EqmEMqQcuTRqEcqU86NAfwbFZKxpump) | `3VkUe5T9uAuU6EqmEMqQcuTRqEcqU86NAfwbFZKxpump` | $34.5k | $141.6k | -30% | +261% | +358% | 14.6x | thin liq $34.5k | not scored |
| [kibble](https://pump.fun/coin/BtB54BEhTsx8syvWFUcMEe6vxASyL9zP7feXY5d1pump) | `BtB54BEhTsx8syvWFUcMEe6vxASyL9zP7feXY5d1pump` | $16.8k | $58.0k | +119% | +113% | +113% | 16.1x | thin liq $16.8k; spike (+119% 1h, +113% 6h) | not scored |
| [JENSEN](https://pump.fun/coin/B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump) | `B2YpP21vQBESJ2jtnuhPujEUT61KVRxZ2X5gsDcUpump` | $55.2k | $525.9k | +33% | -19% | +494% | 46.8x | churn 47x vol/liq | 45 |

_Timing: total 163s (discovery 71.3s, screen 1.3s, GT prime 0.5s, scoring 89.6s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/164; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
