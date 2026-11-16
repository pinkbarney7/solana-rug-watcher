# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 14:46 UTC. Labeled coins: 90 (22 dead/pulled, 68 still alive). Base dead rate 24.4%. Forward 24h samples so far: 57.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 79 | 27% | 58 (73%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 27% of 82 | -24% |
| 3 | 41 | 17% | 34 (83%) | 31% of 49 | -7% |
| 5 | 49 | 33% | 33 (67%) | 15% of 41 | +8% |
| 6 | 21 | 14% | 18 (86%) | 28% of 68 | -10% |
| 7 | 57 | 28% | 41 (72%) | 21% of 28 | +4% |
| 8 | 61 | 36% | 39 (64%) | 0% of 29 | +12% |
| 9 | 41 | 15% | 35 (85%) | 33% of 49 | -10% |
| 10 | 46 | 41% | 27 (59%) | 7% of 44 | +17% |
| 11 | 90 | 24% | 68 (76%) | n/a | +0% |
| 12 | 90 | 24% | 68 (76%) | n/a | +0% |
| 13 | 90 | 24% | 68 (76%) | n/a | +0% |
| 14 | 90 | 24% | 68 (76%) | n/a | +0% |
| 15 | 90 | 24% | 68 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 23% of 52 | +2% |
| 18 | 90 | 24% | 68 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 24%, n=41)
- check #9: lower weight: flagged coins die no more often than average (precision 15% vs base 24%, n=41)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
