# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-14 02:46 UTC. Labeled coins: 65 (9 dead/pulled, 56 still alive). Base dead rate 13.8%. Forward 24h samples so far: 39.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 55 | 15% | 47 (85%) | 0% of 8 | +1% |
| 2 | 7 | 0% | 7 (100%) | 16% of 58 | -14% |
| 3 | 31 | 10% | 28 (90%) | 18% of 34 | -4% |
| 5 | 28 | 21% | 22 (79%) | 8% of 37 | +8% |
| 6 | 19 | 16% | 16 (84%) | 13% of 45 | +2% |
| 7 | 41 | 20% | 33 (80%) | 5% of 20 | +6% |
| 8 | 39 | 23% | 30 (77%) | 0% of 26 | +9% |
| 9 | 28 | 14% | 24 (86%) | 14% of 37 | +0% |
| 10 | 33 | 24% | 25 (76%) | 3% of 32 | +10% |
| 11 | 65 | 14% | 56 (86%) | n/a | +0% |
| 12 | 65 | 14% | 56 (86%) | n/a | +0% |
| 13 | 65 | 14% | 56 (86%) | n/a | +0% |
| 14 | 65 | 14% | 56 (86%) | n/a | +0% |
| 15 | 65 | 14% | 56 (86%) | n/a | +0% |
| 16 | 34 | 18% | 28 (82%) | 10% of 31 | +4% |
| 18 | 65 | 14% | 56 (86%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 4.8 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 10% vs base 14%, n=31)
