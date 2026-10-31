# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-31 08:10 EDT. Labeled coins: 1055 (787 dead/pulled, 268 still alive). Base dead rate 74.6%. Forward 24h samples so far: 31.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 853 | 73% | 228 (27%) | 51% of 49 | -1% |
| 2 | 21 | 19% | 17 (81%) | 74% of 898 | -56% |
| 3 | 303 | 65% | 107 (35%) | 76% of 605 | -10% |
| 4 | 138 | 64% | 50 (36%) | 74% of 771 | -11% |
| 5 | 742 | 79% | 157 (21%) | 46% of 178 | +4% |
| 6 | 72 | 51% | 35 (49%) | 73% of 797 | -23% |
| 7 | 389 | 69% | 119 (31%) | 74% of 454 | -5% |
| 8 | 405 | 63% | 149 (37%) | 74% of 384 | -11% |
| 9 | 696 | 77% | 159 (23%) | 56% of 213 | +3% |
| 10 | 724 | 81% | 136 (19%) | 36% of 182 | +7% |
| 11 | 523 | 87% | 66 (13%) | 55% of 419 | +13% |
| 12 | 857 | 76% | 202 (24%) | 40% of 85 | +2% |
| 13 | 575 | 72% | 159 (28%) | 74% of 367 | -2% |
| 14 | 389 | 77% | 90 (23%) | 71% of 553 | +2% |
| 15 | 448 | 71% | 130 (29%) | 75% of 494 | -4% |
| 16 | 84 | 76% | 20 (24%) | 73% of 858 | +2% |
| 18 | 655 | 81% | 126 (19%) | 56% of 287 | +6% |
| 19 | 341 | 77% | 78 (23%) | 70% of 523 | +3% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=853)
- check #3: lower weight: flagged coins die no more often than average (precision 65% vs base 75%, n=303)
- check #4: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=138)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 75%, n=72)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 75%, n=389)
- check #8: lower weight: flagged coins die no more often than average (precision 63% vs base 75%, n=405)
- check #9: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=696)
- check #12: lower weight: flagged coins die no more often than average (precision 76% vs base 75%, n=857)
- check #13: lower weight: flagged coins die no more often than average (precision 72% vs base 75%, n=575)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=389)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=448)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 75%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=341)
