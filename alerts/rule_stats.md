# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-19 23:42 UTC. Labeled coins: 133 (44 dead/pulled, 89 still alive). Base dead rate 33.1%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 118 | 36% | 75 (64%) | 0% of 13 | +3% |
| 2 | 10 | 0% | 10 (100%) | 36% of 123 | -33% |
| 3 | 55 | 29% | 39 (71%) | 36% of 78 | -4% |
| 5 | 83 | 45% | 46 (55%) | 14% of 50 | +11% |
| 6 | 26 | 12% | 23 (88%) | 39% of 106 | -22% |
| 7 | 87 | 36% | 56 (64%) | 30% of 40 | +3% |
| 8 | 97 | 45% | 53 (55%) | 0% of 36 | +12% |
| 9 | 62 | 29% | 44 (71%) | 37% of 71 | -4% |
| 10 | 70 | 56% | 31 (44%) | 8% of 63 | +23% |
| 11 | 133 | 33% | 89 (67%) | n/a | +0% |
| 12 | 133 | 33% | 89 (67%) | n/a | +0% |
| 13 | 133 | 33% | 89 (67%) | n/a | +0% |
| 14 | 133 | 33% | 89 (67%) | n/a | +0% |
| 15 | 133 | 33% | 89 (67%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 33% of 93 | -1% |
| 18 | 133 | 33% | 89 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 29% vs base 33%, n=55)
- check #7: lower weight: flagged coins die no more often than average (precision 36% vs base 33%, n=87)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 33%, n=62)
- check #10: consider treating WARN like FAIL: strong lift (precision 56% vs base 33%, n=70)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=40)
