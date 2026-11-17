# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 07:10 UTC. Labeled coins: 104 (25 dead/pulled, 79 still alive). Base dead rate 24.0%. Forward 24h samples so far: 69.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 91 | 26% | 67 (74%) | 0% of 11 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 96 | -24% |
| 3 | 44 | 16% | 37 (84%) | 30% of 60 | -8% |
| 5 | 59 | 32% | 40 (68%) | 13% of 45 | +8% |
| 6 | 22 | 14% | 19 (86%) | 27% of 81 | -10% |
| 7 | 68 | 28% | 49 (72%) | 20% of 30 | +4% |
| 8 | 71 | 35% | 46 (65%) | 0% of 33 | +11% |
| 9 | 47 | 13% | 41 (87%) | 33% of 57 | -11% |
| 10 | 53 | 42% | 31 (58%) | 6% of 51 | +17% |
| 11 | 104 | 24% | 79 (76%) | n/a | +0% |
| 12 | 104 | 24% | 79 (76%) | n/a | +0% |
| 13 | 104 | 24% | 79 (76%) | n/a | +0% |
| 14 | 104 | 24% | 79 (76%) | n/a | +0% |
| 15 | 104 | 24% | 79 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 23% of 66 | +2% |
| 18 | 104 | 24% | 79 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 24%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 13% vs base 24%, n=47)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
