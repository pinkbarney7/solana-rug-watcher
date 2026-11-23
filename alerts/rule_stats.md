# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 10:18 UTC. Labeled coins: 166 (61 dead/pulled, 105 still alive). Base dead rate 36.7%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 151 | 40% | 91 (60%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 40% of 154 | -37% |
| 3 | 71 | 31% | 49 (69%) | 41% of 95 | -6% |
| 5 | 109 | 48% | 57 (52%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 42% of 137 | -26% |
| 7 | 106 | 42% | 61 (58%) | 28% of 53 | +6% |
| 8 | 122 | 49% | 62 (51%) | 2% of 44 | +12% |
| 9 | 82 | 29% | 58 (71%) | 44% of 84 | -7% |
| 10 | 87 | 61% | 34 (39%) | 10% of 79 | +24% |
| 11 | 166 | 37% | 105 (63%) | n/a | +0% |
| 12 | 166 | 37% | 105 (63%) | n/a | +0% |
| 13 | 166 | 37% | 105 (63%) | n/a | +0% |
| 14 | 166 | 37% | 105 (63%) | n/a | +0% |
| 15 | 166 | 37% | 105 (63%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 38% of 125 | -3% |
| 18 | 166 | 37% | 105 (63%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 31% vs base 37%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 37%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 61% vs base 37%, n=87)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 37%, n=41)
