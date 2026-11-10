# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-09 20:19 EST. Labeled coins: 1143 (930 dead/pulled, 213 still alive). Base dead rate 81.4%. Forward 24h samples so far: 74.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 934 | 81% | 175 (19%) | 60% of 57 | -0% |
| 2 | 24 | 21% | 19 (79%) | 82% of 984 | -61% |
| 3 | 343 | 83% | 58 (17%) | 78% of 654 | +2% |
| 4 | 151 | 76% | 36 (24%) | 81% of 847 | -5% |
| 5 | 803 | 87% | 106 (13%) | 55% of 206 | +5% |
| 6 | 80 | 54% | 37 (46%) | 82% of 853 | -28% |
| 7 | 424 | 72% | 118 (28%) | 87% of 483 | -9% |
| 8 | 449 | 75% | 114 (25%) | 80% of 426 | -7% |
| 9 | 751 | 85% | 110 (15%) | 64% of 247 | +4% |
| 10 | 784 | 89% | 84 (11%) | 46% of 211 | +8% |
| 11 | 560 | 91% | 50 (9%) | 68% of 471 | +10% |
| 12 | 931 | 85% | 142 (15%) | 43% of 100 | +3% |
| 13 | 630 | 82% | 116 (18%) | 79% of 401 | +0% |
| 14 | 419 | 81% | 80 (19%) | 81% of 612 | -0% |
| 15 | 501 | 75% | 124 (25%) | 86% of 530 | -6% |
| 16 | 88 | 78% | 19 (22%) | 81% of 943 | -3% |
| 18 | 709 | 88% | 88 (12%) | 66% of 322 | +6% |
| 19 | 369 | 81% | 71 (19%) | 78% of 573 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=934)
- check #3: lower weight: flagged coins die no more often than average (precision 83% vs base 81%, n=343)
- check #4: lower weight: flagged coins die no more often than average (precision 76% vs base 81%, n=151)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 81%, n=80)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 81%, n=424)
- check #8: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=449)
- check #13: lower weight: flagged coins die no more often than average (precision 82% vs base 81%, n=630)
- check #14: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=419)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=501)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=369)
