# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 19:34 EST. Labeled coins: 1228 (1062 dead/pulled, 166 still alive). Base dead rate 86.5%. Forward 24h samples so far: 131.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1016 | 87% | 135 (13%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1066 | -68% |
| 3 | 389 | 88% | 47 (12%) | 84% of 693 | +1% |
| 4 | 153 | 93% | 10 (7%) | 84% of 930 | +7% |
| 5 | 862 | 91% | 76 (9%) | 65% of 232 | +5% |
| 6 | 100 | 56% | 44 (44%) | 88% of 918 | -30% |
| 7 | 469 | 77% | 109 (23%) | 93% of 523 | -10% |
| 8 | 503 | 83% | 87 (17%) | 85% of 456 | -4% |
| 9 | 804 | 90% | 84 (10%) | 74% of 279 | +3% |
| 10 | 819 | 92% | 62 (8%) | 64% of 261 | +6% |
| 11 | 644 | 88% | 78 (12%) | 83% of 472 | +1% |
| 12 | 1014 | 90% | 106 (10%) | 50% of 102 | +3% |
| 13 | 713 | 87% | 94 (13%) | 84% of 403 | +0% |
| 14 | 503 | 85% | 75 (15%) | 87% of 613 | -1% |
| 15 | 584 | 79% | 123 (21%) | 94% of 532 | -8% |
| 16 | 95 | 81% | 18 (19%) | 86% of 1021 | -5% |
| 18 | 794 | 90% | 82 (10%) | 77% of 322 | +3% |
| 19 | 370 | 88% | 46 (12%) | 88% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=1016)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=389)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=100)
- check #7: lower weight: flagged coins die no more often than average (precision 77% vs base 86%, n=469)
- check #8: lower weight: flagged coins die no more often than average (precision 83% vs base 86%, n=503)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=644)
- check #13: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=713)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=503)
- check #15: lower weight: flagged coins die no more often than average (precision 79% vs base 86%, n=584)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=370)
