# Last scan 2026-11-27T10:27:21Z - mode: helius (box heartbeat stale (384 min); budget 250/3000)

```
[fast_scan] 113 candidate mints from 10 source tags; 111 with pair data; 23 >= $50,000 liq; 7 pass survivor pre-gates (72s)
[fast_scan] scored Snowball in 71s
[fast_scan] scored KAI in 80s
[fast_scan] scored CLAUDIA in 80s
[fast_scan] scored Rizzmas in 81s
[fast_scan] scored MPLX in 81s
[fast_scan] scored SuperFIONA in 81s
[fast_scan] scored PUMPCHAN in 81s
# Market scan 2026-11-27 10:27 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $61,629 (+1.4% 24h), ETH $1,728 (+1.7% 24h), SOL $73.33 (+3.4% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +2.5% (mcap $1.93B, vol $257.87M), pump-fun +2.9% (mcap $803.94M, vol $88.62M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $143.3k | $861.3k | 1.7 d | h24 +4248% | #9 Price momentum FAIL (+14); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 53* | SKIP | [SuperFIONA](https://dexscreener.com/solana/4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG) | `4AnNhsdRfTEkXN2NDpxwayhqu68pj7hFRuhCAotppXgG` | $213.9k | $119.5k | 1.4 h | h24 +46% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $250.2k | $10.50M | 1.4 d | h24 +61% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 2.4% (+9.1); #8 Turnover / bot pattern WARN (+4) |
| 60* | SKIP | [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $115.6k | $2.26M | 9.7 h | h24 +1974% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Rizzmas](https://dexscreener.com/solana/85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg) | `85cQsFgbi8mBZxiPppbpPXuV7j1hA8tBwhjF4gKW6mHg` | $220.5k | $621.3k | 1068.7 d | h24 +16% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 395,720 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $14.39M | $78.46B | 51.4 d | h24 -6% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 62,338 (growth n/a: first sighting) |
| 74* | SKIP | [MPLX](https://dexscreener.com/solana/METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m) | `METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m` | $3.00M | $26.90M | 1460.3 d | h24 +14% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: authorities, rug-funder link; holders +0.0% in 3h (now 91,347) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [WOOPY](https://pump.fun/coin/2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump) | `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump` | $65.5k | $457.7k | +33% | +142% | +6259% | 10.9x | none flagged (still high risk) | not scored |
| [Snowball](https://pump.fun/coin/9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump) | `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump` | $75.5k | $861.3k | -4% | +43% | +4248% | 29.1x | churn 29x vol/liq | 52 |
| [KAI](https://pump.fun/coin/G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump) | `G2ZDG8q3QMYk3KR58JFFYsvaTk4Gy94UzMo7Re7spump` | $115.5k | $2.26M | -17% | -17% | +1974% | 29.7x | churn 30x vol/liq | 60 |
| [Kibo](https://pump.fun/coin/7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump) | `7XSYaJygcuNe6Q3kPvwsJpg4ZrFL1AEUFb8kCuzppump` | $25.3k | $121.2k | +77% | +276% | +276% | 30.3x | thin liq $25.3k; churn 30x vol/liq | not scored |
| [NIW](https://pump.fun/coin/CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump) | `CVcVTN9yFswizy3DYdPKJJtYup3hpgC9U7FX1yzUpump` | $23.9k | $133.9k | +41% | +361% | +361% | 0.1x | thin liq $23.9k; spike (+41% 1h, +361% 6h) | not scored |
| [Basket](https://dexscreener.com/solana/78GAsw9ixzDzKK5vQtrgpwuMGa4bFhmfNSdoB5ghyEUq) | `78GAsw9ixzDzKK5vQtrgpwuMGa4bFhmfNSdoB5ghyEUq` | $25.0k | $24.9k | +152% | +152% | +152% | 2.9x | thin liq $25.0k; spike (+152% 1h, +152% 6h); < 1h old | not scored |

_Timing: total 154s (discovery 71.3s, screen 1.1s, GT prime 0.5s, scoring 81.3s for 7 coins, 7 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 9/142; Helius 429s 85; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
