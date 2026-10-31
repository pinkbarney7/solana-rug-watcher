# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-30 19:56 EDT. Labeled coins: 1029 (769 dead/pulled, 260 still alive). Base dead rate 74.7%. Forward 24h samples so far: 2.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 828 | 73% | 221 (27%) | 52% of 48 | -1% |
| 2 | 20 | 20% | 16 (80%) | 74% of 873 | -55% |
| 3 | 282 | 65% | 99 (35%) | 76% of 600 | -10% |
| 4 | 138 | 62% | 52 (38%) | 74% of 745 | -12% |
| 5 | 717 | 79% | 149 (21%) | 46% of 177 | +4% |
| 6 | 70 | 50% | 35 (50%) | 73% of 777 | -25% |
| 7 | 387 | 69% | 121 (31%) | 75% of 434 | -6% |
| 8 | 387 | 64% | 140 (36%) | 74% of 378 | -11% |
| 9 | 671 | 78% | 149 (22%) | 55% of 212 | +3% |
| 10 | 700 | 82% | 128 (18%) | 36% of 180 | +7% |
| 11 | 509 | 87% | 64 (13%) | 56% of 407 | +13% |
| 12 | 833 | 77% | 195 (23%) | 40% of 83 | +2% |
| 13 | 552 | 73% | 148 (27%) | 73% of 364 | -2% |
| 14 | 384 | 76% | 91 (24%) | 71% of 532 | +2% |
| 15 | 438 | 71% | 128 (29%) | 76% of 478 | -4% |
| 16 | 84 | 75% | 21 (25%) | 73% of 832 | +0% |
| 18 | 640 | 81% | 122 (19%) | 55% of 276 | +6% |
| 19 | 335 | 77% | 76 (23%) | 70% of 507 | +3% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=828)
- check #3: lower weight: flagged coins die no more often than average (precision 65% vs base 75%, n=282)
- check #4: lower weight: flagged coins die no more often than average (precision 62% vs base 75%, n=138)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 75%, n=70)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 75%, n=387)
- check #8: lower weight: flagged coins die no more often than average (precision 64% vs base 75%, n=387)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=833)
- check #13: lower weight: flagged coins die no more often than average (precision 73% vs base 75%, n=552)
- check #14: lower weight: flagged coins die no more often than average (precision 76% vs base 75%, n=384)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 75%, n=438)
- check #16: lower weight: flagged coins die no more often than average (precision 75% vs base 75%, n=84)
- check #19: lower weight: flagged coins die no more often than average (precision 77% vs base 75%, n=335)
