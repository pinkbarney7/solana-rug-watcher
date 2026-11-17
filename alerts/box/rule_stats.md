# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 08:22 EST. Labeled coins: 1174 (973 dead/pulled, 201 still alive). Base dead rate 82.9%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 964 | 83% | 164 (17%) | 60% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 83% of 1014 | -63% |
| 3 | 359 | 85% | 54 (15%) | 80% of 669 | +2% |
| 4 | 152 | 84% | 25 (16%) | 81% of 877 | +1% |
| 5 | 820 | 89% | 94 (11%) | 57% of 220 | +6% |
| 6 | 88 | 51% | 43 (49%) | 85% of 876 | -32% |
| 7 | 442 | 73% | 120 (27%) | 90% of 496 | -10% |
| 8 | 466 | 77% | 106 (23%) | 81% of 440 | -6% |
| 9 | 770 | 87% | 102 (13%) | 67% of 259 | +4% |
| 10 | 799 | 90% | 76 (10%) | 51% of 227 | +8% |
| 11 | 590 | 89% | 62 (11%) | 73% of 472 | +7% |
| 12 | 960 | 86% | 131 (14%) | 44% of 102 | +3% |
| 13 | 659 | 83% | 110 (17%) | 81% of 403 | +0% |
| 14 | 449 | 81% | 87 (19%) | 84% of 613 | -2% |
| 15 | 530 | 76% | 128 (24%) | 89% of 532 | -7% |
| 16 | 91 | 80% | 18 (20%) | 82% of 971 | -3% |
| 18 | 740 | 88% | 88 (12%) | 69% of 322 | +5% |
| 19 | 370 | 82% | 65 (18%) | 82% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 83% vs base 83%, n=964)
- check #3: lower weight: flagged coins die no more often than average (precision 85% vs base 83%, n=359)
- check #4: lower weight: flagged coins die no more often than average (precision 84% vs base 83%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 83%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 73% vs base 83%, n=442)
- check #8: lower weight: flagged coins die no more often than average (precision 77% vs base 83%, n=466)
- check #13: lower weight: flagged coins die no more often than average (precision 83% vs base 83%, n=659)
- check #14: lower weight: flagged coins die no more often than average (precision 81% vs base 83%, n=449)
- check #15: lower weight: flagged coins die no more often than average (precision 76% vs base 83%, n=530)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 83%, n=91)
- check #19: lower weight: flagged coins die no more often than average (precision 82% vs base 83%, n=370)
