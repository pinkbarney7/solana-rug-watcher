# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 11:15 EST. Labeled coins: 1124 (868 dead/pulled, 256 still alive). Base dead rate 77.2%. Forward 24h samples so far: 67.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 916 | 76% | 216 (24%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 965 | -61% |
| 3 | 338 | 73% | 91 (27%) | 76% of 640 | -4% |
| 4 | 149 | 70% | 44 (30%) | 76% of 830 | -7% |
| 5 | 789 | 82% | 141 (18%) | 50% of 201 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 836 | -29% |
| 7 | 416 | 70% | 124 (30%) | 81% of 472 | -7% |
| 8 | 438 | 69% | 135 (31%) | 75% of 419 | -8% |
| 9 | 742 | 80% | 146 (20%) | 59% of 237 | +3% |
| 10 | 774 | 85% | 117 (15%) | 39% of 202 | +8% |
| 11 | 554 | 88% | 66 (12%) | 62% of 458 | +11% |
| 12 | 917 | 80% | 184 (20%) | 39% of 95 | +3% |
| 13 | 621 | 76% | 149 (24%) | 76% of 391 | -1% |
| 14 | 412 | 77% | 93 (23%) | 75% of 600 | +0% |
| 15 | 491 | 72% | 138 (28%) | 80% of 521 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 924 | +0% |
| 18 | 702 | 84% | 112 (16%) | 58% of 310 | +7% |
| 19 | 366 | 78% | 80 (22%) | 73% of 559 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=916)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=149)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=416)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=438)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=917)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=412)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=491)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=366)
