# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 12:26 UTC. Labeled coins: 78 (16 dead/pulled, 62 still alive). Base dead rate 20.5%. Forward 24h samples so far: 48.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 67 | 22% | 52 (78%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 23% of 70 | -21% |
| 3 | 37 | 16% | 31 (84%) | 24% of 41 | -4% |
| 5 | 39 | 28% | 28 (72%) | 13% of 39 | +8% |
| 6 | 19 | 16% | 16 (84%) | 22% of 58 | -5% |
| 7 | 47 | 23% | 36 (77%) | 19% of 26 | +3% |
| 8 | 51 | 31% | 35 (69%) | 0% of 27 | +11% |
| 9 | 37 | 16% | 31 (84%) | 24% of 41 | -4% |
| 10 | 39 | 33% | 26 (67%) | 8% of 39 | +13% |
| 11 | 78 | 21% | 62 (79%) | n/a | +0% |
| 12 | 78 | 21% | 62 (79%) | n/a | +0% |
| 13 | 78 | 21% | 62 (79%) | n/a | +0% |
| 14 | 78 | 21% | 62 (79%) | n/a | +0% |
| 15 | 78 | 21% | 62 (79%) | n/a | +0% |
| 16 | 38 | 24% | 29 (76%) | 18% of 40 | +3% |
| 18 | 78 | 21% | 62 (79%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 6.2 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 20%, n=37)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 20%, n=37)
