# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 04:48 UTC. Labeled coins: 159 (56 dead/pulled, 103 still alive). Base dead rate 35.2%. Forward 24h samples so far: 89.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 144 | 38% | 89 (62%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 38% of 147 | -35% |
| 3 | 69 | 32% | 47 (68%) | 38% of 90 | -3% |
| 5 | 102 | 46% | 55 (54%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 41% of 130 | -25% |
| 7 | 101 | 40% | 61 (60%) | 29% of 51 | +4% |
| 8 | 116 | 47% | 61 (53%) | 2% of 43 | +12% |
| 9 | 80 | 30% | 56 (70%) | 41% of 79 | -5% |
| 10 | 82 | 59% | 34 (41%) | 10% of 77 | +23% |
| 11 | 159 | 35% | 103 (65%) | n/a | +0% |
| 12 | 159 | 35% | 103 (65%) | n/a | +0% |
| 13 | 159 | 35% | 103 (65%) | n/a | +0% |
| 14 | 159 | 35% | 103 (65%) | n/a | +0% |
| 15 | 159 | 35% | 103 (65%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 36% of 118 | -1% |
| 18 | 159 | 35% | 103 (65%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 35%, n=69)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 35%, n=80)
- check #10: consider treating WARN like FAIL: strong lift (precision 58% vs base 35%, n=82)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 35%, n=41)
