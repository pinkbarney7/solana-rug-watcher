# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 08:50 UTC. Labeled coins: 196 (81 dead/pulled, 115 still alive). Base dead rate 41.3%. Forward 24h samples so far: 125.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 179 | 45% | 99 (55%) | 0% of 15 | +3% |
| 2 | 13 | 0% | 13 (100%) | 44% of 183 | -41% |
| 3 | 81 | 32% | 55 (68%) | 48% of 115 | -9% |
| 5 | 133 | 53% | 62 (47%) | 16% of 63 | +12% |
| 6 | 32 | 9% | 29 (91%) | 48% of 163 | -32% |
| 7 | 128 | 48% | 67 (52%) | 31% of 61 | +6% |
| 8 | 150 | 53% | 70 (47%) | 2% of 46 | +12% |
| 9 | 92 | 33% | 62 (67%) | 49% of 104 | -9% |
| 10 | 106 | 66% | 36 (34%) | 12% of 90 | +25% |
| 11 | 196 | 41% | 115 (59%) | n/a | +0% |
| 12 | 196 | 41% | 115 (59%) | n/a | +0% |
| 13 | 196 | 41% | 115 (59%) | n/a | +0% |
| 14 | 196 | 41% | 115 (59%) | n/a | +0% |
| 15 | 196 | 41% | 115 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 154 | -6% |
| 18 | 196 | 41% | 115 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=81)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 41%, n=32)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=92)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=106)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
