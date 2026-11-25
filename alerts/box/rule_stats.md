# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 21:41 EST. Labeled coins: 1207 (1027 dead/pulled, 180 still alive). Base dead rate 85.1%. Forward 24h samples so far: 109.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 997 | 85% | 146 (15%) | 64% of 58 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1045 | -67% |
| 3 | 375 | 87% | 50 (13%) | 83% of 686 | +2% |
| 4 | 153 | 90% | 15 (10%) | 83% of 909 | +5% |
| 5 | 843 | 90% | 82 (10%) | 63% of 230 | +5% |
| 6 | 95 | 53% | 45 (47%) | 87% of 902 | -32% |
| 7 | 460 | 75% | 113 (25%) | 92% of 511 | -10% |
| 8 | 487 | 82% | 90 (18%) | 83% of 451 | -4% |
| 9 | 788 | 89% | 88 (11%) | 71% of 274 | +4% |
| 10 | 814 | 91% | 71 (9%) | 61% of 245 | +6% |
| 11 | 623 | 88% | 74 (12%) | 80% of 472 | +3% |
| 12 | 993 | 89% | 113 (11%) | 46% of 102 | +4% |
| 13 | 692 | 85% | 101 (15%) | 83% of 403 | +0% |
| 14 | 482 | 83% | 80 (17%) | 86% of 613 | -2% |
| 15 | 563 | 77% | 127 (23%) | 92% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 85% of 1001 | -5% |
| 18 | 773 | 89% | 84 (11%) | 74% of 322 | +4% |
| 19 | 370 | 86% | 53 (14%) | 86% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=997)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=375)
- check #6: lower weight: flagged coins die no more often than average (precision 53% vs base 85%, n=95)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=460)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 85%, n=487)
- check #13: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=692)
- check #14: lower weight: flagged coins die no more often than average (precision 83% vs base 85%, n=482)
- check #15: lower weight: flagged coins die no more often than average (precision 77% vs base 85%, n=563)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=370)
