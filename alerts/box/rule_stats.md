# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 08:58 EST. Labeled coins: 1122 (867 dead/pulled, 255 still alive). Base dead rate 77.3%. Forward 24h samples so far: 66.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 914 | 76% | 215 (24%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 963 | -61% |
| 3 | 338 | 73% | 91 (27%) | 76% of 638 | -4% |
| 4 | 148 | 70% | 44 (30%) | 76% of 829 | -7% |
| 5 | 788 | 82% | 140 (18%) | 50% of 200 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 834 | -29% |
| 7 | 415 | 70% | 123 (30%) | 81% of 471 | -7% |
| 8 | 437 | 69% | 135 (31%) | 76% of 418 | -8% |
| 9 | 741 | 80% | 145 (20%) | 59% of 236 | +3% |
| 10 | 772 | 85% | 116 (15%) | 39% of 202 | +8% |
| 11 | 554 | 88% | 66 (12%) | 62% of 456 | +11% |
| 12 | 915 | 80% | 183 (20%) | 39% of 95 | +3% |
| 13 | 621 | 76% | 149 (24%) | 76% of 389 | -1% |
| 14 | 410 | 78% | 92 (22%) | 75% of 600 | +0% |
| 15 | 489 | 72% | 137 (28%) | 80% of 521 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 922 | +0% |
| 18 | 700 | 84% | 111 (16%) | 58% of 310 | +7% |
| 19 | 364 | 78% | 79 (22%) | 73% of 559 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=914)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=415)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=437)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=915)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=410)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=489)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=364)
