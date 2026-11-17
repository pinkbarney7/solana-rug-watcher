# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 13:56 UTC. Labeled coins: 115 (33 dead/pulled, 82 still alive). Base dead rate 28.7%. Forward 24h samples so far: 75.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 100 | 32% | 68 (68%) | 0% of 13 | +3% |
| 2 | 8 | 0% | 8 (100%) | 31% of 107 | -29% |
| 3 | 45 | 16% | 38 (84%) | 37% of 70 | -13% |
| 5 | 69 | 39% | 42 (61%) | 13% of 46 | +10% |
| 6 | 22 | 14% | 19 (86%) | 33% of 92 | -15% |
| 7 | 78 | 35% | 51 (65%) | 19% of 31 | +6% |
| 8 | 81 | 41% | 48 (59%) | 0% of 34 | +12% |
| 9 | 52 | 17% | 43 (83%) | 38% of 63 | -11% |
| 10 | 63 | 48% | 33 (52%) | 6% of 52 | +19% |
| 11 | 115 | 29% | 82 (71%) | n/a | +0% |
| 12 | 115 | 29% | 82 (71%) | n/a | +0% |
| 13 | 115 | 29% | 82 (71%) | n/a | +0% |
| 14 | 115 | 29% | 82 (71%) | n/a | +0% |
| 15 | 115 | 29% | 82 (71%) | n/a | +0% |
| 16 | 40 | 28% | 29 (72%) | 29% of 75 | -1% |
| 18 | 115 | 29% | 82 (71%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 29%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 29%, n=52)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 29%, n=40)
