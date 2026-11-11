# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-11 03:08 UTC. Labeled coins: 31 (4 dead/pulled, 27 still alive). Base dead rate 12.9%. Forward 24h samples so far: 22.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 26 | 12% | 23 (88%) | 0% of 4 | -1% |
| 2 | 5 | 0% | 5 (100%) | 15% of 26 | -13% |
| 3 | 13 | 8% | 12 (92%) | 17% of 18 | -5% |
| 5 | 10 | 30% | 7 (70%) | 5% of 21 | +17% |
| 6 | 12 | 8% | 11 (92%) | 16% of 19 | -5% |
| 7 | 21 | 19% | 17 (81%) | 0% of 8 | +6% |
| 8 | 16 | 25% | 12 (75%) | 0% of 15 | +12% |
| 9 | 8 | 12% | 7 (88%) | 13% of 23 | -0% |
| 10 | 15 | 27% | 11 (73%) | 0% of 16 | +14% |
| 11 | 31 | 13% | 27 (87%) | n/a | +0% |
| 12 | 31 | 13% | 27 (87%) | n/a | +0% |
| 13 | 31 | 13% | 27 (87%) | n/a | +0% |
| 14 | 31 | 13% | 27 (87%) | n/a | +0% |
| 15 | 31 | 13% | 27 (87%) | n/a | +0% |
| 16 | 18 | 6% | 17 (94%) | 23% of 13 | -7% |
| 18 | 31 | 13% | 27 (87%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.8 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
