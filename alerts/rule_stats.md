# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 09:38 UTC. Labeled coins: 242 (113 dead/pulled, 129 still alive). Base dead rate 46.7%. Forward 24h samples so far: 162.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 224 | 50% | 113 (50%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 50% of 227 | -47% |
| 3 | 88 | 38% | 55 (62%) | 52% of 154 | -9% |
| 5 | 166 | 61% | 64 (39%) | 14% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 53% of 207 | -38% |
| 7 | 160 | 55% | 72 (45%) | 36% of 67 | +8% |
| 8 | 186 | 60% | 74 (40%) | 2% of 56 | +14% |
| 9 | 102 | 37% | 64 (63%) | 54% of 140 | -9% |
| 10 | 140 | 70% | 42 (30%) | 15% of 102 | +23% |
| 11 | 242 | 47% | 129 (53%) | n/a | +0% |
| 12 | 242 | 47% | 129 (53%) | n/a | +0% |
| 13 | 242 | 47% | 129 (53%) | n/a | +0% |
| 14 | 242 | 47% | 129 (53%) | n/a | +0% |
| 15 | 242 | 47% | 129 (53%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 49% of 196 | -12% |
| 18 | 242 | 47% | 129 (53%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 47%, n=88)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 47%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=102)
- check #10: consider treating WARN like FAIL: strong lift (precision 70% vs base 47%, n=140)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 47%, n=46)
