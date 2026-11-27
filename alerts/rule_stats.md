# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 11:24 UTC. Labeled coins: 247 (117 dead/pulled, 130 still alive). Base dead rate 47.4%. Forward 24h samples so far: 166.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 229 | 50% | 114 (50%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 50% of 232 | -47% |
| 3 | 89 | 37% | 56 (63%) | 53% of 158 | -10% |
| 5 | 171 | 62% | 65 (38%) | 14% of 76 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 211 | -39% |
| 7 | 164 | 56% | 72 (44%) | 35% of 68 | +9% |
| 8 | 191 | 61% | 75 (39%) | 2% of 56 | +13% |
| 9 | 103 | 37% | 65 (63%) | 55% of 144 | -10% |
| 10 | 144 | 71% | 42 (29%) | 15% of 103 | +23% |
| 11 | 247 | 47% | 130 (53%) | n/a | +0% |
| 12 | 247 | 47% | 130 (53%) | n/a | +0% |
| 13 | 247 | 47% | 130 (53%) | n/a | +0% |
| 14 | 247 | 47% | 130 (53%) | n/a | +0% |
| 15 | 247 | 47% | 130 (53%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 50% of 201 | -13% |
| 18 | 247 | 47% | 130 (53%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=89)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 47%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 47%, n=144)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 47%, n=46)
