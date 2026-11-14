# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-14 15:59 UTC. Labeled coins: 70 (15 dead/pulled, 55 still alive). Base dead rate 21.4%. Forward 24h samples so far: 39.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 59 | 24% | 45 (76%) | 0% of 9 | +2% |
| 2 | 7 | 0% | 7 (100%) | 24% of 63 | -21% |
| 3 | 33 | 18% | 27 (82%) | 24% of 37 | -3% |
| 5 | 33 | 30% | 23 (70%) | 14% of 37 | +9% |
| 6 | 19 | 16% | 16 (84%) | 24% of 50 | -6% |
| 7 | 44 | 23% | 34 (77%) | 23% of 22 | +1% |
| 8 | 44 | 34% | 29 (66%) | 0% of 26 | +13% |
| 9 | 31 | 19% | 25 (81%) | 23% of 39 | -2% |
| 10 | 36 | 33% | 24 (67%) | 9% of 34 | +12% |
| 11 | 70 | 21% | 55 (79%) | n/a | +0% |
| 12 | 70 | 21% | 55 (79%) | n/a | +0% |
| 13 | 70 | 21% | 55 (79%) | n/a | +0% |
| 14 | 70 | 21% | 55 (79%) | n/a | +0% |
| 15 | 70 | 21% | 55 (79%) | n/a | +0% |
| 16 | 37 | 24% | 28 (76%) | 18% of 33 | +3% |
| 18 | 70 | 21% | 55 (79%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 5.3 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 21%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 19% vs base 21%, n=31)
- check #16: lower weight: flagged coins die no more often than average (precision 24% vs base 21%, n=37)
