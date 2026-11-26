# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 05:40 UTC. Labeled coins: 214 (90 dead/pulled, 124 still alive). Base dead rate 42.1%. Forward 24h samples so far: 142.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 197 | 45% | 108 (55%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 45% of 199 | -42% |
| 3 | 83 | 36% | 53 (64%) | 46% of 131 | -6% |
| 5 | 139 | 58% | 59 (42%) | 13% of 75 | +15% |
| 6 | 34 | 9% | 31 (91%) | 49% of 179 | -33% |
| 7 | 137 | 49% | 70 (51%) | 35% of 62 | +7% |
| 8 | 159 | 56% | 70 (44%) | 2% of 55 | +14% |
| 9 | 93 | 37% | 59 (63%) | 46% of 121 | -5% |
| 10 | 119 | 65% | 42 (35%) | 14% of 95 | +23% |
| 11 | 214 | 42% | 124 (58%) | n/a | +0% |
| 12 | 214 | 42% | 124 (58%) | n/a | +0% |
| 13 | 214 | 42% | 124 (58%) | n/a | +0% |
| 14 | 214 | 42% | 124 (58%) | n/a | +0% |
| 15 | 214 | 42% | 124 (58%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 44% of 169 | -9% |
| 18 | 214 | 42% | 124 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=83)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 42%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 42%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 42%, n=119)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 42%, n=45)
