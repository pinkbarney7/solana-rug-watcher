# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 14:32 EDT. Labeled coins: 1070 (803 dead/pulled, 267 still alive). Base dead rate 75.0%. Forward 24h samples so far: 42.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 866 | 74% | 226 (26%) | 51% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 74% of 913 | -56% |
| 3 | 311 | 66% | 106 (34%) | 76% of 612 | -9% |
| 4 | 143 | 64% | 51 (36%) | 74% of 781 | -11% |
| 5 | 752 | 80% | 154 (20%) | 46% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 74% of 807 | -24% |
| 7 | 395 | 68% | 125 (32%) | 75% of 459 | -7% |
| 8 | 413 | 65% | 145 (35%) | 74% of 391 | -10% |
| 9 | 706 | 78% | 157 (22%) | 56% of 218 | +3% |
| 10 | 734 | 82% | 133 (18%) | 37% of 187 | +7% |
| 11 | 528 | 88% | 66 (12%) | 57% of 429 | +12% |
| 12 | 871 | 77% | 200 (23%) | 40% of 86 | +2% |
| 13 | 585 | 73% | 158 (27%) | 75% of 372 | -2% |
| 14 | 393 | 77% | 89 (23%) | 71% of 564 | +2% |
| 15 | 459 | 71% | 135 (29%) | 77% of 498 | -4% |
| 16 | 85 | 75% | 21 (25%) | 74% of 872 | +0% |
| 18 | 667 | 81% | 127 (19%) | 57% of 290 | +6% |
| 19 | 346 | 77% | 79 (23%) | 71% of 530 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 74% vs base 75%, n=866)
- check #3: lower weight: flagged coins die no more often than average (precision 66% vs base 75%, n=311)
- check #4: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 75%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 68% vs base 75%, n=395)
- check #8: lower weight: flagged coins die no more often than average (precision 65% vs base 75%, n=413)
- check #9: lower weight: flagged coins die no more often than average (precision 78% vs base 75%, n=706)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=871)
- check #13: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=585)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=393)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=459)
- check #16: lower weight: flagged coins die no more often than average (precision 75% vs base 75%, n=85)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=346)
