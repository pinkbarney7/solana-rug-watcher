# Last scan 2026-11-15T12:26:52Z - mode: helius (box heartbeat stale (7148 min); budget 20/3000)

```
[fast_scan] 133 candidate mints from 10 source tags; 133 with pair data; 23 >= $50,000 liq; 7 pass survivor pre-gates (73s)
[fast_scan] scored GETAJOB in 74s
[fast_scan] scored bill in 80s
[fast_scan] scored bill in 81s
[fast_scan] scored DacityCoin in 81s
[fast_scan] scored WANTED in 82s
[fast_scan] scored TTWO in 82s
[fast_scan] scored CATE in 83s
[fast_scan] scored fone in 84s
# Market scan 2026-11-15 12:26 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $65,394 (-2.5% 24h), ETH $1,830 (-3.9% 24h), SOL $72.57 (-4.1% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -6.1% (mcap $2.10B, vol $565.73M), pump-fun -1.7% (mcap $891.42M, vol $146.06M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | CAUTION | [GETAJOB](https://pump.fun/coin/ZGW9B644VgfmmKtBTv1xjWGarkjEhFrcUrQEaqepump) | `ZGW9B644VgfmmKtBTv1xjWGarkjEhFrcUrQEaqepump` | $62.9k | $736.3k | 21.1 h | h24 +496% | #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 53* | SKIP | [bill](https://dexscreener.com/solana/B363HkenheRKssXjM8eEW2T6wS2FwrkH4Pgn9ZNyUWW) | `B363HkenheRKssXjM8eEW2T6wS2FwrkH4Pgn9ZNyUWW` | $158.4k | $97.9k | 1.8 h | h24 +112% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [DacityCoin](https://dexscreener.com/solana/9TjNE2HmETBq4fAh9GZAy6LjPPadQBXuEFasCpMmsim) | `9TjNE2HmETBq4fAh9GZAy6LjPPadQBXuEFasCpMmsim` | $229.4k | $135.8k | 5.9 h | h24 +101% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $136.2k | $587.3k | 16.7 h | h24 +923% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [WANTED](https://pump.fun/coin/CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump) | `CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump` | $63.5k | $751.8k | 10.6 h | h24 +1918% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [fone](https://pump.fun/coin/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | `CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump` | $218.7k | $989.9k | 80.5 d | h24 -6% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 101,854 (growth n/a: first sighting) |
| 45* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.71M | $16.75M | 111.8 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 5h (now 429,387) |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.03M | $99 | 104.5 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +0.9% in 5h (now 259,952) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Socks](https://pump.fun/coin/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump) | `FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump` | $41.5k | $292.0k | -38% | +901% | +901% | 34.0x | thin liq $41.5k; churn 34x vol/liq; spike (-38% 1h, +901% 6h) | not scored |
| [WANTED](https://pump.fun/coin/CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump) | `CiMyaPC9icicJxkFqvqpgL2YT2FjEQmGx1YVdG78pump` | $63.7k | $755.8k | -17% | -49% | +1929% | 20.2x | none flagged (still high risk) | 58 |
| [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $87.0k | $587.3k | +19% | -28% | +923% | 50.3x | churn 50x vol/liq | 55 |
| [GETAJOB](https://pump.fun/coin/ZGW9B644VgfmmKtBTv1xjWGarkjEhFrcUrQEaqepump) | `ZGW9B644VgfmmKtBTv1xjWGarkjEhFrcUrQEaqepump` | $62.9k | $736.3k | +90% | +37% | +496% | 14.5x | none flagged (still high risk) | 52 |
| [DOJE](https://pump.fun/coin/7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump) | `7N2g5tHX2isAXyKmtUek72waREtNKSFuR6KW2xthpump` | $28.6k | $156.6k | -57% | -58% | +365% | 28.6x | thin liq $28.6k; churn 29x vol/liq | not scored |
| [FUTA](https://pump.fun/coin/8JCsa61htnPj2af7g1KSyU1UEncruHE1Ph9aNR6rpump) | `8JCsa61htnPj2af7g1KSyU1UEncruHE1Ph9aNR6rpump` | $25.7k | $123.0k | -7% | +20% | +590% | 5.4x | thin liq $25.7k | not scored |

_Timing: total 157s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 84.0s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/164; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
