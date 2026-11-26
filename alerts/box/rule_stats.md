# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 22:47 EST. Labeled coins: 1215 (1044 dead/pulled, 171 still alive). Base dead rate 85.9%. Forward 24h samples so far: 116.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1003 | 86% | 140 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1053 | -67% |
| 3 | 380 | 88% | 47 (12%) | 83% of 689 | +2% |
| 4 | 153 | 90% | 15 (10%) | 84% of 917 | +4% |
| 5 | 850 | 91% | 76 (9%) | 63% of 231 | +5% |
| 6 | 97 | 56% | 43 (44%) | 88% of 908 | -30% |
| 7 | 464 | 75% | 114 (25%) | 93% of 515 | -10% |
| 8 | 493 | 82% | 87 (18%) | 84% of 453 | -4% |
| 9 | 793 | 90% | 83 (10%) | 71% of 277 | +4% |
| 10 | 816 | 92% | 68 (8%) | 63% of 251 | +6% |
| 11 | 631 | 88% | 74 (12%) | 81% of 472 | +2% |
| 12 | 1001 | 89% | 109 (11%) | 48% of 102 | +3% |
| 13 | 700 | 86% | 96 (14%) | 84% of 403 | +0% |
| 14 | 490 | 85% | 75 (15%) | 86% of 613 | -1% |
| 15 | 571 | 78% | 125 (22%) | 93% of 532 | -8% |
| 16 | 94 | 80% | 19 (20%) | 86% of 1009 | -6% |
| 18 | 781 | 89% | 83 (11%) | 75% of 322 | +3% |
| 19 | 370 | 86% | 50 (14%) | 87% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1003)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=380)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=97)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 86%, n=464)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=493)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=631)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=700)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=490)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=571)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
