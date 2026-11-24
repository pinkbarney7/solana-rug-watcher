# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 16:27 EST. Labeled coins: 1203 (1019 dead/pulled, 184 still alive). Base dead rate 84.7%. Forward 24h samples so far: 106.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 993 | 85% | 149 (15%) | 64% of 58 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1041 | -66% |
| 3 | 373 | 87% | 48 (13%) | 82% of 684 | +2% |
| 4 | 153 | 88% | 18 (12%) | 83% of 905 | +4% |
| 5 | 840 | 90% | 82 (10%) | 61% of 229 | +6% |
| 6 | 94 | 52% | 45 (48%) | 87% of 899 | -33% |
| 7 | 457 | 75% | 114 (25%) | 92% of 510 | -10% |
| 8 | 484 | 81% | 91 (19%) | 82% of 450 | -4% |
| 9 | 786 | 89% | 89 (11%) | 70% of 272 | +4% |
| 10 | 811 | 91% | 70 (9%) | 59% of 244 | +7% |
| 11 | 619 | 89% | 71 (11%) | 79% of 472 | +4% |
| 12 | 989 | 88% | 115 (12%) | 45% of 102 | +4% |
| 13 | 688 | 85% | 101 (15%) | 83% of 403 | +1% |
| 14 | 478 | 83% | 80 (17%) | 85% of 613 | -1% |
| 15 | 559 | 77% | 128 (23%) | 92% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 85% of 997 | -5% |
| 18 | 769 | 89% | 84 (11%) | 73% of 322 | +4% |
| 19 | 370 | 85% | 55 (15%) | 86% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=993)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=373)
- check #6: lower weight: flagged coins die no more often than average (precision 52% vs base 85%, n=94)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=457)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=484)
- check #13: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=688)
- check #14: lower weight: flagged coins die no more often than average (precision 83% vs base 85%, n=478)
- check #15: lower weight: flagged coins die no more often than average (precision 77% vs base 85%, n=559)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
