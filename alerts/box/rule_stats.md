# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 18:48 EST. Labeled coins: 1169 (952 dead/pulled, 217 still alive). Base dead rate 81.4%. Forward 24h samples so far: 83.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 960 | 81% | 179 (19%) | 60% of 57 | -0% |
| 2 | 25 | 20% | 20 (80%) | 82% of 1009 | -61% |
| 3 | 357 | 83% | 60 (17%) | 79% of 666 | +2% |
| 4 | 152 | 78% | 33 (22%) | 81% of 872 | -3% |
| 5 | 819 | 87% | 107 (13%) | 56% of 216 | +5% |
| 6 | 87 | 51% | 43 (49%) | 83% of 872 | -31% |
| 7 | 438 | 72% | 123 (28%) | 87% of 495 | -10% |
| 8 | 461 | 76% | 112 (24%) | 80% of 440 | -6% |
| 9 | 767 | 86% | 111 (14%) | 64% of 257 | +4% |
| 10 | 798 | 89% | 85 (11%) | 48% of 223 | +8% |
| 11 | 585 | 89% | 65 (11%) | 71% of 472 | +7% |
| 12 | 955 | 85% | 145 (15%) | 43% of 102 | +3% |
| 13 | 654 | 81% | 123 (19%) | 80% of 403 | -0% |
| 14 | 444 | 79% | 95 (21%) | 82% of 613 | -3% |
| 15 | 525 | 74% | 138 (26%) | 88% of 532 | -8% |
| 16 | 91 | 78% | 20 (22%) | 81% of 966 | -3% |
| 18 | 735 | 87% | 99 (13%) | 68% of 322 | +5% |
| 19 | 370 | 82% | 67 (18%) | 80% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=960)
- check #3: lower weight: flagged coins die no more often than average (precision 83% vs base 81%, n=357)
- check #4: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 81%, n=87)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 81%, n=438)
- check #8: lower weight: flagged coins die no more often than average (precision 76% vs base 81%, n=461)
- check #13: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=654)
- check #14: lower weight: flagged coins die no more often than average (precision 79% vs base 81%, n=444)
- check #15: lower weight: flagged coins die no more often than average (precision 74% vs base 81%, n=525)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=91)
- check #19: lower weight: flagged coins die no more often than average (precision 82% vs base 81%, n=370)
