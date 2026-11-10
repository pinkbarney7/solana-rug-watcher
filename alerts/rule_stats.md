# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 09:31 UTC. Labeled coins: 15 (2 dead/pulled, 13 still alive). Base dead rate 13.3%. Forward 24h samples so far: 13.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 15 | 13% | 13 (87%) | n/a | +0% |
| 2 | 2 | 0% | 2 (100%) | 15% of 13 | -13% |
| 3 | 8 | 0% | 8 (100%) | 29% of 7 | -13% |
| 5 | 6 | 33% | 4 (67%) | 0% of 9 | +20% |
| 6 | 4 | 0% | 4 (100%) | 18% of 11 | -13% |
| 7 | 9 | 22% | 7 (78%) | 0% of 5 | +9% |
| 8 | 8 | 25% | 6 (75%) | 0% of 7 | +12% |
| 9 | 4 | 0% | 4 (100%) | 18% of 11 | -13% |
| 10 | 5 | 40% | 3 (60%) | 0% of 10 | +27% |
| 11 | 15 | 13% | 13 (87%) | n/a | +0% |
| 12 | 15 | 13% | 13 (87%) | n/a | +0% |
| 13 | 15 | 13% | 13 (87%) | n/a | +0% |
| 14 | 15 | 13% | 13 (87%) | n/a | +0% |
| 15 | 15 | 13% | 13 (87%) | n/a | +0% |
| 16 | 9 | 11% | 8 (89%) | 17% of 6 | -2% |
| 18 | 15 | 13% | 13 (87%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
