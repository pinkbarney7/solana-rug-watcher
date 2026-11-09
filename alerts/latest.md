# Last scan 2026-11-09T20:59:52Z - mode: helius (box heartbeat stale (21 min); budget 150/3000)

```
[fast_scan] 124 candidate mints from 9 source tags; 120 with pair data; 31 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored HODLER in 71s
[fast_scan] scored NVDAx in 79s
[fast_scan] scored CATE in 80s
[fast_scan] scored TJR in 81s
[fast_scan] scored Pepetide in 81s
[fast_scan] scored PUSSY in 81s
[fast_scan] scored SPCX in 81s
# Market scan 2026-11-09 20:59 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,791 (-1.2% 24h), ETH $2,130 (-4.3% 24h), SOL $86.72 (-2.7% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.0% (mcap $2.49B, vol $426.13M), pump-fun -1.6% (mcap $990.55M, vol $134.96M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $376.6k | $1.38M | 1.0 d | h24 -7% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [Pepetide](https://dexscreener.com/solana/22JKmY9YZfnQfb3pGYb6hctL5Jyvv3zhL3nQ8oyNuoYp) | `22JKmY9YZfnQfb3pGYb6hctL5Jyvv3zhL3nQ8oyNuoYp` | $248.7k | $635.1k | 1.9 d | h24 +175% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 62* | SKIP | [TJR](https://dexscreener.com/solana/Hc6295k1Cu9emcLYzMZNZHoqg87CqKXkpPvBMjramk9q) | `Hc6295k1Cu9emcLYzMZNZHoqg87CqKXkpPvBMjramk9q` | $69.3k | $129.7k | 2.0 h | h24 -13% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 70* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $554.6k | $12.97M | 11.4 h | h24 +19951% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.3% (+6.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.35M | $30.75M | 106.2 d | h24 -3% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders +0.0% in 1h (now 426,011) |
| 75* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.70M | $39.42M | 500.4 d | h24 -2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 400,574) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $3.96M | $13.63M | 166.5 d | h24 +5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.2% in 1h (now 343,068) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $554.4k | $12.97M | +6% | +34% | +19951% | 0.1x | liq/mcap 4.3% | 70 |
| [MAYA](https://pump.fun/coin/HqZZhbXWm17vnY29uj4cgczNUWo9o8VLUWsN4RH8pump) | `HqZZhbXWm17vnY29uj4cgczNUWo9o8VLUWsN4RH8pump` | $72.9k | $876.2k | +1916% | +1916% | +1916% | 5.0x | spike (+1916% 1h, +1916% 6h); lopsided buys/sells 3.54; < 1h old | not scored |
| [HWAN](https://dexscreener.com/solana/FNxVZo25dGerP4Tw49f4aHg9xac5qw1FER9F7EzK9cTs) | `FNxVZo25dGerP4Tw49f4aHg9xac5qw1FER9F7EzK9cTs` | $48.3k | $215.3k | +508% | +508% | +508% | 10.6x | thin liq $48.3k; spike (+508% 1h, +508% 6h); < 1h old | not scored |
| [ORBIT](https://pump.fun/coin/6USthxiSZFoCJWhd5bUTcStagAJ2rFd8q8SiF2kupump) | `6USthxiSZFoCJWhd5bUTcStagAJ2rFd8q8SiF2kupump` | $56.7k | $520.3k | +71% | +812% | +812% | 11.2x | spike (+71% 1h, +812% 6h) | not scored |
| [CAT](https://pump.fun/coin/2HbbwKyQqRE2mhhPXd48ehYpGQufY2xGe5vTQaZTpump) | `2HbbwKyQqRE2mhhPXd48ehYpGQufY2xGe5vTQaZTpump` | $24.7k | $107.4k | +155% | +155% | +155% | 9.6x | thin liq $24.7k; spike (+155% 1h, +155% 6h); lopsided buys/sells 6.08; < 1h old | not scored |
| [AMD](https://pump.fun/coin/HjiBij1BcEwjcgPEb22K8y7imdgaf1kHGMHuEgcDpump) | `HjiBij1BcEwjcgPEb22K8y7imdgaf1kHGMHuEgcDpump` | $12.4k | $114.3k | -9% | +80% | +512% | 2.6x | thin liq $12.4k | not scored |

_Timing: total 154s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 81.0s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/136; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
