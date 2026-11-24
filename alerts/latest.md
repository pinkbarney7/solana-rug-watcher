# Last scan 2026-11-24T11:15:52Z - mode: helius (box heartbeat stale (429 min); budget 334/3000)

```
[fast_scan] 121 candidate mints from 10 source tags; 116 with pair data; 31 >= $50,000 liq; 15 pass survivor pre-gates (32s)
[fast_scan] scored GROKIA in 82s
[fast_scan] scored ROCKET in 83s
[fast_scan] scored pippin in 83s
[fast_scan] scored ACHI in 83s
[fast_scan] scored NOHR in 107s
[fast_scan] scored MEW in 115s
[fast_scan] scored JIMMY in 116s
[fast_scan] scored DONJENSEN in 136s
[fast_scan] scored META in 78s
# Market scan 2026-11-24 11:15 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $59,730 (-2.5% 24h), ETH $1,684 (-2.2% 24h), SOL $70.26 (-2.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -2.9% (mcap $1.84B, vol $360.36M), pump-fun -4.3% (mcap $774.67M, vol $131.05M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 33* | CAUTION | [ROCKET](https://pump.fun/coin/6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump) | `6C9r2gzu8Pr54hTevHo3x5gSj9JqtpApj7obJnrtpump` | $79.5k | $754.6k | 3.0 d | h24 +34% | #11 not checked (+3); #12 not checked (+3); #13 not checked (+3) |
| 53* | SKIP | [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $144.5k | $3.58M | 2.8 d | h24 +96% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 4.0% (+7.2); #11 not checked (+3) |
| 53* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $133.7k | $126.7k | 5.9 h | h24 +185% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $101.4k | $432.2k | 14.1 h | h24 +1417% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 60* | SKIP | [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $103.8k | $2.06M | 8.7 h | h24 +5690% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.0% (+6) |
| 66* | SKIP | [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $137.6k | $3.35M | 9.0 h | h24 +2963% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.1% (+7.1) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MEW](https://dexscreener.com/solana/MEW1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5) | `MEW1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5` | $6.08M | $25.58M | 973.2 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #11 not checked (+3); GATES FAILED: rug-funder link; holders 488,837 (growth n/a: first sighting) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.36M | $17.85M | 744.6 d | h24 -4% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,547 (growth n/a: first sighting) |
| 67* | SKIP | [META](https://dexscreener.com/solana/METAaH6MMZZgy2CTEJq3QdNi7AFVTV3NxHFBfFgLEDd) | `METAaH6MMZZgy2CTEJq3QdNi7AFVTV3NxHFBfFgLEDd` | $906.5k | $826.4k | 159.0 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #8 Turnover / bot pattern WARN (+4); #7 unknown (+3); GATES FAILED: authorities, rug-funder link; holders 1,825 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $103.8k | $2.06M | -3% | +9% | +5690% | 12.5x | none flagged (still high risk) | 60 |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $137.6k | $3.35M | -8% | +39% | +2963% | 16.7x | liq/mcap 4.1% | 66 |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $53.2k | $432.2k | +19% | +12% | +1417% | 45.9x | churn 46x vol/liq | 55 |
| [JENSEN](https://pump.fun/coin/9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump) | `9scVbbC7HUwXaBmo8bnYfm2Pa5oouZpjy2NvrvwLpump` | $24.6k | $60.6k | -7% | -56% | +833% | 178.4x | thin liq $24.6k; churn 178x vol/liq | not scored |
| [NVIDIA](https://dexscreener.com/solana/DJZZprmT2ooZvfjXTTPaxdkGymw6YHdAseNqPhQAFZUG) | `DJZZprmT2ooZvfjXTTPaxdkGymw6YHdAseNqPhQAFZUG` | $38.5k | $28.8k | +124% | +124% | +124% | 3.8x | thin liq $38.5k; spike (+124% 1h, +124% 6h); lopsided buys/sells 3.92; < 1h old | not scored |
| [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $134.2k | $127.6k | +7% | +187% | +187% | 170.7x | churn 171x vol/liq | 53 |

_Timing: total 192s (discovery 30.7s, screen 1.3s, GT prime 0.3s, scoring 160.1s for 9 coins, 9 newly scored). ~80 Helius credits (smart-money discovery 40). HTTP cache hits 9/183; Helius 429s 107; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
