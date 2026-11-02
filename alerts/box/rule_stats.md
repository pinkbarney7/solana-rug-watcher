# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 14:53 EST. Labeled coins: 1103 (852 dead/pulled, 251 still alive). Base dead rate 77.2%. Forward 24h samples so far: 46.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 898 | 76% | 214 (24%) | 58% of 53 | -1% |
| 2 | 23 | 17% | 19 (83%) | 77% of 945 | -60% |
| 3 | 327 | 73% | 89 (27%) | 77% of 630 | -4% |
| 4 | 148 | 69% | 46 (31%) | 76% of 810 | -8% |
| 5 | 775 | 82% | 140 (18%) | 50% of 194 | +5% |
| 6 | 76 | 50% | 38 (50%) | 78% of 818 | -27% |
| 7 | 403 | 70% | 119 (30%) | 80% of 465 | -7% |
| 8 | 429 | 69% | 135 (31%) | 76% of 407 | -9% |
| 9 | 729 | 80% | 144 (20%) | 59% of 229 | +3% |
| 10 | 758 | 85% | 115 (15%) | 39% of 197 | +8% |
| 11 | 542 | 89% | 60 (11%) | 61% of 449 | +12% |
| 12 | 899 | 80% | 182 (20%) | 40% of 92 | +3% |
| 13 | 608 | 76% | 146 (24%) | 76% of 383 | -1% |
| 14 | 402 | 78% | 89 (22%) | 75% of 589 | +1% |
| 15 | 480 | 72% | 134 (28%) | 80% of 511 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 903 | +0% |
| 18 | 686 | 84% | 108 (16%) | 58% of 305 | +7% |
| 19 | 356 | 79% | 76 (21%) | 73% of 550 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=898)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=327)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 77%, n=76)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=403)
- check #8: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=429)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=899)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=608)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=402)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=480)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=356)
