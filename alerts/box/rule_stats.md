# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 11:39 EST. Labeled coins: 1210 (1036 dead/pulled, 174 still alive). Base dead rate 85.6%. Forward 24h samples so far: 113.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 999 | 86% | 143 (14%) | 64% of 59 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1048 | -67% |
| 3 | 377 | 87% | 48 (13%) | 83% of 687 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 912 | +5% |
| 5 | 845 | 91% | 79 (9%) | 63% of 231 | +5% |
| 6 | 95 | 54% | 44 (46%) | 87% of 905 | -32% |
| 7 | 461 | 75% | 114 (25%) | 93% of 513 | -10% |
| 8 | 489 | 82% | 89 (18%) | 83% of 452 | -4% |
| 9 | 790 | 89% | 85 (11%) | 71% of 275 | +4% |
| 10 | 814 | 92% | 69 (8%) | 62% of 248 | +6% |
| 11 | 626 | 88% | 74 (12%) | 81% of 472 | +3% |
| 12 | 996 | 89% | 111 (11%) | 47% of 102 | +3% |
| 13 | 695 | 86% | 98 (14%) | 83% of 403 | +0% |
| 14 | 485 | 84% | 77 (16%) | 86% of 613 | -1% |
| 15 | 566 | 78% | 127 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 85% of 1004 | -6% |
| 18 | 776 | 89% | 83 (11%) | 75% of 322 | +4% |
| 19 | 370 | 86% | 53 (14%) | 87% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=999)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=377)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 86%, n=95)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 86%, n=461)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=489)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=626)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=695)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 86%, n=485)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=566)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
