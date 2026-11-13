# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-13 22:49 UTC. Labeled coins: 64 (8 dead/pulled, 56 still alive). Base dead rate 12.5%. Forward 24h samples so far: 38.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 54 | 13% | 47 (87%) | 0% of 8 | +0% |
| 2 | 7 | 0% | 7 (100%) | 14% of 57 | -12% |
| 3 | 31 | 10% | 28 (90%) | 15% of 33 | -3% |
| 5 | 27 | 19% | 22 (81%) | 8% of 37 | +6% |
| 6 | 19 | 16% | 16 (84%) | 11% of 44 | +3% |
| 7 | 40 | 18% | 33 (82%) | 5% of 20 | +5% |
| 8 | 38 | 21% | 30 (79%) | 0% of 26 | +9% |
| 9 | 28 | 14% | 24 (86%) | 11% of 36 | +2% |
| 10 | 32 | 22% | 25 (78%) | 3% of 32 | +9% |
| 11 | 64 | 12% | 56 (88%) | n/a | +0% |
| 12 | 64 | 12% | 56 (88%) | n/a | +0% |
| 13 | 64 | 12% | 56 (88%) | n/a | +0% |
| 14 | 64 | 12% | 56 (88%) | n/a | +0% |
| 15 | 64 | 12% | 56 (88%) | n/a | +0% |
| 16 | 33 | 15% | 28 (85%) | 10% of 31 | +3% |
| 18 | 64 | 12% | 56 (88%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 4.6 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 10% vs base 12%, n=31)
- check #16: lower weight: flagged coins die no more often than average (precision 15% vs base 12%, n=33)
