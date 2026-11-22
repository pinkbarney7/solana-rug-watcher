# Last scan 2026-11-22T15:39:40Z - mode: helius (box heartbeat stale (7293 min); budget 20/3000)

```
[fast_scan] 117 candidate mints from 10 source tags; 114 with pair data; 28 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored AODT in 72s
[fast_scan] scored Singularity in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored PushCoin in 81s
[fast_scan] scored TROLL in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored ROCKET in 85s
[fast_scan] scored FIONA in 86s
# Market scan 2026-11-22 15:39 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,756 (+1.5% 24h), ETH $1,715 (+2.1% 24h), SOL $70.19 (-0.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +0.6% (mcap $1.86B, vol $284.08M), pump-fun +4.0% (mcap $799.54M, vol $120.60M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $78.8k | $780.0k | 1.2 d | h24 +356% | #9 Price momentum WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $201.0k | $1.52M | 4.9 d | h24 +66% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $158.5k | $1.21M | 1.8 d | h24 +1482% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $83.4k | $1.32M | 13.7 h | h24 +3666% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 64* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $100.1k | $2.07M | 1.6 d | h24 +56% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 4.8% (+6.2) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $9.05M | 668.6 d | h24 -12% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.1% in 7h (now 345,127) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.96M | $21.95M | 842.2 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.1% in 7h (now 218,580) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.22M | $13.21M | 179.3 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.3% in 14h (now 386,755) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JAGENT](https://dexscreener.com/solana/HjjvrRzP4KmQxhi8s1MWn2pyCRaP7QfyMQzkXo3U3u1B) | `HjjvrRzP4KmQxhi8s1MWn2pyCRaP7QfyMQzkXo3U3u1B` | $140.8k | $347.1k | +257% | +4184% | +4184% | 86.8x | churn 87x vol/liq; spike (+257% 1h, +4184% 6h) | not scored |
| [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $83.4k | $1.32M | -18% | +13% | +3666% | 18.8x | none flagged (still high risk) | 59 |
| [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $97.5k | $1.21M | +14% | +124% | +1482% | 34.8x | churn 35x vol/liq | 52 |
| [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $47.4k | $74.9k | +166% | +383% | +383% | 5.0x | thin liq $47.4k; spike (+166% 1h, +383% 6h) | not scored |
| [MCAT](https://pump.fun/coin/v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump) | `v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump` | $31.2k | $170.4k | +28% | +480% | +480% | 39.2x | thin liq $31.2k; churn 39x vol/liq; spike (+28% 1h, +480% 6h) | not scored |
| [snowball](https://pump.fun/coin/3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump) | `3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump` | $43.1k | $285.1k | -6% | -25% | +925% | 56.1x | thin liq $43.1k; churn 56x vol/liq | not scored |

_Timing: total 159s (discovery 71.4s, screen 1.2s, GT prime 0.5s, scoring 85.8s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/163; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
