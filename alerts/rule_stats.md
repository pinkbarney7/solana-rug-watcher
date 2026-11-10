# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 10:13 UTC. Labeled coins: 18 (2 dead/pulled, 16 still alive). Base dead rate 11.1%. Forward 24h samples so far: 16.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 17 | 12% | 15 (88%) | 0% of 1 | +1% |
| 2 | 3 | 0% | 3 (100%) | 13% of 15 | -11% |
| 3 | 9 | 0% | 9 (100%) | 22% of 9 | -11% |
| 5 | 6 | 33% | 4 (67%) | 0% of 12 | +22% |
| 6 | 6 | 0% | 6 (100%) | 17% of 12 | -11% |
| 7 | 11 | 18% | 9 (82%) | 0% of 5 | +7% |
| 8 | 11 | 18% | 9 (82%) | 0% of 7 | +7% |
| 9 | 5 | 0% | 5 (100%) | 15% of 13 | -11% |
| 10 | 6 | 33% | 4 (67%) | 0% of 12 | +22% |
| 11 | 18 | 11% | 16 (89%) | n/a | +0% |
| 12 | 18 | 11% | 16 (89%) | n/a | +0% |
| 13 | 18 | 11% | 16 (89%) | n/a | +0% |
| 14 | 18 | 11% | 16 (89%) | n/a | +0% |
| 15 | 18 | 11% | 16 (89%) | n/a | +0% |
| 16 | 11 | 9% | 10 (91%) | 14% of 7 | -2% |
| 18 | 18 | 11% | 16 (89%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
