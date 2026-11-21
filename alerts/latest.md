# Last scan 2026-11-21T22:01:15Z - mode: helius (box heartbeat stale (6234 min); budget 20/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 125 with pair data; 31 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored CoT in 78s
[fast_scan] scored PUNANI in 87s
[fast_scan] scored AODT in 87s
[fast_scan] scored pippin in 88s
[fast_scan] scored VINE in 89s
[fast_scan] scored FIONA in 90s
[fast_scan] scored MAYA in 93s
[fast_scan] scored Singularit in 95s
[fast_scan] scored SPCX in 72s
# Market scan 2026-11-21 22:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,359 (+2.5% 24h), ETH $1,685 (+4.3% 24h), SOL $70.32 (+2.1% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.1% (mcap $1.84B, vol $379.29M), pump-fun -0.4% (mcap $776.82M, vol $132.98M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 43* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $171.6k | $1.25M | 4.1 d | h24 +2% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 56* | SKIP | [Singularit](https://dexscreener.com/solana/8Q14yJbbwzK9NsvFTucUF38qBu51cutGJg6fmLXGkG8A) | `8Q14yJbbwzK9NsvFTucUF38qBu51cutGJg6fmLXGkG8A` | $217.6k | $144.9k | 2.9 h | h24 +210% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 57* | SKIP | [CoT](https://dexscreener.com/solana/5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW) | `5kqi4kDq56H9UfHq14jXtmy189zpyxaYdXCQ4qHvDtHW` | $91.1k | $1.93M | 1.0 d | h24 +87% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.7% (+6.3); #6 Top-10 holders (excl. pools/programs) WARN (+4) |
| 57* | SKIP | [PUNANI](https://pump.fun/coin/2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump) | `2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump` | $61.3k | $692.8k | 17.6 h | h24 +2033% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [MAYA](https://pump.fun/coin/FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump) | `FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump` | $70.6k | $947.8k | 16.9 h | h24 +2516% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $85.1k | $1.50M | 20.6 h | h24 +5164% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.49M | $9.41M | 667.9 d | h24 +23% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 5h (now 345,261) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.28M | $17.04M | 742.1 d | h24 -7% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 5h (now 182,896) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.21M | $13.13M | 178.6 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.4% in 5h (now 384,979) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [HODL](https://pump.fun/coin/14coJKKEShg6ZaSKggQjubtKsCjWUZBWRa2v3E5ypump) | `14coJKKEShg6ZaSKggQjubtKsCjWUZBWRa2v3E5ypump` | $29.1k | $161.6k | +103% | +2138% | +2138% | 5.2x | thin liq $29.1k; spike (+103% 1h, +2138% 6h) | not scored |
| [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $85.1k | $1.50M | +2% | +12% | +5165% | 0.4x | lopsided buys/sells 1056.58 | 68 |
| [UrAnus](https://pump.fun/coin/27u3diWofnXGUkddjLGhcy1nRssFKHW3RtNbpWzUpump) | `27u3diWofnXGUkddjLGhcy1nRssFKHW3RtNbpWzUpump` | $39.4k | $318.6k | +726% | +726% | +726% | 6.9x | thin liq $39.4k; spike (+726% 1h, +726% 6h); lopsided buys/sells 6.99; < 1h old | not scored |
| [FINGERS](https://pump.fun/coin/BSF5xg7CuxkQWsbJWyHYw2HnuNbQtKybGaNhz9cCpump) | `BSF5xg7CuxkQWsbJWyHYw2HnuNbQtKybGaNhz9cCpump` | $34.7k | $250.9k | +710% | +710% | +710% | 5.7x | thin liq $34.7k; spike (+710% 1h, +710% 6h); lopsided buys/sells 5.30; < 1h old | not scored |
| [MAYA](https://pump.fun/coin/FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump) | `FJKt1LxbWBpTRt9BaDEB6Wr2qL5LZzjFF5sx8rXnpump` | $70.5k | $946.5k | -41% | -72% | +2512% | 28.0x | churn 28x vol/liq | 58 |
| [PUNANI](https://pump.fun/coin/2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump) | `2TngN4B7XaoGSKsYvttq5bFAdM4Z4xCSnuyRwGiFpump` | $61.4k | $695.6k | -32% | -62% | +2041% | 41.5x | churn 42x vol/liq | 57 |

_Timing: total 223s (discovery 71.3s, screen 1.4s, GT prime 0.4s, scoring 149.8s for 9 coins, 9 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/175; Helius 429s 105; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
