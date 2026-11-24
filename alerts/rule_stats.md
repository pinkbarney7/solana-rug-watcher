# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 01:37 UTC. Labeled coins: 174 (71 dead/pulled, 103 still alive). Base dead rate 40.8%. Forward 24h samples so far: 96.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 159 | 44% | 89 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 162 | -41% |
| 3 | 73 | 36% | 47 (64%) | 45% of 101 | -5% |
| 5 | 117 | 52% | 56 (48%) | 18% of 57 | +11% |
| 6 | 28 | 11% | 25 (89%) | 47% of 145 | -30% |
| 7 | 112 | 46% | 61 (54%) | 35% of 55 | +5% |
| 8 | 130 | 54% | 60 (46%) | 2% of 44 | +13% |
| 9 | 85 | 34% | 56 (66%) | 47% of 89 | -7% |
| 10 | 92 | 65% | 32 (35%) | 13% of 82 | +24% |
| 11 | 174 | 41% | 103 (59%) | n/a | +0% |
| 12 | 174 | 41% | 103 (59%) | n/a | +0% |
| 13 | 174 | 41% | 103 (59%) | n/a | +0% |
| 14 | 174 | 41% | 103 (59%) | n/a | +0% |
| 15 | 174 | 41% | 103 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 132 | -5% |
| 18 | 174 | 41% | 103 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=73)
- check #9: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=85)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 41%, n=92)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
