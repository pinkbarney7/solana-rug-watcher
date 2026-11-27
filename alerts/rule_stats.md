# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 15:39 UTC. Labeled coins: 251 (120 dead/pulled, 131 still alive). Base dead rate 47.8%. Forward 24h samples so far: 170.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 232 | 50% | 115 (50%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 51% of 235 | -48% |
| 3 | 90 | 37% | 57 (63%) | 54% of 161 | -11% |
| 5 | 174 | 63% | 65 (37%) | 14% of 77 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 215 | -39% |
| 7 | 168 | 57% | 73 (43%) | 35% of 68 | +9% |
| 8 | 194 | 61% | 75 (39%) | 2% of 57 | +14% |
| 9 | 103 | 37% | 65 (63%) | 55% of 148 | -11% |
| 10 | 148 | 71% | 43 (29%) | 15% of 103 | +23% |
| 11 | 251 | 48% | 131 (52%) | n/a | +0% |
| 12 | 251 | 48% | 131 (52%) | n/a | +0% |
| 13 | 251 | 48% | 131 (52%) | n/a | +0% |
| 14 | 251 | 48% | 131 (52%) | n/a | +0% |
| 15 | 251 | 48% | 131 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 205 | -13% |
| 18 | 251 | 48% | 131 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=90)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=148)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
