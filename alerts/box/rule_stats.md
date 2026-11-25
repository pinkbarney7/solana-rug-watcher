# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 19:49 EST. Labeled coins: 1206 (1027 dead/pulled, 179 still alive). Base dead rate 85.2%. Forward 24h samples so far: 108.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 996 | 85% | 145 (15%) | 64% of 58 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1044 | -67% |
| 3 | 374 | 87% | 49 (13%) | 83% of 686 | +2% |
| 4 | 153 | 90% | 15 (10%) | 83% of 908 | +5% |
| 5 | 842 | 90% | 81 (10%) | 63% of 230 | +5% |
| 6 | 94 | 53% | 44 (47%) | 87% of 902 | -32% |
| 7 | 460 | 75% | 113 (25%) | 92% of 510 | -10% |
| 8 | 486 | 82% | 89 (18%) | 83% of 451 | -3% |
| 9 | 787 | 89% | 87 (11%) | 71% of 274 | +4% |
| 10 | 814 | 91% | 71 (9%) | 61% of 244 | +6% |
| 11 | 622 | 88% | 73 (12%) | 80% of 472 | +3% |
| 12 | 992 | 89% | 112 (11%) | 46% of 102 | +4% |
| 13 | 691 | 86% | 100 (14%) | 83% of 403 | +0% |
| 14 | 481 | 84% | 79 (16%) | 86% of 613 | -2% |
| 15 | 562 | 78% | 126 (22%) | 92% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 85% of 1000 | -5% |
| 18 | 772 | 89% | 83 (11%) | 74% of 322 | +4% |
| 19 | 370 | 86% | 53 (14%) | 86% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=996)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=374)
- check #6: lower weight: flagged coins die no more often than average (precision 53% vs base 85%, n=94)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=460)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=486)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=691)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=481)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=562)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=370)
