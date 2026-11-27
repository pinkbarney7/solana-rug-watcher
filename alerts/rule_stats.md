# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 10:32 UTC. Labeled coins: 246 (116 dead/pulled, 130 still alive). Base dead rate 47.2%. Forward 24h samples so far: 165.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 228 | 50% | 114 (50%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 50% of 231 | -47% |
| 3 | 89 | 37% | 56 (63%) | 53% of 157 | -10% |
| 5 | 170 | 62% | 65 (38%) | 14% of 76 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 210 | -39% |
| 7 | 163 | 56% | 72 (44%) | 35% of 68 | +9% |
| 8 | 190 | 61% | 75 (39%) | 2% of 56 | +13% |
| 9 | 103 | 37% | 65 (63%) | 55% of 143 | -10% |
| 10 | 143 | 71% | 42 (29%) | 15% of 103 | +23% |
| 11 | 246 | 47% | 130 (53%) | n/a | +0% |
| 12 | 246 | 47% | 130 (53%) | n/a | +0% |
| 13 | 246 | 47% | 130 (53%) | n/a | +0% |
| 14 | 246 | 47% | 130 (53%) | n/a | +0% |
| 15 | 246 | 47% | 130 (53%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 50% of 200 | -12% |
| 18 | 246 | 47% | 130 (53%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=89)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 47%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 47%, n=143)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 47%, n=46)
