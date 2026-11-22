# Last scan 2026-11-22T17:06:31Z - mode: helius (box heartbeat stale (7380 min); budget 30/3000)

```
[fast_scan] 114 candidate mints from 10 source tags; 111 with pair data; 26 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored FIONA in 74s
[fast_scan] scored PushCoin in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored Singularity in 82s
[fast_scan] scored AODT in 83s
[fast_scan] scored VINE in 83s
[fast_scan] scored TROLL in 83s
[fast_scan] scored ROCKET in 84s
# Market scan 2026-11-22 17:06 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,144 (+1.7% 24h), ETH $1,720 (+2.1% 24h), SOL $70.54 (-0.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.2% (mcap $1.87B, vol $273.78M), pump-fun +3.0% (mcap $792.98M, vol $112.53M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.9k | $818.8k | 1.2 d | h24 -0% | #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $149.3k | $946.3k | 1.9 d | h24 +91% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 43* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $204.9k | $1.67M | 4.9 d | h24 +117% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 59* | SKIP | [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $90.8k | $1.54M | 15.2 h | h24 +4307% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 64* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $102.0k | $2.14M | 1.7 d | h24 +56% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 4.8% (+6.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.45M | $8.92M | 668.7 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 345,123) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.97M | $22.21M | 842.2 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 218,572) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $13.20M | 179.4 d | h24 -0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 1h (now 386,720) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $90.8k | $1.54M | +8% | +46% | +4307% | 18.0x | none flagged (still high risk) | 59 |
| [MCAT](https://pump.fun/coin/v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump) | `v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump` | $33.5k | $189.3k | +23% | +544% | +544% | 42.4x | thin liq $33.5k; churn 42x vol/liq; spike (+23% 1h, +544% 6h) | not scored |
| [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $44.7k | $65.4k | +42% | +322% | +322% | 6.8x | thin liq $44.7k; spike (+42% 1h, +322% 6h) | not scored |
| [snowball](https://pump.fun/coin/3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump) | `3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump` | $38.0k | $220.1k | -30% | -35% | +692% | 66.2x | thin liq $38.0k; churn 66x vol/liq | not scored |
| [casual](https://pump.fun/coin/6EiCk8WmoLai1ziCHa8D2aujGdB7rYr3xGs3x2avpump) | `6EiCk8WmoLai1ziCHa8D2aujGdB7rYr3xGs3x2avpump` | $14.4k | $45.7k | +78% | +175% | +66% | 14.5x | thin liq $14.4k | not scored |
| [FOAM](https://pump.fun/coin/2MdCPWNFufmJSZhajSvi1yqBFTB24GQ4ipjNcB8Vpump) | `2MdCPWNFufmJSZhajSvi1yqBFTB24GQ4ipjNcB8Vpump` | $16.6k | $60.4k | +106% | +106% | +106% | 10.1x | thin liq $16.6k; spike (+106% 1h, +106% 6h); < 1h old | not scored |

_Timing: total 157s (discovery 71.4s, screen 1.2s, GT prime 0.3s, scoring 84.2s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/168; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
