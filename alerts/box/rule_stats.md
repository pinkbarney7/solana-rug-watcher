# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 12:20 EST. Labeled coins: 1183 (1005 dead/pulled, 178 still alive). Base dead rate 85.0%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 973 | 85% | 143 (15%) | 64% of 58 | +0% |
| 2 | 25 | 20% | 20 (80%) | 86% of 1023 | -65% |
| 3 | 364 | 87% | 47 (13%) | 82% of 673 | +2% |
| 4 | 152 | 89% | 17 (11%) | 83% of 886 | +4% |
| 5 | 828 | 90% | 83 (10%) | 63% of 221 | +5% |
| 6 | 88 | 55% | 40 (45%) | 87% of 885 | -30% |
| 7 | 448 | 76% | 109 (24%) | 92% of 499 | -9% |
| 8 | 473 | 81% | 92 (19%) | 83% of 442 | -4% |
| 9 | 775 | 89% | 89 (11%) | 71% of 263 | +4% |
| 10 | 804 | 92% | 68 (8%) | 58% of 231 | +7% |
| 11 | 599 | 90% | 59 (10%) | 78% of 472 | +5% |
| 12 | 969 | 89% | 109 (11%) | 45% of 102 | +4% |
| 13 | 668 | 86% | 94 (14%) | 82% of 403 | +1% |
| 14 | 458 | 84% | 74 (16%) | 85% of 613 | -1% |
| 15 | 539 | 78% | 118 (22%) | 91% of 532 | -7% |
| 16 | 93 | 81% | 18 (19%) | 85% of 978 | -4% |
| 18 | 749 | 90% | 73 (10%) | 71% of 322 | +5% |
| 19 | 370 | 85% | 57 (15%) | 85% of 574 | -0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=973)
- check #3: lower weight: flagged coins die no more often than average (precision 87% vs base 85%, n=364)
- check #6: lower weight: flagged coins die no more often than average (precision 55% vs base 85%, n=88)
- check #7: lower weight: flagged coins die no more often than average (precision 76% vs base 85%, n=448)
- check #8: lower weight: flagged coins die no more often than average (precision 80% vs base 85%, n=473)
- check #13: lower weight: flagged coins die no more often than average (precision 86% vs base 85%, n=668)
- check #14: lower weight: flagged coins die no more often than average (precision 84% vs base 85%, n=458)
- check #15: lower weight: flagged coins die no more often than average (precision 78% vs base 85%, n=539)
- check #16: lower weight: flagged coins die no more often than average (precision 81% vs base 85%, n=93)
- check #19: lower weight: flagged coins die no more often than average (precision 85% vs base 85%, n=370)
