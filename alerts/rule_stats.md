# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 10:12 UTC. Labeled coins: 112 (31 dead/pulled, 81 still alive). Base dead rate 27.7%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 98 | 31% | 68 (69%) | 0% of 12 | +3% |
| 2 | 8 | 0% | 8 (100%) | 30% of 104 | -28% |
| 3 | 45 | 16% | 38 (84%) | 36% of 67 | -12% |
| 5 | 67 | 37% | 42 (63%) | 13% of 45 | +10% |
| 6 | 22 | 14% | 19 (86%) | 31% of 89 | -14% |
| 7 | 75 | 33% | 50 (67%) | 19% of 31 | +6% |
| 8 | 79 | 39% | 48 (61%) | 0% of 33 | +12% |
| 9 | 52 | 17% | 43 (83%) | 37% of 60 | -10% |
| 10 | 60 | 47% | 32 (53%) | 6% of 52 | +19% |
| 11 | 112 | 28% | 81 (72%) | n/a | +0% |
| 12 | 112 | 28% | 81 (72%) | n/a | +0% |
| 13 | 112 | 28% | 81 (72%) | n/a | +0% |
| 14 | 112 | 28% | 81 (72%) | n/a | +0% |
| 15 | 112 | 28% | 81 (72%) | n/a | +0% |
| 16 | 39 | 28% | 28 (72%) | 27% of 73 | +1% |
| 18 | 112 | 28% | 81 (72%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 28%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 28%, n=52)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 28%, n=39)
