# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-12 22:18 UTC. Labeled coins: 56 (6 dead/pulled, 50 still alive). Base dead rate 10.7%. Forward 24h samples so far: 30.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 47 | 11% | 42 (89%) | 0% of 7 | -0% |
| 2 | 7 | 0% | 7 (100%) | 12% of 49 | -11% |
| 3 | 27 | 7% | 25 (93%) | 14% of 29 | -3% |
| 5 | 23 | 17% | 19 (83%) | 6% of 33 | +7% |
| 6 | 17 | 12% | 15 (88%) | 11% of 38 | +1% |
| 7 | 34 | 18% | 28 (82%) | 0% of 19 | +7% |
| 8 | 31 | 19% | 25 (81%) | 0% of 25 | +9% |
| 9 | 22 | 9% | 20 (91%) | 12% of 34 | -2% |
| 10 | 29 | 21% | 23 (79%) | 0% of 27 | +10% |
| 11 | 56 | 11% | 50 (89%) | n/a | +0% |
| 12 | 56 | 11% | 50 (89%) | n/a | +0% |
| 13 | 56 | 11% | 50 (89%) | n/a | +0% |
| 14 | 56 | 11% | 50 (89%) | n/a | +0% |
| 15 | 56 | 11% | 50 (89%) | n/a | +0% |
| 16 | 29 | 10% | 26 (90%) | 11% of 27 | -0% |
| 18 | 56 | 11% | 50 (89%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 3.6 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
