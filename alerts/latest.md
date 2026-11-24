# Last scan 2026-11-24T12:54:34Z - mode: helius (box heartbeat stale (527 min); budget 494/3000)

```
[fast_scan] 109 candidate mints from 10 source tags; 106 with pair data; 28 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored Scamsem in 74s
[fast_scan] scored JIMMY in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored pippin in 82s
[fast_scan] scored Bullseye in 83s
[fast_scan] scored ACHI in 83s
[fast_scan] scored MCAT in 83s
[fast_scan] scored COPIUM in 85s
[fast_scan] scored CATE in 87s
# Market scan 2026-11-24 12:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,385 (-1.2% 24h), ETH $1,700 (-0.9% 24h), SOL $70.72 (-1.7% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.5% (mcap $1.83B, vol $375.65M), pump-fun -4.4% (mcap $772.83M, vol $133.13M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 37* | CAUTION | [COPIUM](https://pump.fun/coin/BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump) | `BAKsQrynzwadyACDMsg3J5R8a4CTvj1u7kEYyjq7pump` | $53.1k | $483.9k | 1.6 d | h24 -24% | #8 Turnover / bot pattern WARN (+4); #11 not checked (+3); #12 not checked (+3) |
| 41* | CAUTION | [MCAT](https://dexscreener.com/solana/BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi) | `BzPyyYCTmQNq2BcfQ4ANAvCYk54rnmQEXMFvFT8RhWMi` | $76.3k | $185.5k | 2.0 d | h24 -48% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 41* | CAUTION | [Scamsem](https://dexscreener.com/solana/5JWeGmA9z6yHd5F9P6B23A8wthho8BpZuDmQv5DfLoat) | `5JWeGmA9z6yHd5F9P6B23A8wthho8BpZuDmQv5DfLoat` | $52.1k | $89.8k | 17.7 d | h24 -14% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [Bullseye](https://dexscreener.com/solana/DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe) | `DtrArWGJHq6cqqRjKo1W19obXQbW5QN6HdNgyByYHGEe` | $178.4k | $119.2k | 1.3 h | h24 +138% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 55* | SKIP | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $88.3k | $421.2k | 15.8 h | h24 +1379% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 56* | SKIP | [ACHI](https://dexscreener.com/solana/cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb) | `cZ9FE2JtR2XCmYu9hPpFpmxs6ciX6bpBmsVjMn2NUsb` | $154.7k | $142.0k | 7.5 h | h24 +220% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #9 Price momentum WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.63M | $16.52M | 120.8 d | h24 -7% | #3 Liquidity vs market cap WARN (+7); #6 unknown (+3); #7 unknown (+3); GATES FAILED: rug-funder link |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.37M | $17.78M | 744.7 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 182,546 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.05M | $13.11M | 181.2 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 386,485 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [DONJENSEN](https://pump.fun/coin/5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump) | `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump` | $109.0k | $2.25M | +3% | +14% | +6221% | 12.7x | liq/mcap 4.8% | not scored |
| [GROKIA](https://pump.fun/coin/3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump) | `3cL47ohWa2HApLYKtqPsqkjaxJ6HLvT5Ri1KvWdXpump` | $152.7k | $4.09M | +22% | +38% | +3631% | 15.6x | liq/mcap 3.7%; spike (+22% 1h, +38% 6h) | not scored |
| [DUVAL](https://pump.fun/coin/7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump) | `7fmD1p3jzva28EPP9bPqbDoxZGj5j398yJoE3EVypump` | $44.0k | $318.4k | +69% | +1072% | +1072% | 33.3x | thin liq $44.0k; churn 33x vol/liq; spike (+69% 1h, +1072% 6h) | not scored |
| [Unemployed](https://pump.fun/coin/FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump) | `FJ3eLHQJqq8NsVkUyQmj5jSJJXvdf1ZiP2YMdEWUpump` | $24.8k | $123.4k | +342% | +342% | +342% | 13.2x | thin liq $24.8k; spike (+342% 1h, +342% 6h); < 1h old | not scored |
| [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $52.8k | $421.6k | +12% | +34% | +1380% | 47.4x | churn 47x vol/liq | 55 |
| [NOHR](https://pump.fun/coin/Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump) | `Jd3NCawdFiDNWpLiTtsMqoeoBMjC1ZQMrMScRVzpump` | $144.7k | $3.57M | -3% | +378% | +277% | 8.0x | liq/mcap 4.1%; spike (-3% 1h, +378% 6h) | not scored |

_Timing: total 233s (discovery 71.2s, screen 1.1s, GT prime 0.4s, scoring 160.6s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 11/187; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
