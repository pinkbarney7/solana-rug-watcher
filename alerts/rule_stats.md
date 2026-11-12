# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-12 00:35 UTC. Labeled coins: 50 (6 dead/pulled, 44 still alive). Base dead rate 12.0%. Forward 24h samples so far: 30.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 43 | 12% | 38 (88%) | 0% of 6 | -0% |
| 2 | 7 | 0% | 7 (100%) | 14% of 43 | -12% |
| 3 | 24 | 8% | 22 (92%) | 15% of 26 | -4% |
| 5 | 20 | 20% | 16 (80%) | 7% of 30 | +8% |
| 6 | 16 | 12% | 14 (88%) | 12% of 33 | +1% |
| 7 | 31 | 19% | 25 (81%) | 0% of 16 | +7% |
| 8 | 26 | 23% | 20 (77%) | 0% of 24 | +11% |
| 9 | 18 | 11% | 16 (89%) | 12% of 32 | -1% |
| 10 | 27 | 22% | 21 (78%) | 0% of 23 | +10% |
| 11 | 50 | 12% | 44 (88%) | n/a | +0% |
| 12 | 50 | 12% | 44 (88%) | n/a | +0% |
| 13 | 50 | 12% | 44 (88%) | n/a | +0% |
| 14 | 50 | 12% | 44 (88%) | n/a | +0% |
| 15 | 50 | 12% | 44 (88%) | n/a | +0% |
| 16 | 27 | 11% | 24 (89%) | 13% of 23 | -1% |
| 18 | 50 | 12% | 44 (88%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 2.7 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
