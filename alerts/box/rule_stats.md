# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 20:21 EST. Labeled coins: 1108 (858 dead/pulled, 250 still alive). Base dead rate 77.4%. Forward 24h samples so far: 51.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 901 | 77% | 211 (23%) | 56% of 55 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 949 | -61% |
| 3 | 329 | 74% | 86 (26%) | 76% of 633 | -4% |
| 4 | 148 | 69% | 46 (31%) | 77% of 815 | -9% |
| 5 | 778 | 82% | 138 (18%) | 50% of 196 | +5% |
| 6 | 77 | 49% | 39 (51%) | 78% of 821 | -28% |
| 7 | 407 | 70% | 121 (30%) | 81% of 465 | -7% |
| 8 | 432 | 69% | 133 (31%) | 76% of 409 | -8% |
| 9 | 731 | 81% | 142 (19%) | 59% of 232 | +3% |
| 10 | 762 | 85% | 113 (15%) | 38% of 198 | +8% |
| 11 | 545 | 89% | 61 (11%) | 61% of 451 | +11% |
| 12 | 902 | 80% | 179 (20%) | 39% of 94 | +3% |
| 13 | 611 | 77% | 143 (23%) | 76% of 385 | -1% |
| 14 | 403 | 78% | 90 (22%) | 75% of 593 | +0% |
| 15 | 482 | 72% | 135 (28%) | 80% of 514 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 908 | -0% |
| 18 | 690 | 84% | 107 (16%) | 58% of 306 | +7% |
| 19 | 357 | 78% | 77 (22%) | 73% of 553 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=901)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 77%, n=329)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=77)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=407)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=432)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=902)
- check #13: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=611)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=403)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=482)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=357)
