# Last scan 2026-11-15T19:02:58Z - mode: helius (box heartbeat stale (7544 min); budget 30/3000)

```
[fast_scan] 127 candidate mints from 10 source tags; 126 with pair data; 24 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BUTTHOLE in 80s
[fast_scan] scored TTWO in 85s
[fast_scan] scored bill in 87s
[fast_scan] scored UM in 88s
[fast_scan] scored VINE in 88s
[fast_scan] scored USPR in 96s
[fast_scan] scored SPCX in 104s
# Market scan 2026-11-15 19:02 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,655 (-1.3% 24h), ETH $1,813 (-0.9% 24h), SOL $71.00 (-1.7% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.1% (mcap $2.07B, vol $473.64M), pump-fun +2.4% (mcap $880.45M, vol $149.91M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [BUTTHOLE](https://pump.fun/coin/4B8CdHPZ8ng1CtMP2Jk2W8wGAwJ5nJnap1deVsz2pump) | `4B8CdHPZ8ng1CtMP2Jk2W8wGAwJ5nJnap1deVsz2pump` | $181.7k | $365.1k | 4.1 h | h24 -23% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3) |
| 55* | SKIP | [bill](https://pump.fun/coin/85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump) | `85RhcSEMy15SNhFLmSArNm7udPKXVagVgsq4YmSopump` | $121.0k | $609.4k | 23.3 h | h24 +962% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 58* | SKIP | [UM](https://pump.fun/coin/FL3LnVeZTtn7uvcpytRLyAYsqUJtznskjdE4p1HSpump) | `FL3LnVeZTtn7uvcpytRLyAYsqUJtznskjdE4p1HSpump` | $1.09M | $1.40M | 19.3 h | h24 +1520% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 75* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $908.5k | $165.32M | 21.3 h | h24 +564968% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.45M | $9.51M | 661.8 d | h24 +97% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 343,407 (growth n/a: first sighting) |
| 66* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.52M | $13.06M | 156.1 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #6 unknown (+3); #7 unknown (+3); GATES FAILED: authorities, rug-funder link |
| 67* | SKIP | [TTWO](https://dexscreener.com/solana/TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo) | `TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo` | $1.38M | $99 | 104.8 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders +1.3% in 7h (now 263,419) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $908.7k | $165.38M | +2% | +15% | +565191% | 0.6x | liq/mcap 0.5%; lopsided buys/sells 155.57 | 75 |
| [Mag](https://dexscreener.com/solana/AxPzkSJKU3ACqZu7qpq8ov29g4BENZBM4SAZwUUUFo8M) | `AxPzkSJKU3ACqZu7qpq8ov29g4BENZBM4SAZwUUUFo8M` | $15.7k | $34.0k | -42% | +937% | +891% | 18.8x | thin liq $15.7k; spike (-42% 1h, +937% 6h) | not scored |
| [SWJ](https://pump.fun/coin/13EAww2eo8g1Xp9U7qrLNg1WoHFHKbs9xy2EQJjfpump) | `13EAww2eo8g1Xp9U7qrLNg1WoHFHKbs9xy2EQJjfpump` | $54.9k | $583.9k | -12% | +651% | +542% | 10.6x | spike (-12% 1h, +651% 6h) | not scored |
| [UM](https://pump.fun/coin/FL3LnVeZTtn7uvcpytRLyAYsqUJtznskjdE4p1HSpump) | `FL3LnVeZTtn7uvcpytRLyAYsqUJtznskjdE4p1HSpump` | $1.09M | $1.40M | -90% | -2% | +1520% | 0.3x | none flagged (still high risk) | 58 |
| [BFS](https://dexscreener.com/solana/A3vB4dggaaMScchjNW9WifagMRiWaWtDAzunooDYcREQ) | `A3vB4dggaaMScchjNW9WifagMRiWaWtDAzunooDYcREQ` | $35.1k | $156.9k | +249% | +249% | +249% | 13.3x | thin liq $35.1k; spike (+249% 1h, +249% 6h); < 1h old | not scored |
| [BAWSAQ](https://pump.fun/coin/7dzdHo9DKx2dqnXBVXRyMUJUETQhfwFoV4NwcgfVpump) | `7dzdHo9DKx2dqnXBVXRyMUJUETQhfwFoV4NwcgfVpump` | $51.3k | $264.6k | +232% | +134% | +125% | 5.1x | spike (+232% 1h, +134% 6h) | not scored |

_Timing: total 177s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 103.7s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/141; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
