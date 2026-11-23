# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 13:14 UTC. Labeled coins: 170 (68 dead/pulled, 102 still alive). Base dead rate 40.0%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 155 | 43% | 88 (57%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 43% of 158 | -40% |
| 3 | 71 | 34% | 47 (66%) | 44% of 99 | -6% |
| 5 | 113 | 52% | 54 (48%) | 16% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 46% of 141 | -29% |
| 7 | 110 | 45% | 61 (55%) | 34% of 53 | +5% |
| 8 | 126 | 53% | 59 (47%) | 2% of 44 | +13% |
| 9 | 82 | 33% | 55 (67%) | 47% of 88 | -7% |
| 10 | 91 | 64% | 33 (36%) | 13% of 79 | +24% |
| 11 | 170 | 40% | 102 (60%) | n/a | +0% |
| 12 | 170 | 40% | 102 (60%) | n/a | +0% |
| 13 | 170 | 40% | 102 (60%) | n/a | +0% |
| 14 | 170 | 40% | 102 (60%) | n/a | +0% |
| 15 | 170 | 40% | 102 (60%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 41% of 128 | -4% |
| 18 | 170 | 40% | 102 (60%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 40%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 40%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 40%, n=91)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 40%, n=42)
