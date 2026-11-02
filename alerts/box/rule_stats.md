# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 08:35 EST. Labeled coins: 1101 (846 dead/pulled, 255 still alive). Base dead rate 76.8%. Forward 24h samples so far: 46.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 896 | 76% | 217 (24%) | 57% of 53 | -1% |
| 2 | 23 | 17% | 19 (83%) | 76% of 943 | -59% |
| 3 | 326 | 72% | 92 (28%) | 76% of 629 | -5% |
| 4 | 148 | 68% | 47 (32%) | 76% of 808 | -9% |
| 5 | 773 | 82% | 143 (18%) | 49% of 194 | +5% |
| 6 | 76 | 50% | 38 (50%) | 77% of 816 | -27% |
| 7 | 402 | 70% | 119 (30%) | 80% of 464 | -6% |
| 8 | 429 | 68% | 138 (32%) | 76% of 405 | -9% |
| 9 | 727 | 80% | 147 (20%) | 59% of 229 | +3% |
| 10 | 756 | 84% | 118 (16%) | 38% of 197 | +8% |
| 11 | 541 | 89% | 61 (11%) | 60% of 448 | +12% |
| 12 | 897 | 79% | 186 (21%) | 40% of 92 | +2% |
| 13 | 607 | 75% | 150 (25%) | 76% of 382 | -2% |
| 14 | 401 | 78% | 90 (22%) | 74% of 588 | +1% |
| 15 | 479 | 72% | 136 (28%) | 79% of 510 | -5% |
| 16 | 88 | 76% | 21 (24%) | 76% of 901 | -1% |
| 18 | 684 | 84% | 112 (16%) | 58% of 305 | +7% |
| 19 | 355 | 79% | 76 (21%) | 72% of 549 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=896)
- check #3: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=326)
- check #4: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 77%, n=76)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=402)
- check #8: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=429)
- check #9: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=727)
- check #12: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=897)
- check #13: lower weight: flagged coins die no more often than average (precision 75% vs base 77%, n=607)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=401)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=479)
- check #16: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=355)
