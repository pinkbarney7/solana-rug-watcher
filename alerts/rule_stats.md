# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 04:56 UTC. Labeled coins: 193 (80 dead/pulled, 113 still alive). Base dead rate 41.5%. Forward 24h samples so far: 117.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 177 | 45% | 98 (55%) | 0% of 14 | +3% |
| 2 | 13 | 0% | 13 (100%) | 44% of 180 | -41% |
| 3 | 79 | 33% | 53 (67%) | 47% of 114 | -9% |
| 5 | 131 | 53% | 61 (47%) | 16% of 62 | +12% |
| 6 | 31 | 10% | 28 (90%) | 48% of 161 | -32% |
| 7 | 126 | 48% | 66 (52%) | 32% of 60 | +6% |
| 8 | 147 | 54% | 68 (46%) | 2% of 46 | +12% |
| 9 | 90 | 32% | 61 (68%) | 50% of 103 | -9% |
| 10 | 104 | 66% | 35 (34%) | 12% of 89 | +25% |
| 11 | 193 | 41% | 113 (59%) | n/a | +0% |
| 12 | 193 | 41% | 113 (59%) | n/a | +0% |
| 13 | 193 | 41% | 113 (59%) | n/a | +0% |
| 14 | 193 | 41% | 113 (59%) | n/a | +0% |
| 15 | 193 | 41% | 113 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 151 | -6% |
| 18 | 193 | 41% | 113 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 33% vs base 42%, n=79)
- check #6: lower weight: flagged coins die no more often than average (precision 10% vs base 42%, n=31)
- check #9: lower weight: flagged coins die no more often than average (precision 32% vs base 42%, n=90)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 42%, n=104)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=42)
