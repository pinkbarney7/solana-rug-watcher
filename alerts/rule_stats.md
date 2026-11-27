# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 04:52 UTC. Labeled coins: 237 (108 dead/pulled, 129 still alive). Base dead rate 45.6%. Forward 24h samples so far: 154.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 219 | 48% | 113 (52%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 49% of 222 | -46% |
| 3 | 87 | 37% | 55 (63%) | 51% of 150 | -9% |
| 5 | 161 | 61% | 63 (39%) | 13% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 52% of 202 | -37% |
| 7 | 156 | 53% | 73 (47%) | 36% of 66 | +8% |
| 8 | 181 | 59% | 74 (41%) | 2% of 56 | +14% |
| 9 | 100 | 37% | 63 (63%) | 52% of 137 | -9% |
| 10 | 136 | 68% | 43 (32%) | 15% of 101 | +23% |
| 11 | 237 | 46% | 129 (54%) | n/a | +0% |
| 12 | 237 | 46% | 129 (54%) | n/a | +0% |
| 13 | 237 | 46% | 129 (54%) | n/a | +0% |
| 14 | 237 | 46% | 129 (54%) | n/a | +0% |
| 15 | 237 | 46% | 129 (54%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 48% of 191 | -11% |
| 18 | 237 | 46% | 129 (54%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 46%, n=87)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 46%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 46%, n=100)
- check #10: consider treating WARN like FAIL: strong lift (precision 68% vs base 46%, n=136)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 46%, n=46)
