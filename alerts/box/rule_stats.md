# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 20:50 EST. Labeled coins: 1186 (1012 dead/pulled, 174 still alive). Base dead rate 85.3%. Forward 24h samples so far: 89.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 976 | 86% | 139 (14%) | 64% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 86% of 1026 | -65% |
| 3 | 364 | 88% | 44 (12%) | 83% of 676 | +3% |
| 4 | 152 | 89% | 17 (11%) | 84% of 889 | +3% |
| 5 | 830 | 91% | 78 (9%) | 63% of 222 | +5% |
| 6 | 88 | 55% | 40 (45%) | 87% of 888 | -31% |
| 7 | 451 | 76% | 110 (24%) | 93% of 499 | -10% |
| 8 | 474 | 82% | 87 (18%) | 83% of 444 | -4% |
| 9 | 776 | 89% | 84 (11%) | 71% of 265 | +4% |
| 10 | 806 | 92% | 67 (8%) | 60% of 232 | +6% |
| 11 | 602 | 90% | 59 (10%) | 78% of 472 | +5% |
| 12 | 972 | 89% | 105 (11%) | 45% of 102 | +4% |
| 13 | 671 | 86% | 91 (14%) | 83% of 403 | +1% |
| 14 | 461 | 85% | 70 (15%) | 85% of 613 | -1% |
| 15 | 542 | 79% | 116 (21%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 981 | -5% |
| 18 | 752 | 90% | 72 (10%) | 72% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 85% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=976)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 85%, n=364)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 85%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 85%, n=451)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=474)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=671)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=461)
- check #15: lower weight: flagged coins die no more often than average (precision 79% vs base 85%, n=542)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
