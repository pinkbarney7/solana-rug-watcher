# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 18:43 EST. Labeled coins: 1127 (873 dead/pulled, 254 still alive). Base dead rate 77.5%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 919 | 77% | 214 (23%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 968 | -61% |
| 3 | 338 | 74% | 89 (26%) | 77% of 643 | -4% |
| 4 | 150 | 70% | 45 (30%) | 77% of 832 | -7% |
| 5 | 792 | 82% | 140 (18%) | 50% of 201 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 839 | -29% |
| 7 | 418 | 70% | 124 (30%) | 81% of 473 | -7% |
| 8 | 440 | 69% | 135 (31%) | 76% of 420 | -8% |
| 9 | 743 | 81% | 142 (19%) | 59% of 239 | +3% |
| 10 | 775 | 85% | 115 (15%) | 39% of 204 | +8% |
| 11 | 554 | 88% | 64 (12%) | 62% of 461 | +11% |
| 12 | 918 | 80% | 180 (20%) | 38% of 97 | +3% |
| 13 | 621 | 76% | 147 (24%) | 76% of 394 | -1% |
| 14 | 413 | 78% | 92 (22%) | 75% of 602 | +0% |
| 15 | 494 | 72% | 140 (28%) | 81% of 521 | -6% |
| 16 | 88 | 77% | 20 (23%) | 76% of 927 | -0% |
| 18 | 705 | 84% | 113 (16%) | 59% of 310 | +7% |
| 19 | 367 | 78% | 79 (22%) | 73% of 561 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=919)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=150)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 78%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=418)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 78%, n=440)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 78%, n=918)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 78%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=413)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=494)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=367)
