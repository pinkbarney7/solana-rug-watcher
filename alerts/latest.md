# Last scan 2026-11-26T11:46:13Z - mode: helius (box heartbeat stale (464 min); budget 317/3000)

```
[fast_scan] 115 candidate mints from 9 source tags; 111 with pair data; 22 >= $50,000 liq; 8 pass survivor pre-gates (73s)
[fast_scan] scored JIMMY in 72s
[fast_scan] scored SPCX in 79s
[fast_scan] scored NORFEATH in 79s
[fast_scan] scored MOODENG in 80s
[fast_scan] scored UHI in 80s
[fast_scan] scored VINE in 81s
[fast_scan] scored DOG in 81s
# Market scan 2026-11-26 11:46 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,661 (+3.8% 24h), ETH $1,699 (+3.8% 24h), SOL $70.73 (+5.0% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +8.3% (mcap $1.90B, vol $353.36M), pump-fun +5.8% (mcap $787.22M, vol $128.32M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $128.2k | $766.8k | 2.6 d | h24 -30% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe) | `3nsEzgrXoGWWBgQLZ11cY22mtoXLM9Pfi36oB1ReBiKe` | $239.0k | $144.1k | 3.0 h | h24 +101% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 57* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $92.1k | $1.62M | 12.5 h | h24 +4431% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.7% (+5.2) |
| 57* | SKIP | [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $56.9k | $585.8k | 14.7 h | h24 +1177% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.48M | $9.20M | 672.5 d | h24 +1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders 345,129 (growth n/a: first sighting) |
| 56* | SKIP | [MOODENG](https://dexscreener.com/solana/ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY) | `ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY` | $1.90M | $29.11M | 806.8 d | h24 +6% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) FAIL (+5); GATES FAILED: rug-funder link; holders 228,025 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.38M | $13.67M | 183.2 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 395,199 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $208.4k | $7.85M | +19% | +439% | +24814% | 17.8x | liq/mcap 2.7%; spike (+19% 1h, +439% 6h) | not scored |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $91.6k | $1.60M | +18% | +37% | +4378% | 10.0x | none flagged (still high risk) | 57 |
| [Grodia](https://pump.fun/coin/6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump) | `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump` | $48.9k | $438.9k | -8% | -53% | +1144% | 48.2x | thin liq $48.9k; churn 48x vol/liq | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $57.3k | $594.3k | +17% | +10% | +1195% | 32.3x | churn 32x vol/liq | 57 |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $44.6k | $295.1k | +32% | -11% | +916% | 93.5x | thin liq $44.6k; churn 93x vol/liq | not scored |
| [Maru](https://pump.fun/coin/FokVFH6mDsazoKbtnUaA2FRMsRbDSwZhNfn17Fdvpump) | `FokVFH6mDsazoKbtnUaA2FRMsRbDSwZhNfn17Fdvpump` | $19.0k | $77.8k | +169% | +169% | +169% | 9.4x | thin liq $19.0k; spike (+169% 1h, +169% 6h); < 1h old | not scored |

_Timing: total 154s (discovery 71.6s, screen 1.3s, GT prime 0.3s, scoring 80.9s for 7 coins, 7 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 7/142; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
