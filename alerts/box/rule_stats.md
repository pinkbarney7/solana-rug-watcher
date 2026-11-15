# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 18:17 EST. Labeled coins: 1153 (946 dead/pulled, 207 still alive). Base dead rate 82.0%. Forward 24h samples so far: 83.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 944 | 82% | 169 (18%) | 60% of 57 | +0% |
| 2 | 25 | 20% | 20 (80%) | 83% of 993 | -62% |
| 3 | 346 | 85% | 53 (15%) | 79% of 661 | +3% |
| 4 | 152 | 78% | 33 (22%) | 81% of 856 | -4% |
| 5 | 808 | 88% | 101 (12%) | 56% of 211 | +5% |
| 6 | 82 | 54% | 38 (46%) | 83% of 861 | -28% |
| 7 | 431 | 73% | 118 (27%) | 88% of 486 | -9% |
| 8 | 454 | 76% | 109 (24%) | 81% of 431 | -6% |
| 9 | 757 | 86% | 106 (14%) | 65% of 251 | +4% |
| 10 | 787 | 90% | 80 (10%) | 49% of 218 | +8% |
| 11 | 569 | 91% | 52 (9%) | 70% of 472 | +9% |
| 12 | 939 | 86% | 135 (14%) | 43% of 102 | +4% |
| 13 | 638 | 82% | 113 (18%) | 80% of 403 | +0% |
| 14 | 428 | 82% | 79 (18%) | 81% of 613 | -1% |
| 15 | 509 | 75% | 125 (25%) | 87% of 532 | -7% |
| 16 | 89 | 80% | 18 (20%) | 82% of 952 | -2% |
| 18 | 719 | 88% | 85 (12%) | 66% of 322 | +6% |
| 19 | 370 | 81% | 70 (19%) | 80% of 574 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 82% vs base 82%, n=944)
- check #3: lower weight: flagged coins die no more often than average (precision 85% vs base 82%, n=346)
- check #4: lower weight: flagged coins die no more often than average (precision 78% vs base 82%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 82%, n=82)
- check #7: lower weight: flagged coins die no more often than average (precision 73% vs base 82%, n=431)
- check #8: lower weight: flagged coins die no more often than average (precision 76% vs base 82%, n=454)
- check #13: lower weight: flagged coins die no more often than average (precision 82% vs base 82%, n=638)
- check #14: lower weight: flagged coins die no more often than average (precision 82% vs base 82%, n=428)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 82%, n=509)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 82%, n=89)
- check #19: lower weight: flagged coins die no more often than average (precision 81% vs base 82%, n=370)
