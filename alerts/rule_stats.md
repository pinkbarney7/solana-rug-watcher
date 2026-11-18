# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-18 02:23 UTC. Labeled coins: 117 (39 dead/pulled, 78 still alive). Base dead rate 33.3%. Forward 24h samples so far: 78.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 102 | 37% | 64 (63%) | 0% of 13 | +4% |
| 2 | 8 | 0% | 8 (100%) | 36% of 109 | -33% |
| 3 | 47 | 28% | 34 (72%) | 37% of 70 | -6% |
| 5 | 69 | 46% | 37 (54%) | 15% of 48 | +13% |
| 6 | 22 | 14% | 19 (86%) | 38% of 94 | -20% |
| 7 | 80 | 38% | 50 (62%) | 29% of 31 | +4% |
| 8 | 83 | 47% | 44 (53%) | 0% of 34 | +14% |
| 9 | 53 | 28% | 38 (72%) | 38% of 64 | -5% |
| 10 | 65 | 55% | 29 (45%) | 6% of 52 | +22% |
| 11 | 117 | 33% | 78 (67%) | n/a | +0% |
| 12 | 117 | 33% | 78 (67%) | n/a | +0% |
| 13 | 117 | 33% | 78 (67%) | n/a | +0% |
| 14 | 117 | 33% | 78 (67%) | n/a | +0% |
| 15 | 117 | 33% | 78 (67%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 34% of 77 | -1% |
| 18 | 117 | 33% | 78 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 28% vs base 33%, n=47)
- check #9: lower weight: flagged coins die no more often than average (precision 28% vs base 33%, n=53)
- check #10: consider treating WARN like FAIL: strong lift (precision 55% vs base 33%, n=65)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=40)
