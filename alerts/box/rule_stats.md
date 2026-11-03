# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 18:59 EST. Labeled coins: 1106 (857 dead/pulled, 249 still alive). Base dead rate 77.5%. Forward 24h samples so far: 49.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 900 | 77% | 211 (23%) | 57% of 54 | -1% |
| 2 | 23 | 17% | 19 (83%) | 77% of 948 | -60% |
| 3 | 329 | 74% | 86 (26%) | 76% of 631 | -4% |
| 4 | 148 | 69% | 46 (31%) | 77% of 813 | -9% |
| 5 | 777 | 82% | 138 (18%) | 50% of 195 | +5% |
| 6 | 76 | 50% | 38 (50%) | 78% of 820 | -27% |
| 7 | 405 | 70% | 120 (30%) | 81% of 465 | -7% |
| 8 | 431 | 69% | 133 (31%) | 76% of 408 | -8% |
| 9 | 731 | 81% | 142 (19%) | 60% of 230 | +3% |
| 10 | 760 | 85% | 112 (15%) | 38% of 198 | +8% |
| 11 | 545 | 89% | 61 (11%) | 61% of 449 | +11% |
| 12 | 901 | 80% | 179 (20%) | 40% of 93 | +3% |
| 13 | 610 | 77% | 143 (23%) | 76% of 384 | -1% |
| 14 | 403 | 78% | 90 (22%) | 75% of 591 | +0% |
| 15 | 481 | 72% | 134 (28%) | 80% of 513 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 906 | -0% |
| 18 | 688 | 85% | 106 (15%) | 58% of 306 | +7% |
| 19 | 356 | 79% | 76 (21%) | 73% of 552 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=900)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=329)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 78%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 78%, n=76)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=405)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 78%, n=431)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 78%, n=901)
- check #13: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=610)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=403)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=481)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 78%, n=356)
