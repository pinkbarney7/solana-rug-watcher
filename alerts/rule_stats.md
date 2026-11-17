# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 03:55 UTC. Labeled coins: 96 (24 dead/pulled, 72 still alive). Base dead rate 25.0%. Forward 24h samples so far: 61.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 84 | 27% | 61 (73%) | 0% of 10 | +2% |
| 2 | 8 | 0% | 8 (100%) | 27% of 88 | -25% |
| 3 | 42 | 17% | 35 (83%) | 31% of 54 | -8% |
| 5 | 54 | 33% | 36 (67%) | 14% of 42 | +8% |
| 6 | 22 | 14% | 19 (86%) | 29% of 73 | -11% |
| 7 | 63 | 29% | 45 (71%) | 21% of 28 | +4% |
| 8 | 65 | 37% | 41 (63%) | 0% of 31 | +12% |
| 9 | 43 | 14% | 37 (86%) | 34% of 53 | -11% |
| 10 | 50 | 42% | 29 (58%) | 7% of 46 | +17% |
| 11 | 96 | 25% | 72 (75%) | n/a | +0% |
| 12 | 96 | 25% | 72 (75%) | n/a | +0% |
| 13 | 96 | 25% | 72 (75%) | n/a | +0% |
| 14 | 96 | 25% | 72 (75%) | n/a | +0% |
| 15 | 96 | 25% | 72 (75%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 24% of 58 | +1% |
| 18 | 96 | 25% | 72 (75%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 25%, n=42)
- check #9: lower weight: flagged coins die no more often than average (precision 14% vs base 25%, n=43)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 25%, n=38)
