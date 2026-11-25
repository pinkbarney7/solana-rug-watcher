# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 07:54 EST. Labeled coins: 1208 (1035 dead/pulled, 173 still alive). Base dead rate 85.7%. Forward 24h samples so far: 109.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 997 | 86% | 142 (14%) | 64% of 59 | +0% |
| 2 | 27 | 19% | 22 (81%) | 86% of 1046 | -67% |
| 3 | 376 | 87% | 48 (13%) | 83% of 686 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 910 | +5% |
| 5 | 843 | 91% | 78 (9%) | 63% of 231 | +5% |
| 6 | 95 | 54% | 44 (46%) | 87% of 903 | -32% |
| 7 | 460 | 75% | 113 (25%) | 93% of 512 | -10% |
| 8 | 487 | 82% | 88 (18%) | 83% of 452 | -4% |
| 9 | 788 | 89% | 84 (11%) | 71% of 275 | +4% |
| 10 | 814 | 91% | 70 (9%) | 62% of 246 | +6% |
| 11 | 624 | 88% | 73 (12%) | 81% of 472 | +3% |
| 12 | 994 | 89% | 110 (11%) | 47% of 102 | +3% |
| 13 | 693 | 86% | 97 (14%) | 83% of 403 | +0% |
| 14 | 483 | 84% | 76 (16%) | 86% of 613 | -1% |
| 15 | 564 | 78% | 126 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 86% of 1002 | -6% |
| 18 | 774 | 89% | 82 (11%) | 75% of 322 | +4% |
| 19 | 370 | 86% | 53 (14%) | 87% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=997)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=376)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 86%, n=95)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 86%, n=460)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=487)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=624)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=693)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 86%, n=483)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=564)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
