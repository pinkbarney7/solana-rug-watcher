# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 17:37 EST. Labeled coins: 1184 (1008 dead/pulled, 176 still alive). Base dead rate 85.1%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 974 | 86% | 141 (14%) | 64% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 86% of 1024 | -65% |
| 3 | 364 | 87% | 46 (13%) | 83% of 674 | +2% |
| 4 | 152 | 89% | 17 (11%) | 84% of 887 | +4% |
| 5 | 829 | 90% | 81 (10%) | 63% of 221 | +5% |
| 6 | 88 | 55% | 40 (45%) | 87% of 886 | -31% |
| 7 | 449 | 76% | 109 (24%) | 92% of 499 | -9% |
| 8 | 473 | 81% | 90 (19%) | 84% of 443 | -4% |
| 9 | 776 | 89% | 87 (11%) | 71% of 263 | +4% |
| 10 | 805 | 92% | 68 (8%) | 59% of 231 | +6% |
| 11 | 600 | 90% | 59 (10%) | 78% of 472 | +5% |
| 12 | 970 | 89% | 107 (11%) | 45% of 102 | +4% |
| 13 | 669 | 86% | 92 (14%) | 82% of 403 | +1% |
| 14 | 459 | 84% | 72 (16%) | 85% of 613 | -1% |
| 15 | 540 | 78% | 118 (22%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 979 | -4% |
| 18 | 750 | 90% | 72 (10%) | 72% of 322 | +5% |
| 19 | 370 | 85% | 57 (15%) | 85% of 574 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=974)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=364)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 85%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 85%, n=449)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=473)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=669)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=459)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=540)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
