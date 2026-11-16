# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 15:27 EST. Labeled coins: 1169 (963 dead/pulled, 206 still alive). Base dead rate 82.4%. Forward 24h samples so far: 83.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 960 | 82% | 169 (18%) | 60% of 57 | +0% |
| 2 | 25 | 20% | 20 (80%) | 83% of 1009 | -62% |
| 3 | 357 | 84% | 56 (16%) | 79% of 666 | +2% |
| 4 | 152 | 81% | 29 (19%) | 81% of 872 | -1% |
| 5 | 819 | 88% | 101 (12%) | 57% of 216 | +5% |
| 6 | 87 | 52% | 42 (48%) | 84% of 872 | -31% |
| 7 | 438 | 73% | 120 (27%) | 89% of 495 | -10% |
| 8 | 461 | 77% | 107 (23%) | 81% of 440 | -6% |
| 9 | 767 | 86% | 105 (14%) | 66% of 257 | +4% |
| 10 | 798 | 90% | 82 (10%) | 51% of 223 | +7% |
| 11 | 585 | 90% | 61 (10%) | 72% of 472 | +7% |
| 12 | 955 | 86% | 135 (14%) | 43% of 102 | +3% |
| 13 | 654 | 83% | 114 (17%) | 80% of 403 | +0% |
| 14 | 444 | 80% | 88 (20%) | 83% of 613 | -2% |
| 15 | 525 | 75% | 130 (25%) | 88% of 532 | -7% |
| 16 | 91 | 80% | 18 (20%) | 82% of 966 | -2% |
| 18 | 735 | 87% | 92 (13%) | 69% of 322 | +5% |
| 19 | 370 | 82% | 66 (18%) | 81% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 82% vs base 82%, n=960)
- check #3: lower weight: flagged coins die no more often than average (precision 84% vs base 82%, n=357)
- check #4: lower weight: flagged coins die no more often than average (precision 81% vs base 82%, n=152)
- check #6: lower weight: flagged coins die no more often than average (precision 52% vs base 82%, n=87)
- check #7: lower weight: flagged coins die no more often than average (precision 73% vs base 82%, n=438)
- check #8: lower weight: flagged coins die no more often than average (precision 77% vs base 82%, n=461)
- check #13: lower weight: flagged coins die no more often than average (precision 83% vs base 82%, n=654)
- check #14: lower weight: flagged coins die no more often than average (precision 80% vs base 82%, n=444)
- check #15: lower weight: flagged coins die no more often than average (precision 75% vs base 82%, n=525)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 82%, n=91)
- check #19: lower weight: flagged coins die no more often than average (precision 82% vs base 82%, n=370)
