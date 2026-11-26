# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 11:01 UTC. Labeled coins: 226 (100 dead/pulled, 126 still alive). Base dead rate 44.2%. Forward 24h samples so far: 150.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 209 | 47% | 110 (53%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 47% of 211 | -44% |
| 3 | 85 | 38% | 53 (62%) | 48% of 141 | -7% |
| 5 | 150 | 60% | 60 (40%) | 13% of 76 | +16% |
| 6 | 34 | 9% | 31 (91%) | 51% of 191 | -35% |
| 7 | 147 | 51% | 72 (49%) | 38% of 64 | +7% |
| 8 | 170 | 58% | 71 (42%) | 2% of 56 | +14% |
| 9 | 97 | 38% | 60 (62%) | 49% of 129 | -6% |
| 10 | 128 | 66% | 43 (34%) | 15% of 98 | +22% |
| 11 | 226 | 44% | 126 (56%) | n/a | +0% |
| 12 | 226 | 44% | 126 (56%) | n/a | +0% |
| 13 | 226 | 44% | 126 (56%) | n/a | +0% |
| 14 | 226 | 44% | 126 (56%) | n/a | +0% |
| 15 | 226 | 44% | 126 (56%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 47% of 181 | -11% |
| 18 | 226 | 44% | 126 (56%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 44%, n=85)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 44%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 44%, n=97)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 44%, n=128)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 44%, n=45)
