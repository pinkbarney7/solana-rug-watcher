# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 15:39 UTC. Labeled coins: 152 (53 dead/pulled, 99 still alive). Base dead rate 34.9%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 137 | 38% | 85 (62%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 38% of 140 | -35% |
| 3 | 65 | 32% | 44 (68%) | 37% of 87 | -3% |
| 5 | 96 | 46% | 52 (54%) | 16% of 56 | +11% |
| 6 | 28 | 11% | 25 (89%) | 41% of 123 | -24% |
| 7 | 97 | 39% | 59 (61%) | 29% of 48 | +4% |
| 8 | 110 | 47% | 58 (53%) | 2% of 42 | +12% |
| 9 | 75 | 31% | 52 (69%) | 39% of 77 | -4% |
| 10 | 78 | 59% | 32 (41%) | 9% of 74 | +24% |
| 11 | 152 | 35% | 99 (65%) | n/a | +0% |
| 12 | 152 | 35% | 99 (65%) | n/a | +0% |
| 13 | 152 | 35% | 99 (65%) | n/a | +0% |
| 14 | 152 | 35% | 99 (65%) | n/a | +0% |
| 15 | 152 | 35% | 99 (65%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 35% of 111 | -1% |
| 18 | 152 | 35% | 99 (65%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 35%, n=65)
- check #9: lower weight: flagged coins die no more often than average (precision 31% vs base 35%, n=75)
- check #10: consider treating WARN like FAIL: strong lift (precision 59% vs base 35%, n=78)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 35%, n=41)
