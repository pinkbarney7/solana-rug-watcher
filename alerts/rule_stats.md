# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 07:42 UTC. Labeled coins: 240 (111 dead/pulled, 129 still alive). Base dead rate 46.2%. Forward 24h samples so far: 159.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 222 | 49% | 113 (51%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 49% of 225 | -46% |
| 3 | 88 | 38% | 55 (62%) | 51% of 152 | -9% |
| 5 | 164 | 61% | 64 (39%) | 14% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 53% of 205 | -37% |
| 7 | 158 | 54% | 72 (46%) | 36% of 67 | +8% |
| 8 | 184 | 60% | 74 (40%) | 2% of 56 | +14% |
| 9 | 102 | 37% | 64 (63%) | 53% of 138 | -9% |
| 10 | 138 | 70% | 42 (30%) | 15% of 102 | +23% |
| 11 | 240 | 46% | 129 (54%) | n/a | +0% |
| 12 | 240 | 46% | 129 (54%) | n/a | +0% |
| 13 | 240 | 46% | 129 (54%) | n/a | +0% |
| 14 | 240 | 46% | 129 (54%) | n/a | +0% |
| 15 | 240 | 46% | 129 (54%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 49% of 194 | -11% |
| 18 | 240 | 46% | 129 (54%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 46%, n=88)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 46%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 46%, n=102)
- check #10: consider treating WARN like FAIL: strong lift (precision 70% vs base 46%, n=138)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 46%, n=46)
