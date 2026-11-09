# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-08 21:13 EST. Labeled coins: 1140 (909 dead/pulled, 231 still alive). Base dead rate 79.7%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 931 | 79% | 192 (21%) | 58% of 57 | -0% |
| 2 | 24 | 17% | 20 (83%) | 80% of 981 | -63% |
| 3 | 342 | 80% | 69 (20%) | 77% of 652 | +0% |
| 4 | 151 | 74% | 39 (26%) | 79% of 844 | -6% |
| 5 | 802 | 85% | 123 (15%) | 54% of 204 | +5% |
| 6 | 80 | 51% | 39 (49%) | 81% of 850 | -28% |
| 7 | 423 | 72% | 119 (28%) | 84% of 481 | -8% |
| 8 | 447 | 72% | 126 (28%) | 79% of 425 | -8% |
| 9 | 750 | 83% | 125 (17%) | 62% of 245 | +4% |
| 10 | 782 | 88% | 97 (12%) | 43% of 210 | +8% |
| 11 | 558 | 90% | 55 (10%) | 66% of 470 | +10% |
| 12 | 928 | 83% | 159 (17%) | 42% of 100 | +3% |
| 13 | 628 | 79% | 130 (21%) | 78% of 400 | -0% |
| 14 | 418 | 80% | 85 (20%) | 78% of 610 | -0% |
| 15 | 500 | 73% | 133 (27%) | 84% of 528 | -6% |
| 16 | 88 | 78% | 19 (22%) | 79% of 940 | -1% |
| 18 | 708 | 87% | 94 (13%) | 62% of 320 | +7% |
| 19 | 369 | 79% | 76 (21%) | 77% of 571 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 79% vs base 80%, n=931)
- check #3: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=342)
- check #4: lower weight: flagged coins die no more often than average (precision 74% vs base 80%, n=151)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 80%, n=80)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 80%, n=423)
- check #8: lower weight: flagged coins die no more often than average (precision 72% vs base 80%, n=447)
- check #13: lower weight: flagged coins die no more often than average (precision 79% vs base 80%, n=628)
- check #14: lower weight: flagged coins die no more often than average (precision 80% vs base 80%, n=418)
- check #15: lower weight: flagged coins die no more often than average (precision 73% vs base 80%, n=500)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 80%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 80%, n=369)
