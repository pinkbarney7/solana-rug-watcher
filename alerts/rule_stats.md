# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 09:14 UTC. Labeled coins: 13 (1 dead/pulled, 12 still alive). Base dead rate 7.7%. Forward 24h samples so far: 12.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 13 | 8% | 12 (92%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 9% of 11 | -8% |
| 3 | 8 | 0% | 8 (100%) | 20% of 5 | -8% |
| 5 | 5 | 20% | 4 (80%) | 0% of 8 | +12% |
| 6 | 4 | 0% | 4 (100%) | 11% of 9 | -8% |
| 7 | 8 | 12% | 7 (88%) | 0% of 5 | +5% |
| 8 | 7 | 14% | 6 (86%) | 0% of 6 | +7% |
| 9 | 4 | 0% | 4 (100%) | 11% of 9 | -8% |
| 10 | 3 | 33% | 2 (67%) | 0% of 10 | +26% |
| 11 | 13 | 8% | 12 (92%) | n/a | +0% |
| 12 | 13 | 8% | 12 (92%) | n/a | +0% |
| 13 | 13 | 8% | 12 (92%) | n/a | +0% |
| 14 | 13 | 8% | 12 (92%) | n/a | +0% |
| 15 | 13 | 8% | 12 (92%) | n/a | +0% |
| 16 | 7 | 0% | 7 (100%) | 17% of 6 | -8% |
| 18 | 13 | 8% | 12 (92%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
