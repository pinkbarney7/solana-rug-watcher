# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 02:44 UTC. Labeled coins: 252 (122 dead/pulled, 130 still alive). Base dead rate 48.4%. Forward 24h samples so far: 170.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 233 | 51% | 114 (49%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 52% of 236 | -48% |
| 3 | 90 | 38% | 56 (62%) | 54% of 162 | -11% |
| 5 | 175 | 63% | 64 (37%) | 14% of 77 | +15% |
| 6 | 35 | 9% | 32 (91%) | 55% of 216 | -40% |
| 7 | 169 | 57% | 73 (43%) | 37% of 68 | +8% |
| 8 | 195 | 62% | 74 (38%) | 2% of 57 | +14% |
| 9 | 103 | 38% | 64 (62%) | 56% of 149 | -11% |
| 10 | 149 | 71% | 43 (29%) | 16% of 103 | +23% |
| 11 | 252 | 48% | 130 (52%) | n/a | +0% |
| 12 | 252 | 48% | 130 (52%) | n/a | +0% |
| 13 | 252 | 48% | 130 (52%) | n/a | +0% |
| 14 | 252 | 48% | 130 (52%) | n/a | +0% |
| 15 | 252 | 48% | 130 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 206 | -14% |
| 18 | 252 | 48% | 130 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=90)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=149)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
