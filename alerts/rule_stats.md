# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-21 09:20 UTC. Labeled coins: 144 (48 dead/pulled, 96 still alive). Base dead rate 33.3%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 129 | 36% | 82 (64%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 36% of 132 | -33% |
| 3 | 60 | 33% | 40 (67%) | 33% of 84 | +0% |
| 5 | 88 | 44% | 49 (56%) | 16% of 56 | +11% |
| 6 | 27 | 11% | 24 (89%) | 39% of 116 | -22% |
| 7 | 94 | 36% | 60 (64%) | 30% of 44 | +3% |
| 8 | 104 | 46% | 56 (54%) | 0% of 40 | +13% |
| 9 | 70 | 30% | 49 (70%) | 36% of 74 | -3% |
| 10 | 73 | 58% | 31 (42%) | 8% of 71 | +24% |
| 11 | 144 | 33% | 96 (67%) | n/a | +0% |
| 12 | 144 | 33% | 96 (67%) | n/a | +0% |
| 13 | 144 | 33% | 96 (67%) | n/a | +0% |
| 14 | 144 | 33% | 96 (67%) | n/a | +0% |
| 15 | 144 | 33% | 96 (67%) | n/a | +0% |
| 16 | 41 | 32% | 28 (68%) | 34% of 103 | -2% |
| 18 | 144 | 33% | 96 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 33% vs base 33%, n=60)
- check #7: lower weight: flagged coins die no more often than average (precision 36% vs base 33%, n=94)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 33%, n=70)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 33%, n=73)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=41)
