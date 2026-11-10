# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 09:48 UTC. Labeled coins: 16 (2 dead/pulled, 14 still alive). Base dead rate 12.5%. Forward 24h samples so far: 14.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 16 | 12% | 14 (88%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 14% of 14 | -12% |
| 3 | 8 | 0% | 8 (100%) | 25% of 8 | -12% |
| 5 | 6 | 33% | 4 (67%) | 0% of 10 | +21% |
| 6 | 5 | 0% | 5 (100%) | 18% of 11 | -12% |
| 7 | 10 | 20% | 8 (80%) | 0% of 5 | +8% |
| 8 | 9 | 22% | 7 (78%) | 0% of 7 | +10% |
| 9 | 4 | 0% | 4 (100%) | 17% of 12 | -12% |
| 10 | 5 | 40% | 3 (60%) | 0% of 11 | +28% |
| 11 | 16 | 12% | 14 (88%) | n/a | +0% |
| 12 | 16 | 12% | 14 (88%) | n/a | +0% |
| 13 | 16 | 12% | 14 (88%) | n/a | +0% |
| 14 | 16 | 12% | 14 (88%) | n/a | +0% |
| 15 | 16 | 12% | 14 (88%) | n/a | +0% |
| 16 | 10 | 10% | 9 (90%) | 17% of 6 | -2% |
| 18 | 16 | 12% | 14 (88%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
