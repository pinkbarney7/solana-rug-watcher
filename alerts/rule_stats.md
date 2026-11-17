# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 20:05 UTC. Labeled coins: 115 (34 dead/pulled, 81 still alive). Base dead rate 29.6%. Forward 24h samples so far: 75.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 100 | 33% | 67 (67%) | 0% of 13 | +3% |
| 2 | 8 | 0% | 8 (100%) | 32% of 107 | -30% |
| 3 | 45 | 18% | 37 (82%) | 37% of 70 | -12% |
| 5 | 69 | 41% | 41 (59%) | 13% of 46 | +11% |
| 6 | 22 | 14% | 19 (86%) | 34% of 92 | -16% |
| 7 | 78 | 35% | 51 (65%) | 23% of 31 | +5% |
| 8 | 81 | 42% | 47 (58%) | 0% of 34 | +12% |
| 9 | 52 | 19% | 42 (81%) | 38% of 63 | -10% |
| 10 | 63 | 49% | 32 (51%) | 6% of 52 | +20% |
| 11 | 115 | 30% | 81 (70%) | n/a | +0% |
| 12 | 115 | 30% | 81 (70%) | n/a | +0% |
| 13 | 115 | 30% | 81 (70%) | n/a | +0% |
| 14 | 115 | 30% | 81 (70%) | n/a | +0% |
| 15 | 115 | 30% | 81 (70%) | n/a | +0% |
| 16 | 40 | 30% | 28 (70%) | 29% of 75 | +0% |
| 18 | 115 | 30% | 81 (70%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 30%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 19% vs base 30%, n=52)
- check #16: lower weight: flagged coins die no more often than average (precision 30% vs base 30%, n=40)
