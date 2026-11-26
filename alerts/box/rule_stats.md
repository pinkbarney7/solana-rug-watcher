# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 14:35 EST. Labeled coins: 1221 (1049 dead/pulled, 172 still alive). Base dead rate 85.9%. Forward 24h samples so far: 123.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1009 | 86% | 141 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1059 | -67% |
| 3 | 383 | 88% | 47 (12%) | 83% of 692 | +2% |
| 4 | 153 | 91% | 14 (9%) | 84% of 923 | +5% |
| 5 | 855 | 91% | 78 (9%) | 63% of 232 | +5% |
| 6 | 98 | 55% | 44 (45%) | 88% of 913 | -31% |
| 7 | 468 | 75% | 116 (25%) | 93% of 517 | -11% |
| 8 | 499 | 82% | 90 (18%) | 84% of 453 | -4% |
| 9 | 798 | 89% | 85 (11%) | 72% of 278 | +3% |
| 10 | 817 | 92% | 68 (8%) | 63% of 256 | +6% |
| 11 | 637 | 88% | 78 (12%) | 82% of 472 | +2% |
| 12 | 1007 | 89% | 111 (11%) | 49% of 102 | +3% |
| 13 | 706 | 86% | 99 (14%) | 84% of 403 | +0% |
| 14 | 496 | 84% | 77 (16%) | 86% of 613 | -1% |
| 15 | 577 | 78% | 128 (22%) | 93% of 532 | -8% |
| 16 | 95 | 81% | 18 (19%) | 86% of 1014 | -5% |
| 18 | 787 | 89% | 85 (11%) | 76% of 322 | +3% |
| 19 | 370 | 86% | 50 (14%) | 87% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1009)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=383)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 86%, n=98)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 86%, n=468)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=499)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=637)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=706)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 86%, n=496)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=577)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=370)
