# Last scan 2026-11-25T05:44:37Z - mode: helius (box heartbeat stale (111 min); budget 30/3000)

```
[fast_scan] 122 candidate mints from 9 source tags; 116 with pair data; 24 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored 4CHAN in 70s
[fast_scan] scored SPCX in 79s
[fast_scan] scored pippin in 79s
[fast_scan] scored MCAT in 80s
[fast_scan] scored CATE in 82s
[fast_scan] scored JIMMY in 83s
# Market scan 2026-11-25 05:44 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,975 (-2.8% 24h), ETH $1,653 (-3.2% 24h), SOL $68.38 (-4.9% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.7% (mcap $1.79B, vol $322.80M), pump-fun -6.2% (mcap $761.85M, vol $138.00M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $57.6k | $112.3k | 2.7 d | h24 -31% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 44* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $246.9k | $1.55M | 1.4 d | h24 +395% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $193.6k | $719.5k | 7.8 h | h24 +2527% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | CAUTION | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.56M | $16.48M | 121.5 d | h24 -5% | #3 Liquidity vs market cap WARN (+7); #6 unknown (+3); #7 unknown (+3); GATES FAILED: rug-funder link |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.39M | $18.62M | 745.4 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,577 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $12.97M | 181.9 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,170 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $73.3k | $1.04M | -10% | +2616% | +2616% | 21.3x | spike (-10% 1h, +2616% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $76.7k | $1.17M | +2% | +500% | +3594% | 8.9x | spike (+2% 1h, +500% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $102.0k | $421.1k | +501% | +501% | +501% | 9.6x | spike (+501% 1h, +501% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $68.3k | $719.5k | -46% | +193% | +2527% | 52.3x | churn 52x vol/liq | 56 |
| [GRAUDIA](https://pump.fun/coin/4V7zqQMRCiiMN9RodQ8nQQYFPBK8QnyyEq15zunepump) | `4V7zqQMRCiiMN9RodQ8nQQYFPBK8QnyyEq15zunepump` | $22.9k | $119.2k | +248% | +248% | +248% | 0.9x | thin liq $22.9k; spike (+248% 1h, +248% 6h); lopsided buys/sells 3.17; < 1h old | not scored |
| [TIKTOK](https://dexscreener.com/solana/BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57) | `BNidyMmNZgae6FtjGgHzr7UJN6F6x612u65XgCbwjk57` | $148.8k | $200.2k | +153% | +301% | +301% | 70.8x | churn 71x vol/liq; spike (+153% 1h, +301% 6h) | not scored |

_Timing: total 156s (discovery 71.7s, screen 1.4s, GT prime 0.4s, scoring 82.5s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/135; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
