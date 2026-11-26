# Last scan 2026-11-26T01:48:08Z - mode: helius (box heartbeat stale (21 min); budget 383/3000)

```
[fast_scan] 138 candidate mints from 10 source tags; 133 with pair data; 26 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BASKET in 67s
[fast_scan] scored SPCX in 76s
[fast_scan] scored VINE in 76s
[fast_scan] scored CLAUDIA in 78s
# Market scan 2026-11-26 01:48 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,669 (+2.3% 24h), ETH $1,698 (+2.3% 24h), SOL $70.86 (+2.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.7% (mcap $1.88B, vol $365.57M), pump-fun +4.2% (mcap $784.54M, vol $136.80M)

## Cleanest on real liquidity (younger than 3 days)
Top 1 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $157.6k | $629.4k | 21.2 h | h24 +798% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 38* | CAUTION | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $8.47M | $16.88M | 50.0 d | h24 -100% | #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders -0.1% in 21h (now 61,621) |
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.39M | 672.1 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 12h (now 345,092) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.30M | $13.64M | 182.7 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.4% in 11h (now 391,791) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [MemeStonks](https://pump.fun/coin/ERhjmSpLh6Rr4ozYjkGohr7rLizv7Mw6MgWpEFH7pump) | `ERhjmSpLh6Rr4ozYjkGohr7rLizv7Mw6MgWpEFH7pump` | $56.6k | $654.0k | +1579% | +1579% | +1579% | 4.1x | spike (+1579% 1h, +1579% 6h); lopsided buys/sells 3.54; < 1h old | not scored |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $69.2k | $916.0k | -47% | +2496% | +2496% | 21.5x | spike (-47% 1h, +2496% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $68.7k | $926.6k | +44% | +2497% | +2497% | 6.6x | spike (+44% 1h, +2497% 6h) | not scored |
| [Memeployed](https://dexscreener.com/solana/3ENSPxghg4nKdvZ3RyfTHNf4FGuk4Yb8HFgnjeEunYTK) | `3ENSPxghg4nKdvZ3RyfTHNf4FGuk4Yb8HFgnjeEunYTK` | $11.4k | $39.1k | -14% | +2526% | +2526% | 2.9x | thin liq $11.4k; spike (-14% 1h, +2526% 6h) | not scored |
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $40.5k | $344.9k | +995% | +995% | +995% | 2.3x | thin liq $40.5k; spike (+995% 1h, +995% 6h); < 1h old | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $59.8k | $616.6k | +64% | +2023% | +2023% | 28.3x | churn 28x vol/liq; spike (+64% 1h, +2023% 6h) | not scored |

_Timing: total 151s (discovery 71.4s, screen 1.5s, GT prime 0.4s, scoring 77.5s for 4 coins, 4 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 4/95; Helius 429s 55; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
