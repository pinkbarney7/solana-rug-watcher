# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-21 02:01 UTC. Labeled coins: 141 (46 dead/pulled, 95 still alive). Base dead rate 32.6%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 126 | 36% | 81 (64%) | 0% of 13 | +3% |
| 2 | 11 | 0% | 11 (100%) | 35% of 130 | -33% |
| 3 | 59 | 31% | 41 (69%) | 34% of 82 | -2% |
| 5 | 87 | 43% | 50 (57%) | 17% of 54 | +10% |
| 6 | 27 | 11% | 24 (89%) | 38% of 113 | -22% |
| 7 | 92 | 36% | 59 (64%) | 28% of 43 | +3% |
| 8 | 103 | 45% | 57 (55%) | 0% of 38 | +12% |
| 9 | 68 | 28% | 49 (72%) | 37% of 73 | -5% |
| 10 | 72 | 57% | 31 (43%) | 7% of 69 | +24% |
| 11 | 141 | 33% | 95 (67%) | n/a | +0% |
| 12 | 141 | 33% | 95 (67%) | n/a | +0% |
| 13 | 141 | 33% | 95 (67%) | n/a | +0% |
| 14 | 141 | 33% | 95 (67%) | n/a | +0% |
| 15 | 141 | 33% | 95 (67%) | n/a | +0% |
| 16 | 41 | 32% | 28 (68%) | 33% of 100 | -1% |
| 18 | 141 | 33% | 95 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 33%, n=59)
- check #9: lower weight: flagged coins die no more often than average (precision 28% vs base 33%, n=68)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 33%, n=72)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=41)
