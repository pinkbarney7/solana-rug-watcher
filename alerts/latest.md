# Last scan 2026-11-12T00:35:25Z - mode: helius (box heartbeat stale (2116 min); budget 30/3000)

```
[fast_scan] 156 candidate mints from 11 source tags; 153 with pair data; 33 >= $50,000 liq; 10 pass survivor pre-gates (73s)
[fast_scan] scored KMNO in 72s
[fast_scan] scored USPR in 80s
[fast_scan] scored FOTF in 81s
[fast_scan] scored SPCX in 81s
[fast_scan] scored LuckyCoin in 82s
[fast_scan] scored USOE in 82s
[fast_scan] scored UODF in 82s
[fast_scan] scored ZEC in 83s
[fast_scan] scored CATE in 71s
# Market scan 2026-11-12 00:35 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $74,054 (+0.7% 24h), ETH $2,061 (+0.5% 24h), SOL $83.67 (+0.4% 24h)
- Fear & Greed: 28 (Fear)
- Sector 24h (CoinGecko): solana-meme-coins -0.8% (mcap $2.42B, vol $352.92M), pump-fun +2.6% (mcap $963.93M, vol $198.24M)

## Cleanest on real liquidity (younger than 3 days)
Top 6 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 59* | SKIP | [USPR](https://pump.fun/coin/d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump) | `d7UsZ3yyyncVnQm9yP248ekJ6o3dV4CtWi4d2cCpump` | $1.36M | $185.02M | 2.4 d | h24 +32% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.7% (+11.1); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UODF](https://pump.fun/coin/Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump) | `Wb9zosTQgemQ1zK9eEcmifmRvoyJBxBF4jJh3etpump` | $1.17M | $135.85M | 2.4 d | h24 +49% | #3 Liquidity vs market cap FAIL (+18); liq/mcap 0.9% (+11); #8 Turnover / bot pattern WARN (+4) |
| 68* | SKIP | [KMNO](https://dexscreener.com/solana/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS) | `KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS` | $3.21M | $190.06M | 926.6 d | h24 -1% | #3 Liquidity vs market cap FAIL (+18); #7 Insiders / bundles / LP lock FAIL (+14); liq/mcap 1.7% (+10) |
| 71* | SKIP | [USOE](https://pump.fun/coin/nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump) | `nDUSTtA3bAR4CT3MQqnatnjcbERV62LE7X1A3abpump` | $1.05M | $108.84M | 2.4 d | h24 +41% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.0% (+10.8) |
| 71* | SKIP | [FOTF](https://pump.fun/coin/q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump) | `q8So8CFBNUdR9LGih3CR6PS552XuJGs2qLvfnCtpump` | $993.3k | $98.08M | 2.4 d | h24 +44% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #3 Liquidity vs market cap FAIL (+18); liq/mcap 1.0% (+10.8) |
| 72* | SKIP | [LuckyCoin](https://pump.fun/coin/89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump) | `89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump` | $64.1k | $718.6k | 8.6 h | h24 +2006% | #16 Exit liquidity (Jupiter quotes) FAIL (+24); #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 51* | SKIP | [CATE](https://pump.fun/coin/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | `Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump` | $2.10M | $22.86M | 108.3 d | h24 -3% | #7 Insiders / bundles / LP lock FAIL (+14); #3 Liquidity vs market cap WARN (+7); #11 not checked (+3); GATES FAILED: rug-funder link; holders +0.0% in 6h (now 427,366) |
| 70* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.64M | $12.87M | 168.7 d | h24 -4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #11 not checked (+3); GATES FAILED: authorities, rug-funder link; holders +2.7% in 35h (now 356,167) |
| 80* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $9.37M | $24.3k | 392.3 d | h24 -5% | #2 Authorities / extensions FAIL (+40); #16 Exit liquidity (Jupiter quotes) FAIL (+24); #7 Insiders / bundles / LP lock FAIL (+14); GATES FAILED: authorities, rug-funder link, exit test; holders -0.0% in 25h (now 389,302) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [Max](https://pump.fun/coin/5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump) | `5qaP7oKUqKffwwo5DaEqDoTtsBLMpdbQTxEkCDaTpump` | $290.0k | $5.86M | +34% | +15745% | +15745% | 158.5x | liq/mcap 5.0%; churn 158x vol/liq; spike (+34% 1h, +15745% 6h) | not scored |
| [HUNG](https://pump.fun/coin/4xgqefa5WcdHWKXzqvM9MRJqWYGaHVEUnpUL4Vq5pump) | `4xgqefa5WcdHWKXzqvM9MRJqWYGaHVEUnpUL4Vq5pump` | $79.0k | $628.4k | +69% | +5981% | +6255% | 36.3x | churn 36x vol/liq; spike (+69% 1h, +5981% 6h) | not scored |
| [:3](https://pump.fun/coin/FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump) | `FSkyjfqB26u6c2GSgpACrjbxp9yQAR8rutxprVNppump` | $24.1k | $92.5k | +7% | +40% | +3428% | 24.6x | thin liq $24.1k | not scored |
| [LuckyCoin](https://pump.fun/coin/89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump) | `89iRVoDVPd8tuRrMyhgPfe58eDneasPsdEVu5AUMpump` | $61.1k | $718.6k | +32% | -6% | +2006% | 15.7x | none flagged (still high risk) | 72 |
| [mihao](https://dexscreener.com/solana/Cs68zKac7JZZKXQLZtBUnnuaYTQptJpxexisAGu61AyQ) | `Cs68zKac7JZZKXQLZtBUnnuaYTQptJpxexisAGu61AyQ` | $23.5k | $19.2k | +140% | +140% | +140% | 2.7x | thin liq $23.5k; spike (+140% 1h, +140% 6h); < 1h old | not scored |
| [vibeshift](https://dexscreener.com/solana/8xMxrxPTCYJRwumZEpMfkRjNry4UJoRy75J4B96eJTkM) | `8xMxrxPTCYJRwumZEpMfkRjNry4UJoRy75J4B96eJTkM` | $18.7k | $12.3k | -97% | -92% | -92% | 62.0x | thin liq $18.7k; churn 62x vol/liq; dumping -92% 24h | not scored |

_Timing: total 216s (discovery 70.9s, screen 1.6s, GT prime 0.4s, scoring 143.3s for 9 coins, 9 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 9/162; Helius 429s 100; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
