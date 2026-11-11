# Last scan 2026-11-11T18:08:51Z - mode: helius (box heartbeat stale (1729 min); budget 10/3000)

```
[fast_scan] 146 candidate mints from 10 source tags; 145 with pair data; 39 >= $50,000 liq; 11 pass survivor pre-gates (65s)
[fast_scan] scored USOE in 73s
[fast_scan] scored Pnut  in 81s
[fast_scan] scored CATE in 81s
[fast_scan] scored USPR in 82s
[fast_scan] scored FOTF in 82s
[fast_scan] scored AODF in 83s
[fast_scan] scored HOLD in 83s
[fast_scan] scored UODF in 83s
[fast_scan] scored FLOAT in 73s
# Market scan 2026-11-11 18:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,410 (+1.7% 24h), ETH $2,089 (+3.0% 24h), SOL $85.24 (+3.7% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins +3.4% (mcap $2.48B, vol $355.01M), pump-fun +6.9% (mcap $995.06M, vol $263.85M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $1.00M | $100.23M | 2.1 d | h24 +44% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.0% (+10.8); #8 Turnover / bot pattern WARN (+4) |
| 68* | SKIP | [HOLD](https://pump.fun/coin/4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump) | `4iJ7xEQrUvVUQH9KVStvw3FaY2PZDd7RtR4L9zx2pump` | $98.2k | $473.1k | 21.2 h | h24 +1300% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 71* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.32M | $173.65M | 2.1 d | h24 +35% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.8% (+11.1) |
| 71* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.32M | $172.58M | 2.1 d | h24 +33% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.8% (+11.1) |
| 71* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $1.11M | $122.84M | 2.2 d | h24 +49% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.9% (+10.9) |
| 71* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $950.2k | $89.79M | 2.1 d | h24 +48% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.1% (+10.7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [FLOAT](https://dexscreener.com/solana/Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr) | `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr` | $1.13M | $10.89M | 13.8 d | h24 +8% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +2.0% in 15h (now 44,372) |
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.23M | $26.69M | 108.1 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 7h (now 427,350) |
| 56* | SKIP | [Pnut ](https://pump.fun/coin/2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump) | `2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump` | $2.47M | $33.15M | 741.2 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 269,294 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WONDER](https://pump.fun/coin/GLQdavjK9HvcuXYHriH1KcqQogGpjubQH8nzVzMPpump) | `GLQdavjK9HvcuXYHriH1KcqQogGpjubQH8nzVzMPpump` | $2.03M | $2.09M | +1620% | +5860% | +5860% | 0.2x | spike (+1620% 1h, +5860% 6h) | not scored |
| [LuckyCoin](https://pump.fun/coin/89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump) | `89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump` | $62.1k | $616.5k | +318% | +1707% | +1707% | 4.5x | spike (+318% 1h, +1707% 6h) | not scored |
| [woohao](https://pump.fun/coin/BLVpn8ofkjnAzpWGaVpspZ5bHTeXDbXFgX4vn3fkpump) | `BLVpn8ofkjnAzpWGaVpspZ5bHTeXDbXFgX4vn3fkpump` | $86.1k | $195.7k | +1081% | +101% | +514% | 8.1x | spike (+1081% 1h, +101% 6h) | not scored |
| [:3](https://pump.fun/coin/FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump) | `FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump` | $20.5k | $68.1k | -39% | +19% | +2704% | 23.8x | thin liq $20.5k | not scored |
| [DACITY](https://pump.fun/coin/5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump) | `5tBXkPVh716zSXHNZSr8i1PX7e6Uuj46JnBLdYchpump` | $69.9k | $726.4k | +176% | -70% | +1652% | 45.8x | churn 46x vol/liq; spike (+176% 1h, -70% 6h) | not scored |
| [CHICAT](https://pump.fun/coin/GYiLFfHeTgXiK5BKpHN6fvv68R6DKwK5rh3SGPvapump) | `GYiLFfHeTgXiK5BKpHN6fvv68R6DKwK5rh3SGPvapump` | $33.5k | $198.1k | +363% | +363% | +363% | 7.2x | thin liq $33.5k; spike (+363% 1h, +363% 6h); lopsided buys/sells 3.84; < 1h old | not scored |

_Timing: total 211s (discovery 63.3s, screen 1.4s, GT prime 0.8s, scoring 145.9s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/164; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
