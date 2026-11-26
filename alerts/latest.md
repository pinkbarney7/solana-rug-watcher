# Last scan 2026-11-26T01:54:47Z - mode: helius (box heartbeat stale (27 min); budget 393/3000)

```
[fast_scan] 136 candidate mints from 10 source tags; 131 with pair data; 25 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored VINE in 75s
[fast_scan] scored SPCX in 83s
[fast_scan] scored BASKET in 84s
[fast_scan] scored CLAUDIA in 84s
# Market scan 2026-11-26 01:54 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,722 (+2.6% 24h), ETH $1,699 (+2.6% 24h), SOL $70.84 (+2.6% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +5.7% (mcap $1.88B, vol $365.57M), pump-fun +4.2% (mcap $784.54M, vol $136.80M)

## Cleanest on real liquidity (younger than 3 days)
Top 1 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 55* | SKIP | [BASKET](https://dexscreener.com/solana/3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f) | `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f` | $156.8k | $635.6k | 21.3 h | h24 +807% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.50M | $9.41M | 672.1 d | h24 +8% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,092 (growth n/a: first sighting) |
| 59* | SKIP | [CLAUDIA](https://dexscreener.com/solana/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | `2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM` | $13.64M | $76.26B | 50.0 d | h24 +1% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.0% (+12); #7 Insiders / bundles / LP lock WARN (+5); GATES FAILED: rug-funder link; holders 61,708 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.30M | $13.64M | 182.8 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 391,791 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $78.4k | $1.17M | -30% | +3214% | +3214% | 19.2x | spike (-30% 1h, +3214% 6h); lopsided buys/sells 3.03 | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $69.9k | $959.4k | +67% | +2589% | +2589% | 6.6x | spike (+67% 1h, +2589% 6h) | not scored |
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $41.8k | $365.2k | +1059% | +1059% | +1059% | 3.3x | thin liq $41.8k; spike (+1059% 1h, +1059% 6h); < 1h old | not scored |
| [Memeployed](https://dexscreener.com/solana/3ENSPxghg4nKdvZ3RyfTHNf4FGuk4Yb8HFgnjeEunYTK) | `3ENSPxghg4nKdvZ3RyfTHNf4FGuk4Yb8HFgnjeEunYTK` | $10.9k | $36.4k | -12% | +2347% | +2347% | 3.0x | thin liq $10.9k; spike (-12% 1h, +2347% 6h) | not scored |
| [Inufinity](https://pump.fun/coin/wxE5okdbtn3QRcgt9QcEM45T2EoPdvf3N8FM2Tnpump) | `wxE5okdbtn3QRcgt9QcEM45T2EoPdvf3N8FM2Tnpump` | $41.5k | $322.6k | +929% | +929% | +929% | 26.1x | thin liq $41.5k; churn 26x vol/liq; spike (+929% 1h, +929% 6h); < 1h old | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $58.8k | $589.8k | +105% | +1930% | +1930% | 29.3x | churn 29x vol/liq; spike (+105% 1h, +1930% 6h) | not scored |

_Timing: total 157s (discovery 71.5s, screen 1.5s, GT prime 0.3s, scoring 84.2s for 4 coins, 4 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 6/90; Helius 429s 55; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
