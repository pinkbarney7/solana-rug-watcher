# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-14 09:31 UTC. Labeled coins: 66 (11 dead/pulled, 55 still alive). Base dead rate 16.7%. Forward 24h samples so far: 39.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 56 | 18% | 46 (82%) | 0% of 8 | +1% |
| 2 | 7 | 0% | 7 (100%) | 19% of 59 | -17% |
| 3 | 31 | 10% | 28 (90%) | 23% of 35 | -7% |
| 5 | 29 | 24% | 22 (76%) | 11% of 37 | +7% |
| 6 | 19 | 16% | 16 (84%) | 17% of 46 | -1% |
| 7 | 42 | 21% | 33 (79%) | 10% of 20 | +5% |
| 8 | 40 | 28% | 29 (72%) | 0% of 26 | +11% |
| 9 | 28 | 14% | 24 (86%) | 18% of 38 | -2% |
| 10 | 34 | 26% | 25 (74%) | 6% of 32 | +10% |
| 11 | 66 | 17% | 55 (83%) | n/a | +0% |
| 12 | 66 | 17% | 55 (83%) | n/a | +0% |
| 13 | 66 | 17% | 55 (83%) | n/a | +0% |
| 14 | 66 | 17% | 55 (83%) | n/a | +0% |
| 15 | 66 | 17% | 55 (83%) | n/a | +0% |
| 16 | 34 | 18% | 28 (82%) | 16% of 32 | +1% |
| 18 | 66 | 17% | 55 (83%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 5.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 10% vs base 17%, n=31)
- check #16: lower weight: flagged coins die no more often than average (precision 18% vs base 17%, n=34)
