# Last scan 2026-11-25T04:56:33Z - mode: helius (box heartbeat stale (63 min); budget 534/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 121 with pair data; 23 >= $50,000 liq; 6 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 70s
[fast_scan] scored pippin in 77s
[fast_scan] scored CLAUDIA in 77s
[fast_scan] scored JIMMY in 80s
[fast_scan] scored DCTY in 81s
# Market scan 2026-11-25 04:56 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $58,919 (-2.4% 24h), ETH $1,653 (-2.7% 24h), SOL $68.49 (-4.3% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.2% (mcap $1.79B, vol $320.37M), pump-fun -5.8% (mcap $760.49M, vol $134.88M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $58.5k | $115.8k | 2.7 d | h24 -16% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $257.1k | $1.78M | 1.3 d | h24 +414% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [DCTY](https://pump.fun/coin/9hjBLBrc7WZW2H8UQvBAvG5WiTZotXUv2Bdcn4f4pump) | `9hjBLBrc7WZW2H8UQvBAvG5WiTZotXUv2Bdcn4f4pump` | $242.6k | $1.02M | 38.0 d | h24 -33% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 69,432 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.39M | $18.56M | 745.4 d | h24 +4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,580 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.09M | $74.03B | 49.1 d | h24 -11% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 61,720 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $84.1k | $1.11M | +22% | +3586% | +3941% | 37.4x | churn 37x vol/liq; spike (+22% 1h, +3586% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $77.6k | $1.20M | +43% | +3676% | +3676% | 8.4x | spike (+43% 1h, +3676% 6h) | not scored |
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $76.0k | $1.12M | +589% | +2827% | +2827% | 19.5x | spike (+589% 1h, +2827% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $74.5k | $252.3k | +260% | +260% | +260% | 3.7x | spike (+260% 1h, +260% 6h); < 1h old | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $27.1k | $127.2k | -14% | +370% | +370% | 59.8x | thin liq $27.1k; churn 60x vol/liq; spike (-14% 1h, +370% 6h) | not scored |
| [Manlet](https://pump.fun/coin/6LuwyvmTMyJiQRZQPneZCfr2gehSSAvQbMWgXCjopump) | `6LuwyvmTMyJiQRZQPneZCfr2gehSSAvQbMWgXCjopump` | $35.0k | $159.3k | -44% | +215% | +215% | 1.5x | thin liq $35.0k | not scored |

_Timing: total 154s (discovery 71.1s, screen 1.5s, GT prime 0.3s, scoring 80.6s for 5 coins, 5 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/121; Helius 429s 60; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
