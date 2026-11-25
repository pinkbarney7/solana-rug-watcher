# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 13:59 EST. Labeled coins: 1211 (1038 dead/pulled, 173 still alive). Base dead rate 85.7%. Forward 24h samples so far: 114.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1000 | 86% | 142 (14%) | 64% of 59 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1049 | -67% |
| 3 | 377 | 88% | 47 (12%) | 83% of 688 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 913 | +4% |
| 5 | 846 | 91% | 78 (9%) | 63% of 231 | +5% |
| 6 | 95 | 55% | 43 (45%) | 87% of 906 | -31% |
| 7 | 462 | 76% | 113 (24%) | 93% of 513 | -10% |
| 8 | 490 | 82% | 89 (18%) | 84% of 452 | -4% |
| 9 | 790 | 89% | 84 (11%) | 71% of 276 | +4% |
| 10 | 815 | 92% | 68 (8%) | 62% of 248 | +6% |
| 11 | 627 | 88% | 73 (12%) | 81% of 472 | +3% |
| 12 | 997 | 89% | 110 (11%) | 47% of 102 | +3% |
| 13 | 696 | 86% | 97 (14%) | 83% of 403 | +0% |
| 14 | 486 | 84% | 76 (16%) | 86% of 613 | -1% |
| 15 | 567 | 78% | 126 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 86% of 1005 | -6% |
| 18 | 777 | 89% | 83 (11%) | 75% of 322 | +4% |
| 19 | 370 | 86% | 52 (14%) | 87% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1000)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=377)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 86%, n=95)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=462)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=490)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=627)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=696)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 86%, n=486)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=567)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
