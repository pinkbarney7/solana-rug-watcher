# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 11:11 UTC. Labeled coins: 167 (65 dead/pulled, 102 still alive). Base dead rate 38.9%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 152 | 42% | 88 (58%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 42% of 155 | -39% |
| 3 | 71 | 34% | 47 (66%) | 43% of 96 | -5% |
| 5 | 110 | 51% | 54 (49%) | 16% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 45% of 138 | -28% |
| 7 | 107 | 43% | 61 (57%) | 34% of 53 | +4% |
| 8 | 123 | 52% | 59 (48%) | 2% of 44 | +13% |
| 9 | 82 | 33% | 55 (67%) | 45% of 85 | -6% |
| 10 | 88 | 62% | 33 (38%) | 13% of 79 | +24% |
| 11 | 167 | 39% | 102 (61%) | n/a | +0% |
| 12 | 167 | 39% | 102 (61%) | n/a | +0% |
| 13 | 167 | 39% | 102 (61%) | n/a | +0% |
| 14 | 167 | 39% | 102 (61%) | n/a | +0% |
| 15 | 167 | 39% | 102 (61%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 40% of 126 | -5% |
| 18 | 167 | 39% | 102 (61%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 39%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 39%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 62% vs base 39%, n=88)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 39%, n=41)
