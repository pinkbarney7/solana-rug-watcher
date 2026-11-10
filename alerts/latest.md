# Last scan 2026-11-10T12:01:10Z - mode: helius (box heartbeat stale (478 min); budget 120/3000)

```
[fast_scan] 127 candidate mints from 9 source tags; 122 with pair data; 27 >= $50,000 liq; 9 pass survivor pre-gates (73s)
[fast_scan] scored BIG in 78s
[fast_scan] scored AODF in 87s
[fast_scan] scored SPCX in 87s
[fast_scan] scored PREDICT in 87s
[fast_scan] scored ZEC in 88s
[fast_scan] scored USPR in 89s
[fast_scan] scored UODF in 89s
[fast_scan] scored MILES in 89s
[fast_scan] scored CATE in 72s
# Market scan 2026-11-10 12:01 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,328 (-0.1% 24h), ETH $2,092 (-1.0% 24h), SOL $84.62 (-1.7% 24h)
- Fear & Greed: 32 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $2.44B, vol $340.96M), pump-fun -2.6% (mcap $957.01M, vol $109.30M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 49* | SKIP | [MILES](https://pump.fun/coin/7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump) | `7v8LoULtAhg3hT43YYQvKdF3LD3stdudBZAv5oTqpump` | $51.1k | $143.5k | 23.2 h | h24 -6% | #16 Exit liquidity (Jupiter quotes) WARN (+7); #5 Token / pool age WARN (+5); #6 Top-10 holders (excl. pools/programs) FAIL (+5) |
| 55* | SKIP | [BIG](https://pump.fun/coin/34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump) | `34DXEU2ttEtBSb1TqGJm7izgvYTTkqKcCoiNWdPDpump` | $86.2k | $817.2k | 2.0 d | h24 +675% | #7 Insiders / bundles / LP lock FAIL (+14); #9 Price momentum FAIL (+14); #11 not checked (+3) |
| 64* | SKIP | [PREDICT](https://dexscreener.com/solana/8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN) | `8CykGobYKN3og6VqeU17Dfhk5RZe6v7VJLQC8oUoC7yN` | $159.5k | $3.15M | 1.3 d | h24 +308% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); liq/mcap 5.1% (+5.9) |
| 69* | SKIP | [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $121.52M | 21.3 h | h24 +205766% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.9% (+10.9) |
| 78* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $119.47M | 21.0 h | h24 +202290% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |
| 78* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $866.5k | $74.79M | 22.1 h | h24 +126607% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.23M | $28.11M | 106.8 d | h24 -5% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 2h (now 426,366) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.42M | $13.48M | 167.2 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 346,666 (growth n/a: first sighting) |
| 81* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.89M | $28.4k | 390.8 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders 388,005 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AODF](https://pump.fun/coin/svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump) | `svyXJ9K6uPR3RjTLTow541w5fq1WQeBuXMNTAM2pump` | $1.10M | $121.52M | +1% | +8% | +205766% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 56.57 | 69 |
| [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.10M | $119.49M | +1% | +8% | +202336% | 0.6x | liq/mcap 0.9%; lopsided buys/sells 57.43 | 78 |
| [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $866.5k | $74.79M | +2% | +11% | +126607% | 0.6x | liq/mcap 1.2%; lopsided buys/sells 51.36 | 78 |
| [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $736.0k | $54.02M | +2% | +14% | +91414% | 0.6x | liq/mcap 1.4%; lopsided buys/sells 57.88 | not scored |
| [BORLY](https://pump.fun/coin/F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump) | `F22QdNn7VYrtTgYDHEYcqQKVtDH8msh2xs6tnGxepump` | $78.4k | $936.4k | -13% | -39% | +1540% | 29.4x | churn 29x vol/liq | not scored |
| [Rockstar](https://pump.fun/coin/C4qHPWr9TzMG1x8X5oAMyZF9SodmR5BodNbxYrTtpump) | `C4qHPWr9TzMG1x8X5oAMyZF9SodmR5BodNbxYrTtpump` | $22.3k | $95.0k | +170% | +170% | +170% | 0.2x | thin liq $22.3k; spike (+170% 1h, +170% 6h); < 1h old | not scored |

_Timing: total 224s (discovery 72.0s, screen 1.4s, GT prime 0.3s, scoring 150.3s for 9 coins, 9 newly scored). ~0 Helius credits (smart-money discovery 0). HTTP cache hits 11/160; Helius 429s 110; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
