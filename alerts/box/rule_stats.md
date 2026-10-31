# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 12:00 EDT. Labeled coins: 1068 (793 dead/pulled, 275 still alive). Base dead rate 74.3%. Forward 24h samples so far: 40.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 864 | 73% | 233 (27%) | 49% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 73% of 911 | -55% |
| 3 | 310 | 65% | 110 (35%) | 75% of 611 | -10% |
| 4 | 143 | 62% | 54 (38%) | 74% of 779 | -12% |
| 5 | 750 | 79% | 160 (21%) | 45% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 73% of 805 | -24% |
| 7 | 394 | 69% | 124 (31%) | 73% of 458 | -6% |
| 8 | 411 | 64% | 150 (36%) | 73% of 391 | -11% |
| 9 | 704 | 77% | 162 (23%) | 55% of 218 | +3% |
| 10 | 732 | 81% | 139 (19%) | 36% of 187 | +7% |
| 11 | 528 | 87% | 67 (13%) | 55% of 427 | +13% |
| 12 | 869 | 76% | 208 (24%) | 40% of 86 | +2% |
| 13 | 584 | 72% | 163 (28%) | 74% of 371 | -2% |
| 14 | 392 | 77% | 91 (23%) | 70% of 563 | +3% |
| 15 | 458 | 70% | 136 (30%) | 75% of 497 | -4% |
| 16 | 84 | 76% | 20 (24%) | 72% of 871 | +2% |
| 18 | 666 | 80% | 132 (20%) | 56% of 289 | +6% |
| 19 | 345 | 77% | 81 (23%) | 69% of 530 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 73% vs base 74%, n=864)
- check #3: lower weight: flagged coins die no more often than average (precision 64% vs base 74%, n=310)
- check #4: lower weight: flagged coins die no more often than average (precision 62% vs base 74%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 74%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 68% vs base 74%, n=394)
- check #8: lower weight: flagged coins die no more often than average (precision 64% vs base 74%, n=411)
- check #9: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=704)
- check #12: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=869)
- check #13: lower weight: flagged coins die no more often than average (precision 72% vs base 74%, n=584)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=392)
- check #15: lower weight: flagged coins die no more often than average (precision 70% vs base 74%, n=458)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=345)
