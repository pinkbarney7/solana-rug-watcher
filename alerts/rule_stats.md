# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 05:37 UTC. Labeled coins: 255 (122 dead/pulled, 133 still alive). Base dead rate 47.8%. Forward 24h samples so far: 177.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 236 | 50% | 117 (50%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 51% of 239 | -48% |
| 3 | 90 | 38% | 56 (62%) | 53% of 165 | -10% |
| 5 | 176 | 63% | 65 (37%) | 14% of 79 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 219 | -39% |
| 7 | 172 | 56% | 76 (44%) | 37% of 68 | +8% |
| 8 | 197 | 61% | 76 (39%) | 2% of 58 | +14% |
| 9 | 105 | 37% | 66 (63%) | 55% of 150 | -11% |
| 10 | 150 | 71% | 44 (29%) | 15% of 105 | +23% |
| 11 | 255 | 48% | 133 (52%) | n/a | +0% |
| 12 | 255 | 48% | 133 (52%) | n/a | +0% |
| 13 | 255 | 48% | 133 (52%) | n/a | +0% |
| 14 | 255 | 48% | 133 (52%) | n/a | +0% |
| 15 | 255 | 48% | 133 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 209 | -13% |
| 18 | 255 | 48% | 133 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=90)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=105)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=150)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
