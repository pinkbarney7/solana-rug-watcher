# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 12:07 UTC. Labeled coins: 270 (136 dead/pulled, 134 still alive). Base dead rate 50.4%. Forward 24h samples so far: 190.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 250 | 53% | 118 (47%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 54% of 254 | -50% |
| 3 | 92 | 39% | 56 (61%) | 56% of 178 | -11% |
| 5 | 189 | 66% | 65 (34%) | 15% of 81 | +15% |
| 6 | 36 | 8% | 33 (92%) | 57% of 233 | -42% |
| 7 | 186 | 58% | 78 (42%) | 39% of 69 | +8% |
| 8 | 211 | 64% | 77 (36%) | 3% of 59 | +13% |
| 9 | 106 | 38% | 66 (62%) | 59% of 164 | -13% |
| 10 | 162 | 73% | 44 (27%) | 17% of 108 | +22% |
| 11 | 270 | 50% | 134 (50%) | n/a | +0% |
| 12 | 270 | 50% | 134 (50%) | n/a | +0% |
| 13 | 270 | 50% | 134 (50%) | n/a | +0% |
| 14 | 270 | 50% | 134 (50%) | n/a | +0% |
| 15 | 270 | 50% | 134 (50%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 54% of 224 | -16% |
| 18 | 270 | 50% | 134 (50%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 50%, n=92)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 50%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 50%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 73% vs base 50%, n=162)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 50%, n=46)
