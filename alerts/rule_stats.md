# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 10:48 UTC. Labeled coins: 265 (132 dead/pulled, 133 still alive). Base dead rate 49.8%. Forward 24h samples so far: 187.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 245 | 52% | 117 (48%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 53% of 249 | -50% |
| 3 | 92 | 39% | 56 (61%) | 55% of 173 | -11% |
| 5 | 185 | 65% | 65 (35%) | 15% of 80 | +15% |
| 6 | 36 | 8% | 33 (92%) | 57% of 228 | -41% |
| 7 | 181 | 57% | 77 (43%) | 39% of 69 | +8% |
| 8 | 207 | 63% | 77 (37%) | 3% of 58 | +13% |
| 9 | 106 | 38% | 66 (62%) | 58% of 159 | -12% |
| 10 | 158 | 72% | 44 (28%) | 17% of 107 | +22% |
| 11 | 265 | 50% | 133 (50%) | n/a | +0% |
| 12 | 265 | 50% | 133 (50%) | n/a | +0% |
| 13 | 265 | 50% | 133 (50%) | n/a | +0% |
| 14 | 265 | 50% | 133 (50%) | n/a | +0% |
| 15 | 265 | 50% | 133 (50%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 53% of 219 | -15% |
| 18 | 265 | 50% | 133 (50%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 50%, n=92)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 50%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 50%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 72% vs base 50%, n=158)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 50%, n=46)
