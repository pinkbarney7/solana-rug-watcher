# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 18:59 EST. Labeled coins: 1205 (1024 dead/pulled, 181 still alive). Base dead rate 85.0%. Forward 24h samples so far: 108.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 995 | 85% | 146 (15%) | 64% of 58 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1043 | -66% |
| 3 | 374 | 87% | 49 (13%) | 83% of 685 | +2% |
| 4 | 153 | 90% | 15 (10%) | 83% of 907 | +5% |
| 5 | 841 | 90% | 81 (10%) | 62% of 230 | +5% |
| 6 | 94 | 53% | 44 (47%) | 87% of 901 | -32% |
| 7 | 459 | 75% | 113 (25%) | 92% of 510 | -10% |
| 8 | 485 | 81% | 90 (19%) | 83% of 451 | -4% |
| 9 | 787 | 89% | 87 (11%) | 70% of 273 | +4% |
| 10 | 813 | 91% | 71 (9%) | 61% of 244 | +6% |
| 11 | 621 | 88% | 73 (12%) | 80% of 472 | +3% |
| 12 | 991 | 89% | 113 (11%) | 46% of 102 | +4% |
| 13 | 690 | 85% | 101 (15%) | 83% of 403 | +0% |
| 14 | 480 | 83% | 80 (17%) | 86% of 613 | -2% |
| 15 | 561 | 78% | 126 (22%) | 92% of 532 | -7% |
| 16 | 94 | 80% | 19 (20%) | 85% of 999 | -5% |
| 18 | 771 | 89% | 83 (11%) | 74% of 322 | +4% |
| 19 | 370 | 86% | 53 (14%) | 86% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=995)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=374)
- check #6: lower weight: flagged coins die no more often than average (precision 53% vs base 85%, n=94)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=459)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=485)
- check #13: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=690)
- check #14: lower weight: flagged coins die no more often than average (precision 83% vs base 85%, n=480)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=561)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=370)
