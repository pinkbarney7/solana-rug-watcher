# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-09 22:38 EST. Labeled coins: 1145 (931 dead/pulled, 214 still alive). Base dead rate 81.3%. Forward 24h samples so far: 76.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 936 | 81% | 176 (19%) | 60% of 57 | -0% |
| 2 | 24 | 21% | 19 (79%) | 82% of 986 | -60% |
| 3 | 343 | 83% | 58 (17%) | 78% of 656 | +2% |
| 4 | 152 | 76% | 36 (24%) | 81% of 848 | -5% |
| 5 | 804 | 87% | 106 (13%) | 55% of 207 | +6% |
| 6 | 80 | 54% | 37 (46%) | 82% of 855 | -28% |
| 7 | 426 | 72% | 119 (28%) | 87% of 483 | -9% |
| 8 | 449 | 75% | 114 (25%) | 80% of 428 | -7% |
| 9 | 752 | 85% | 110 (15%) | 64% of 248 | +4% |
| 10 | 785 | 89% | 84 (11%) | 46% of 212 | +8% |
| 11 | 561 | 91% | 50 (9%) | 68% of 472 | +10% |
| 12 | 932 | 85% | 142 (15%) | 43% of 101 | +3% |
| 13 | 631 | 82% | 116 (18%) | 79% of 402 | +0% |
| 14 | 420 | 81% | 80 (19%) | 80% of 613 | -0% |
| 15 | 502 | 75% | 124 (25%) | 86% of 531 | -6% |
| 16 | 88 | 78% | 19 (22%) | 81% of 945 | -3% |
| 18 | 711 | 87% | 89 (13%) | 66% of 322 | +6% |
| 19 | 369 | 81% | 71 (19%) | 78% of 574 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=936)
- check #3: lower weight: flagged coins die no more often than average (precision 83% vs base 81%, n=343)
- check #4: lower weight: flagged coins die no more often than average (precision 76% vs base 81%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 81%, n=80)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 81%, n=426)
- check #8: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=449)
- check #13: lower weight: flagged coins die no more often than average (precision 82% vs base 81%, n=631)
- check #14: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=420)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=502)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=369)
