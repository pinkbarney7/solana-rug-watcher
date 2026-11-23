# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 07:40 UTC. Labeled coins: 162 (59 dead/pulled, 103 still alive). Base dead rate 36.4%. Forward 24h samples so far: 89.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 147 | 39% | 89 (61%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 39% of 150 | -36% |
| 3 | 69 | 32% | 47 (68%) | 40% of 93 | -5% |
| 5 | 105 | 48% | 55 (52%) | 16% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 42% of 133 | -26% |
| 7 | 104 | 41% | 61 (59%) | 29% of 51 | +5% |
| 8 | 119 | 49% | 61 (51%) | 2% of 43 | +12% |
| 9 | 80 | 30% | 56 (70%) | 43% of 82 | -6% |
| 10 | 85 | 60% | 34 (40%) | 10% of 77 | +24% |
| 11 | 162 | 36% | 103 (64%) | n/a | +0% |
| 12 | 162 | 36% | 103 (64%) | n/a | +0% |
| 13 | 162 | 36% | 103 (64%) | n/a | +0% |
| 14 | 162 | 36% | 103 (64%) | n/a | +0% |
| 15 | 162 | 36% | 103 (64%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 37% of 121 | -2% |
| 18 | 162 | 36% | 103 (64%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 36%, n=69)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 36%, n=80)
- check #10: consider treating WARN like FAIL: strong lift (precision 60% vs base 36%, n=85)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 36%, n=41)
