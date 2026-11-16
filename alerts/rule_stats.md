# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 13:25 UTC. Labeled coins: 89 (21 dead/pulled, 68 still alive). Base dead rate 23.6%. Forward 24h samples so far: 57.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 78 | 26% | 58 (74%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 81 | -24% |
| 3 | 41 | 17% | 34 (83%) | 29% of 48 | -7% |
| 5 | 48 | 31% | 33 (69%) | 15% of 41 | +8% |
| 6 | 21 | 14% | 18 (86%) | 27% of 67 | -9% |
| 7 | 56 | 27% | 41 (73%) | 21% of 28 | +3% |
| 8 | 60 | 35% | 39 (65%) | 0% of 29 | +11% |
| 9 | 41 | 15% | 35 (85%) | 31% of 48 | -9% |
| 10 | 45 | 40% | 27 (60%) | 7% of 44 | +16% |
| 11 | 89 | 24% | 68 (76%) | n/a | +0% |
| 12 | 89 | 24% | 68 (76%) | n/a | +0% |
| 13 | 89 | 24% | 68 (76%) | n/a | +0% |
| 14 | 89 | 24% | 68 (76%) | n/a | +0% |
| 15 | 89 | 24% | 68 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 22% of 51 | +3% |
| 18 | 89 | 24% | 68 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 24%, n=41)
- check #9: lower weight: flagged coins die no more often than average (precision 15% vs base 24%, n=41)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
