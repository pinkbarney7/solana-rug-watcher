# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-09 19:00 EST. Labeled coins: 1140 (927 dead/pulled, 213 still alive). Base dead rate 81.3%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 931 | 81% | 175 (19%) | 60% of 57 | -0% |
| 2 | 24 | 21% | 19 (79%) | 82% of 981 | -60% |
| 3 | 342 | 83% | 59 (17%) | 79% of 652 | +1% |
| 4 | 151 | 76% | 36 (24%) | 81% of 844 | -5% |
| 5 | 802 | 87% | 106 (13%) | 54% of 204 | +5% |
| 6 | 80 | 54% | 37 (46%) | 82% of 850 | -28% |
| 7 | 423 | 72% | 117 (28%) | 87% of 481 | -9% |
| 8 | 447 | 74% | 115 (26%) | 80% of 425 | -7% |
| 9 | 750 | 85% | 110 (15%) | 64% of 245 | +4% |
| 10 | 782 | 89% | 84 (11%) | 46% of 210 | +8% |
| 11 | 558 | 91% | 50 (9%) | 68% of 470 | +10% |
| 12 | 928 | 85% | 142 (15%) | 43% of 100 | +3% |
| 13 | 628 | 82% | 116 (18%) | 79% of 400 | +0% |
| 14 | 418 | 81% | 80 (19%) | 80% of 610 | -0% |
| 15 | 500 | 75% | 125 (25%) | 86% of 528 | -6% |
| 16 | 88 | 78% | 19 (22%) | 81% of 940 | -3% |
| 18 | 708 | 87% | 89 (13%) | 66% of 320 | +6% |
| 19 | 369 | 80% | 72 (20%) | 78% of 571 | -1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=931)
- check #3: lower weight: flagged coins die no more often than average (precision 83% vs base 81%, n=342)
- check #4: lower weight: flagged coins die no more often than average (precision 76% vs base 81%, n=151)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 81%, n=80)
- check #7: lower weight: flagged coins die no more often than average (precision 72% vs base 81%, n=423)
- check #8: lower weight: flagged coins die no more often than average (precision 74% vs base 81%, n=447)
- check #13: lower weight: flagged coins die no more often than average (precision 82% vs base 81%, n=628)
- check #14: lower weight: flagged coins die no more often than average (precision 81% vs base 81%, n=418)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 81%, n=500)
- check #16: lower weight: flagged coins die no more often than average (precision 78% vs base 81%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 80% vs base 81%, n=369)
