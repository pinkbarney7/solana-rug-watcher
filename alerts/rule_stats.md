# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-20 04:19 UTC. Labeled coins: 135 (44 dead/pulled, 91 still alive). Base dead rate 32.6%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 120 | 36% | 77 (64%) | 0% of 13 | +3% |
| 2 | 10 | 0% | 10 (100%) | 35% of 125 | -33% |
| 3 | 56 | 29% | 40 (71%) | 35% of 79 | -4% |
| 5 | 84 | 44% | 47 (56%) | 14% of 51 | +11% |
| 6 | 26 | 12% | 23 (88%) | 38% of 108 | -21% |
| 7 | 88 | 35% | 57 (65%) | 29% of 41 | +3% |
| 8 | 99 | 44% | 55 (56%) | 0% of 36 | +12% |
| 9 | 64 | 28% | 46 (72%) | 37% of 71 | -4% |
| 10 | 70 | 56% | 31 (44%) | 8% of 65 | +23% |
| 11 | 135 | 33% | 91 (67%) | n/a | +0% |
| 12 | 135 | 33% | 91 (67%) | n/a | +0% |
| 13 | 135 | 33% | 91 (67%) | n/a | +0% |
| 14 | 135 | 33% | 91 (67%) | n/a | +0% |
| 15 | 135 | 33% | 91 (67%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 33% of 95 | -0% |
| 18 | 135 | 33% | 91 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 29% vs base 33%, n=56)
- check #7: lower weight: flagged coins die no more often than average (precision 35% vs base 33%, n=88)
- check #9: lower weight: flagged coins die no more often than average (precision 28% vs base 33%, n=64)
- check #10: consider treating WARN like FAIL: strong lift (precision 56% vs base 33%, n=70)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 33%, n=40)
