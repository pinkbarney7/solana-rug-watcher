# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 15:20 UTC. Labeled coins: 277 (140 dead/pulled, 137 still alive). Base dead rate 50.5%. Forward 24h samples so far: 193.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 257 | 53% | 121 (47%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 54% of 261 | -51% |
| 3 | 93 | 39% | 57 (61%) | 57% of 184 | -12% |
| 5 | 194 | 66% | 66 (34%) | 14% of 83 | +15% |
| 6 | 36 | 8% | 33 (92%) | 57% of 237 | -42% |
| 7 | 188 | 58% | 79 (42%) | 39% of 69 | +7% |
| 8 | 216 | 64% | 78 (36%) | 3% of 61 | +13% |
| 9 | 107 | 37% | 67 (63%) | 59% of 170 | -13% |
| 10 | 169 | 72% | 47 (28%) | 17% of 108 | +22% |
| 11 | 277 | 51% | 137 (49%) | n/a | +0% |
| 12 | 277 | 51% | 137 (49%) | n/a | +0% |
| 13 | 277 | 51% | 137 (49%) | n/a | +0% |
| 14 | 277 | 51% | 137 (49%) | n/a | +0% |
| 15 | 277 | 51% | 137 (49%) | n/a | +0% |
| 16 | 48 | 33% | 32 (67%) | 54% of 229 | -17% |
| 18 | 277 | 51% | 137 (49%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 50%, n=93)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 50%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 50%, n=107)
- check #10: consider treating WARN like FAIL: strong lift (precision 72% vs base 50%, n=169)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 50%, n=48)
