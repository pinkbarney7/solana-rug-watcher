# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 08:03 EST. Labeled coins: 1225 (1057 dead/pulled, 168 still alive). Base dead rate 86.3%. Forward 24h samples so far: 127.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1013 | 86% | 137 (14%) | 65% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 87% of 1063 | -68% |
| 3 | 387 | 88% | 46 (12%) | 84% of 692 | +2% |
| 4 | 153 | 92% | 12 (8%) | 84% of 927 | +6% |
| 5 | 859 | 91% | 76 (9%) | 64% of 232 | +5% |
| 6 | 100 | 56% | 44 (44%) | 88% of 915 | -30% |
| 7 | 468 | 76% | 111 (24%) | 93% of 521 | -10% |
| 8 | 500 | 83% | 87 (17%) | 84% of 456 | -4% |
| 9 | 802 | 90% | 84 (10%) | 73% of 278 | +3% |
| 10 | 818 | 92% | 63 (8%) | 63% of 259 | +6% |
| 11 | 641 | 88% | 77 (12%) | 83% of 472 | +2% |
| 12 | 1011 | 89% | 107 (11%) | 49% of 102 | +3% |
| 13 | 710 | 86% | 96 (14%) | 84% of 403 | +0% |
| 14 | 500 | 85% | 75 (15%) | 86% of 613 | -1% |
| 15 | 581 | 78% | 125 (22%) | 94% of 532 | -8% |
| 16 | 95 | 81% | 18 (19%) | 86% of 1018 | -5% |
| 18 | 791 | 90% | 83 (10%) | 76% of 322 | +3% |
| 19 | 370 | 87% | 48 (13%) | 88% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=1013)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=387)
- check #6: lower weight: flagged coins die no more often than average (precision 56% vs base 86%, n=100)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 86%, n=468)
- check #8: lower weight: flagged coins die no more often than average (precision 83% vs base 86%, n=500)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 86%, n=641)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 86%, n=710)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 86%, n=500)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 86%, n=581)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 86%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 87% vs base 86%, n=370)
