# Last scan 2026-11-26T14:45:04Z - mode: helius (box heartbeat stale (21 min); budget 437/3000)

```
[fast_scan] 118 candidate mints from 9 source tags; 115 with pair data; 24 >= $50,000 liq; 11 pass survivor pre-gates (72s)
[fast_scan] scored UHI in 71s
[fast_scan] scored DOG in 79s
[fast_scan] scored PUMPCHAN in 80s
[fast_scan] scored ZEC in 80s
[fast_scan] scored SPCX in 81s
[fast_scan] scored pippin in 81s
[fast_scan] scored JIMMY in 83s
# Market scan 2026-11-26 14:45 UTC

Info/risk only, not advice. Risk 0-100, higher = riskier; a low score = fewer red flags found, NOT safe. * = incomplete score.

## Market context
- Majors: BTC $60,697 (+5.4% 24h), ETH $1,698 (+5.0% 24h), SOL $71.22 (+7.2% 24h)
- Fear & Greed: 11 (Extreme Fear)
- Sector 24h (CoinGecko): solana-meme-coins +8.1% (mcap $1.90B, vol $322.61M), pump-fun +7.3% (mcap $788.58M, vol $120.01M)

## Cleanest on real liquidity (younger than 3 days)
Top 4 by free pre-rank (deep liquidity, sane turnover, balanced buys/sells, no spike), then full scorecard. Sorted by risk.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 41* | CAUTION | [JIMMY](https://pump.fun/coin/38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump) | `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump` | $162.9k | $1.11M | 2.7 d | h24 -38% | #7 Insiders / bundles / LP lock WARN (+5); #8 Turnover / bot pattern WARN (+4); #11 not checked (+3) |
| 53* | SKIP | [DOG](https://dexscreener.com/solana/Evjt31qD83BBWGA2UuywYmXHMrAPCueym9bkC5XJz9XY) | `Evjt31qD83BBWGA2UuywYmXHMrAPCueym9bkC5XJz9XY` | $204.7k | $112.8k | 1.3 h | h24 +43% | #7 Insiders / bundles / LP lock FAIL (+14); #5 Token / pool age WARN (+5); #8 Turnover / bot pattern WARN (+4) |
| 59* | SKIP | [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $84.2k | $1.33M | 15.4 h | h24 +3630% | #9 Price momentum FAIL (+14); #3 Liquidity vs market cap WARN (+7); #5 Token / pool age WARN (+5) |
| 67* | SKIP | [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $216.4k | $8.25M | 13.2 h | h24 +26078% | #3 Liquidity vs market cap FAIL (+18); #9 Price momentum FAIL (+14); liq/mcap 2.6% (+8.9) |

## Cleanest survivors (3+ days old, >= $100k liquidity, steady volume)
Must also pass: no rug-funder or same-operator-as-rug link, no coordinated launch, exit test PASS, creator <= 5% (or sold out), no wash FAIL, authorities revoked. Coins that failed a gate are still listed with the gate named.

| Risk | Verdict | Ticker | Mint (full CA) | Liq | Mcap | Age | 24h | Main drivers / notes |
|---|---|---|---|---|---|---|---|---|
| 52* | SKIP | [pippin](https://pump.fun/coin/Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump) | `Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump` | $3.42M | $18.18M | 746.8 d | h24 -1% | #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) FAIL (+5); #8 Turnover / bot pattern WARN (+4); GATES FAILED: rug-funder link; holders -0.0% in 2h (now 182,585) |
| 72* | SKIP | [SPCX](https://dexscreener.com/solana/SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb) | `SPCXxcqXj6e5dJDVNovHN8744zkbhM2bYudU45BimGb` | $4.53M | $13.78M | 183.3 d | h24 +13% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.0% in 2h (now 395,508) |
| 73* | SKIP | [ZEC](https://dexscreener.com/solana/A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) | `A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS` | $6.14M | $17.4k | 406.9 d | h24 +4% | #2 Authorities / extensions FAIL (+40); #7 Insiders / bundles / LP lock FAIL (+14); #6 Top-10 holders (excl. pools/programs) WARN (+4); GATES FAILED: authorities, rug-funder link; holders -0.1% in 50h (now 394,999) |

## Biggest movers (mostly traps)
Largest moves among coins with >= $10k liquidity. Pre-rank red flags only (free data); not scored unless --score-movers.

| Ticker | Mint (full CA) | Liq | Mcap | 1h | 6h | 24h | Vol/liq | Red flags | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [PUMPCHAN](https://pump.fun/coin/Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump) | `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump` | $216.4k | $8.25M | -10% | +79% | +26078% | 22.1x | liq/mcap 2.6% | 67 |
| [UHI](https://pump.fun/coin/Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump) | `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump` | $83.3k | $1.30M | -20% | +15% | +3555% | 13.9x | none flagged (still high risk) | 59 |
| [PAIR](https://pump.fun/coin/32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump) | `32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump` | $37.3k | $257.4k | +100% | +801% | +801% | 23.1x | thin liq $37.3k; spike (+100% 1h, +801% 6h) | not scored |
| [NORFEATH](https://pump.fun/coin/3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump) | `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump` | $47.0k | $390.4k | -15% | -22% | +751% | 47.2x | thin liq $47.0k; churn 47x vol/liq | not scored |
| [Irochan](https://pump.fun/coin/BSMz6chW26adx25hkfRZvmTSu6q4d3ieixPx73hQpump) | `BSMz6chW26adx25hkfRZvmTSu6q4d3ieixPx73hQpump` | $17.5k | $65.9k | +129% | +129% | +129% | 8.9x | thin liq $17.5k; spike (+129% 1h, +129% 6h); < 1h old | not scored |
| [Zero](https://pump.fun/coin/DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump) | `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump` | $34.1k | $172.0k | -22% | -37% | +492% | 125.5x | thin liq $34.1k; churn 125x vol/liq | not scored |

_Timing: total 155s (discovery 71.2s, screen 1.2s, GT prime 0.4s, scoring 82.7s for 7 coins, 7 newly scored). ~20 Helius credits (smart-money discovery 20). HTTP cache hits 7/142; Helius 429s 80; DEX Screener ok._

_Full reports: out/<mint>.md (+ .json)_
```
