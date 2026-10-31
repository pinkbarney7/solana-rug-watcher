# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 08:53 EDT. Labeled coins: 1062 (789 dead/pulled, 273 still alive). Base dead rate 74.3%. Forward 24h samples so far: 37.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 858 | 73% | 231 (27%) | 49% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 73% of 905 | -55% |
| 3 | 304 | 64% | 108 (36%) | 75% of 611 | -10% |
| 4 | 143 | 62% | 54 (38%) | 74% of 773 | -12% |
| 5 | 744 | 79% | 158 (21%) | 45% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 73% of 802 | -24% |
| 7 | 393 | 69% | 123 (31%) | 73% of 456 | -6% |
| 8 | 407 | 63% | 150 (37%) | 74% of 389 | -11% |
| 9 | 698 | 77% | 160 (23%) | 55% of 218 | +3% |
| 10 | 726 | 81% | 137 (19%) | 36% of 187 | +7% |
| 11 | 524 | 87% | 67 (13%) | 55% of 425 | +13% |
| 12 | 863 | 76% | 206 (24%) | 40% of 86 | +2% |
| 13 | 578 | 72% | 161 (28%) | 74% of 371 | -2% |
| 14 | 392 | 77% | 91 (23%) | 70% of 557 | +2% |
| 15 | 455 | 70% | 135 (30%) | 75% of 494 | -4% |
| 16 | 84 | 76% | 20 (24%) | 72% of 865 | +2% |
| 18 | 662 | 80% | 131 (20%) | 56% of 287 | +6% |
| 19 | 343 | 77% | 80 (23%) | 69% of 527 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 73% vs base 74%, n=858)
- check #3: lower weight: flagged coins die no more often than average (precision 64% vs base 74%, n=304)
- check #4: lower weight: flagged coins die no more often than average (precision 62% vs base 74%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 74%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 74%, n=393)
- check #8: lower weight: flagged coins die no more often than average (precision 63% vs base 74%, n=407)
- check #9: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=698)
- check #12: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=863)
- check #13: lower weight: flagged coins die no more often than average (precision 72% vs base 74%, n=578)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=392)
- check #15: lower weight: flagged coins die no more often than average (precision 70% vs base 74%, n=455)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=343)
