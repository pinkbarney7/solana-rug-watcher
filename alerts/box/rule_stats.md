# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 09:23 EST. Labeled coins: 1102 (847 dead/pulled, 255 still alive). Base dead rate 76.9%. Forward 24h samples so far: 46.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 897 | 76% | 217 (24%) | 57% of 53 | -1% |
| 2 | 23 | 17% | 19 (83%) | 76% of 944 | -59% |
| 3 | 326 | 72% | 92 (28%) | 76% of 630 | -5% |
| 4 | 148 | 68% | 47 (32%) | 76% of 809 | -9% |
| 5 | 774 | 82% | 143 (18%) | 49% of 194 | +5% |
| 6 | 76 | 50% | 38 (50%) | 77% of 817 | -27% |
| 7 | 403 | 70% | 119 (30%) | 80% of 464 | -6% |
| 8 | 429 | 68% | 138 (32%) | 76% of 406 | -9% |
| 9 | 728 | 80% | 147 (20%) | 59% of 229 | +3% |
| 10 | 757 | 84% | 118 (16%) | 38% of 197 | +8% |
| 11 | 542 | 89% | 61 (11%) | 60% of 448 | +12% |
| 12 | 898 | 79% | 186 (21%) | 40% of 92 | +2% |
| 13 | 607 | 75% | 150 (25%) | 76% of 383 | -2% |
| 14 | 402 | 78% | 90 (22%) | 74% of 588 | +1% |
| 15 | 480 | 72% | 136 (28%) | 79% of 510 | -5% |
| 16 | 88 | 76% | 21 (24%) | 76% of 902 | -1% |
| 18 | 685 | 84% | 112 (16%) | 58% of 305 | +7% |
| 19 | 356 | 79% | 76 (21%) | 72% of 549 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=897)
- check #3: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=326)
- check #4: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 77%, n=76)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=403)
- check #8: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=429)
- check #9: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=728)
- check #12: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=898)
- check #13: lower weight: flagged coins die no more often than average (precision 75% vs base 77%, n=607)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=402)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=480)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=356)
