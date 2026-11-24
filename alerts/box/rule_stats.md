# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 11:02 EST. Labeled coins: 1199 (1019 dead/pulled, 180 still alive). Base dead rate 85.0%. Forward 24h samples so far: 101.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 989 | 85% | 145 (15%) | 64% of 58 | +0% |
| 2 | 26 | 19% | 21 (81%) | 86% of 1038 | -66% |
| 3 | 372 | 87% | 47 (13%) | 82% of 681 | +2% |
| 4 | 152 | 89% | 17 (11%) | 83% of 902 | +4% |
| 5 | 837 | 91% | 79 (9%) | 61% of 228 | +6% |
| 6 | 91 | 54% | 42 (46%) | 87% of 898 | -31% |
| 7 | 456 | 75% | 113 (25%) | 92% of 507 | -10% |
| 8 | 483 | 81% | 90 (19%) | 83% of 447 | -4% |
| 9 | 783 | 89% | 86 (11%) | 70% of 271 | +4% |
| 10 | 808 | 92% | 67 (8%) | 59% of 243 | +7% |
| 11 | 615 | 89% | 67 (11%) | 79% of 472 | +4% |
| 12 | 985 | 89% | 111 (11%) | 45% of 102 | +4% |
| 13 | 684 | 86% | 97 (14%) | 83% of 403 | +1% |
| 14 | 474 | 84% | 76 (16%) | 85% of 613 | -1% |
| 15 | 555 | 78% | 124 (22%) | 92% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 994 | -4% |
| 18 | 765 | 90% | 80 (10%) | 73% of 322 | +5% |
| 19 | 370 | 85% | 55 (15%) | 86% of 574 | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=989)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=372)
- check #6: lower weight: flagged coins die no more often than average (precision 54% vs base 85%, n=91)
- check #7: lower weight: flagged coins die no more often than average (precision 75% vs base 85%, n=456)
- check #8: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=483)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=684)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=474)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=555)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
