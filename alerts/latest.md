# Last scan 2026-11-25T06:27:32Z - mode: helius (box heartbeat stale (153 min); budget 40/3000)

```
[fast_scan] 121 candidate mints from 9 source tags; 116 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored MCAT in 73s
[fast_scan] scored KOOP in 80s
[fast_scan] scored CHUCK in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored 4CHAN in 82s
[fast_scan] scored SPCX in 82s
[fast_scan] scored JIMMY in 83s
[fast_scan] scored pippin in 115s
# Market scan 2026-11-25 06:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,117 (-2.1% 24h), ETH $1,657 (-2.5% 24h), SOL $68.55 (-4.2% 24h)
- Fear & Greed: 13 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -5.6% (mcap $1.79B, vol $306.69M), pump-fun -6.5% (mcap $758.81M, vol $135.66M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $55.7k | $104.6k | 2.7 d | h24 -36% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3) |
| 45* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $237.3k | $1.37M | 1.4 d | h24 +321% | #7 Insiders / bundles / LP lock WARN (+5); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [KOOP](https://dexscreener.com/solana/6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS) | `6zD5fGV11kU4bBshABjBNN4t3CbsDrd9gr1GwpNKjSiS` | $219.0k | $124.8k | 2.2 h | h24 +63% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $134.0k | $142.8k | 1.6 h | h24 +189% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 56* | SKIP | [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $166.8k | $637.7k | 8.6 h | h24 +2228% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 42* | CAUTION | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.43M | $19.00M | 745.4 d | h24 +5% | #8 Turnover / bot pattern WARN (+4); #6 unknown (+3); #7 unknown (+3); GATES FAILED: rug-funder link |
| 51* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.45M | $9.08M | 671.3 d | h24 +3% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 41h (now 345,014) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.17M | $13.04M | 181.9 d | h24 -8% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 390,217 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BOOBS](https://pump.fun/coin/E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump) | `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump` | $91.0k | $1.58M | +35% | +4040% | +4040% | 17.7x | spike (+35% 1h, +4040% 6h) | not scored |
| [Jimmies](https://pump.fun/coin/GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump) | `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump` | $86.2k | $1.46M | +32% | +595% | +4514% | 9.0x | spike (+32% 1h, +595% 6h) | not scored |
| [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $110.0k | $599.6k | +187% | +756% | +756% | 12.0x | spike (+187% 1h, +756% 6h) | not scored |
| [4CHAN](https://pump.fun/coin/DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump) | `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump` | $64.6k | $637.7k | -26% | +110% | +2228% | 57.3x | churn 57x vol/liq | 56 |
| [PERRO](https://pump.fun/coin/4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump) | `4Di56UJzpnb7E4D7aLXFf7aLF5TrpJYv9Q3mR398pump` | $31.4k | $165.8k | +33% | +513% | +513% | 54.7x | thin liq $31.4k; churn 55x vol/liq; spike (+33% 1h, +513% 6h) | not scored |
| [CHUCK](https://dexscreener.com/solana/F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW) | `F7FsMCj9GVxmW52qerHe9t7sDTYyZRiWDDVnR3HR5yCW` | $135.1k | $145.1k | +65% | +193% | +193% | 93.5x | churn 93x vol/liq | 53 |

_Timing: total 188s (discovery 71.8s, screen 1.3s, GT prime 0.3s, scoring 114.7s for 8 coins, 8 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 10/167; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
