# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 09:06 UTC. Labeled coins: 163 (60 dead/pulled, 103 still alive). Base dead rate 36.8%. Forward 24h samples so far: 89.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 148 | 40% | 89 (60%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 40% of 151 | -37% |
| 3 | 69 | 32% | 47 (68%) | 40% of 94 | -5% |
| 5 | 106 | 48% | 55 (52%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 43% of 134 | -26% |
| 7 | 105 | 42% | 61 (58%) | 29% of 51 | +5% |
| 8 | 120 | 49% | 61 (51%) | 2% of 43 | +12% |
| 9 | 80 | 30% | 56 (70%) | 43% of 83 | -7% |
| 10 | 86 | 60% | 34 (40%) | 10% of 77 | +24% |
| 11 | 163 | 37% | 103 (63%) | n/a | +0% |
| 12 | 163 | 37% | 103 (63%) | n/a | +0% |
| 13 | 163 | 37% | 103 (63%) | n/a | +0% |
| 14 | 163 | 37% | 103 (63%) | n/a | +0% |
| 15 | 163 | 37% | 103 (63%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 38% of 122 | -3% |
| 18 | 163 | 37% | 103 (63%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 37%, n=69)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 37%, n=80)
- check #10: consider treating WARN like FAIL: strong lift (precision 60% vs base 37%, n=86)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 37%, n=41)
