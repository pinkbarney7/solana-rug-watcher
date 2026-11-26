# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 09:14 UTC. Labeled coins: 223 (98 dead/pulled, 125 still alive). Base dead rate 43.9%. Forward 24h samples so far: 147.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 206 | 47% | 109 (53%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 47% of 208 | -44% |
| 3 | 85 | 38% | 53 (62%) | 48% of 138 | -6% |
| 5 | 148 | 59% | 60 (41%) | 13% of 75 | +16% |
| 6 | 34 | 9% | 31 (91%) | 51% of 188 | -35% |
| 7 | 144 | 51% | 71 (49%) | 38% of 64 | +7% |
| 8 | 168 | 58% | 71 (42%) | 2% of 55 | +14% |
| 9 | 97 | 38% | 60 (62%) | 48% of 126 | -6% |
| 10 | 126 | 66% | 43 (34%) | 15% of 97 | +22% |
| 11 | 223 | 44% | 125 (56%) | n/a | +0% |
| 12 | 223 | 44% | 125 (56%) | n/a | +0% |
| 13 | 223 | 44% | 125 (56%) | n/a | +0% |
| 14 | 223 | 44% | 125 (56%) | n/a | +0% |
| 15 | 223 | 44% | 125 (56%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 47% of 178 | -11% |
| 18 | 223 | 44% | 125 (56%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 44%, n=85)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 44%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 44%, n=97)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 44%, n=126)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 44%, n=45)
