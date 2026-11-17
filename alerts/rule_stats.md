# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 13:38 UTC. Labeled coins: 114 (32 dead/pulled, 82 still alive). Base dead rate 28.1%. Forward 24h samples so far: 75.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 99 | 31% | 68 (69%) | 0% of 13 | +3% |
| 2 | 8 | 0% | 8 (100%) | 30% of 106 | -28% |
| 3 | 45 | 16% | 38 (84%) | 36% of 69 | -13% |
| 5 | 68 | 38% | 42 (62%) | 13% of 46 | +10% |
| 6 | 22 | 14% | 19 (86%) | 32% of 91 | -14% |
| 7 | 77 | 34% | 51 (66%) | 19% of 31 | +6% |
| 8 | 80 | 40% | 48 (60%) | 0% of 34 | +12% |
| 9 | 52 | 17% | 43 (83%) | 37% of 62 | -11% |
| 10 | 62 | 47% | 33 (53%) | 6% of 52 | +19% |
| 11 | 114 | 28% | 82 (72%) | n/a | +0% |
| 12 | 114 | 28% | 82 (72%) | n/a | +0% |
| 13 | 114 | 28% | 82 (72%) | n/a | +0% |
| 14 | 114 | 28% | 82 (72%) | n/a | +0% |
| 15 | 114 | 28% | 82 (72%) | n/a | +0% |
| 16 | 40 | 28% | 29 (72%) | 28% of 74 | -1% |
| 18 | 114 | 28% | 82 (72%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 28%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 28%, n=52)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 28%, n=40)
