# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 10:03 UTC. Labeled coins: 244 (114 dead/pulled, 130 still alive). Base dead rate 46.7%. Forward 24h samples so far: 165.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 226 | 50% | 114 (50%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 50% of 229 | -47% |
| 3 | 89 | 37% | 56 (63%) | 52% of 155 | -10% |
| 5 | 168 | 61% | 65 (39%) | 14% of 76 | +15% |
| 6 | 35 | 9% | 32 (91%) | 53% of 208 | -38% |
| 7 | 161 | 55% | 72 (45%) | 35% of 68 | +9% |
| 8 | 188 | 60% | 75 (40%) | 2% of 56 | +13% |
| 9 | 103 | 37% | 65 (63%) | 54% of 141 | -10% |
| 10 | 141 | 70% | 42 (30%) | 15% of 103 | +23% |
| 11 | 244 | 47% | 130 (53%) | n/a | +0% |
| 12 | 244 | 47% | 130 (53%) | n/a | +0% |
| 13 | 244 | 47% | 130 (53%) | n/a | +0% |
| 14 | 244 | 47% | 130 (53%) | n/a | +0% |
| 15 | 244 | 47% | 130 (53%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 49% of 198 | -12% |
| 18 | 244 | 47% | 130 (53%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=89)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 47%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 47%, n=103)
- check #10: consider treating WARN like FAIL: strong lift (precision 70% vs base 47%, n=141)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 47%, n=46)
