# Last scan 2026-11-18T10:29:10Z - mode: helius (box heartbeat stale (1222 min); budget 0/3000)

```
[fast_scan] 120 candidate mints from 10 source tags; 119 with pair data; 28 >= $50,000 liq; 10 pass survivor pre-gates (72s)
[fast_scan] scored GTA6 in 72s
[fast_scan] scored USPR in 80s
[fast_scan] scored GTA in 81s
[fast_scan] scored pippin in 81s
[fast_scan] scored GTA6 in 82s
[fast_scan] scored GTAVI in 82s
[fast_scan] scored Fartcoin  in 83s
[fast_scan] scored BAWSAQ in 83s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-18 10:29 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,428 (+0.4% 24h), ETH $1,806 (+0.8% 24h), SOL $74.83 (+3.5% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +1.4% (mcap $2.07B, vol $393.81M), pump-fun +1.9% (mcap $863.78M, vol $144.20M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [BAWSAQ](https://pump.fun/coin/4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump) | `4La95NEVJdYK9kr375SfKPXnLA8ef8GtsjfVfW27pump` | $87.0k | $521.8k | 1.5 d | h24 +8% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [GTA6](https://dexscreener.com/solana/FTUoPqHYfzktKvNEtmoQyxA9uDtrcgNWduNGJRtEhDA) | `FTUoPqHYfzktKvNEtmoQyxA9uDtrcgNWduNGJRtEhDA` | $116.4k | $76.6k | 1.3 h | h24 +146% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 62* | SKIP | [GTA](https://pump.fun/coin/7KBFymfGAe8MmKEuNersoM59TvpiHzZ76jP7rSLrpump) | `7KBFymfGAe8MmKEuNersoM59TvpiHzZ76jP7rSLrpump` | $92.8k | $1.57M | 7.8 h | h24 +4099% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 68* | SKIP | [GTAVI](https://pump.fun/coin/6wiaCq8oQiupFfeDU4ouAuYnCKXCch581HAmpvrxpump) | `6wiaCq8oQiupFfeDU4ouAuYnCKXCch581HAmpvrxpump` | $111.6k | $2.26M | 10.3 h | h24 +5395% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 4.9% (+6.1) |
| 69* | SKIP | [USPR](https://pump.fun/coin/ELQdP9fkMR5SkeYv1tKJMAFwBZkkCS4iedW2XREkpump) | `ELQdP9fkMR5SkeYv1tKJMAFwBZkkCS4iedW2XREkpump` | $939.9k | $167.89M | 21.8 h | h24 +550231% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 0.6% (+11.3) |
| 70* | SKIP | [GTA6](https://dexscreener.com/solana/GTA6ot7gjnojk8WwAoxKrqDkrLtCPtSfzAikk6zu2koH) | `GTA6ot7gjnojk8WwAoxKrqDkrLtCPtSfzAikk6zu2koH` | $102.4k | $46.2k | 15.4 h | h24 +0% | #2 Authorities / extensions FAIL (+40); #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.85M | $21.04M | 114.8 d | h24 +19% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.3% in 22h (now 431,723) |
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.78M | $21.72M | 738.6 d | h24 +97% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 181,804 (growth n/a: first sighting) |
| 56* | SKIP | [Fartcoin ](https://pump.fun/coin/9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump) | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` | $5.99M | $89.08M | 761.2 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: rug-funder link; holders +0.1% in 52h (now 587,686) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [USPR](https://pump.fun/coin/ELQdP9fkMR5SkeYv1tKJMAFwBZkkCS4iedW2XREkpump) | `ELQdP9fkMR5SkeYv1tKJMAFwBZkkCS4iedW2XREkpump` | $939.9k | $167.87M | +2% | +14% | +550165% | 0.6x | liq/mcap 0.6%; lopsided buys/sells 151.37 | 69 |
| [GTAVI](https://pump.fun/coin/6wiaCq8oQiupFfeDU4ouAuYnCKXCch581HAmpvrxpump) | `6wiaCq8oQiupFfeDU4ouAuYnCKXCch581HAmpvrxpump` | $111.6k | $2.26M | -5% | -15% | +5395% | 13.0x | liq/mcap 4.9% | 68 |
| [GTA](https://pump.fun/coin/7KBFymfGAe8MmKEuNersoM59TvpiHzZ76jP7rSLrpump) | `7KBFymfGAe8MmKEuNersoM59TvpiHzZ76jP7rSLrpump` | $92.0k | $1.54M | +8% | +32% | +4030% | 14.3x | none flagged (still high risk) | 62 |
| [DCI](https://pump.fun/coin/HCNhQCu5nrmWhSE3mo7fRU9eGiGLmi2fnE8omgLpump) | `HCNhQCu5nrmWhSE3mo7fRU9eGiGLmi2fnE8omgLpump` | $84.3k | $775.6k | -7% | +79% | +2115% | 43.0x | churn 43x vol/liq | not scored |
| [JALU](https://pump.fun/coin/BSsmLA6UN8fzJ8qUkV4KwC5LxR7ab3TaUtcwvAyJpump) | `BSsmLA6UN8fzJ8qUkV4KwC5LxR7ab3TaUtcwvAyJpump` | $48.2k | $393.7k | -14% | -39% | +744% | 44.0x | thin liq $48.2k; churn 44x vol/liq | not scored |
| [GTA6](https://dexscreener.com/solana/FTUoPqHYfzktKvNEtmoQyxA9uDtrcgNWduNGJRtEhDA) | `FTUoPqHYfzktKvNEtmoQyxA9uDtrcgNWduNGJRtEhDA` | $115.8k | $75.7k | +52% | +143% | +143% | 68.2x | churn 68x vol/liq | 53 |

_Timing: total 216s (discovery 70.9s, screen 1.1s, GT prime 0.3s, scoring 143.5s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/174; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
