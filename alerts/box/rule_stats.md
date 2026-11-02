# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-01 22:39 EST. Labeled coins: 1096 (837 dead/pulled, 259 still alive). Base dead rate 76.4%. Forward 24h samples so far: 45.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 890 | 75% | 220 (25%) | 55% of 53 | -1% |
| 2 | 23 | 17% | 19 (83%) | 76% of 937 | -59% |
| 3 | 323 | 71% | 95 (29%) | 76% of 626 | -6% |
| 4 | 147 | 67% | 48 (33%) | 75% of 803 | -9% |
| 5 | 769 | 81% | 146 (19%) | 48% of 192 | +5% |
| 6 | 74 | 50% | 37 (50%) | 77% of 812 | -26% |
| 7 | 399 | 70% | 120 (30%) | 79% of 461 | -6% |
| 8 | 426 | 67% | 140 (33%) | 75% of 402 | -9% |
| 9 | 722 | 79% | 149 (21%) | 58% of 228 | +3% |
| 10 | 752 | 84% | 122 (16%) | 37% of 195 | +7% |
| 11 | 538 | 88% | 63 (12%) | 59% of 445 | +12% |
| 12 | 891 | 79% | 189 (21%) | 39% of 92 | +2% |
| 13 | 604 | 75% | 154 (25%) | 76% of 379 | -2% |
| 14 | 400 | 77% | 91 (23%) | 74% of 583 | +1% |
| 15 | 477 | 71% | 136 (29%) | 78% of 506 | -5% |
| 16 | 87 | 77% | 20 (23%) | 75% of 896 | +1% |
| 18 | 682 | 83% | 116 (17%) | 57% of 301 | +7% |
| 19 | 354 | 79% | 76 (21%) | 72% of 544 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 75% vs base 76%, n=890)
- check #3: lower weight: flagged coins die no more often than average (precision 71% vs base 76%, n=323)
- check #4: lower weight: flagged coins die no more often than average (precision 67% vs base 76%, n=147)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 76%, n=74)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 76%, n=399)
- check #8: lower weight: flagged coins die no more often than average (precision 67% vs base 76%, n=426)
- check #9: lower weight: flagged coins die no more often than average (precision 79% vs base 76%, n=722)
- check #12: lower weight: flagged coins die no more often than average (precision 79% vs base 76%, n=891)
- check #13: lower weight: flagged coins die no more often than average (precision 74% vs base 76%, n=604)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 76%, n=400)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 76%, n=477)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 76%, n=87)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 76%, n=354)
