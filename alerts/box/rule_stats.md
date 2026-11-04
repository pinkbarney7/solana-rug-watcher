# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 19:04 EST. Labeled coins: 1127 (876 dead/pulled, 251 still alive). Base dead rate 77.7%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 919 | 77% | 211 (23%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 78% of 968 | -61% |
| 3 | 338 | 74% | 88 (26%) | 77% of 643 | -4% |
| 4 | 150 | 71% | 44 (29%) | 77% of 832 | -7% |
| 5 | 792 | 83% | 138 (17%) | 51% of 201 | +5% |
| 6 | 78 | 50% | 39 (50%) | 79% of 839 | -28% |
| 7 | 418 | 71% | 123 (29%) | 82% of 473 | -7% |
| 8 | 440 | 70% | 133 (30%) | 76% of 420 | -8% |
| 9 | 743 | 81% | 140 (19%) | 59% of 239 | +3% |
| 10 | 775 | 85% | 114 (15%) | 40% of 204 | +8% |
| 11 | 554 | 89% | 62 (11%) | 62% of 461 | +11% |
| 12 | 918 | 81% | 178 (19%) | 39% of 97 | +3% |
| 13 | 621 | 77% | 145 (23%) | 77% of 394 | -1% |
| 14 | 413 | 78% | 91 (22%) | 76% of 602 | +0% |
| 15 | 494 | 72% | 139 (28%) | 81% of 521 | -6% |
| 16 | 88 | 78% | 19 (22%) | 76% of 927 | +1% |
| 18 | 705 | 84% | 110 (16%) | 59% of 310 | +7% |
| 19 | 367 | 79% | 78 (21%) | 74% of 561 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=919)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 71% vs base 78%, n=150)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 78%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 71% vs base 78%, n=418)
- check #8: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=440)
- check #12: lower weight: flagged coins die no more often than average (precision 81% vs base 78%, n=918)
- check #13: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=413)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=494)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 78%, n=367)
