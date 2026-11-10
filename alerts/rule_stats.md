# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 08:57 UTC. Labeled coins: 12 (1 dead/pulled, 11 still alive). Base dead rate 8.3%. Forward 24h samples so far: 11.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 12 | 8% | 11 (92%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 10% of 10 | -8% |
| 3 | 7 | 0% | 7 (100%) | 20% of 5 | -8% |
| 5 | 5 | 20% | 4 (80%) | 0% of 7 | +12% |
| 6 | 3 | 0% | 3 (100%) | 11% of 9 | -8% |
| 7 | 7 | 14% | 6 (86%) | 0% of 5 | +6% |
| 8 | 7 | 14% | 6 (86%) | 0% of 5 | +6% |
| 9 | 4 | 0% | 4 (100%) | 12% of 8 | -8% |
| 10 | 3 | 33% | 2 (67%) | 0% of 9 | +25% |
| 11 | 12 | 8% | 11 (92%) | n/a | +0% |
| 12 | 12 | 8% | 11 (92%) | n/a | +0% |
| 13 | 12 | 8% | 11 (92%) | n/a | +0% |
| 14 | 12 | 8% | 11 (92%) | n/a | +0% |
| 15 | 12 | 8% | 11 (92%) | n/a | +0% |
| 16 | 7 | 0% | 7 (100%) | 20% of 5 | -8% |
| 18 | 12 | 8% | 11 (92%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
