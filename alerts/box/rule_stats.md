# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 09:26 EST. Labeled coins: 1228 (1059 dead/pulled, 169 still alive). Base dead rate 86.2%. Forward 24h samples so far: 129.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1016 | 86% | 138 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1066 | -68% |
| 3 | 389 | 88% | 48 (12%) | 84% of 693 | +1% |
| 4 | 153 | 93% | 11 (7%) | 84% of 930 | +7% |
| 5 | 862 | 91% | 78 (9%) | 65% of 232 | +5% |
| 6 | 100 | 56% | 44 (44%) | 88% of 918 | -30% |
| 7 | 469 | 77% | 110 (23%) | 93% of 523 | -10% |
| 8 | 503 | 82% | 89 (18%) | 85% of 456 | -4% |
| 9 | 804 | 89% | 86 (11%) | 73% of 279 | +3% |
| 10 | 819 | 92% | 63 (8%) | 63% of 261 | +6% |
| 11 | 644 | 88% | 79 (12%) | 83% of 472 | +1% |
| 12 | 1014 | 89% | 108 (11%) | 49% of 102 | +3% |
| 13 | 713 | 86% | 97 (14%) | 84% of 403 | +0% |
| 14 | 503 | 85% | 77 (15%) | 86% of 613 | -2% |
| 15 | 584 | 78% | 126 (22%) | 94% of 532 | -8% |
| 16 | 95 | 81% | 18 (19%) | 86% of 1021 | -5% |
| 18 | 794 | 89% | 84 (11%) | 76% of 322 | +3% |
| 19 | 370 | 87% | 47 (13%) | 88% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1016)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=389)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=100)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=469)
- check #8: lower weight: flagged coins die no more often than average (precision 82% vs base 86%, n=503)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=644)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=713)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=503)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=584)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=370)
