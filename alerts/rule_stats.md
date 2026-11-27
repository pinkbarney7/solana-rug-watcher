# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 10:00 UTC. Labeled coins: 243 (114 dead/pulled, 129 still alive). Base dead rate 46.9%. Forward 24h samples so far: 162.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 225 | 50% | 113 (50%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 50% of 228 | -47% |
| 3 | 88 | 38% | 55 (62%) | 52% of 155 | -9% |
| 5 | 167 | 62% | 64 (38%) | 14% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 53% of 208 | -38% |
| 7 | 161 | 55% | 72 (45%) | 36% of 67 | +8% |
| 8 | 187 | 60% | 74 (40%) | 2% of 56 | +14% |
| 9 | 102 | 37% | 64 (63%) | 54% of 141 | -10% |
| 10 | 141 | 70% | 42 (30%) | 15% of 102 | +23% |
| 11 | 243 | 47% | 129 (53%) | n/a | +0% |
| 12 | 243 | 47% | 129 (53%) | n/a | +0% |
| 13 | 243 | 47% | 129 (53%) | n/a | +0% |
| 14 | 243 | 47% | 129 (53%) | n/a | +0% |
| 15 | 243 | 47% | 129 (53%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 50% of 197 | -12% |
| 18 | 243 | 47% | 129 (53%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 47%, n=88)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 47%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=102)
- check #10: consider treating WARN like FAIL: strong lift (precision 70% vs base 47%, n=141)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 47%, n=46)
