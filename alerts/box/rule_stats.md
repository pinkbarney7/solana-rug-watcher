# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 22:23 EST. Labeled coins: 1188 (1013 dead/pulled, 175 still alive). Base dead rate 85.3%. Forward 24h samples so far: 90.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 978 | 86% | 140 (14%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1027 | -66% |
| 3 | 366 | 88% | 45 (12%) | 83% of 676 | +2% |
| 4 | 152 | 89% | 17 (11%) | 84% of 891 | +4% |
| 5 | 830 | 91% | 78 (9%) | 62% of 224 | +5% |
| 6 | 89 | 54% | 41 (46%) | 87% of 889 | -31% |
| 7 | 452 | 75% | 111 (25%) | 93% of 500 | -10% |
| 8 | 475 | 82% | 87 (18%) | 83% of 445 | -4% |
| 9 | 776 | 89% | 84 (11%) | 71% of 267 | +4% |
| 10 | 806 | 92% | 67 (8%) | 60% of 234 | +6% |
| 11 | 604 | 90% | 60 (10%) | 78% of 472 | +5% |
| 12 | 974 | 89% | 106 (11%) | 45% of 102 | +4% |
| 13 | 673 | 86% | 92 (14%) | 83% of 403 | +1% |
| 14 | 463 | 85% | 71 (15%) | 85% of 613 | -1% |
| 15 | 544 | 78% | 117 (22%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 983 | -5% |
| 18 | 754 | 90% | 73 (10%) | 72% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 85% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=978)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 85%, n=366)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 85%, n=89)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=452)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=475)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=673)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=463)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=544)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
