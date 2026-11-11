# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-11 18:08 UTC. Labeled coins: 47 (5 dead/pulled, 42 still alive). Base dead rate 10.6%. Forward 24h samples so far: 27.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 40 | 10% | 36 (90%) | 0% of 6 | -1% |
| 2 | 7 | 0% | 7 (100%) | 12% of 40 | -11% |
| 3 | 23 | 9% | 21 (91%) | 12% of 24 | -2% |
| 5 | 18 | 17% | 15 (83%) | 7% of 29 | +6% |
| 6 | 16 | 12% | 14 (88%) | 10% of 30 | +2% |
| 7 | 28 | 18% | 23 (82%) | 0% of 16 | +7% |
| 8 | 24 | 21% | 19 (79%) | 0% of 23 | +10% |
| 9 | 17 | 12% | 15 (88%) | 10% of 30 | +1% |
| 10 | 24 | 21% | 19 (79%) | 0% of 23 | +10% |
| 11 | 47 | 11% | 42 (89%) | n/a | +0% |
| 12 | 47 | 11% | 42 (89%) | n/a | +0% |
| 13 | 47 | 11% | 42 (89%) | n/a | +0% |
| 14 | 47 | 11% | 42 (89%) | n/a | +0% |
| 15 | 47 | 11% | 42 (89%) | n/a | +0% |
| 16 | 26 | 8% | 24 (92%) | 14% of 21 | -3% |
| 18 | 47 | 11% | 42 (89%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 2.4 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
