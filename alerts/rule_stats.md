# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 07:12 UTC. Labeled coins: 217 (93 dead/pulled, 124 still alive). Base dead rate 42.9%. Forward 24h samples so far: 145.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 200 | 46% | 108 (54%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 46% of 202 | -43% |
| 3 | 84 | 38% | 52 (62%) | 46% of 133 | -5% |
| 5 | 142 | 58% | 59 (42%) | 13% of 75 | +16% |
| 6 | 34 | 9% | 31 (91%) | 49% of 182 | -34% |
| 7 | 139 | 49% | 71 (51%) | 38% of 63 | +6% |
| 8 | 162 | 57% | 70 (43%) | 2% of 55 | +14% |
| 9 | 95 | 38% | 59 (62%) | 47% of 122 | -5% |
| 10 | 121 | 64% | 43 (36%) | 16% of 96 | +22% |
| 11 | 217 | 43% | 124 (57%) | n/a | +0% |
| 12 | 217 | 43% | 124 (57%) | n/a | +0% |
| 13 | 217 | 43% | 124 (57%) | n/a | +0% |
| 14 | 217 | 43% | 124 (57%) | n/a | +0% |
| 15 | 217 | 43% | 124 (57%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 45% of 172 | -10% |
| 18 | 217 | 43% | 124 (57%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 43%, n=84)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 43%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 43%, n=95)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 43%, n=121)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 43%, n=45)
