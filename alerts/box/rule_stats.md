# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 21:16 EST. Labeled coins: 1109 (858 dead/pulled, 251 still alive). Base dead rate 77.4%. Forward 24h samples so far: 52.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 901 | 77% | 211 (23%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 950 | -61% |
| 3 | 330 | 74% | 87 (26%) | 76% of 633 | -4% |
| 4 | 148 | 69% | 46 (31%) | 77% of 816 | -8% |
| 5 | 778 | 82% | 138 (18%) | 50% of 197 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 821 | -29% |
| 7 | 408 | 70% | 122 (30%) | 81% of 465 | -7% |
| 8 | 432 | 69% | 133 (31%) | 76% of 410 | -8% |
| 9 | 731 | 81% | 142 (19%) | 59% of 233 | +3% |
| 10 | 762 | 85% | 113 (15%) | 38% of 199 | +8% |
| 11 | 546 | 89% | 62 (11%) | 61% of 451 | +11% |
| 12 | 903 | 80% | 180 (20%) | 39% of 94 | +3% |
| 13 | 612 | 76% | 144 (24%) | 76% of 385 | -1% |
| 14 | 403 | 78% | 90 (22%) | 75% of 594 | +0% |
| 15 | 483 | 72% | 136 (28%) | 80% of 514 | -6% |
| 16 | 88 | 77% | 20 (23%) | 76% of 909 | -0% |
| 18 | 691 | 84% | 108 (16%) | 58% of 306 | +7% |
| 19 | 357 | 78% | 77 (22%) | 73% of 554 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=901)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 77%, n=330)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=408)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=432)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=903)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=612)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=403)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=483)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=357)
