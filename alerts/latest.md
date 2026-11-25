# Last scan 2026-11-25T06:46:46Z - mode: helius (box heartbeat stale (173 min); budget 40/3000)

```
[fast_scan] 125 candidate mints from 10 source tags; 121 with pair data; 29 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored 4CHAN in 72s
[fast_scan] scored pippin in 80s
[fast_scan] scored CATE in 81s
[fast_scan] scored CHUCK in 82s
[fast_scan] scored KOOP in 82s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored VINE in 83s
[fast_scan] scored MCAT in 84s
# Market scan 2026-11-25 06:46 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,127 (-2.2% 24h), ETH $1,657 (-2.5% 24h), SOL $68.68 (-4.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.2% (mcap $1.80B, vol $310.82M), pump-fun -6.3% (mcap $760.97M, vol $138.56M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $54.4k | $99.1k | 2.7 d | h24 -38% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $232.0k | $1.26M | 1.4 d | h24 +294% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $225.3k | $130.4k | 2.5 h | h24 +70% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $158.9k | $182.3k | 1.9 h | h24 +269% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |
| 69* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $151.8k | $563.0k | 8.9 h | h24 +1955% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.69M | 671.3 d | h24 +10% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 345,014 (growth n/a: first sighting) |
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.58M | $16.58M | 121.6 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders -0.0% in 1h (now 436,948) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.42M | $18.87M | 745.4 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,578 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $89.6k | $1.52M | +49% | +786% | +3900% | 18.4x | spike (+49% 1h, +786% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $83.4k | $1.36M | +18% | +472% | +4200% | 9.5x | spike (+18% 1h, +472% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $60.8k | $563.0k | -22% | +110% | +1955% | 61.5x | churn 61x vol/liq | 69 |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $102.8k | $524.2k | +71% | +648% | +648% | 15.8x | spike (+71% 1h, +648% 6h) | not scored |
| [Taffy](https://pump.fun/coin/5nmZzANRvvKSR49QsodoAtspjbGft7pfwmFBPxrKpump) | `5nmZzANRvvKSR49QsodoAtspjbGft7pfwmFBPxrKpump` | $21.3k | $99.1k | +245% | +245% | +245% | 12.3x | thin liq $21.3k; spike (+245% 1h, +245% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $31.7k | $167.5k | -1% | +519% | +519% | 54.9x | thin liq $31.7k; churn 55x vol/liq; spike (-1% 1h, +519% 6h) | not scored |

_Timing: total 158s (discovery 71.5s, screen 1.6s, GT prime 0.5s, scoring 84.3s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 10/164; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
