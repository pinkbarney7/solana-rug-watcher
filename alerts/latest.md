# Last scan 2026-11-25T04:34:01Z - mode: helius (box heartbeat stale (40 min); budget 534/3000)

```
[fast_scan] 125 candidate mints from 9 source tags; 119 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 71s
[fast_scan] scored pippin in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored CATE in 79s
[fast_scan] scored GROKIA in 79s
[fast_scan] scored JIMMY in 81s
# Market scan 2026-11-25 04:33 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,224 (-2.0% 24h), ETH $1,661 (-2.2% 24h), SOL $69.08 (-3.8% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -4.5% (mcap $1.79B, vol $320.78M), pump-fun -5.1% (mcap $761.57M, vol $137.44M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $55.8k | $104.4k | 2.7 d | h24 -22% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $269.2k | $1.62M | 1.3 d | h24 +305% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $125.2k | $2.73M | 1.1 d | h24 +15% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.6% (+6.5); #8 Turnover / bot pattern WARN (+4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.59M | $16.87M | 121.5 d | h24 -2% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 436,872) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.41M | $18.64M | 745.3 d | h24 +5% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,578 (growth n/a: first sighting) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.23M | $13.04M | 181.9 d | h24 -7% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders 390,089 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $92.6k | $1.34M | +85% | +9168% | +4785% | 29.2x | churn 29x vol/liq; spike (+85% 1h, +9168% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $77.3k | $1.18M | +52% | +3619% | +3619% | 8.0x | spike (+52% 1h, +3619% 6h) | not scored |
| [YUMA](https://pump.fun/coin/CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump) | `CkwFsrupdFHzo5kYk8b5W47CVx1v5ymzeu6BBoDjpump` | $27.2k | $152.1k | +285% | +407% | +407% | 8.9x | thin liq $27.2k; spike (+285% 1h, +407% 6h) | not scored |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $28.3k | $136.1k | -33% | +403% | +403% | 56.0x | thin liq $28.3k; churn 56x vol/liq; spike (-33% 1h, +403% 6h) | not scored |
| [TROLL](https://pump.fun/coin/7ykeHoEnjnGkY6tqteXn47fdGtd7kfXWghiyZ7YKpump) | `7ykeHoEnjnGkY6tqteXn47fdGtd7kfXWghiyZ7YKpump` | $24.0k | $82.7k | +180% | +180% | +180% | 1.4x | thin liq $24.0k; spike (+180% 1h, +180% 6h); < 1h old | not scored |
| [1](https://pump.fun/coin/BWPv5jje9xipZ6V4q855fjiu5e7HiWGNvS5x8c1Mpump) | `BWPv5jje9xipZ6V4q855fjiu5e7HiWGNvS5x8c1Mpump` | $28.8k | $76.5k | +89% | +289% | +289% | 0.7x | thin liq $28.8k | not scored |

_Timing: total 154s (discovery 71.7s, screen 1.4s, GT prime 0.4s, scoring 80.9s for 6 coins, 6 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 8/132; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
