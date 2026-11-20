# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-20 13:03 UTC. Labeled coins: 138 (46 dead/pulled, 92 still alive). Base dead rate 33.3%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 123 | 37% | 78 (63%) | 0% of 13 | +3% |
| 2 | 11 | 0% | 11 (100%) | 36% of 127 | -33% |
| 3 | 59 | 31% | 41 (69%) | 35% of 79 | -3% |
| 5 | 86 | 43% | 49 (57%) | 17% of 52 | +10% |
| 6 | 27 | 11% | 24 (89%) | 39% of 110 | -22% |
| 7 | 89 | 37% | 56 (63%) | 28% of 43 | +4% |
| 8 | 101 | 46% | 55 (54%) | 0% of 37 | +12% |
| 9 | 67 | 28% | 48 (72%) | 38% of 71 | -5% |
| 10 | 72 | 57% | 31 (43%) | 8% of 66 | +24% |
| 11 | 138 | 33% | 92 (67%) | n/a | +0% |
| 12 | 138 | 33% | 92 (67%) | n/a | +0% |
| 13 | 138 | 33% | 92 (67%) | n/a | +0% |
| 14 | 138 | 33% | 92 (67%) | n/a | +0% |
| 15 | 138 | 33% | 92 (67%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 34% of 98 | -1% |
| 18 | 138 | 33% | 92 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 33%, n=59)
- check #9: lower weight: flagged coins die no more often than average (precision 28% vs base 33%, n=67)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 33%, n=72)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=40)
