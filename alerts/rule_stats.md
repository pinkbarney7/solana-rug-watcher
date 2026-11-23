# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 12:59 UTC. Labeled coins: 169 (67 dead/pulled, 102 still alive). Base dead rate 39.6%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 154 | 43% | 88 (57%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 43% of 157 | -40% |
| 3 | 71 | 34% | 47 (66%) | 44% of 98 | -6% |
| 5 | 112 | 52% | 54 (48%) | 16% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 46% of 140 | -29% |
| 7 | 109 | 44% | 61 (56%) | 34% of 53 | +4% |
| 8 | 125 | 53% | 59 (47%) | 2% of 44 | +13% |
| 9 | 82 | 33% | 55 (67%) | 46% of 87 | -7% |
| 10 | 90 | 63% | 33 (37%) | 13% of 79 | +24% |
| 11 | 169 | 40% | 102 (60%) | n/a | +0% |
| 12 | 169 | 40% | 102 (60%) | n/a | +0% |
| 13 | 169 | 40% | 102 (60%) | n/a | +0% |
| 14 | 169 | 40% | 102 (60%) | n/a | +0% |
| 15 | 169 | 40% | 102 (60%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 41% of 128 | -5% |
| 18 | 169 | 40% | 102 (60%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 40%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 40%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 63% vs base 40%, n=90)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 40%, n=41)
