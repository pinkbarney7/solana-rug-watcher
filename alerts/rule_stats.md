# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 05:42 UTC. Labeled coins: 101 (24 dead/pulled, 77 still alive). Base dead rate 23.8%. Forward 24h samples so far: 67.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 89 | 26% | 66 (74%) | 0% of 10 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 93 | -24% |
| 3 | 44 | 16% | 37 (84%) | 30% of 57 | -8% |
| 5 | 58 | 31% | 40 (69%) | 14% of 43 | +7% |
| 6 | 22 | 14% | 19 (86%) | 27% of 78 | -10% |
| 7 | 65 | 28% | 47 (72%) | 20% of 30 | +4% |
| 8 | 69 | 35% | 45 (65%) | 0% of 32 | +11% |
| 9 | 46 | 13% | 40 (87%) | 33% of 55 | -11% |
| 10 | 52 | 40% | 31 (60%) | 6% of 49 | +17% |
| 11 | 101 | 24% | 77 (76%) | n/a | +0% |
| 12 | 101 | 24% | 77 (76%) | n/a | +0% |
| 13 | 101 | 24% | 77 (76%) | n/a | +0% |
| 14 | 101 | 24% | 77 (76%) | n/a | +0% |
| 15 | 101 | 24% | 77 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 22% of 63 | +3% |
| 18 | 101 | 24% | 77 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 24%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 13% vs base 24%, n=46)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
