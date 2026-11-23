# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 23:03 UTC. Labeled coins: 173 (71 dead/pulled, 102 still alive). Base dead rate 41.0%. Forward 24h samples so far: 95.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 158 | 44% | 88 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 161 | -41% |
| 3 | 73 | 36% | 47 (64%) | 45% of 100 | -5% |
| 5 | 116 | 53% | 55 (47%) | 18% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 47% of 144 | -30% |
| 7 | 111 | 46% | 60 (54%) | 35% of 55 | +5% |
| 8 | 129 | 54% | 59 (46%) | 2% of 44 | +13% |
| 9 | 84 | 35% | 55 (65%) | 47% of 89 | -7% |
| 10 | 92 | 65% | 32 (35%) | 14% of 81 | +24% |
| 11 | 173 | 41% | 102 (59%) | n/a | +0% |
| 12 | 173 | 41% | 102 (59%) | n/a | +0% |
| 13 | 173 | 41% | 102 (59%) | n/a | +0% |
| 14 | 173 | 41% | 102 (59%) | n/a | +0% |
| 15 | 173 | 41% | 102 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 131 | -5% |
| 18 | 173 | 41% | 102 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=73)
- check #9: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=84)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 41%, n=92)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
