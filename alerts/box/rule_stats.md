# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 22:29 EDT. Labeled coins: 1072 (816 dead/pulled, 256 still alive). Base dead rate 76.1%. Forward 24h samples so far: 43.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 868 | 75% | 218 (25%) | 55% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 75% of 915 | -57% |
| 3 | 313 | 69% | 98 (31%) | 76% of 612 | -7% |
| 4 | 143 | 66% | 49 (34%) | 75% of 783 | -10% |
| 5 | 754 | 81% | 146 (19%) | 48% of 183 | +5% |
| 6 | 73 | 51% | 36 (49%) | 75% of 808 | -25% |
| 7 | 395 | 70% | 120 (30%) | 77% of 460 | -6% |
| 8 | 415 | 67% | 138 (33%) | 75% of 391 | -9% |
| 9 | 708 | 79% | 149 (21%) | 57% of 218 | +3% |
| 10 | 736 | 83% | 125 (17%) | 38% of 187 | +7% |
| 11 | 529 | 88% | 63 (12%) | 58% of 430 | +12% |
| 12 | 873 | 78% | 190 (22%) | 40% of 86 | +2% |
| 13 | 586 | 74% | 150 (26%) | 75% of 373 | -2% |
| 14 | 393 | 78% | 88 (22%) | 73% of 566 | +1% |
| 15 | 461 | 72% | 131 (28%) | 78% of 498 | -5% |
| 16 | 85 | 75% | 21 (25%) | 75% of 874 | -1% |
| 18 | 669 | 82% | 119 (18%) | 58% of 290 | +6% |
| 19 | 348 | 77% | 79 (23%) | 72% of 530 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 75% vs base 76%, n=868)
- check #3: lower weight: flagged coins die no more often than average (precision 69% vs base 76%, n=313)
- check #4: lower weight: flagged coins die no more often than average (precision 66% vs base 76%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 76%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 76%, n=395)
- check #8: lower weight: flagged coins die no more often than average (precision 67% vs base 76%, n=415)
- check #9: lower weight: flagged coins die no more often than average (precision 79% vs base 76%, n=708)
- check #12: lower weight: flagged coins die no more often than average (precision 78% vs base 76%, n=873)
- check #13: lower weight: flagged coins die no more often than average (precision 74% vs base 76%, n=586)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 76%, n=393)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 76%, n=461)
- check #16: lower weight: flagged coins die no more often than average (precision 75% vs base 76%, n=85)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 76%, n=348)
