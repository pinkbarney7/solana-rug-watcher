# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 18:35 EST. Labeled coins: 1214 (1041 dead/pulled, 173 still alive). Base dead rate 85.7%. Forward 24h samples so far: 116.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1003 | 86% | 142 (14%) | 64% of 59 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1052 | -67% |
| 3 | 380 | 88% | 47 (12%) | 83% of 688 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 916 | +4% |
| 5 | 849 | 91% | 78 (9%) | 63% of 231 | +5% |
| 6 | 97 | 56% | 43 (44%) | 87% of 907 | -30% |
| 7 | 463 | 75% | 114 (25%) | 93% of 515 | -10% |
| 8 | 492 | 82% | 89 (18%) | 84% of 453 | -4% |
| 9 | 793 | 89% | 84 (11%) | 71% of 276 | +4% |
| 10 | 815 | 92% | 68 (8%) | 62% of 251 | +6% |
| 11 | 630 | 88% | 74 (12%) | 81% of 472 | +3% |
| 12 | 1000 | 89% | 110 (11%) | 47% of 102 | +3% |
| 13 | 699 | 86% | 97 (14%) | 83% of 403 | +0% |
| 14 | 489 | 84% | 76 (16%) | 86% of 613 | -1% |
| 15 | 570 | 78% | 126 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 86% of 1008 | -6% |
| 18 | 780 | 89% | 84 (11%) | 75% of 322 | +3% |
| 19 | 370 | 86% | 51 (14%) | 87% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1003)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=380)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=97)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 86%, n=463)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=492)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=630)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=699)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 86%, n=489)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=570)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
