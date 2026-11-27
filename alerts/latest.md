# Last scan 2026-11-27T12:13:24Z - mode: helius (box heartbeat stale (485 min); budget 350/3000)

```
[fast_scan] 105 candidate mints from 10 source tags; 103 with pair data; 25 >= $50,000 liq; 6 pass survivor pre-gates (32s)
[fast_scan] scored Snowball in 97s
[fast_scan] scored GAIB in 114s
[fast_scan] scored CLAUDIA in 114s
[fast_scan] scored BASKET in 141s
[fast_scan] scored PUMPCHAN in 183s
[fast_scan] scored TROLL in 228s
[fast_scan] scored CATE in 173s
[fast_scan] scored FSD V15 in 278s
[fast_scan] scored Suki in 439s
# Market scan 2026-11-27 12:13 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,593 (+1.3% 24h), ETH $1,722 (+1.0% 24h), SOL $73.08 (+2.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.2% (mcap $1.93B, vol $257.15M), pump-fun +2.4% (mcap $800.29M, vol $90.49M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $126.6k | $505.2k | 2.3 d | h24 -35% | #18 Wash trading (recent swaps) WARN (+7); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3) |
| 52* | SKIP | [GAIB](https://dexscreener.com/solana/BSDB4NSJg93X47N3pAVvf9CdUtvUJ4Ei7Ca3T5H6p6cy) | `BSDB4NSJg93X47N3pAVvf9CdUtvUJ4Ei7Ca3T5H6p6cy` | $202.5k | $113.1k | 1.7 h | h24 +70% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $129.4k | $703.5k | 1.7 d | h24 +4617% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $261.2k | $11.48M | 1.4 d | h24 +45% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.3% (+9.3); #11 not checked (+3) |
| 56* | SKIP | [Suki](https://dexscreener.com/solana/A2mkRc2RBbXgF63av2kNjiA3JtqybM5UnzQyRsNRaRVg) | `A2mkRc2RBbXgF63av2kNjiA3JtqybM5UnzQyRsNRaRVg` | $212.5k | $159.1k | 2.2 h | h24 +200% | #7 Insiders / bundles / LP lock FAIL (+14); #18 Wash trading (recent swaps) FAIL (+8); #5 Token / pool age WARN (+5) |
| 60* | SKIP | [FSD V15](https://dexscreener.com/solana/6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3) | `6fnowXxtdKwGqBz1tKUWdZXNehmFDFBthuA7SnMzDaS3` | n/a | n/a | 1.1 d | h24 +113% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.68M | $17.52M | 123.8 d | h24 +2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 438,627 (growth n/a: first sighting) |
| 54* | SKIP | [TROLL](https://dexscreener.com/solana/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` | $2.01M | $22.06M | 847.0 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 3h (now 219,038) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.12M | $76.24B | 51.4 d | h24 -9% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 62,341 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [monky](https://pump.fun/coin/At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump) | `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump` | $2.27M | $2.66M | +111991% | +8627% | +8627% | 0.1x | spike (+111991% 1h, +8627% 6h) | not scored |
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $61.5k | $566.2k | +5% | +190% | +7766% | 17.5x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $68.7k | $716.8k | -13% | +10% | +4283% | 32.6x | churn 33x vol/liq | 52 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $35.4k | $224.7k | +12% | +1399% | +597% | 26.7x | thin liq $35.4k; churn 27x vol/liq; spike (+12% 1h, +1399% 6h) | not scored |
| [VAULT](https://pump.fun/coin/4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump) | `4tqzkSWA9tiWYhzYpSt81We3cVNkrEbkD1tzjFDZpump` | $26.8k | $145.4k | +406% | +406% | +406% | 8.3x | thin liq $26.8k; spike (+406% 1h, +406% 6h); < 1h old | not scored |
| [SNOWBALLZ](https://pump.fun/coin/DCFiFuRwjwdSKcYKmuz47gcSNsjjtZ6Rh8KkLaVCpump) | `DCFiFuRwjwdSKcYKmuz47gcSNsjjtZ6Rh8KkLaVCpump` | $25.6k | $136.6k | +18% | +353% | +353% | 5.0x | thin liq $25.6k; spike (+18% 1h, +353% 6h) | not scored |

_Timing: total 486s (discovery 31.0s, screen 1.1s, GT prime 14.3s, scoring 439.2s for 9 coins, 9 newly scored). ~95 Helius credits (smart-money discovery 40). HTTP cache hits 2/208; Helius 429s 137; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
