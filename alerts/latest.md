# Last scan 2026-11-17T20:05:07Z - mode: helius (box heartbeat stale (358 min); budget 400/3000)

```
[fast_scan] 126 candidate mints from 9 source tags; 125 with pair data; 30 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored BAWSAQ in 72s
[fast_scan] scored ZEC in 81s
[fast_scan] scored VINE in 81s
[fast_scan] scored bul in 83s
[fast_scan] scored ANT in 88s
[fast_scan] scored SPCX in 90s
[fast_scan] scored HOGE in 92s
[fast_scan] scored GTA in 96s
# Market scan 2026-11-17 20:04 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $63,694 (-2.0% 24h), ETH $1,790 (-1.8% 24h), SOL $72.77 (+1.8% 24h)
- Fear & Greed: 12 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.1% (mcap $2.04B, vol $402.09M), pump-fun -1.8% (mcap $835.35M, vol $153.03M)

## Cleanest on real liquidity (younger than 3 days)
Top 5 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [HOGE](https://pump.fun/coin/FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump) | `FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump` | $104.9k | $559.9k | 2.6 d | h24 -24% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 45* | CAUTION | [bul](https://dexscreener.com/solana/Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv) | `Dys6SYbjUsy8kksaqrXqo5L2GzgCYDiguGGcS8B5rkrv` | $52.2k | $87.1k | 17.5 h | h24 -19% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 46* | CAUTION | [GTA](https://pump.fun/coin/2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump) | `2NWgu4fqN2AxS5pp5v3f3SH54qArP9JepQFJm58gpump` | $81.7k | $1.17M | 1.1 d | h24 +78% | #3 Liquidity vs market cap WARN (+7); #8 Turnover / bot pattern WARN (+4); liq/mcap 7.0% (+3.6) |
| 55* | SKIP | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $97.4k | $723.1k | 22.6 h | h24 +2407% | #9 Price momentum FAIL (+14); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |
| 59* | SKIP | [ANT](https://dexscreener.com/solana/ELR9i6Z7uhtZMWqkySYNnDhviSuSMA7nnyZ1BocKkEK) | `ELR9i6Z7uhtZMWqkySYNnDhviSuSMA7nnyZ1BocKkEK` | $148.4k | $1.73M | 1.1 d | h24 +279% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #9 Price momentum WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 48* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.29M | $7.12M | 663.8 d | h24 -18% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 7h (now 344,399) |
| 72* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.43M | $22.7k | 398.1 d | h24 +2% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders +0.1% in 7h (now 392,811) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.81M | $12.89M | 174.5 d | h24 +1% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.1% in 7h (now 380,290) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [JALU](https://pump.fun/coin/BSsmLA6UN8fzJ8qUkV4KwC5LxR7ab3TaUtcwvAyJpump) | `BSsmLA6UN8fzJ8qUkV4KwC5LxR7ab3TaUtcwvAyJpump` | $65.3k | $802.8k | +183% | +1622% | +1622% | 10.2x | spike (+183% 1h, +1622% 6h) | not scored |
| [CSI](https://pump.fun/coin/4z7LXmQewWk5LLDTbTZEeGpeUhTFR1dHGvg7ckhbpump) | `4z7LXmQewWk5LLDTbTZEeGpeUhTFR1dHGvg7ckhbpump` | $30.8k | $195.5k | +436% | +436% | +436% | 4.9x | thin liq $30.8k; spike (+436% 1h, +436% 6h); lopsided buys/sells 5.26; < 1h old | not scored |
| [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $74.2k | $707.6k | +28% | +15% | +2353% | 78.5x | churn 79x vol/liq | 55 |
| [GM](https://pump.fun/coin/CSmSeS8XkxXTVa47LHtY9Mx1FSSwqw94tjqy4te3pump) | `CSmSeS8XkxXTVa47LHtY9Mx1FSSwqw94tjqy4te3pump` | $37.6k | $282.2k | +22% | +797% | +797% | 7.9x | thin liq $37.6k; spike (+22% 1h, +797% 6h) | not scored |
| [Rex](https://pump.fun/coin/6MjDb45kzriv6cpW6oaDjZGw1rujmpA185dHcvZzpump) | `6MjDb45kzriv6cpW6oaDjZGw1rujmpA185dHcvZzpump` | $39.8k | $306.7k | -54% | +674% | +674% | 23.4x | thin liq $39.8k; spike (-54% 1h, +674% 6h); lopsided buys/sells 3.92 | not scored |
| [ViceCat](https://pump.fun/coin/58tcG4YSeH3c7JeEBrngipHJ2Ph3SX89EP6ZH4aupump) | `58tcG4YSeH3c7JeEBrngipHJ2Ph3SX89EP6ZH4aupump` | $23.8k | $121.1k | +237% | +237% | +237% | 3.9x | thin liq $23.8k; spike (+237% 1h, +237% 6h); lopsided buys/sells 7.75; < 1h old | not scored |

_Timing: total 169s (discovery 71.5s, screen 1.4s, GT prime 0.4s, scoring 95.7s for 8 coins, 8 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 8/169; Helius 429s 95; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
