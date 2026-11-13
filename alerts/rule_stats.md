# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-13 10:00 UTC. Labeled coins: 61 (7 dead/pulled, 54 still alive). Base dead rate 11.5%. Forward 24h samples so far: 35.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 51 | 12% | 45 (88%) | 0% of 8 | +0% |
| 2 | 7 | 0% | 7 (100%) | 13% of 54 | -11% |
| 3 | 30 | 10% | 27 (90%) | 13% of 31 | -1% |
| 5 | 26 | 15% | 22 (85%) | 9% of 35 | +4% |
| 6 | 19 | 16% | 16 (84%) | 10% of 41 | +4% |
| 7 | 38 | 18% | 31 (82%) | 0% of 19 | +7% |
| 8 | 36 | 19% | 29 (81%) | 0% of 25 | +8% |
| 9 | 26 | 12% | 23 (88%) | 11% of 35 | +0% |
| 10 | 32 | 22% | 25 (78%) | 0% of 29 | +10% |
| 11 | 61 | 11% | 54 (89%) | n/a | +0% |
| 12 | 61 | 11% | 54 (89%) | n/a | +0% |
| 13 | 61 | 11% | 54 (89%) | n/a | +0% |
| 14 | 61 | 11% | 54 (89%) | n/a | +0% |
| 15 | 61 | 11% | 54 (89%) | n/a | +0% |
| 16 | 32 | 12% | 28 (88%) | 10% of 29 | +1% |
| 18 | 61 | 11% | 54 (89%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 4.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 10% vs base 12%, n=30)
