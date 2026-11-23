# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 20:43 EST. Labeled coins: 1183 (994 dead/pulled, 189 still alive). Base dead rate 84.0%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 973 | 84% | 152 (16%) | 60% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 85% of 1023 | -64% |
| 3 | 364 | 86% | 51 (14%) | 81% of 673 | +2% |
| 4 | 152 | 86% | 21 (14%) | 83% of 886 | +2% |
| 5 | 828 | 89% | 89 (11%) | 61% of 221 | +5% |
| 6 | 88 | 55% | 40 (45%) | 86% of 885 | -29% |
| 7 | 448 | 75% | 114 (25%) | 91% of 499 | -9% |
| 8 | 473 | 79% | 98 (21%) | 82% of 442 | -5% |
| 9 | 775 | 88% | 96 (12%) | 70% of 263 | +4% |
| 10 | 804 | 91% | 70 (9%) | 55% of 231 | +7% |
| 11 | 599 | 90% | 60 (10%) | 75% of 472 | +6% |
| 12 | 969 | 88% | 120 (12%) | 45% of 102 | +4% |
| 13 | 668 | 85% | 101 (15%) | 81% of 403 | +1% |
| 14 | 458 | 82% | 82 (18%) | 85% of 613 | -2% |
| 15 | 539 | 77% | 124 (23%) | 90% of 532 | -7% |
| 16 | 93 | 80% | 19 (20%) | 84% of 978 | -4% |
| 18 | 749 | 89% | 81 (11%) | 70% of 322 | +5% |
| 19 | 370 | 83% | 62 (17%) | 84% of 574 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 84% vs base 84%, n=973)
- check #3: lower weight: flagged coins die no more often than average (precision 86% vs base 84%, n=364)
- check #4: lower weight: flagged coins die no more often than average (precision 86% vs base 84%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 84%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 84%, n=448)
- check #8: lower weight: flagged coins die no more often than average (precision 79% vs base 84%, n=473)
- check #13: lower weight: flagged coins die no more often than average (precision 85% vs base 84%, n=668)
- check #14: lower weight: flagged coins die no more often than average (precision 82% vs base 84%, n=458)
- check #15: lower weight: flagged coins die no more often than average (precision 77% vs base 84%, n=539)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 84%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 83% vs base 84%, n=370)
