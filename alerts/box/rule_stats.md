# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 10:33 EST. Labeled coins: 1232 (1068 dead/pulled, 164 still alive). Base dead rate 86.7%. Forward 24h samples so far: 135.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 1020 | 87% | 134 (13%) | 67% of 60 | +0% |
| 2 | 27 | 19% | 22 (81%) | 88% of 1070 | -68% |
| 3 | 390 | 88% | 46 (12%) | 84% of 696 | +2% |
| 4 | 153 | 95% | 8 (5%) | 84% of 934 | +8% |
| 5 | 865 | 91% | 74 (9%) | 65% of 233 | +5% |
| 6 | 100 | 58% | 42 (42%) | 88% of 920 | -29% |
| 7 | 471 | 77% | 110 (23%) | 94% of 523 | -10% |
| 8 | 507 | 83% | 86 (17%) | 85% of 456 | -4% |
| 9 | 806 | 90% | 83 (10%) | 74% of 281 | +3% |
| 10 | 822 | 92% | 62 (8%) | 65% of 262 | +6% |
| 11 | 648 | 88% | 77 (12%) | 83% of 472 | +1% |
| 12 | 1018 | 90% | 104 (10%) | 50% of 102 | +3% |
| 13 | 717 | 87% | 93 (13%) | 85% of 403 | +0% |
| 14 | 507 | 85% | 74 (15%) | 87% of 613 | -1% |
| 15 | 588 | 79% | 121 (21%) | 94% of 532 | -7% |
| 16 | 95 | 81% | 18 (19%) | 87% of 1025 | -6% |
| 18 | 798 | 90% | 81 (10%) | 77% of 322 | +3% |
| 19 | 370 | 88% | 45 (12%) | 88% of 574 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 87% vs base 87%, n=1020)
- check #3: lower weight: flagged coins die no more often than average (precision 88% vs base 87%, n=390)
- check #6: lower weight: flagged coins die no more often than average (precision 58% vs base 87%, n=100)
- check #7: lower weight: flagged coins die no more often than average (precision 77% vs base 87%, n=471)
- check #8: lower weight: flagged coins die no more often than average (precision 83% vs base 87%, n=507)
- check #11: lower weight: flagged coins die no more often than average (precision 88% vs base 87%, n=648)
- check #13: lower weight: flagged coins die no more often than average (precision 87% vs base 87%, n=717)
- check #14: lower weight: flagged coins die no more often than average (precision 85% vs base 87%, n=507)
- check #15: lower weight: flagged coins die no more often than average (precision 79% vs base 87%, n=588)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 87%, n=95)
- check #19: lower weight: flagged coins die no more often than average (precision 88% vs base 87%, n=370)
