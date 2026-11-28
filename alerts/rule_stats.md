# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 11:42 UTC. Labeled coins: 269 (135 dead/pulled, 134 still alive). Base dead rate 50.2%. Forward 24h samples so far: 189.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 249 | 53% | 118 (47%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 53% of 253 | -50% |
| 3 | 92 | 39% | 56 (61%) | 56% of 177 | -11% |
| 5 | 188 | 65% | 65 (35%) | 15% of 81 | +15% |
| 6 | 36 | 8% | 33 (92%) | 57% of 232 | -42% |
| 7 | 185 | 58% | 78 (42%) | 39% of 69 | +8% |
| 8 | 210 | 63% | 77 (37%) | 3% of 59 | +13% |
| 9 | 106 | 38% | 66 (62%) | 58% of 163 | -12% |
| 10 | 161 | 73% | 44 (27%) | 17% of 108 | +22% |
| 11 | 269 | 50% | 134 (50%) | n/a | +0% |
| 12 | 269 | 50% | 134 (50%) | n/a | +0% |
| 13 | 269 | 50% | 134 (50%) | n/a | +0% |
| 14 | 269 | 50% | 134 (50%) | n/a | +0% |
| 15 | 269 | 50% | 134 (50%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 53% of 223 | -15% |
| 18 | 269 | 50% | 134 (50%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 50%, n=92)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 50%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 50%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 73% vs base 50%, n=161)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 50%, n=46)
