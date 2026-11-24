# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 22:46 EST. Labeled coins: 1189 (1013 dead/pulled, 176 still alive). Base dead rate 85.2%. Forward 24h samples so far: 91.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 979 | 86% | 141 (14%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1028 | -66% |
| 3 | 367 | 87% | 46 (13%) | 83% of 676 | +2% |
| 4 | 152 | 89% | 17 (11%) | 84% of 892 | +4% |
| 5 | 831 | 90% | 79 (10%) | 62% of 224 | +5% |
| 6 | 90 | 53% | 42 (47%) | 87% of 889 | -32% |
| 7 | 452 | 75% | 111 (25%) | 92% of 501 | -10% |
| 8 | 475 | 82% | 87 (18%) | 83% of 446 | -4% |
| 9 | 777 | 89% | 85 (11%) | 71% of 267 | +4% |
| 10 | 806 | 92% | 67 (8%) | 60% of 235 | +6% |
| 11 | 605 | 90% | 61 (10%) | 78% of 472 | +5% |
| 12 | 975 | 89% | 107 (11%) | 45% of 102 | +4% |
| 13 | 674 | 86% | 93 (14%) | 83% of 403 | +1% |
| 14 | 464 | 84% | 72 (16%) | 85% of 613 | -1% |
| 15 | 545 | 78% | 118 (22%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 984 | -5% |
| 18 | 755 | 90% | 74 (10%) | 72% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 85% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=979)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 85%, n=367)
- check #6: lower weight: flagged coins die no more often than average (precision 53% vs base 85%, n=90)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=452)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=475)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=674)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=464)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=545)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
