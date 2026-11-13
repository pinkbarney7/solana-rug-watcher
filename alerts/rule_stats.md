# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-13 17:33 UTC. Labeled coins: 63 (8 dead/pulled, 55 still alive). Base dead rate 12.7%. Forward 24h samples so far: 37.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 53 | 13% | 46 (87%) | 0% of 8 | +1% |
| 2 | 7 | 0% | 7 (100%) | 14% of 56 | -13% |
| 3 | 31 | 10% | 28 (90%) | 16% of 32 | -3% |
| 5 | 27 | 19% | 22 (81%) | 8% of 36 | +6% |
| 6 | 19 | 16% | 16 (84%) | 12% of 43 | +3% |
| 7 | 39 | 18% | 32 (82%) | 5% of 20 | +5% |
| 8 | 38 | 21% | 30 (79%) | 0% of 25 | +8% |
| 9 | 28 | 14% | 24 (86%) | 11% of 35 | +2% |
| 10 | 32 | 22% | 25 (78%) | 3% of 31 | +9% |
| 11 | 63 | 13% | 55 (87%) | n/a | +0% |
| 12 | 63 | 13% | 55 (87%) | n/a | +0% |
| 13 | 63 | 13% | 55 (87%) | n/a | +0% |
| 14 | 63 | 13% | 55 (87%) | n/a | +0% |
| 15 | 63 | 13% | 55 (87%) | n/a | +0% |
| 16 | 33 | 15% | 28 (85%) | 10% of 30 | +2% |
| 18 | 63 | 13% | 55 (87%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 4.4 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 10% vs base 13%, n=31)
- check #16: lower weight: flagged coins die no more often than average (precision 15% vs base 13%, n=33)
