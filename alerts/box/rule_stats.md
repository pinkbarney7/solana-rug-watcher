# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 20:15 EST. Labeled coins: 1128 (878 dead/pulled, 250 still alive). Base dead rate 77.8%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 920 | 77% | 211 (23%) | 57% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 78% of 969 | -61% |
| 3 | 339 | 74% | 88 (26%) | 77% of 643 | -4% |
| 4 | 150 | 71% | 43 (29%) | 77% of 833 | -7% |
| 5 | 793 | 83% | 138 (17%) | 51% of 201 | +5% |
| 6 | 79 | 51% | 39 (49%) | 79% of 839 | -27% |
| 7 | 418 | 71% | 123 (29%) | 82% of 474 | -7% |
| 8 | 440 | 70% | 133 (30%) | 76% of 420 | -8% |
| 9 | 744 | 81% | 140 (19%) | 60% of 239 | +3% |
| 10 | 776 | 85% | 114 (15%) | 41% of 204 | +7% |
| 11 | 555 | 89% | 62 (11%) | 62% of 461 | +11% |
| 12 | 919 | 81% | 177 (19%) | 39% of 97 | +3% |
| 13 | 622 | 77% | 145 (23%) | 77% of 394 | -1% |
| 14 | 414 | 78% | 90 (22%) | 76% of 602 | +0% |
| 15 | 495 | 72% | 138 (28%) | 81% of 521 | -6% |
| 16 | 88 | 78% | 19 (22%) | 77% of 928 | +1% |
| 18 | 706 | 85% | 109 (15%) | 59% of 310 | +7% |
| 19 | 368 | 79% | 78 (21%) | 74% of 561 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=920)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=339)
- check #4: lower weight: flagged coins die no more often than average (precision 71% vs base 78%, n=150)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 78%, n=79)
- check #7: lower weight: flagged coins die no more often than average (precision 71% vs base 78%, n=418)
- check #8: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=440)
- check #12: lower weight: flagged coins die no more often than average (precision 81% vs base 78%, n=919)
- check #13: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=622)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=414)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=495)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 78%, n=368)
