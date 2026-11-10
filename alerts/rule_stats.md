# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 08:12 UTC. Labeled coins: 10 (1 dead/pulled, 9 still alive). Base dead rate 10.0%. Forward 24h samples so far: 9.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 10 | 10% | 9 (90%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 12% of 8 | -10% |
| 3 | 6 | 0% | 6 (100%) | 25% of 4 | -10% |
| 5 | 4 | 25% | 3 (75%) | 0% of 6 | +15% |
| 6 | 3 | 0% | 3 (100%) | 14% of 7 | -10% |
| 7 | 6 | 17% | 5 (83%) | 0% of 4 | +7% |
| 8 | 6 | 17% | 5 (83%) | 0% of 4 | +7% |
| 9 | 3 | 0% | 3 (100%) | 14% of 7 | -10% |
| 10 | 3 | 33% | 2 (67%) | 0% of 7 | +23% |
| 11 | 10 | 10% | 9 (90%) | n/a | +0% |
| 12 | 10 | 10% | 9 (90%) | n/a | +0% |
| 13 | 10 | 10% | 9 (90%) | n/a | +0% |
| 14 | 10 | 10% | 9 (90%) | n/a | +0% |
| 15 | 10 | 10% | 9 (90%) | n/a | +0% |
| 16 | 6 | 0% | 6 (100%) | 25% of 4 | -10% |
| 18 | 10 | 10% | 9 (90%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.0 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
