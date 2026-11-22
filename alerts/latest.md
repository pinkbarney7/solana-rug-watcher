# Last scan 2026-11-22T09:08:30Z - mode: helius (box heartbeat stale (6901 min); budget 0/3000)

```
[fast_scan] 119 candidate mints from 10 source tags; 116 with pair data; 29 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored GTACAT in 72s
[fast_scan] scored ZEC in 81s
[fast_scan] scored Singularity in 81s
[fast_scan] scored FIONA in 82s
[fast_scan] scored AODT in 82s
[fast_scan] scored ROCKET in 82s
[fast_scan] scored PushCoin in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored TROLL in 71s
# Market scan 2026-11-22 09:08 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,692 (+3.3% 24h), ETH $1,684 (+3.4% 24h), SOL $69.75 (+3.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.0% (mcap $1.84B, vol $305.54M), pump-fun +4.7% (mcap $772.13M, vol $122.63M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $206.6k | $1.55M | 4.6 d | h24 +90% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 52* | SKIP | [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $89.3k | $554.3k | 1.5 d | h24 +723% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [GTACAT](https://dexscreener.com/solana/3aoVzicyutREo1eJHexyQwa7ZjNnNy6EBNyqwEQo6p7J) | `3aoVzicyutREo1eJHexyQwa7ZjNnNy6EBNyqwEQo6p7J` | $220.7k | $126.5k | 2.2 h | h24 +65% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 54* | SKIP | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $81.7k | $842.2k | 21.4 h | h24 +1710% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 58* | SKIP | [AODT](https://pump.fun/coin/2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump) | `2wh7dPQV4w1tgVQzYzJB683fqxcTkU4A8WeaoNZJpump` | $93.9k | $1.84M | 1.3 d | h24 +66% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.9) |
| 60* | SKIP | [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $91.1k | $1.63M | 7.2 h | h24 +4540% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.6% (+5.3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.46M | $9.04M | 668.4 d | h24 +30% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 345,361) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $1.92M | $21.20M | 841.9 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 123h (now 218,694) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.19M | $19.6k | 402.7 d | h24 +9% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 24h (now 393,831) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [snowball](https://pump.fun/coin/3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump) | `3D7YQcnXi6RMjWxheiE8VLuGXJTtgQkmyugGYvzjpump` | $57.6k | $541.3k | +82% | +1847% | +1847% | 26.1x | churn 26x vol/liq; spike (+82% 1h, +1847% 6h) | not scored |
| [PushCoin](https://pump.fun/coin/3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump) | `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump` | $90.7k | $1.61M | -0% | +7% | +4499% | 10.7x | none flagged (still high risk) | 60 |
| [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $80.7k | $821.1k | -0% | +0% | +1665% | 2.6x | none flagged (still high risk) | 54 |
| [Singularity](https://pump.fun/coin/7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump) | `7R4MP6VX7n3RMNhL9zsk5Zu5ibZvwq8npUYnRq7epump` | $63.3k | $540.2k | -7% | +32% | +702% | 42.7x | churn 43x vol/liq | 52 |
| [FIREBALL](https://pump.fun/coin/5o7AFuoNWsy7gQS85ospXhWFJRnxDwTtwTR3JF2Jpump) | `5o7AFuoNWsy7gQS85ospXhWFJRnxDwTtwTR3JF2Jpump` | $13.4k | $40.1k | +157% | +50% | +50% | 8.9x | thin liq $13.4k; spike (+157% 1h, +50% 6h) | not scored |
| [BLOB](https://pump.fun/coin/8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump) | `8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump` | $323.4k | $13.05M | +44% | +110% | +133% | 3.0x | liq/mcap 2.5% | not scored |

_Timing: total 216s (discovery 70.8s, screen 1.1s, GT prime 0.4s, scoring 143.5s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/174; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
