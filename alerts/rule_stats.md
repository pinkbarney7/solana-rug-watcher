# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 04:29 UTC. Labeled coins: 234 (106 dead/pulled, 128 still alive). Base dead rate 45.3%. Forward 24h samples so far: 153.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 216 | 48% | 112 (52%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 48% of 219 | -45% |
| 3 | 86 | 37% | 54 (63%) | 50% of 148 | -8% |
| 5 | 158 | 61% | 62 (39%) | 13% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 52% of 199 | -36% |
| 7 | 154 | 53% | 73 (47%) | 37% of 65 | +7% |
| 8 | 178 | 59% | 73 (41%) | 2% of 56 | +14% |
| 9 | 99 | 37% | 62 (63%) | 51% of 135 | -8% |
| 10 | 134 | 68% | 43 (32%) | 15% of 100 | +23% |
| 11 | 234 | 45% | 128 (55%) | n/a | +0% |
| 12 | 234 | 45% | 128 (55%) | n/a | +0% |
| 13 | 234 | 45% | 128 (55%) | n/a | +0% |
| 14 | 234 | 45% | 128 (55%) | n/a | +0% |
| 15 | 234 | 45% | 128 (55%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 48% of 188 | -11% |
| 18 | 234 | 45% | 128 (55%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 45%, n=86)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 45%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 45%, n=99)
- check #10: consider treating WARN like FAIL: strong lift (precision 68% vs base 45%, n=134)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 45%, n=46)
