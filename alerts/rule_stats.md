# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 07:19 UTC. Labeled coins: 77 (16 dead/pulled, 61 still alive). Base dead rate 20.8%. Forward 24h samples so far: 46.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 66 | 23% | 51 (77%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 23% of 69 | -21% |
| 3 | 36 | 17% | 30 (83%) | 24% of 41 | -4% |
| 5 | 38 | 29% | 27 (71%) | 13% of 39 | +8% |
| 6 | 19 | 16% | 16 (84%) | 23% of 57 | -5% |
| 7 | 47 | 23% | 36 (77%) | 20% of 25 | +3% |
| 8 | 50 | 32% | 34 (68%) | 0% of 27 | +11% |
| 9 | 36 | 17% | 30 (83%) | 24% of 41 | -4% |
| 10 | 39 | 33% | 26 (67%) | 8% of 38 | +13% |
| 11 | 77 | 21% | 61 (79%) | n/a | +0% |
| 12 | 77 | 21% | 61 (79%) | n/a | +0% |
| 13 | 77 | 21% | 61 (79%) | n/a | +0% |
| 14 | 77 | 21% | 61 (79%) | n/a | +0% |
| 15 | 77 | 21% | 61 (79%) | n/a | +0% |
| 16 | 38 | 24% | 29 (76%) | 18% of 39 | +3% |
| 18 | 77 | 21% | 61 (79%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 6.0 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 21%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 21%, n=36)
- check #16: lower weight: flagged coins die no more often than average (precision 24% vs base 21%, n=38)
