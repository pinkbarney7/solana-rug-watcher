# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-13 02:41 UTC. Labeled coins: 58 (6 dead/pulled, 52 still alive). Base dead rate 10.3%. Forward 24h samples so far: 32.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 48 | 10% | 43 (90%) | 0% of 8 | +0% |
| 2 | 7 | 0% | 7 (100%) | 12% of 51 | -10% |
| 3 | 29 | 7% | 27 (93%) | 14% of 29 | -3% |
| 5 | 24 | 17% | 20 (83%) | 6% of 34 | +6% |
| 6 | 18 | 11% | 16 (89%) | 10% of 39 | +1% |
| 7 | 35 | 17% | 29 (83%) | 0% of 19 | +7% |
| 8 | 33 | 18% | 27 (82%) | 0% of 25 | +8% |
| 9 | 23 | 9% | 21 (91%) | 11% of 35 | -2% |
| 10 | 31 | 19% | 25 (81%) | 0% of 27 | +9% |
| 11 | 58 | 10% | 52 (90%) | n/a | +0% |
| 12 | 58 | 10% | 52 (90%) | n/a | +0% |
| 13 | 58 | 10% | 52 (90%) | n/a | +0% |
| 14 | 58 | 10% | 52 (90%) | n/a | +0% |
| 15 | 58 | 10% | 52 (90%) | n/a | +0% |
| 16 | 30 | 10% | 27 (90%) | 11% of 28 | -0% |
| 18 | 58 | 10% | 52 (90%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 3.8 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
