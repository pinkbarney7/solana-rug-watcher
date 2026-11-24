# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 05:17 UTC. Labeled coins: 175 (71 dead/pulled, 104 still alive). Base dead rate 40.6%. Forward 24h samples so far: 99.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 160 | 44% | 90 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 163 | -41% |
| 3 | 74 | 35% | 48 (65%) | 45% of 101 | -5% |
| 5 | 118 | 52% | 57 (48%) | 18% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 47% of 146 | -30% |
| 7 | 112 | 46% | 61 (54%) | 34% of 56 | +5% |
| 8 | 131 | 53% | 61 (47%) | 2% of 44 | +13% |
| 9 | 86 | 34% | 57 (66%) | 47% of 89 | -7% |
| 10 | 92 | 65% | 32 (35%) | 13% of 83 | +25% |
| 11 | 175 | 41% | 104 (59%) | n/a | +0% |
| 12 | 175 | 41% | 104 (59%) | n/a | +0% |
| 13 | 175 | 41% | 104 (59%) | n/a | +0% |
| 14 | 175 | 41% | 104 (59%) | n/a | +0% |
| 15 | 175 | 41% | 104 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 133 | -5% |
| 18 | 175 | 41% | 104 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 35% vs base 41%, n=74)
- check #9: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=86)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 41%, n=92)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
