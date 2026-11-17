# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 08:27 UTC. Labeled coins: 107 (28 dead/pulled, 79 still alive). Base dead rate 26.2%. Forward 24h samples so far: 70.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 94 | 29% | 67 (71%) | 0% of 11 | +3% |
| 2 | 8 | 0% | 8 (100%) | 28% of 99 | -26% |
| 3 | 44 | 16% | 37 (84%) | 33% of 63 | -10% |
| 5 | 62 | 35% | 40 (65%) | 13% of 45 | +9% |
| 6 | 22 | 14% | 19 (86%) | 30% of 84 | -13% |
| 7 | 71 | 31% | 49 (69%) | 20% of 30 | +5% |
| 8 | 74 | 38% | 46 (62%) | 0% of 33 | +12% |
| 9 | 49 | 16% | 41 (84%) | 34% of 58 | -10% |
| 10 | 56 | 45% | 31 (55%) | 6% of 51 | +18% |
| 11 | 107 | 26% | 79 (74%) | n/a | +0% |
| 12 | 107 | 26% | 79 (74%) | n/a | +0% |
| 13 | 107 | 26% | 79 (74%) | n/a | +0% |
| 14 | 107 | 26% | 79 (74%) | n/a | +0% |
| 15 | 107 | 26% | 79 (74%) | n/a | +0% |
| 16 | 39 | 28% | 28 (72%) | 25% of 68 | +2% |
| 18 | 107 | 26% | 79 (74%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 26%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 26%, n=49)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 26%, n=39)
