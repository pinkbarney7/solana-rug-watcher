# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 15:01 EST. Labeled coins: 1212 (1040 dead/pulled, 172 still alive). Base dead rate 85.8%. Forward 24h samples so far: 114.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1001 | 86% | 141 (14%) | 64% of 59 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1050 | -67% |
| 3 | 378 | 88% | 46 (12%) | 83% of 688 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 914 | +4% |
| 5 | 847 | 91% | 77 (9%) | 63% of 231 | +5% |
| 6 | 96 | 55% | 43 (45%) | 87% of 906 | -31% |
| 7 | 462 | 76% | 113 (24%) | 93% of 514 | -10% |
| 8 | 490 | 82% | 88 (18%) | 84% of 453 | -4% |
| 9 | 791 | 90% | 83 (10%) | 71% of 276 | +4% |
| 10 | 815 | 92% | 68 (8%) | 62% of 249 | +6% |
| 11 | 628 | 88% | 73 (12%) | 81% of 472 | +3% |
| 12 | 998 | 89% | 109 (11%) | 47% of 102 | +3% |
| 13 | 697 | 86% | 96 (14%) | 83% of 403 | +0% |
| 14 | 487 | 85% | 75 (15%) | 86% of 613 | -1% |
| 15 | 568 | 78% | 125 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 86% of 1006 | -6% |
| 18 | 778 | 89% | 83 (11%) | 75% of 322 | +4% |
| 19 | 370 | 86% | 51 (14%) | 87% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1001)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=378)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 86%, n=96)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=462)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=490)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=628)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=697)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=487)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=568)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
