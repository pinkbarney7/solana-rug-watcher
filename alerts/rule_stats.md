# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 04:58 UTC. Labeled coins: 76 (15 dead/pulled, 61 still alive). Base dead rate 19.7%. Forward 24h samples so far: 46.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 65 | 22% | 51 (78%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 22% of 68 | -20% |
| 3 | 36 | 17% | 30 (83%) | 22% of 40 | -3% |
| 5 | 37 | 27% | 27 (73%) | 13% of 39 | +7% |
| 6 | 19 | 16% | 16 (84%) | 21% of 56 | -4% |
| 7 | 46 | 22% | 36 (78%) | 20% of 25 | +2% |
| 8 | 49 | 31% | 34 (69%) | 0% of 27 | +11% |
| 9 | 36 | 17% | 30 (83%) | 22% of 40 | -3% |
| 10 | 38 | 32% | 26 (68%) | 8% of 38 | +12% |
| 11 | 76 | 20% | 61 (80%) | n/a | +0% |
| 12 | 76 | 20% | 61 (80%) | n/a | +0% |
| 13 | 76 | 20% | 61 (80%) | n/a | +0% |
| 14 | 76 | 20% | 61 (80%) | n/a | +0% |
| 15 | 76 | 20% | 61 (80%) | n/a | +0% |
| 16 | 38 | 24% | 29 (76%) | 16% of 38 | +4% |
| 18 | 76 | 20% | 61 (80%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 5.9 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 20%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 20%, n=36)
