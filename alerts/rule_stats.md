# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 15:10 UTC. Labeled coins: 231 (104 dead/pulled, 127 still alive). Base dead rate 45.0%. Forward 24h samples so far: 152.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 213 | 48% | 111 (52%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 48% of 216 | -45% |
| 3 | 85 | 38% | 53 (62%) | 49% of 146 | -7% |
| 5 | 155 | 61% | 61 (39%) | 13% of 76 | +16% |
| 6 | 34 | 9% | 31 (91%) | 52% of 196 | -36% |
| 7 | 152 | 52% | 73 (48%) | 38% of 64 | +7% |
| 8 | 175 | 59% | 72 (41%) | 2% of 56 | +14% |
| 9 | 98 | 38% | 61 (62%) | 50% of 133 | -7% |
| 10 | 132 | 67% | 43 (33%) | 15% of 99 | +22% |
| 11 | 231 | 45% | 127 (55%) | n/a | +0% |
| 12 | 231 | 45% | 127 (55%) | n/a | +0% |
| 13 | 231 | 45% | 127 (55%) | n/a | +0% |
| 14 | 231 | 45% | 127 (55%) | n/a | +0% |
| 15 | 231 | 45% | 127 (55%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 48% of 185 | -10% |
| 18 | 231 | 45% | 127 (55%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 45%, n=85)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 45%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 45%, n=98)
- check #10: consider treating WARN like FAIL: strong lift (precision 67% vs base 45%, n=132)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 45%, n=46)
