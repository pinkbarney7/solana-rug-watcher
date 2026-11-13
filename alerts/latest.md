# Last scan 2026-11-13T10:00:19Z - mode: helius (box heartbeat stale (4122 min); budget 0/3000)

```
[fast_scan] 131 candidate mints from 10 source tags; 131 with pair data; 27 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored FOOD in 72s
[fast_scan] scored ZEC in 81s
[fast_scan] scored USPR in 81s
[fast_scan] scored Max in 81s
[fast_scan] scored NVDAx in 82s
[fast_scan] scored XTO in 82s
[fast_scan] scored SHARKBUX in 82s
[fast_scan] scored STONK in 82s
# Market scan 2026-11-13 10:00 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $69,001 (-5.9% 24h), ETH $1,938 (-5.1% 24h), SOL $79.92 (-3.7% 24h)
- Fear & Greed: 20 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -1.9% (mcap $2.34B, vol $395.70M), pump-fun -3.5% (mcap $925.65M, vol $157.86M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 39* | CAUTION | [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $251.0k | $1.71M | 1.5 d | h24 -20% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [USPR](https://dexscreener.com/solana/SnaNyd3KgXZJafzvM3EdhpKkcQrTaBAb3qBybL9pYLy) | `SnaNyd3KgXZJafzvM3EdhpKkcQrTaBAb3qBybL9pYLy` | $331.5k | $188.2k | 16.7 h | h24 +78% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 67* | SKIP | [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $218.0k | $809.8k | 12.5 h | h24 +2116% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5) |
| 69* | SKIP | [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $65.5k | $670.5k | 10.5 h | h24 +818% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |
| 78* | SKIP | [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $971.6k | $167.97M | 22.0 h | h24 +487586% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [STONK](https://dexscreener.com/solana/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | `6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx` | $3.32M | $35.75M | 112.6 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 334,160) |
| 80* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $8.75M | $23.4k | 393.7 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.1% in 33h (now 389,845) |
| 80* | SKIP | [NVDAx](https://dexscreener.com/solana/Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh) | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` | $4.69M | $37.25M | 504.0 d | h24 +3% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders +0.2% in 7h (now 428,564) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [XTO](https://pump.fun/coin/9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump) | `9bVzrsofzesaoEXbWLPSTHTWUcmcqfwkXK7Ha2bMpump` | $971.6k | $167.97M | +2% | +12% | +487586% | 0.6x | liq/mcap 0.6%; lopsided buys/sells 7.59 | 78 |
| [LAB](https://dexscreener.com/solana/BQ1onbEAtSdwoXiMB8Png6akW4tJsKEBX9BpxfmhBDEJ) | `BQ1onbEAtSdwoXiMB8Png6akW4tJsKEBX9BpxfmhBDEJ` | $104.9k | $98.4k | +41% | +1188% | +1188% | 150.5x | churn 151x vol/liq; spike (+41% 1h, +1188% 6h) | not scored |
| [FOOD](https://pump.fun/coin/FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump) | `FTu55MyigXns96jz4nTCDDiTCjYJjyrHSceCgG9Upump` | $84.5k | $809.8k | +18% | +27% | +2116% | 101.5x | churn 102x vol/liq | 67 |
| [Sakura](https://pump.fun/coin/9sFGCTjEsBk78uC2bCdxtwuUM1aartbBhe8WQXwRpump) | `9sFGCTjEsBk78uC2bCdxtwuUM1aartbBhe8WQXwRpump` | $42.1k | $261.2k | -1% | +725% | +725% | 39.3x | thin liq $42.1k; churn 39x vol/liq; spike (-1% 1h, +725% 6h) | not scored |
| [Shitcoin](https://pump.fun/coin/8p7GCo3fWJ55LFQbhkBd8hCpw3ACk98PgK7Lsd6Upump) | `8p7GCo3fWJ55LFQbhkBd8hCpw3ACk98PgK7Lsd6Upump` | $25.6k | $111.8k | -42% | -9% | +917% | 18.1x | thin liq $25.6k | not scored |
| [SHARKBUX](https://dexscreener.com/solana/ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v) | `ttwocSxKgj4NpQEUzBaFzLxEFzVdLytUbLsnnjGew9v` | $65.2k | $669.2k | +6% | +10% | +816% | 22.3x | none flagged (still high risk) | 69 |

_Timing: total 155s (discovery 70.9s, screen 1.3s, GT prime 0.3s, scoring 82.5s for 8 coins, 8 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 8/149; Helius 429s 90; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
