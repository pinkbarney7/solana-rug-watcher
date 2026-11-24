# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 12:50 EST. Labeled coins: 1200 (1019 dead/pulled, 181 still alive). Base dead rate 84.9%. Forward 24h samples so far: 102.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 990 | 85% | 146 (15%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1039 | -66% |
| 3 | 372 | 87% | 47 (13%) | 82% of 682 | +2% |
| 4 | 152 | 89% | 17 (11%) | 83% of 903 | +4% |
| 5 | 838 | 90% | 80 (10%) | 61% of 228 | +6% |
| 6 | 91 | 54% | 42 (46%) | 87% of 899 | -31% |
| 7 | 456 | 75% | 113 (25%) | 92% of 508 | -10% |
| 8 | 484 | 81% | 91 (19%) | 83% of 447 | -4% |
| 9 | 784 | 89% | 87 (11%) | 70% of 271 | +4% |
| 10 | 809 | 92% | 68 (8%) | 59% of 243 | +7% |
| 11 | 616 | 89% | 68 (11%) | 79% of 472 | +4% |
| 12 | 986 | 89% | 112 (11%) | 45% of 102 | +4% |
| 13 | 685 | 86% | 98 (14%) | 83% of 403 | +1% |
| 14 | 475 | 84% | 77 (16%) | 85% of 613 | -1% |
| 15 | 556 | 78% | 125 (22%) | 92% of 532 | -7% |
| 16 | 94 | 80% | 19 (20%) | 85% of 994 | -5% |
| 18 | 766 | 89% | 81 (11%) | 73% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 86% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=990)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=372)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 85%, n=91)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=456)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=484)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=685)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=475)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=556)
- check #16: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=94)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
