# Last scan 2026-11-15T23:22:53Z - mode: helius (box heartbeat stale (7804 min); budget 50/3000)

```
[fast_scan] 132 candidate mints from 10 source tags; 129 with pair data; 24 >= $50,000 liq; 13 pass survivor pre-gates (73s)
[fast_scan] scored USPR in 69s
[fast_scan] scored VINE in 77s
[fast_scan] scored SPCX in 77s
[fast_scan] scored CATE in 78s
[fast_scan] scored BUTTHOLE in 79s
# Market scan 2026-11-15 23:22 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $64,881 (+1.8% 24h), ETH $1,820 (+4.1% 24h), SOL $72.01 (+3.7% 24h)
- Fear & Greed: 10 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +6.6% (mcap $2.10B, vol $417.46M), pump-fun +8.8% (mcap $899.81M, vol $161.28M)

## Cleanest on real liquidity (younger than 3 days)
Top 2 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 44* | CAUTION | [BUTTHOLE](https://pump.fun/coin/4B8CdHPZ8ng1CtMP2Jk2W8wGAwJ5nJnap1deVsz2pump) | `4B8CdHPZ8ng1CtMP2Jk2W8wGAwJ5nJnap1deVsz2pump` | $208.1k | $494.5k | 8.5 h | h24 +1% | #5 Token / pool age WARN (+5); #7 Insiders / bundles / LP lock WARN (+5); #11 not checked (+3) |
| 67* | SKIP | [USPR](https://pump.fun/coin/DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump) | `DFev755KT1b6nkfAFNj1fyRQMwoVzNywsSBEBamepump` | $972.9k | $186.61M | 1.1 d | h24 +88% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 0.5% (+11.4) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 50* | SKIP | [VINE](https://pump.fun/coin/6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump) | `6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump` | $1.69M | $12.41M | 662.0 d | h24 +173% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders 343,853 (growth n/a: first sighting) |
| 50* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $1.69M | $17.06M | 112.3 d | h24 +14% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders 429,680 (growth n/a: first sighting) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.29M | $13.13M | 172.6 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders 370,517 (growth n/a: first sighting) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [BJB](https://pump.fun/coin/CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump) | `CHuLmJXz8F3YXUyv984PRxeECfSvqD5MZ3W1FoDmpump` | $79.7k | $1.22M | -18% | +2993% | +2993% | 10.5x | spike (-18% 1h, +2993% 6h) | not scored |
| [ANIME](https://dexscreener.com/solana/6XGN3oMrjLuWvDyvHL1VZNNPN5d7dTspD9N7LKjAnime) | `6XGN3oMrjLuWvDyvHL1VZNNPN5d7dTspD9N7LKjAnime` | $23.5k | $109.6k | +272% | +272% | +272% | 9.4x | thin liq $23.5k; spike (+272% 1h, +272% 6h); < 1h old | not scored |
| [Retire](https://pump.fun/coin/DQSHcUsHEKKz5gXzpj4Xp3ioEjmfNB5obb3saDFMpump) | `DQSHcUsHEKKz5gXzpj4Xp3ioEjmfNB5obb3saDFMpump` | $29.0k | $169.5k | -3% | +378% | +378% | 9.4x | thin liq $29.0k; spike (-3% 1h, +378% 6h); lopsided buys/sells 3.86 | not scored |
| [WIGGLES](https://pump.fun/coin/2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump) | `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump` | $19.3k | $75.0k | +72% | +161% | +161% | 13.5x | thin liq $19.3k | not scored |
| [GTAVI](https://pump.fun/coin/HQjXLbFPkpJP1BmF55DgXj9F6614FURvGLKuyCZQpump) | `HQjXLbFPkpJP1BmF55DgXj9F6614FURvGLKuyCZQpump` | $31.2k | $119.7k | -14% | +168% | +168% | 27.8x | thin liq $31.2k; churn 28x vol/liq | not scored |
| [Socks](https://pump.fun/coin/FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump) | `FS1pBmZKp2Qw1atC64GoLamHstECAos9ot8bGPgDpump` | $29.1k | $136.9k | +10% | +10% | +370% | 72.3x | thin liq $29.1k; churn 72x vol/liq | not scored |

_Timing: total 153s (discovery 71.5s, screen 1.5s, GT prime 0.3s, scoring 79.4s for 5 coins, 5 newly scored). ~10 Helius credits (smart-money discovery 10). HTTP cache hits 7/111; Helius 429s 65; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
