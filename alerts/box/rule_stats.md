# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 11:05 EST. Labeled coins: 1183 (1000 dead/pulled, 183 still alive). Base dead rate 84.5%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 973 | 85% | 146 (15%) | 60% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 85% of 1023 | -65% |
| 3 | 364 | 87% | 48 (13%) | 82% of 673 | +2% |
| 4 | 152 | 88% | 19 (12%) | 83% of 886 | +3% |
| 5 | 828 | 90% | 85 (10%) | 62% of 221 | +5% |
| 6 | 88 | 55% | 40 (45%) | 86% of 885 | -30% |
| 7 | 448 | 75% | 113 (25%) | 92% of 499 | -10% |
| 8 | 473 | 80% | 95 (20%) | 83% of 442 | -5% |
| 9 | 775 | 88% | 92 (12%) | 70% of 263 | +4% |
| 10 | 804 | 91% | 69 (9%) | 57% of 231 | +7% |
| 11 | 599 | 90% | 59 (10%) | 76% of 472 | +6% |
| 12 | 969 | 88% | 114 (12%) | 45% of 102 | +4% |
| 13 | 668 | 85% | 97 (15%) | 82% of 403 | +1% |
| 14 | 458 | 83% | 78 (17%) | 85% of 613 | -2% |
| 15 | 539 | 78% | 120 (22%) | 91% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 84% of 978 | -4% |
| 18 | 749 | 90% | 76 (10%) | 71% of 322 | +5% |
| 19 | 370 | 84% | 59 (16%) | 84% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 84%, n=973)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 84%, n=364)
- check #4: lower weight: flagged coins die no more often than average (precision 88% vs base 84%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 84%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 84%, n=448)
- check #8: lower weight: flagged coins die no more often than average (precision 80% vs base 84%, n=473)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 84%, n=668)
- check #14: lower weight: flagged coins die no more often than average (precision 83% vs base 84%, n=458)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 84%, n=539)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 84%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 84% vs base 84%, n=370)
