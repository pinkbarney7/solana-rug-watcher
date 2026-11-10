# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 08:23 UTC. Labeled coins: 11 (1 dead/pulled, 10 still alive). Base dead rate 9.1%. Forward 24h samples so far: 10.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 11 | 9% | 10 (91%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 11% of 9 | -9% |
| 3 | 7 | 0% | 7 (100%) | 25% of 4 | -9% |
| 5 | 5 | 20% | 4 (80%) | 0% of 6 | +11% |
| 6 | 3 | 0% | 3 (100%) | 12% of 8 | -9% |
| 7 | 6 | 17% | 5 (83%) | 0% of 5 | +8% |
| 8 | 7 | 14% | 6 (86%) | 0% of 4 | +5% |
| 9 | 4 | 0% | 4 (100%) | 14% of 7 | -9% |
| 10 | 3 | 33% | 2 (67%) | 0% of 8 | +24% |
| 11 | 11 | 9% | 10 (91%) | n/a | +0% |
| 12 | 11 | 9% | 10 (91%) | n/a | +0% |
| 13 | 11 | 9% | 10 (91%) | n/a | +0% |
| 14 | 11 | 9% | 10 (91%) | n/a | +0% |
| 15 | 11 | 9% | 10 (91%) | n/a | +0% |
| 16 | 7 | 0% | 7 (100%) | 25% of 4 | -9% |
| 18 | 11 | 9% | 10 (91%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.0 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
