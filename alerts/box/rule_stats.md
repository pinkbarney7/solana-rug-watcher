# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 08:37 EST. Labeled coins: 1197 (1016 dead/pulled, 181 still alive). Base dead rate 84.9%. Forward 24h samples so far: 100.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 987 | 85% | 146 (15%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1036 | -66% |
| 3 | 372 | 87% | 48 (13%) | 82% of 679 | +2% |
| 4 | 152 | 89% | 17 (11%) | 83% of 900 | +4% |
| 5 | 835 | 90% | 80 (10%) | 61% of 228 | +6% |
| 6 | 91 | 54% | 42 (46%) | 87% of 896 | -31% |
| 7 | 454 | 75% | 113 (25%) | 92% of 507 | -10% |
| 8 | 481 | 81% | 91 (19%) | 83% of 447 | -4% |
| 9 | 782 | 89% | 87 (11%) | 70% of 270 | +4% |
| 10 | 806 | 92% | 67 (8%) | 59% of 243 | +7% |
| 11 | 613 | 89% | 68 (11%) | 79% of 472 | +4% |
| 12 | 983 | 89% | 112 (11%) | 45% of 102 | +4% |
| 13 | 682 | 86% | 98 (14%) | 83% of 403 | +1% |
| 14 | 472 | 84% | 77 (16%) | 85% of 613 | -1% |
| 15 | 553 | 77% | 125 (23%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 992 | -4% |
| 18 | 763 | 89% | 81 (11%) | 73% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 86% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=987)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=372)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 85%, n=91)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=454)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=481)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=682)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=472)
- check #15: lower weight: flagged coins die no more often than average (precision 77% vs base 85%, n=553)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
