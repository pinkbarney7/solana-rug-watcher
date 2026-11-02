# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-02 18:16 EST. Labeled coins: 1105 (853 dead/pulled, 252 still alive). Base dead rate 77.2%. Forward 24h samples so far: 48.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 900 | 76% | 215 (24%) | 58% of 53 | -1% |
| 2 | 23 | 17% | 19 (83%) | 77% of 947 | -60% |
| 3 | 329 | 73% | 90 (27%) | 77% of 630 | -5% |
| 4 | 148 | 69% | 46 (31%) | 76% of 812 | -8% |
| 5 | 777 | 82% | 141 (18%) | 50% of 194 | +5% |
| 6 | 76 | 50% | 38 (50%) | 78% of 819 | -27% |
| 7 | 404 | 70% | 120 (30%) | 80% of 465 | -7% |
| 8 | 431 | 68% | 136 (32%) | 76% of 407 | -9% |
| 9 | 731 | 80% | 145 (20%) | 59% of 229 | +3% |
| 10 | 760 | 85% | 116 (15%) | 39% of 197 | +8% |
| 11 | 544 | 89% | 61 (11%) | 61% of 449 | +12% |
| 12 | 901 | 80% | 183 (20%) | 40% of 92 | +2% |
| 13 | 610 | 76% | 147 (24%) | 76% of 383 | -1% |
| 14 | 403 | 78% | 90 (22%) | 75% of 590 | +0% |
| 15 | 480 | 72% | 134 (28%) | 80% of 513 | -5% |
| 16 | 88 | 77% | 20 (23%) | 76% of 905 | +0% |
| 18 | 687 | 84% | 108 (16%) | 58% of 306 | +7% |
| 19 | 356 | 79% | 76 (21%) | 73% of 551 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=900)
- check #3: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=329)
- check #4: lower weight: flagged coins die no more often than average (precision 69% vs base 77%, n=148)
- check #6: lower weight: flagged coins die no more often than average (precision 50% vs base 77%, n=76)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=404)
- check #8: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=431)
- check #9: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=731)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=901)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=610)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=403)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 77%, n=480)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 77%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=356)
