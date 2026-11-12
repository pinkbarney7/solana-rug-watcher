# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-12 07:42 UTC. Labeled coins: 51 (6 dead/pulled, 45 still alive). Base dead rate 11.8%. Forward 24h samples so far: 30.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 44 | 11% | 39 (89%) | 0% of 6 | -0% |
| 2 | 7 | 0% | 7 (100%) | 14% of 44 | -12% |
| 3 | 25 | 8% | 23 (92%) | 15% of 26 | -4% |
| 5 | 21 | 19% | 17 (81%) | 7% of 30 | +7% |
| 6 | 16 | 12% | 14 (88%) | 12% of 34 | +1% |
| 7 | 31 | 19% | 25 (81%) | 0% of 17 | +8% |
| 8 | 27 | 22% | 21 (78%) | 0% of 24 | +10% |
| 9 | 19 | 11% | 17 (89%) | 12% of 32 | -1% |
| 10 | 27 | 22% | 21 (78%) | 0% of 24 | +10% |
| 11 | 51 | 12% | 45 (88%) | n/a | +0% |
| 12 | 51 | 12% | 45 (88%) | n/a | +0% |
| 13 | 51 | 12% | 45 (88%) | n/a | +0% |
| 14 | 51 | 12% | 45 (88%) | n/a | +0% |
| 15 | 51 | 12% | 45 (88%) | n/a | +0% |
| 16 | 27 | 11% | 24 (89%) | 12% of 24 | -1% |
| 18 | 51 | 12% | 45 (88%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 3.0 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
