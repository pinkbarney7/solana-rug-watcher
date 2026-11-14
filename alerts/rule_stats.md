# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-14 20:20 UTC. Labeled coins: 72 (15 dead/pulled, 57 still alive). Base dead rate 20.8%. Forward 24h samples so far: 41.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 61 | 23% | 47 (77%) | 0% of 9 | +2% |
| 2 | 7 | 0% | 7 (100%) | 23% of 65 | -21% |
| 3 | 34 | 18% | 28 (82%) | 24% of 38 | -3% |
| 5 | 34 | 29% | 24 (71%) | 13% of 38 | +9% |
| 6 | 19 | 16% | 16 (84%) | 23% of 52 | -5% |
| 7 | 45 | 22% | 35 (78%) | 22% of 23 | +1% |
| 8 | 46 | 33% | 31 (67%) | 0% of 26 | +12% |
| 9 | 33 | 18% | 27 (82%) | 23% of 39 | -3% |
| 10 | 36 | 33% | 24 (67%) | 8% of 36 | +12% |
| 11 | 72 | 21% | 57 (79%) | n/a | +0% |
| 12 | 72 | 21% | 57 (79%) | n/a | +0% |
| 13 | 72 | 21% | 57 (79%) | n/a | +0% |
| 14 | 72 | 21% | 57 (79%) | n/a | +0% |
| 15 | 72 | 21% | 57 (79%) | n/a | +0% |
| 16 | 38 | 24% | 29 (76%) | 18% of 34 | +3% |
| 18 | 72 | 21% | 57 (79%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 5.5 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 21%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 18% vs base 21%, n=33)
- check #16: lower weight: flagged coins die no more often than average (precision 24% vs base 21%, n=38)
