# Last scan 2026-11-25T06:02:53Z - mode: helius (box heartbeat stale (128 min); budget 30/3000)

```
[fast_scan] 125 candidate mints from 10 source tags; 119 with pair data; 25 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored CHUCK in 72s
[fast_scan] scored KOOP in 81s
[fast_scan] scored SPCX in 82s
[fast_scan] scored pippin in 82s
[fast_scan] scored JIMMY in 82s
[fast_scan] scored 4CHAN in 83s
[fast_scan] scored MCAT in 85s
[fast_scan] scored BASKET in 85s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-25 06:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,125 (-2.3% 24h), ETH $1,656 (-2.8% 24h), SOL $68.70 (-4.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.6% (mcap $1.79B, vol $307.87M), pump-fun -6.4% (mcap $759.97M, vol $136.08M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $57.3k | $110.5k | 2.7 d | h24 -27% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $246.3k | $1.50M | 1.4 d | h24 +442% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 49* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $76.8k | $260.5k | 1.4 h | h24 +272% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $211.0k | $118.7k | 1.8 h | h24 +55% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $114.9k | $120.5k | 1.2 h | h24 +144% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $187.3k | $771.9k | 8.1 h | h24 +2718% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.57M | $16.49M | 121.6 d | h24 -6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 436,951 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.42M | $18.85M | 745.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,578 (growth n/a: first sighting) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.17M | $12.95M | 181.9 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 390,217 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $79.6k | $1.21M | -1% | +3076% | +3076% | 19.8x | spike (-1% 1h, +3076% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $79.0k | $1.23M | +1% | +570% | +3787% | 8.9x | spike (+1% 1h, +570% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $71.1k | $771.9k | -14% | +169% | +2718% | 50.9x | churn 51x vol/liq | 56 |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $32.2k | $174.4k | +45% | +545% | +545% | 52.7x | thin liq $32.2k; churn 53x vol/liq; spike (+45% 1h, +545% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $71.9k | $257.7k | -31% | +268% | +268% | 15.5x | none flagged (still high risk) | 49 |
| [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $115.0k | $120.5k | +59% | +144% | +144% | 79.2x | churn 79x vol/liq | 53 |

_Timing: total 217s (discovery 71.2s, screen 1.4s, GT prime 0.4s, scoring 144.1s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/185; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
