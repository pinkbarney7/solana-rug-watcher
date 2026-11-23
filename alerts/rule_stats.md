# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 09:15 UTC. Labeled coins: 165 (60 dead/pulled, 105 still alive). Base dead rate 36.4%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 150 | 39% | 91 (61%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 39% of 153 | -36% |
| 3 | 71 | 31% | 49 (69%) | 40% of 94 | -5% |
| 5 | 108 | 47% | 57 (53%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 42% of 136 | -26% |
| 7 | 105 | 42% | 61 (58%) | 28% of 53 | +6% |
| 8 | 121 | 49% | 62 (51%) | 2% of 44 | +12% |
| 9 | 82 | 29% | 58 (71%) | 43% of 83 | -7% |
| 10 | 86 | 60% | 34 (40%) | 10% of 79 | +24% |
| 11 | 165 | 36% | 105 (64%) | n/a | +0% |
| 12 | 165 | 36% | 105 (64%) | n/a | +0% |
| 13 | 165 | 36% | 105 (64%) | n/a | +0% |
| 14 | 165 | 36% | 105 (64%) | n/a | +0% |
| 15 | 165 | 36% | 105 (64%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 37% of 124 | -2% |
| 18 | 165 | 36% | 105 (64%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 31% vs base 36%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 36%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 60% vs base 36%, n=86)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 36%, n=41)
