# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 21:02 EST. Labeled coins: 1223 (1053 dead/pulled, 170 still alive). Base dead rate 86.1%. Forward 24h samples so far: 126.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1011 | 86% | 139 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1061 | -68% |
| 3 | 385 | 88% | 46 (12%) | 83% of 692 | +2% |
| 4 | 153 | 92% | 13 (8%) | 84% of 925 | +5% |
| 5 | 857 | 91% | 77 (9%) | 64% of 232 | +5% |
| 6 | 99 | 56% | 44 (44%) | 88% of 914 | -31% |
| 7 | 468 | 76% | 114 (24%) | 93% of 519 | -10% |
| 8 | 500 | 82% | 88 (18%) | 84% of 454 | -4% |
| 9 | 800 | 89% | 85 (11%) | 73% of 278 | +3% |
| 10 | 817 | 92% | 66 (8%) | 64% of 258 | +6% |
| 11 | 639 | 88% | 78 (12%) | 82% of 472 | +2% |
| 12 | 1009 | 89% | 109 (11%) | 49% of 102 | +3% |
| 13 | 708 | 86% | 98 (14%) | 84% of 403 | +0% |
| 14 | 498 | 85% | 76 (15%) | 86% of 613 | -1% |
| 15 | 579 | 78% | 126 (22%) | 93% of 532 | -8% |
| 16 | 95 | 81% | 18 (19%) | 86% of 1016 | -5% |
| 18 | 789 | 89% | 84 (11%) | 76% of 322 | +3% |
| 19 | 370 | 87% | 48 (13%) | 87% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1011)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=385)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=99)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=468)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=500)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=639)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=708)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=498)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=579)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=370)
