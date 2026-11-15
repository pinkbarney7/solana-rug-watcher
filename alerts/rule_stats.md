# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 00:00 UTC. Labeled coins: 74 (15 dead/pulled, 59 still alive). Base dead rate 20.3%. Forward 24h samples so far: 43.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 63 | 22% | 49 (78%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 23% of 66 | -20% |
| 3 | 34 | 18% | 28 (82%) | 22% of 40 | -3% |
| 5 | 35 | 29% | 25 (71%) | 13% of 39 | +8% |
| 6 | 19 | 16% | 16 (84%) | 22% of 54 | -4% |
| 7 | 45 | 22% | 35 (78%) | 21% of 24 | +2% |
| 8 | 48 | 31% | 33 (69%) | 0% of 26 | +11% |
| 9 | 34 | 18% | 28 (82%) | 22% of 40 | -3% |
| 10 | 37 | 32% | 25 (68%) | 8% of 37 | +12% |
| 11 | 74 | 20% | 59 (80%) | n/a | +0% |
| 12 | 74 | 20% | 59 (80%) | n/a | +0% |
| 13 | 74 | 20% | 59 (80%) | n/a | +0% |
| 14 | 74 | 20% | 59 (80%) | n/a | +0% |
| 15 | 74 | 20% | 59 (80%) | n/a | +0% |
| 16 | 38 | 24% | 29 (76%) | 17% of 36 | +3% |
| 18 | 74 | 20% | 59 (80%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 5.7 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 20%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 18% vs base 20%, n=34)
