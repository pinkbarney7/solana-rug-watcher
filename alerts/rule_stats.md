# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 11:17 UTC. Labeled coins: 23 (4 dead/pulled, 19 still alive). Base dead rate 17.4%. Forward 24h samples so far: 19.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 20 | 15% | 17 (85%) | 0% of 2 | -2% |
| 2 | 3 | 0% | 3 (100%) | 20% of 20 | -17% |
| 3 | 11 | 9% | 10 (91%) | 25% of 12 | -8% |
| 5 | 7 | 43% | 4 (57%) | 6% of 16 | +25% |
| 6 | 8 | 12% | 7 (88%) | 20% of 15 | -5% |
| 7 | 15 | 27% | 11 (73%) | 0% of 6 | +9% |
| 8 | 14 | 29% | 10 (71%) | 0% of 9 | +11% |
| 9 | 6 | 17% | 5 (83%) | 18% of 17 | -1% |
| 10 | 10 | 40% | 6 (60%) | 0% of 13 | +23% |
| 11 | 23 | 17% | 19 (83%) | n/a | +0% |
| 12 | 23 | 17% | 19 (83%) | n/a | +0% |
| 13 | 23 | 17% | 19 (83%) | n/a | +0% |
| 14 | 23 | 17% | 19 (83%) | n/a | +0% |
| 15 | 23 | 17% | 19 (83%) | n/a | +0% |
| 16 | 12 | 8% | 11 (92%) | 27% of 11 | -9% |
| 18 | 23 | 17% | 19 (83%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.2 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
