# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 22:52 EST. Labeled coins: 1110 (858 dead/pulled, 252 still alive). Base dead rate 77.3%. Forward 24h samples so far: 56.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 902 | 76% | 212 (24%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 951 | -61% |
| 3 | 331 | 73% | 88 (27%) | 76% of 633 | -4% |
| 4 | 148 | 69% | 46 (31%) | 76% of 817 | -8% |
| 5 | 779 | 82% | 139 (18%) | 50% of 197 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 822 | -29% |
| 7 | 408 | 70% | 122 (30%) | 81% of 466 | -7% |
| 8 | 432 | 69% | 133 (31%) | 75% of 411 | -8% |
| 9 | 732 | 80% | 143 (20%) | 59% of 233 | +3% |
| 10 | 763 | 85% | 114 (15%) | 38% of 199 | +8% |
| 11 | 546 | 89% | 62 (11%) | 61% of 452 | +11% |
| 12 | 904 | 80% | 181 (20%) | 39% of 94 | +3% |
| 13 | 613 | 76% | 145 (24%) | 76% of 385 | -1% |
| 14 | 403 | 78% | 90 (22%) | 75% of 595 | +0% |
| 15 | 483 | 72% | 136 (28%) | 80% of 515 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 910 | -0% |
| 18 | 691 | 84% | 108 (16%) | 58% of 307 | +7% |
| 19 | 357 | 78% | 77 (22%) | 73% of 555 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=902)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=331)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 77%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=408)
- check #8: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=432)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=904)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=613)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=403)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=483)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=357)
