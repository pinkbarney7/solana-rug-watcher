# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 09:08 EST. Labeled coins: 1123 (867 dead/pulled, 256 still alive). Base dead rate 77.2%. Forward 24h samples so far: 67.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 915 | 76% | 216 (24%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 964 | -61% |
| 3 | 338 | 73% | 91 (27%) | 76% of 639 | -4% |
| 4 | 148 | 70% | 44 (30%) | 76% of 830 | -7% |
| 5 | 789 | 82% | 141 (18%) | 50% of 200 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 835 | -28% |
| 7 | 416 | 70% | 124 (30%) | 81% of 471 | -7% |
| 8 | 437 | 69% | 135 (31%) | 75% of 419 | -8% |
| 9 | 742 | 80% | 146 (20%) | 59% of 236 | +3% |
| 10 | 773 | 85% | 117 (15%) | 39% of 202 | +8% |
| 11 | 554 | 88% | 66 (12%) | 61% of 457 | +11% |
| 12 | 916 | 80% | 184 (20%) | 39% of 95 | +3% |
| 13 | 621 | 76% | 149 (24%) | 76% of 390 | -1% |
| 14 | 411 | 77% | 93 (23%) | 75% of 600 | +0% |
| 15 | 490 | 72% | 138 (28%) | 80% of 521 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 923 | +0% |
| 18 | 701 | 84% | 112 (16%) | 58% of 310 | +7% |
| 19 | 365 | 78% | 80 (22%) | 73% of 559 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=915)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=416)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=437)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=916)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=411)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=490)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=365)
