# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 16:05 UTC. Labeled coins: 171 (69 dead/pulled, 102 still alive). Base dead rate 40.4%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 156 | 44% | 88 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 43% of 159 | -40% |
| 3 | 71 | 34% | 47 (66%) | 45% of 100 | -7% |
| 5 | 114 | 53% | 54 (47%) | 16% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 46% of 142 | -30% |
| 7 | 111 | 45% | 61 (55%) | 34% of 53 | +5% |
| 8 | 127 | 54% | 59 (46%) | 2% of 44 | +13% |
| 9 | 82 | 33% | 55 (67%) | 47% of 89 | -7% |
| 10 | 92 | 64% | 33 (36%) | 13% of 79 | +24% |
| 11 | 171 | 40% | 102 (60%) | n/a | +0% |
| 12 | 171 | 40% | 102 (60%) | n/a | +0% |
| 13 | 171 | 40% | 102 (60%) | n/a | +0% |
| 14 | 171 | 40% | 102 (60%) | n/a | +0% |
| 15 | 171 | 40% | 102 (60%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 129 | -5% |
| 18 | 171 | 40% | 102 (60%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 40%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 40%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 40%, n=92)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 40%, n=42)
