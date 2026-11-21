# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-21 22:01 UTC. Labeled coins: 148 (49 dead/pulled, 99 still alive). Base dead rate 33.1%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 133 | 36% | 85 (64%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 36% of 136 | -33% |
| 3 | 63 | 32% | 43 (68%) | 34% of 85 | -1% |
| 5 | 92 | 43% | 52 (57%) | 16% of 56 | +10% |
| 6 | 27 | 11% | 24 (89%) | 38% of 120 | -22% |
| 7 | 95 | 37% | 60 (63%) | 28% of 46 | +4% |
| 8 | 107 | 46% | 58 (54%) | 0% of 41 | +13% |
| 9 | 73 | 29% | 52 (71%) | 37% of 75 | -4% |
| 10 | 75 | 57% | 32 (43%) | 8% of 73 | +24% |
| 11 | 148 | 33% | 99 (67%) | n/a | +0% |
| 12 | 148 | 33% | 99 (67%) | n/a | +0% |
| 13 | 148 | 33% | 99 (67%) | n/a | +0% |
| 14 | 148 | 33% | 99 (67%) | n/a | +0% |
| 15 | 148 | 33% | 99 (67%) | n/a | +0% |
| 16 | 41 | 32% | 28 (68%) | 34% of 107 | -1% |
| 18 | 148 | 33% | 99 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=63)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 33%, n=73)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 33%, n=75)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=41)
