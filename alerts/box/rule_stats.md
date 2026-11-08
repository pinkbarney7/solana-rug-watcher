# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-08 18:11 EST. Labeled coins: 1128 (900 dead/pulled, 228 still alive). Base dead rate 79.8%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 920 | 79% | 190 (21%) | 59% of 56 | -0% |
| 2 | 24 | 17% | 20 (83%) | 80% of 969 | -63% |
| 3 | 339 | 80% | 69 (20%) | 77% of 643 | -0% |
| 4 | 150 | 73% | 40 (27%) | 79% of 833 | -6% |
| 5 | 793 | 85% | 120 (15%) | 53% of 201 | +5% |
| 6 | 79 | 52% | 38 (48%) | 81% of 839 | -28% |
| 7 | 418 | 72% | 117 (28%) | 85% of 474 | -8% |
| 8 | 440 | 72% | 123 (28%) | 79% of 420 | -8% |
| 9 | 744 | 83% | 123 (17%) | 62% of 239 | +4% |
| 10 | 776 | 88% | 97 (12%) | 43% of 204 | +8% |
| 11 | 555 | 90% | 54 (10%) | 65% of 461 | +10% |
| 12 | 919 | 83% | 157 (17%) | 41% of 97 | +3% |
| 13 | 622 | 80% | 127 (20%) | 78% of 394 | -0% |
| 14 | 414 | 79% | 85 (21%) | 79% of 602 | -0% |
| 15 | 495 | 73% | 132 (27%) | 84% of 521 | -6% |
| 16 | 88 | 78% | 19 (22%) | 79% of 928 | -1% |
| 18 | 706 | 86% | 97 (14%) | 62% of 310 | +6% |
| 19 | 368 | 79% | 76 (21%) | 77% of 561 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 79% vs base 80%, n=920)
- check #3: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=339)
- check #4: lower weight: flagged coins die no more often than average (precision 73% vs base 80%, n=150)
- check #6: lower weight: flagged coins die no more often than average (precision 52% vs base 80%, n=79)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 80%, n=418)
- check #8: lower weight: flagged coins die no more often than average (precision 72% vs base 80%, n=440)
- check #13: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=622)
- check #14: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=414)
- check #15: lower weight: flagged coins die no more often than average (precision 73% vs base 80%, n=495)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 80%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 80%, n=368)
