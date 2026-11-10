# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 11:10 UTC. Labeled coins: 21 (3 dead/pulled, 18 still alive). Base dead rate 14.3%. Forward 24h samples so far: 18.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 19 | 16% | 16 (84%) | 0% of 2 | +2% |
| 2 | 3 | 0% | 3 (100%) | 17% of 18 | -14% |
| 3 | 10 | 10% | 9 (90%) | 18% of 11 | -4% |
| 5 | 6 | 33% | 4 (67%) | 7% of 15 | +19% |
| 6 | 8 | 12% | 7 (88%) | 15% of 13 | -2% |
| 7 | 13 | 23% | 10 (77%) | 0% of 6 | +9% |
| 8 | 12 | 25% | 9 (75%) | 0% of 9 | +11% |
| 9 | 6 | 17% | 5 (83%) | 13% of 15 | +2% |
| 10 | 8 | 38% | 5 (62%) | 0% of 13 | +23% |
| 11 | 21 | 14% | 18 (86%) | n/a | +0% |
| 12 | 21 | 14% | 18 (86%) | n/a | +0% |
| 13 | 21 | 14% | 18 (86%) | n/a | +0% |
| 14 | 21 | 14% | 18 (86%) | n/a | +0% |
| 15 | 21 | 14% | 18 (86%) | n/a | +0% |
| 16 | 12 | 8% | 11 (92%) | 22% of 9 | -6% |
| 18 | 21 | 14% | 18 (86%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
