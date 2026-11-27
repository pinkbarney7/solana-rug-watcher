# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 13:11 UTC. Labeled coins: 249 (119 dead/pulled, 130 still alive). Base dead rate 47.8%. Forward 24h samples so far: 168.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 230 | 50% | 114 (50%) | 12% of 17 | +3% |
| 2 | 15 | 0% | 15 (100%) | 51% of 234 | -48% |
| 3 | 89 | 37% | 56 (63%) | 54% of 160 | -11% |
| 5 | 173 | 62% | 65 (38%) | 14% of 76 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 213 | -39% |
| 7 | 166 | 57% | 72 (43%) | 35% of 68 | +9% |
| 8 | 193 | 61% | 75 (39%) | 2% of 56 | +13% |
| 9 | 103 | 37% | 65 (63%) | 55% of 146 | -11% |
| 10 | 146 | 71% | 42 (29%) | 15% of 103 | +23% |
| 11 | 249 | 48% | 130 (52%) | n/a | +0% |
| 12 | 249 | 48% | 130 (52%) | n/a | +0% |
| 13 | 249 | 48% | 130 (52%) | n/a | +0% |
| 14 | 249 | 48% | 130 (52%) | n/a | +0% |
| 15 | 249 | 48% | 130 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 203 | -13% |
| 18 | 249 | 48% | 130 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=89)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=146)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
