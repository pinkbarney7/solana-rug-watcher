# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 15:58 EDT. Labeled coins: 1071 (805 dead/pulled, 266 still alive). Base dead rate 75.2%. Forward 24h samples so far: 43.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 867 | 74% | 225 (26%) | 51% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 74% of 914 | -56% |
| 3 | 312 | 66% | 105 (34%) | 76% of 612 | -9% |
| 4 | 143 | 64% | 51 (36%) | 74% of 782 | -11% |
| 5 | 753 | 80% | 153 (20%) | 46% of 183 | +5% |
| 6 | 73 | 51% | 36 (49%) | 74% of 808 | -24% |
| 7 | 395 | 69% | 124 (31%) | 75% of 460 | -7% |
| 8 | 414 | 65% | 145 (35%) | 74% of 391 | -10% |
| 9 | 707 | 78% | 156 (22%) | 56% of 218 | +3% |
| 10 | 735 | 82% | 132 (18%) | 37% of 187 | +7% |
| 11 | 528 | 88% | 65 (12%) | 57% of 430 | +13% |
| 12 | 872 | 77% | 199 (23%) | 40% of 86 | +2% |
| 13 | 585 | 73% | 156 (27%) | 75% of 373 | -2% |
| 14 | 393 | 77% | 89 (23%) | 71% of 565 | +2% |
| 15 | 460 | 71% | 134 (29%) | 77% of 498 | -4% |
| 16 | 85 | 75% | 21 (25%) | 74% of 873 | +0% |
| 18 | 668 | 81% | 126 (19%) | 57% of 290 | +6% |
| 19 | 347 | 77% | 79 (23%) | 71% of 530 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 74% vs base 75%, n=867)
- check #3: lower weight: flagged coins die no more often than average (precision 66% vs base 75%, n=312)
- check #4: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 75%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 75%, n=395)
- check #8: lower weight: flagged coins die no more often than average (precision 65% vs base 75%, n=414)
- check #9: lower weight: flagged coins die no more often than average (precision 78% vs base 75%, n=707)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=872)
- check #13: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=585)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=393)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=460)
- check #16: lower weight: flagged coins die no more often than average (precision 75% vs base 75%, n=85)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=347)
