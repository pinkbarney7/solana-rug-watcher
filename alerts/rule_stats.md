# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 12:09 UTC. Labeled coins: 24 (4 dead/pulled, 20 still alive). Base dead rate 16.7%. Forward 24h samples so far: 20.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 20 | 15% | 17 (85%) | 0% of 3 | -2% |
| 2 | 4 | 0% | 4 (100%) | 20% of 20 | -17% |
| 3 | 11 | 9% | 10 (91%) | 23% of 13 | -8% |
| 5 | 7 | 43% | 4 (57%) | 6% of 17 | +26% |
| 6 | 9 | 11% | 8 (89%) | 20% of 15 | -6% |
| 7 | 16 | 25% | 12 (75%) | 0% of 6 | +8% |
| 8 | 14 | 29% | 10 (71%) | 0% of 10 | +12% |
| 9 | 6 | 17% | 5 (83%) | 17% of 18 | +0% |
| 10 | 11 | 36% | 7 (64%) | 0% of 13 | +20% |
| 11 | 24 | 17% | 20 (83%) | n/a | +0% |
| 12 | 24 | 17% | 20 (83%) | n/a | +0% |
| 13 | 24 | 17% | 20 (83%) | n/a | +0% |
| 14 | 24 | 17% | 20 (83%) | n/a | +0% |
| 15 | 24 | 17% | 20 (83%) | n/a | +0% |
| 16 | 12 | 8% | 11 (92%) | 25% of 12 | -8% |
| 18 | 24 | 17% | 20 (83%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.2 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
