# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 13:35 EDT. Labeled coins: 1069 (802 dead/pulled, 267 still alive). Base dead rate 75.0%. Forward 24h samples so far: 41.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 865 | 74% | 226 (26%) | 51% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 74% of 912 | -56% |
| 3 | 311 | 66% | 106 (34%) | 76% of 611 | -9% |
| 4 | 143 | 64% | 51 (36%) | 74% of 780 | -11% |
| 5 | 751 | 79% | 154 (21%) | 46% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 74% of 806 | -24% |
| 7 | 394 | 69% | 124 (31%) | 75% of 459 | -6% |
| 8 | 412 | 65% | 145 (35%) | 74% of 391 | -10% |
| 9 | 705 | 78% | 157 (22%) | 56% of 218 | +3% |
| 10 | 733 | 82% | 133 (18%) | 37% of 187 | +7% |
| 11 | 528 | 87% | 67 (13%) | 57% of 428 | +12% |
| 12 | 870 | 77% | 200 (23%) | 40% of 86 | +2% |
| 13 | 585 | 73% | 159 (27%) | 75% of 371 | -2% |
| 14 | 392 | 77% | 89 (23%) | 71% of 564 | +2% |
| 15 | 458 | 71% | 134 (29%) | 76% of 498 | -4% |
| 16 | 84 | 76% | 20 (24%) | 73% of 872 | +1% |
| 18 | 667 | 81% | 127 (19%) | 57% of 289 | +6% |
| 19 | 345 | 77% | 79 (23%) | 71% of 530 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 74% vs base 75%, n=865)
- check #3: lower weight: flagged coins die no more often than average (precision 66% vs base 75%, n=311)
- check #4: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 75%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 68% vs base 75%, n=394)
- check #8: lower weight: flagged coins die no more often than average (precision 65% vs base 75%, n=412)
- check #9: lower weight: flagged coins die no more often than average (precision 78% vs base 75%, n=705)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=870)
- check #13: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=585)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=392)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=458)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 75%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=345)
