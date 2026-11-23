# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 02:14 UTC. Labeled coins: 159 (55 dead/pulled, 104 still alive). Base dead rate 34.6%. Forward 24h samples so far: 89.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 144 | 38% | 90 (62%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 37% of 147 | -35% |
| 3 | 69 | 30% | 48 (70%) | 38% of 90 | -4% |
| 5 | 102 | 45% | 56 (55%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 40% of 130 | -24% |
| 7 | 101 | 40% | 61 (60%) | 27% of 51 | +5% |
| 8 | 116 | 47% | 62 (53%) | 2% of 43 | +12% |
| 9 | 80 | 29% | 57 (71%) | 41% of 79 | -6% |
| 10 | 82 | 59% | 34 (41%) | 9% of 77 | +24% |
| 11 | 159 | 35% | 104 (65%) | n/a | +0% |
| 12 | 159 | 35% | 104 (65%) | n/a | +0% |
| 13 | 159 | 35% | 104 (65%) | n/a | +0% |
| 14 | 159 | 35% | 104 (65%) | n/a | +0% |
| 15 | 159 | 35% | 104 (65%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 35% of 118 | -0% |
| 18 | 159 | 35% | 104 (65%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 35%, n=69)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 35%, n=80)
- check #10: consider treating WARN like FAIL: strong lift (precision 58% vs base 35%, n=82)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 35%, n=41)
