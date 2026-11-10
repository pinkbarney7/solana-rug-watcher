# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 08:08 EST. Labeled coins: 1152 (936 dead/pulled, 216 still alive). Base dead rate 81.2%. Forward 24h samples so far: 83.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 943 | 81% | 178 (19%) | 60% of 57 | -0% |
| 2 | 25 | 20% | 20 (80%) | 82% of 992 | -61% |
| 3 | 346 | 83% | 59 (17%) | 78% of 660 | +2% |
| 4 | 152 | 77% | 35 (23%) | 80% of 855 | -4% |
| 5 | 808 | 87% | 105 (13%) | 54% of 210 | +6% |
| 6 | 82 | 52% | 39 (48%) | 82% of 860 | -29% |
| 7 | 431 | 71% | 123 (29%) | 88% of 485 | -10% |
| 8 | 453 | 75% | 114 (25%) | 80% of 431 | -6% |
| 9 | 757 | 85% | 111 (15%) | 64% of 250 | +4% |
| 10 | 786 | 89% | 83 (11%) | 46% of 218 | +8% |
| 11 | 568 | 90% | 54 (10%) | 69% of 472 | +9% |
| 12 | 938 | 85% | 143 (15%) | 42% of 102 | +4% |
| 13 | 637 | 81% | 118 (19%) | 79% of 403 | +0% |
| 14 | 427 | 80% | 84 (20%) | 81% of 613 | -1% |
| 15 | 508 | 75% | 129 (25%) | 86% of 532 | -7% |
| 16 | 89 | 78% | 20 (22%) | 81% of 951 | -4% |
| 18 | 718 | 87% | 91 (13%) | 66% of 322 | +6% |
| 19 | 370 | 81% | 70 (19%) | 78% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=943)
- check #3: lower weight: flagged coins die no more often than average (precision 83% vs base 81%, n=346)
- check #4: lower weight: flagged coins die no more often than average (precision 77% vs base 81%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 52% vs base 81%, n=82)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 81%, n=431)
- check #8: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=453)
- check #13: lower weight: flagged coins die no more often than average (precision 82% vs base 81%, n=637)
- check #14: lower weight: flagged coins die no more often than average (precision 80% vs base 81%, n=427)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=508)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=89)
- check #19: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=370)
