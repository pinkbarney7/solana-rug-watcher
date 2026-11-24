# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 06:19 UTC. Labeled coins: 178 (72 dead/pulled, 106 still alive). Base dead rate 40.4%. Forward 24h samples so far: 102.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 163 | 44% | 92 (56%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 43% of 166 | -40% |
| 3 | 75 | 35% | 49 (65%) | 45% of 103 | -6% |
| 5 | 120 | 52% | 58 (48%) | 17% of 58 | +11% |
| 6 | 29 | 10% | 26 (90%) | 47% of 148 | -30% |
| 7 | 114 | 46% | 62 (54%) | 33% of 57 | +5% |
| 8 | 134 | 53% | 63 (47%) | 2% of 44 | +13% |
| 9 | 87 | 33% | 58 (67%) | 47% of 91 | -7% |
| 10 | 93 | 66% | 32 (34%) | 13% of 85 | +25% |
| 11 | 178 | 40% | 106 (60%) | n/a | +0% |
| 12 | 178 | 40% | 106 (60%) | n/a | +0% |
| 13 | 178 | 40% | 106 (60%) | n/a | +0% |
| 14 | 178 | 40% | 106 (60%) | n/a | +0% |
| 15 | 178 | 40% | 106 (60%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 136 | -5% |
| 18 | 178 | 40% | 106 (60%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 35% vs base 40%, n=75)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 40%, n=87)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 40%, n=93)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 40%, n=42)
