# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 08:30 EDT. Labeled coins: 1061 (789 dead/pulled, 272 still alive). Base dead rate 74.4%. Forward 24h samples so far: 36.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 857 | 73% | 230 (27%) | 49% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 73% of 904 | -55% |
| 3 | 303 | 65% | 107 (35%) | 75% of 611 | -10% |
| 4 | 143 | 62% | 54 (38%) | 74% of 772 | -12% |
| 5 | 743 | 79% | 157 (21%) | 45% of 183 | +5% |
| 6 | 73 | 51% | 36 (49%) | 73% of 801 | -24% |
| 7 | 392 | 69% | 122 (31%) | 73% of 456 | -5% |
| 8 | 407 | 63% | 150 (37%) | 74% of 388 | -11% |
| 9 | 697 | 77% | 159 (23%) | 55% of 218 | +3% |
| 10 | 725 | 81% | 136 (19%) | 36% of 187 | +7% |
| 11 | 524 | 87% | 67 (13%) | 55% of 424 | +13% |
| 12 | 862 | 76% | 205 (24%) | 40% of 86 | +2% |
| 13 | 577 | 72% | 160 (28%) | 74% of 371 | -2% |
| 14 | 392 | 77% | 91 (23%) | 70% of 556 | +2% |
| 15 | 454 | 70% | 134 (30%) | 75% of 494 | -4% |
| 16 | 84 | 76% | 20 (24%) | 73% of 864 | +2% |
| 18 | 661 | 80% | 130 (20%) | 56% of 287 | +6% |
| 19 | 343 | 77% | 80 (23%) | 69% of 526 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 73% vs base 74%, n=857)
- check #3: lower weight: flagged coins die no more often than average (precision 65% vs base 74%, n=303)
- check #4: lower weight: flagged coins die no more often than average (precision 62% vs base 74%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 74%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 74%, n=392)
- check #8: lower weight: flagged coins die no more often than average (precision 63% vs base 74%, n=407)
- check #9: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=697)
- check #12: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=862)
- check #13: lower weight: flagged coins die no more often than average (precision 72% vs base 74%, n=577)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=392)
- check #15: lower weight: flagged coins die no more often than average (precision 70% vs base 74%, n=454)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 74%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=343)
