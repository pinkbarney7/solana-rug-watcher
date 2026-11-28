# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 03:59 UTC. Labeled coins: 254 (122 dead/pulled, 132 still alive). Base dead rate 48.0%. Forward 24h samples so far: 174.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 235 | 51% | 116 (49%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 51% of 238 | -48% |
| 3 | 90 | 38% | 56 (62%) | 54% of 164 | -10% |
| 5 | 175 | 63% | 64 (37%) | 14% of 79 | +15% |
| 6 | 35 | 9% | 32 (91%) | 55% of 218 | -39% |
| 7 | 171 | 56% | 75 (44%) | 37% of 68 | +8% |
| 8 | 196 | 62% | 75 (38%) | 2% of 58 | +14% |
| 9 | 104 | 38% | 65 (62%) | 55% of 150 | -11% |
| 10 | 150 | 71% | 44 (29%) | 15% of 104 | +23% |
| 11 | 254 | 48% | 132 (52%) | n/a | +0% |
| 12 | 254 | 48% | 132 (52%) | n/a | +0% |
| 13 | 254 | 48% | 132 (52%) | n/a | +0% |
| 14 | 254 | 48% | 132 (52%) | n/a | +0% |
| 15 | 254 | 48% | 132 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 208 | -13% |
| 18 | 254 | 48% | 132 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=90)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=104)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=150)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
