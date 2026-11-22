# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 17:06 UTC. Labeled coins: 156 (54 dead/pulled, 102 still alive). Base dead rate 34.6%. Forward 24h samples so far: 86.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 141 | 38% | 88 (62%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 38% of 144 | -35% |
| 3 | 68 | 31% | 47 (69%) | 38% of 88 | -4% |
| 5 | 100 | 45% | 55 (55%) | 16% of 56 | +10% |
| 6 | 28 | 11% | 25 (89%) | 40% of 127 | -24% |
| 7 | 98 | 40% | 59 (60%) | 27% of 51 | +5% |
| 8 | 113 | 47% | 60 (53%) | 2% of 43 | +12% |
| 9 | 78 | 29% | 55 (71%) | 40% of 78 | -5% |
| 10 | 80 | 59% | 33 (41%) | 9% of 76 | +24% |
| 11 | 156 | 35% | 102 (65%) | n/a | +0% |
| 12 | 156 | 35% | 102 (65%) | n/a | +0% |
| 13 | 156 | 35% | 102 (65%) | n/a | +0% |
| 14 | 156 | 35% | 102 (65%) | n/a | +0% |
| 15 | 156 | 35% | 102 (65%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 35% of 115 | -0% |
| 18 | 156 | 35% | 102 (65%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 31% vs base 35%, n=68)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 35%, n=78)
- check #10: consider treating WARN like FAIL: strong lift (precision 59% vs base 35%, n=80)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 35%, n=41)
