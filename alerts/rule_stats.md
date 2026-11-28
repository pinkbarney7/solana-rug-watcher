# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 10:06 UTC. Labeled coins: 262 (129 dead/pulled, 133 still alive). Base dead rate 49.2%. Forward 24h samples so far: 186.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 242 | 52% | 117 (48%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 52% of 246 | -49% |
| 3 | 92 | 39% | 56 (61%) | 55% of 170 | -10% |
| 5 | 182 | 64% | 65 (36%) | 15% of 80 | +15% |
| 6 | 36 | 8% | 33 (92%) | 56% of 225 | -41% |
| 7 | 178 | 57% | 77 (43%) | 39% of 69 | +8% |
| 8 | 204 | 62% | 77 (38%) | 3% of 58 | +13% |
| 9 | 106 | 38% | 66 (62%) | 57% of 156 | -12% |
| 10 | 155 | 72% | 44 (28%) | 17% of 107 | +22% |
| 11 | 262 | 49% | 133 (51%) | n/a | +0% |
| 12 | 262 | 49% | 133 (51%) | n/a | +0% |
| 13 | 262 | 49% | 133 (51%) | n/a | +0% |
| 14 | 262 | 49% | 133 (51%) | n/a | +0% |
| 15 | 262 | 49% | 133 (51%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 52% of 216 | -14% |
| 18 | 262 | 49% | 133 (51%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 49%, n=92)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 49%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 49%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 72% vs base 49%, n=155)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 49%, n=46)
