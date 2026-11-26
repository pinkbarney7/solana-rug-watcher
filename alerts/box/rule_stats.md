# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 12:40 EST. Labeled coins: 1218 (1048 dead/pulled, 170 still alive). Base dead rate 86.0%. Forward 24h samples so far: 120.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1006 | 86% | 139 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1056 | -68% |
| 3 | 382 | 88% | 47 (12%) | 83% of 690 | +2% |
| 4 | 153 | 91% | 14 (9%) | 84% of 920 | +5% |
| 5 | 852 | 91% | 76 (9%) | 63% of 232 | +5% |
| 6 | 98 | 55% | 44 (45%) | 88% of 910 | -31% |
| 7 | 466 | 76% | 114 (24%) | 93% of 516 | -11% |
| 8 | 496 | 82% | 88 (18%) | 84% of 453 | -4% |
| 9 | 795 | 90% | 83 (10%) | 72% of 278 | +4% |
| 10 | 816 | 92% | 67 (8%) | 63% of 254 | +6% |
| 11 | 634 | 88% | 76 (12%) | 82% of 472 | +2% |
| 12 | 1004 | 89% | 109 (11%) | 49% of 102 | +3% |
| 13 | 703 | 86% | 97 (14%) | 84% of 403 | +0% |
| 14 | 493 | 85% | 75 (15%) | 86% of 613 | -1% |
| 15 | 574 | 78% | 126 (22%) | 93% of 532 | -8% |
| 16 | 94 | 81% | 18 (19%) | 86% of 1012 | -5% |
| 18 | 784 | 89% | 83 (11%) | 76% of 322 | +3% |
| 19 | 370 | 86% | 50 (14%) | 87% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1006)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=382)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 86%, n=98)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=466)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=496)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=634)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=703)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=493)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=574)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
