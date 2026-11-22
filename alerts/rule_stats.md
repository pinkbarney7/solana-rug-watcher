# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 01:55 UTC. Labeled coins: 149 (51 dead/pulled, 98 still alive). Base dead rate 34.2%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 134 | 37% | 84 (63%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 37% of 137 | -34% |
| 3 | 63 | 33% | 42 (67%) | 35% of 86 | -1% |
| 5 | 93 | 45% | 51 (55%) | 16% of 56 | +11% |
| 6 | 27 | 11% | 24 (89%) | 40% of 121 | -23% |
| 7 | 96 | 38% | 60 (62%) | 30% of 46 | +3% |
| 8 | 108 | 46% | 58 (54%) | 2% of 41 | +12% |
| 9 | 74 | 31% | 51 (69%) | 37% of 75 | -3% |
| 10 | 76 | 58% | 32 (42%) | 10% of 73 | +24% |
| 11 | 149 | 34% | 98 (66%) | n/a | +0% |
| 12 | 149 | 34% | 98 (66%) | n/a | +0% |
| 13 | 149 | 34% | 98 (66%) | n/a | +0% |
| 14 | 149 | 34% | 98 (66%) | n/a | +0% |
| 15 | 149 | 34% | 98 (66%) | n/a | +0% |
| 16 | 41 | 32% | 28 (68%) | 35% of 108 | -3% |
| 18 | 149 | 34% | 98 (66%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 33% vs base 34%, n=63)
- check #9: lower weight: flagged coins die no more often than average (precision 31% vs base 34%, n=74)
- check #10: consider treating WARN like FAIL: strong lift (precision 58% vs base 34%, n=76)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 34%, n=41)
