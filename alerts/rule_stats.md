# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 10:54 UTC. Labeled coins: 20 (3 dead/pulled, 17 still alive). Base dead rate 15.0%. Forward 24h samples so far: 17.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 18 | 17% | 15 (83%) | 0% of 2 | +2% |
| 2 | 3 | 0% | 3 (100%) | 18% of 17 | -15% |
| 3 | 10 | 10% | 9 (90%) | 20% of 10 | -5% |
| 5 | 6 | 33% | 4 (67%) | 7% of 14 | +18% |
| 6 | 8 | 12% | 7 (88%) | 17% of 12 | -2% |
| 7 | 13 | 23% | 10 (77%) | 0% of 5 | +8% |
| 8 | 12 | 25% | 9 (75%) | 0% of 8 | +10% |
| 9 | 6 | 17% | 5 (83%) | 14% of 14 | +2% |
| 10 | 7 | 43% | 4 (57%) | 0% of 13 | +28% |
| 11 | 20 | 15% | 17 (85%) | n/a | +0% |
| 12 | 20 | 15% | 17 (85%) | n/a | +0% |
| 13 | 20 | 15% | 17 (85%) | n/a | +0% |
| 14 | 20 | 15% | 17 (85%) | n/a | +0% |
| 15 | 20 | 15% | 17 (85%) | n/a | +0% |
| 16 | 11 | 9% | 10 (91%) | 22% of 9 | -6% |
| 18 | 20 | 15% | 17 (85%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
