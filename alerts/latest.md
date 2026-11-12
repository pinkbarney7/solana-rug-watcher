# Last scan 2026-11-12T22:18:06Z - mode: helius (box heartbeat stale (3420 min); budget 42/3000)

```
[fast_scan] 136 candidate mints from 11 source tags; 134 with pair data; 30 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored NOBUSHIBA in 71s
[fast_scan] scored UODF in 78s
[fast_scan] scored CATE in 78s
[fast_scan] scored SPCX in 79s
[fast_scan] scored PREDICT in 79s
[fast_scan] scored STONK in 79s
# Market scan 2026-11-12 22:18 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $71,398 (-4.0% 24h), ETH $2,012 (-2.8% 24h), SOL $81.37 (-3.8% 24h)
- Fear & Greed: 28 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -3.1% (mcap $2.36B, vol $345.50M), pump-fun -3.7% (mcap $937.85M, vol $138.03M)

## Cleanest on real liquidity (younger than 3 days)
Top 3 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 47* | CAUTION | [NOBUSHIBA](https://pump.fun/coin/8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump) | `8AAVuQpJcqpvCuutxyBTVvgBEXZJSkZoNv1sExpBpump` | $72.3k | $771.0k | 1.9 d | h24 +359% | #3 Liquidity vs market cap WARN (+7); #9 Price momentum WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [UODF](https://pump.fun/coin/51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump) | `51rmodatSFEcZgzVohX97YXPnX5dh7RH5JXyxSoepump` | $1.18M | $243.80M | 2.6 d | h24 +34% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |
| 70* | SKIP | [PREDICT](https://dexscreener.com/solana/7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9) | `7GM6DTUa3q9V2Dv6efRuGhrvW4aDz6Gk2GAgoC4AUTd9` | $139.9k | $6.43M | 1.9 d | h24 +277% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 2.2% (+9.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 45* | SKIP | [STONK](https://dexscreener.com/solana/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | `6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx` | $3.96M | $33.33M | 112.1 d | h24 -9% | #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); #12 not checked (+3); GATES FAILED: rug-funder link; holders 334,195 (growth n/a: first sighting) |
| 66* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.02M | $23.23M | 109.2 d | h24 -0% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); GATES FAILED: rug-funder link, exit test; holders +0.1% in 6h (now 427,855) |
| 80* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.28M | $13.17M | 169.6 d | h24 +0% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.5% in 6h (now 359,887) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [AI](https://pump.fun/coin/2T56GBrvcyeWWyhUAzsTFW4AcFag1nr7xyzrtZn7pump) | `2T56GBrvcyeWWyhUAzsTFW4AcFag1nr7xyzrtZn7pump` | $89.8k | $847.9k | +16% | +1379% | +1379% | 32.6x | churn 33x vol/liq; spike (+16% 1h, +1379% 6h) | not scored |
| [mihao](https://pump.fun/coin/GasYxdh4RP971cY9odYBDPxa7Dwid8qVxDqKXnk7pump) | `GasYxdh4RP971cY9odYBDPxa7Dwid8qVxDqKXnk7pump` | $42.6k | $330.8k | +83% | +890% | +890% | 1.6x | thin liq $42.6k; spike (+83% 1h, +890% 6h) | not scored |
| [FANDEMON](https://pump.fun/coin/a9zoLRHvqn12KiGxERC298Gr2rS8YQxuMuN9VFMpump) | `a9zoLRHvqn12KiGxERC298Gr2rS8YQxuMuN9VFMpump` | $47.6k | $390.2k | +149% | +705% | +705% | 12.8x | thin liq $47.6k; spike (+149% 1h, +705% 6h); lopsided buys/sells 4.11 | not scored |
| [DOGGLE](https://pump.fun/coin/E8qaeXz7CF2auJebXaQkLZyrFPfRQft3KrGgvRvwpump) | `E8qaeXz7CF2auJebXaQkLZyrFPfRQft3KrGgvRvwpump` | $39.8k | $289.4k | -38% | +743% | +743% | 5.1x | thin liq $39.8k; spike (-38% 1h, +743% 6h) | not scored |
| [Pois](https://pump.fun/coin/CM65K38bqGePYkNQBjGRRDYMhyxgh9xTQg2HPQTFpump) | `CM65K38bqGePYkNQBjGRRDYMhyxgh9xTQg2HPQTFpump` | $14.8k | $31.4k | +11% | +159% | +714% | 7.4x | thin liq $14.8k | not scored |
| [AI](https://pump.fun/coin/2s9kHmkeHU3oKwuJYV1VTiBTsZwUWUbMUVtBgoJFpump) | `2s9kHmkeHU3oKwuJYV1VTiBTsZwUWUbMUVtBgoJFpump` | $21.7k | $88.8k | +126% | +126% | +126% | 10.9x | thin liq $21.7k; spike (+126% 1h, +126% 6h); < 1h old | not scored |

_Timing: total 152s (discovery 70.8s, screen 1.3s, GT prime 0.3s, scoring 79.3s for 6 coins, 6 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 6/121; Helius 429s 70; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
