# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 12:43 EDT. Labeled coins: 1068 (800 dead/pulled, 268 still alive). Base dead rate 74.9%. Forward 24h samples so far: 40.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 864 | 74% | 227 (26%) | 51% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 74% of 911 | -56% |
| 3 | 310 | 65% | 107 (35%) | 76% of 611 | -9% |
| 4 | 143 | 64% | 51 (36%) | 74% of 779 | -11% |
| 5 | 750 | 79% | 155 (21%) | 46% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 74% of 805 | -24% |
| 7 | 394 | 69% | 124 (31%) | 75% of 458 | -6% |
| 8 | 411 | 64% | 146 (36%) | 74% of 391 | -10% |
| 9 | 704 | 78% | 158 (22%) | 56% of 218 | +3% |
| 10 | 732 | 82% | 134 (18%) | 37% of 187 | +7% |
| 11 | 528 | 87% | 67 (13%) | 56% of 427 | +12% |
| 12 | 869 | 77% | 201 (23%) | 40% of 86 | +2% |
| 13 | 584 | 73% | 160 (27%) | 75% of 371 | -2% |
| 14 | 392 | 77% | 89 (23%) | 71% of 563 | +2% |
| 15 | 458 | 71% | 134 (29%) | 76% of 497 | -4% |
| 16 | 84 | 76% | 20 (24%) | 73% of 871 | +1% |
| 18 | 666 | 81% | 128 (19%) | 57% of 289 | +6% |
| 19 | 345 | 77% | 79 (23%) | 70% of 530 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 74% vs base 75%, n=864)
- check #3: lower weight: flagged coins die no more often than average (precision 66% vs base 75%, n=310)
- check #4: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 75%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 68% vs base 75%, n=394)
- check #8: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=411)
- check #9: lower weight: flagged coins die no more often than average (precision 78% vs base 75%, n=704)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=869)
- check #13: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=584)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=392)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=458)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 75%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=345)
