# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 05:50 UTC. Labeled coins: 215 (90 dead/pulled, 125 still alive). Base dead rate 41.9%. Forward 24h samples so far: 143.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 198 | 45% | 109 (55%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 45% of 200 | -42% |
| 3 | 83 | 36% | 53 (64%) | 45% of 132 | -6% |
| 5 | 140 | 57% | 60 (43%) | 13% of 75 | +15% |
| 6 | 34 | 9% | 31 (91%) | 48% of 180 | -33% |
| 7 | 138 | 49% | 71 (51%) | 35% of 62 | +7% |
| 8 | 160 | 56% | 71 (44%) | 2% of 55 | +14% |
| 9 | 94 | 36% | 60 (64%) | 46% of 121 | -6% |
| 10 | 120 | 64% | 43 (36%) | 14% of 95 | +22% |
| 11 | 215 | 42% | 125 (58%) | n/a | +0% |
| 12 | 215 | 42% | 125 (58%) | n/a | +0% |
| 13 | 215 | 42% | 125 (58%) | n/a | +0% |
| 14 | 215 | 42% | 125 (58%) | n/a | +0% |
| 15 | 215 | 42% | 125 (58%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 44% of 170 | -9% |
| 18 | 215 | 42% | 125 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=83)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 42%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=94)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 42%, n=120)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 42%, n=45)
