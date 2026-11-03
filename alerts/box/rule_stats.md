# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 13:43 EST. Labeled coins: 1124 (872 dead/pulled, 252 still alive). Base dead rate 77.6%. Forward 24h samples so far: 69.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 916 | 77% | 212 (23%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 965 | -61% |
| 3 | 338 | 74% | 89 (26%) | 77% of 640 | -4% |
| 4 | 149 | 70% | 44 (30%) | 77% of 830 | -7% |
| 5 | 789 | 83% | 138 (17%) | 50% of 201 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 836 | -29% |
| 7 | 416 | 70% | 123 (30%) | 81% of 472 | -7% |
| 8 | 438 | 70% | 133 (30%) | 76% of 419 | -8% |
| 9 | 742 | 81% | 142 (19%) | 59% of 237 | +3% |
| 10 | 774 | 85% | 115 (15%) | 40% of 202 | +8% |
| 11 | 554 | 88% | 65 (12%) | 62% of 458 | +11% |
| 12 | 917 | 80% | 180 (20%) | 39% of 95 | +3% |
| 13 | 621 | 76% | 147 (24%) | 77% of 391 | -1% |
| 14 | 412 | 78% | 92 (22%) | 76% of 600 | +0% |
| 15 | 491 | 72% | 137 (28%) | 81% of 521 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 924 | -0% |
| 18 | 702 | 84% | 111 (16%) | 59% of 310 | +7% |
| 19 | 366 | 78% | 79 (22%) | 74% of 559 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=916)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=149)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 78%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=416)
- check #8: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=438)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 78%, n=917)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 78%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=412)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=491)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=366)
