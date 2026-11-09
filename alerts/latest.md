# Last scan 2026-11-09T20:21:42Z - mode: helius (box heartbeat stale (23 min); budget 140/3000)

```
[fast_scan] 121 candidate mints from 10 source tags; 117 with pair data; 30 >= $50,000 liq; 12 pass survivor pre-gates (73s)
[fast_scan] scored PUSSY in 71s
[fast_scan] scored NVDAx in 80s
[fast_scan] scored DOPE in 80s
[fast_scan] scored HODLER in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored TJR in 81s
[fast_scan] scored CATE in 81s
# Market scan 2026-11-09 20:21 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,905 (-1.2% 24h), ETH $2,131 (-4.3% 24h), SOL $86.88 (-2.7% 24h)
- Fear & Greed: 29 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.2% (mcap $2.50B, vol $432.79M), pump-fun -2.0% (mcap $992.91M, vol $136.03M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $419.8k | $1.61M | 1.0 d | h24 +1139% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | CAUTION | [DOPE](https://dexscreener.com/solana/H5CPUyFcLWRsNKmxnqGBboXErgPv43MUkfTft7nA5BzE) | `H5CPUyFcLWRsNKmxnqGBboXErgPv43MUkfTft7nA5BzE` | $58.9k | $85.6k | 19.6 h | h24 -37% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [TJR](https://dexscreener.com/solana/Hc6295k1Cu9emcLYzMZNZHoqg87CqKXkpPvBMjramk9q) | `Hc6295k1Cu9emcLYzMZNZHoqg87CqKXkpPvBMjramk9q` | $78.2k | $159.3k | 1.3 h | h24 +7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 79* | SKIP | [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $548.4k | $12.35M | 10.7 h | h24 +18992% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.35M | $30.64M | 106.2 d | h24 -7% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders +0.0% in 7h (now 425,991) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $3.97M | $13.48M | 166.5 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders -0.2% in 4h (now 342,351) |
| 82* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $3.67M | $39.16M | 500.4 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.4% in 4h (now 400,690) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODLER](https://pump.fun/coin/8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump) | `8ctbRatrLwS6m35mNajbDimiaM4x7bmfGTprBmZnpump` | $548.2k | $12.35M | +1% | +65% | +18992% | 0.1x | liq/mcap 4.4% | 79 |
| [HWAN](https://dexscreener.com/solana/FNxVZo25dGerP4Tw49f4aHg9xac5qw1FER9F7EzK9cTs) | `FNxVZo25dGerP4Tw49f4aHg9xac5qw1FER9F7EzK9cTs` | $48.1k | $288.5k | +714% | +714% | +714% | 5.6x | thin liq $48.1k; spike (+714% 1h, +714% 6h); < 1h old | not scored |
| [ORBIT](https://pump.fun/coin/6USthxiSZFoCJWhd5bUTcStagAJ2rFd8q8SiF2kupump) | `6USthxiSZFoCJWhd5bUTcStagAJ2rFd8q8SiF2kupump` | $51.1k | $425.8k | +646% | +646% | +646% | 11.8x | spike (+646% 1h, +646% 6h); lopsided buys/sells 3.11; < 1h old | not scored |
| [PUSSY](https://dexscreener.com/solana/FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat) | `FZxHLUGiGchY5uvvoeqh1EKiXTrGdN67WUBhUc1fLoat` | $235.7k | $1.58M | +4% | -19% | +1116% | 45.4x | churn 45x vol/liq | 50 |
| [AMD](https://pump.fun/coin/HjiBij1BcEwjcgPEb22K8y7imdgaf1kHGMHuEgcDpump) | `HjiBij1BcEwjcgPEb22K8y7imdgaf1kHGMHuEgcDpump` | $16.2k | $144.6k | +37% | +145% | +679% | 2.0x | thin liq $16.2k | not scored |
| [USYC](https://dexscreener.com/solana/GhgGZiqphHoFDagvsvggu6AcR3G9mR9xLmYcpjzbh8qf) | `GhgGZiqphHoFDagvsvggu6AcR3G9mR9xLmYcpjzbh8qf` | $19.3k | $10.1k | -55% | -92% | -92% | 17.8x | thin liq $19.3k; dumping -92% 24h | not scored |

_Timing: total 155s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 81.3s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/135; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
