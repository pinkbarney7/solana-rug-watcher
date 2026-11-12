# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-12 16:16 UTC. Labeled coins: 55 (6 dead/pulled, 49 still alive). Base dead rate 10.9%. Forward 24h samples so far: 30.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 46 | 11% | 41 (89%) | 0% of 7 | -0% |
| 2 | 7 | 0% | 7 (100%) | 12% of 48 | -11% |
| 3 | 26 | 8% | 24 (92%) | 14% of 29 | -3% |
| 5 | 23 | 17% | 19 (83%) | 6% of 32 | +6% |
| 6 | 16 | 12% | 14 (88%) | 11% of 38 | +2% |
| 7 | 33 | 18% | 27 (82%) | 0% of 19 | +7% |
| 8 | 31 | 19% | 25 (81%) | 0% of 24 | +8% |
| 9 | 22 | 9% | 20 (91%) | 12% of 33 | -2% |
| 10 | 29 | 21% | 23 (79%) | 0% of 26 | +10% |
| 11 | 55 | 11% | 49 (89%) | n/a | +0% |
| 12 | 55 | 11% | 49 (89%) | n/a | +0% |
| 13 | 55 | 11% | 49 (89%) | n/a | +0% |
| 14 | 55 | 11% | 49 (89%) | n/a | +0% |
| 15 | 55 | 11% | 49 (89%) | n/a | +0% |
| 16 | 29 | 10% | 26 (90%) | 12% of 26 | -1% |
| 18 | 55 | 11% | 49 (89%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 3.4 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
