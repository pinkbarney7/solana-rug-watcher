# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 20:43 UTC. Labeled coins: 252 (121 dead/pulled, 131 still alive). Base dead rate 48.0%. Forward 24h samples so far: 170.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 233 | 51% | 115 (49%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 51% of 236 | -48% |
| 3 | 90 | 37% | 57 (63%) | 54% of 162 | -11% |
| 5 | 175 | 63% | 65 (37%) | 14% of 77 | +15% |
| 6 | 35 | 9% | 32 (91%) | 55% of 216 | -39% |
| 7 | 169 | 57% | 73 (43%) | 35% of 68 | +9% |
| 8 | 195 | 62% | 75 (38%) | 2% of 57 | +14% |
| 9 | 103 | 37% | 65 (63%) | 56% of 149 | -11% |
| 10 | 149 | 71% | 43 (29%) | 15% of 103 | +23% |
| 11 | 252 | 48% | 131 (52%) | n/a | +0% |
| 12 | 252 | 48% | 131 (52%) | n/a | +0% |
| 13 | 252 | 48% | 131 (52%) | n/a | +0% |
| 14 | 252 | 48% | 131 (52%) | n/a | +0% |
| 15 | 252 | 48% | 131 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 206 | -13% |
| 18 | 252 | 48% | 131 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=90)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=149)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
