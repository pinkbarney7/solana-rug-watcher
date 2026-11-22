# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 09:08 UTC. Labeled coins: 150 (51 dead/pulled, 99 still alive). Base dead rate 34.0%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 135 | 37% | 85 (63%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 37% of 138 | -34% |
| 3 | 64 | 33% | 43 (67%) | 35% of 86 | -1% |
| 5 | 94 | 45% | 52 (55%) | 16% of 56 | +11% |
| 6 | 28 | 11% | 25 (89%) | 40% of 121 | -23% |
| 7 | 96 | 38% | 60 (62%) | 30% of 47 | +3% |
| 8 | 108 | 46% | 58 (54%) | 2% of 42 | +12% |
| 9 | 74 | 31% | 51 (69%) | 37% of 76 | -3% |
| 10 | 77 | 57% | 33 (43%) | 10% of 73 | +23% |
| 11 | 150 | 34% | 99 (66%) | n/a | +0% |
| 12 | 150 | 34% | 99 (66%) | n/a | +0% |
| 13 | 150 | 34% | 99 (66%) | n/a | +0% |
| 14 | 150 | 34% | 99 (66%) | n/a | +0% |
| 15 | 150 | 34% | 99 (66%) | n/a | +0% |
| 16 | 41 | 32% | 28 (68%) | 35% of 109 | -2% |
| 18 | 150 | 34% | 99 (66%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 33% vs base 34%, n=64)
- check #9: lower weight: flagged coins die no more often than average (precision 31% vs base 34%, n=74)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 34%, n=77)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 34%, n=41)
