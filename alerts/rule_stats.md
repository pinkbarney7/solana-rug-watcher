# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 05:59 UTC. Labeled coins: 177 (72 dead/pulled, 105 still alive). Base dead rate 40.7%. Forward 24h samples so far: 101.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 162 | 44% | 91 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 165 | -41% |
| 3 | 75 | 35% | 49 (65%) | 45% of 102 | -6% |
| 5 | 120 | 52% | 58 (48%) | 18% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 47% of 148 | -30% |
| 7 | 113 | 46% | 61 (54%) | 33% of 57 | +5% |
| 8 | 133 | 53% | 62 (47%) | 2% of 44 | +13% |
| 9 | 87 | 33% | 58 (67%) | 48% of 90 | -7% |
| 10 | 93 | 66% | 32 (34%) | 13% of 84 | +25% |
| 11 | 177 | 41% | 105 (59%) | n/a | +0% |
| 12 | 177 | 41% | 105 (59%) | n/a | +0% |
| 13 | 177 | 41% | 105 (59%) | n/a | +0% |
| 14 | 177 | 41% | 105 (59%) | n/a | +0% |
| 15 | 177 | 41% | 105 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 135 | -5% |
| 18 | 177 | 41% | 105 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 35% vs base 41%, n=75)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=87)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=93)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
