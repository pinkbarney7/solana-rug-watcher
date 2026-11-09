# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-09 08:43 EST. Labeled coins: 1140 (918 dead/pulled, 222 still alive). Base dead rate 80.5%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 931 | 80% | 183 (20%) | 58% of 57 | -0% |
| 2 | 24 | 21% | 19 (79%) | 81% of 981 | -60% |
| 3 | 342 | 81% | 64 (19%) | 78% of 652 | +1% |
| 4 | 151 | 75% | 37 (25%) | 80% of 844 | -5% |
| 5 | 802 | 86% | 115 (14%) | 54% of 204 | +5% |
| 6 | 80 | 52% | 38 (48%) | 82% of 850 | -28% |
| 7 | 423 | 72% | 119 (28%) | 86% of 481 | -9% |
| 8 | 447 | 73% | 121 (27%) | 80% of 425 | -8% |
| 9 | 750 | 84% | 118 (16%) | 63% of 245 | +4% |
| 10 | 782 | 88% | 90 (12%) | 44% of 210 | +8% |
| 11 | 558 | 91% | 53 (9%) | 67% of 470 | +10% |
| 12 | 928 | 84% | 151 (16%) | 43% of 100 | +3% |
| 13 | 628 | 80% | 123 (20%) | 79% of 400 | -0% |
| 14 | 418 | 80% | 84 (20%) | 80% of 610 | -1% |
| 15 | 500 | 74% | 129 (26%) | 85% of 528 | -6% |
| 16 | 88 | 78% | 19 (22%) | 80% of 940 | -2% |
| 18 | 708 | 87% | 91 (13%) | 63% of 320 | +7% |
| 19 | 369 | 80% | 75 (20%) | 77% of 571 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=931)
- check #3: lower weight: flagged coins die no more often than average (precision 81% vs base 80%, n=342)
- check #4: lower weight: flagged coins die no more often than average (precision 76% vs base 80%, n=151)
- check #6: lower weight: flagged coins die no more often than average (precision 52% vs base 80%, n=80)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 80%, n=423)
- check #8: lower weight: flagged coins die no more often than average (precision 73% vs base 80%, n=447)
- check #13: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=628)
- check #14: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=418)
- check #15: lower weight: flagged coins die no more often than average (precision 74% vs base 80%, n=500)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 80%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=369)
