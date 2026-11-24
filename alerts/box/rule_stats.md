# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 21:50 EST. Labeled coins: 1187 (1012 dead/pulled, 175 still alive). Base dead rate 85.3%. Forward 24h samples so far: 90.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 977 | 86% | 140 (14%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1026 | -66% |
| 3 | 365 | 88% | 45 (12%) | 83% of 676 | +2% |
| 4 | 152 | 89% | 17 (11%) | 84% of 890 | +4% |
| 5 | 830 | 91% | 78 (9%) | 62% of 223 | +5% |
| 6 | 89 | 54% | 41 (46%) | 87% of 888 | -31% |
| 7 | 452 | 75% | 111 (25%) | 93% of 499 | -10% |
| 8 | 474 | 82% | 87 (18%) | 83% of 445 | -4% |
| 9 | 776 | 89% | 84 (11%) | 71% of 266 | +4% |
| 10 | 806 | 92% | 67 (8%) | 60% of 233 | +6% |
| 11 | 603 | 90% | 60 (10%) | 78% of 472 | +5% |
| 12 | 973 | 89% | 106 (11%) | 45% of 102 | +4% |
| 13 | 672 | 86% | 92 (14%) | 83% of 403 | +1% |
| 14 | 462 | 85% | 71 (15%) | 85% of 613 | -1% |
| 15 | 543 | 78% | 117 (22%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 982 | -5% |
| 18 | 753 | 90% | 73 (10%) | 72% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 85% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=977)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 85%, n=365)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 85%, n=89)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=452)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=474)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=672)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=462)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=543)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
