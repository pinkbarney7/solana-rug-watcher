# Last scan 2026-11-19T23:42:46Z - mode: helius (box heartbeat stale (3456 min); budget 40/3000)

```
[fast_scan] 134 candidate mints from 10 source tags; 132 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored Leonida in 69s
[fast_scan] scored VINE in 75s
[fast_scan] scored pippin in 76s
[fast_scan] scored CYBERLEEK in 77s
# Market scan 2026-11-19 23:42 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,771 (-1.8% 24h), ETH $1,748 (-1.5% 24h), SOL $72.91 (-0.8% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.9% (mcap $1.99B, vol $429.13M), pump-fun -0.6% (mcap $817.52M, vol $134.25M)

## Cleanest on real liquidity (younger than 3 days)
Top 1 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 46* | CAUTION | [Leonida](https://pump.fun/coin/9rbKkz2BDQBVgZmrHY6d7PTq2ge91gkpEyE4y9PPpump) | `9rbKkz2BDQBVgZmrHY6d7PTq2ge91gkpEyE4y9PPpump` | $99.0k | $1.61M | 1.9 d | h24 +7% | #3 Liquidity vs market cap WARN (+7); liq/mcap 6.1% (+4.6); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [CYBERLEEK](https://dexscreener.com/solana/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | `ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg` | $377.9k | $1.81M | 96.3 d | h24 +42% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders +0.6% in 29h (now 133,181) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.42M | $8.46M | 666.0 d | h24 +25% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.1% in 6h (now 344,913) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.46M | $18.49M | 740.1 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 6h (now 182,669) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [QUATS](https://pump.fun/coin/Q8epAD6hoSfGTTpHfNKz6z78A3pP8tMkHBAuvYTpump) | `Q8epAD6hoSfGTTpHfNKz6z78A3pP8tMkHBAuvYTpump` | $42.4k | $262.8k | +295% | +4631% | +15478% | 17.6x | thin liq $42.4k; spike (+295% 1h, +4631% 6h) | not scored |
| [FIONA](https://pump.fun/coin/B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump) | `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump` | $100.2k | $1.32M | -16% | +4142% | +4142% | 51.3x | churn 51x vol/liq; spike (-16% 1h, +4142% 6h) | not scored |
| [LOOSY](https://pump.fun/coin/F6tKmax3uQA4MMqzcE2HYEyu379QjCvVSPm9woyspump) | `F6tKmax3uQA4MMqzcE2HYEyu379QjCvVSPm9woyspump` | $52.4k | $538.9k | +1239% | +1239% | +1239% | 4.3x | spike (+1239% 1h, +1239% 6h); lopsided buys/sells 3.32; < 1h old | not scored |
| [AI](https://pump.fun/coin/8SacNb6sgiAcscRe4m915B6nL9XX55dk8FS7L532pump) | `8SacNb6sgiAcscRe4m915B6nL9XX55dk8FS7L532pump` | $64.3k | $399.8k | +252% | +869% | +869% | 20.2x | spike (+252% 1h, +869% 6h) | not scored |
| [OGTA](https://pump.fun/coin/7bCiddGLe5aM8HE2pigT9jsqkmC1HSPxyXN6GkHEpump) | `7bCiddGLe5aM8HE2pigT9jsqkmC1HSPxyXN6GkHEpump` | $72.6k | $927.1k | -8% | +924% | +924% | 29.0x | churn 29x vol/liq; spike (-8% 1h, +924% 6h) | not scored |
| [SIM](https://dexscreener.com/solana/fRxGeXTCXLPQyChrq5sanfUWAe2vseLBiGdDE7k4S1M) | `fRxGeXTCXLPQyChrq5sanfUWAe2vseLBiGdDE7k4S1M` | $22.6k | $102.4k | +9% | +249% | +249% | 8.2x | thin liq $22.6k | not scored |

_Timing: total 151s (discovery 71.4s, screen 1.4s, GT prime 0.4s, scoring 77.4s for 4 coins, 4 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 4/100; Helius 429s 55; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
