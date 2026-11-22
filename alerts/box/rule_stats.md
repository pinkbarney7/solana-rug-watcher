# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 18:16 EST. Labeled coins: 1176 (986 dead/pulled, 190 still alive). Base dead rate 83.8%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 966 | 84% | 153 (16%) | 60% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 85% of 1016 | -64% |
| 3 | 359 | 86% | 51 (14%) | 81% of 671 | +2% |
| 4 | 152 | 85% | 23 (15%) | 82% of 879 | +1% |
| 5 | 822 | 89% | 87 (11%) | 59% of 220 | +6% |
| 6 | 88 | 53% | 41 (47%) | 86% of 878 | -30% |
| 7 | 443 | 74% | 115 (26%) | 91% of 497 | -10% |
| 8 | 468 | 79% | 98 (21%) | 82% of 440 | -5% |
| 9 | 770 | 88% | 94 (12%) | 68% of 261 | +4% |
| 10 | 800 | 91% | 71 (9%) | 54% of 228 | +7% |
| 11 | 592 | 90% | 58 (10%) | 75% of 472 | +6% |
| 12 | 962 | 87% | 121 (13%) | 45% of 102 | +4% |
| 13 | 661 | 85% | 101 (15%) | 81% of 403 | +1% |
| 14 | 451 | 82% | 83 (18%) | 85% of 613 | -2% |
| 15 | 532 | 77% | 124 (23%) | 90% of 532 | -7% |
| 16 | 91 | 80% | 18 (20%) | 84% of 973 | -4% |
| 18 | 742 | 89% | 81 (11%) | 70% of 322 | +5% |
| 19 | 370 | 83% | 63 (17%) | 84% of 574 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 84% vs base 84%, n=966)
- check #3: lower weight: flagged coins die no more often than average (precision 86% vs base 84%, n=359)
- check #4: lower weight: flagged coins die no more often than average (precision 85% vs base 84%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 53% vs base 84%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 74% vs base 84%, n=443)
- check #8: lower weight: flagged coins die no more often than average (precision 79% vs base 84%, n=468)
- check #13: lower weight: flagged coins die no more often than average (precision 85% vs base 84%, n=661)
- check #14: lower weight: flagged coins die no more often than average (precision 82% vs base 84%, n=451)
- check #15: lower weight: flagged coins die no more often than average (precision 77% vs base 84%, n=532)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 84%, n=91)
- check #19: lower weight: flagged coins die no more often than average (precision 83% vs base 84%, n=370)
