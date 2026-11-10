# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-10 13:20 UTC. Labeled coins: 26 (4 dead/pulled, 22 still alive). Base dead rate 15.4%. Forward 24h samples so far: 22.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 21 | 14% | 18 (86%) | 0% of 4 | -1% |
| 2 | 4 | 0% | 4 (100%) | 18% of 22 | -15% |
| 3 | 12 | 8% | 11 (92%) | 21% of 14 | -7% |
| 5 | 7 | 43% | 4 (57%) | 5% of 19 | +27% |
| 6 | 9 | 11% | 8 (89%) | 18% of 17 | -4% |
| 7 | 18 | 22% | 14 (78%) | 0% of 6 | +7% |
| 8 | 14 | 29% | 10 (71%) | 0% of 12 | +13% |
| 9 | 7 | 14% | 6 (86%) | 16% of 19 | -1% |
| 10 | 11 | 36% | 7 (64%) | 0% of 15 | +21% |
| 11 | 26 | 15% | 22 (85%) | n/a | +0% |
| 12 | 26 | 15% | 22 (85%) | n/a | +0% |
| 13 | 26 | 15% | 22 (85%) | n/a | +0% |
| 14 | 26 | 15% | 22 (85%) | n/a | +0% |
| 15 | 26 | 15% | 22 (85%) | n/a | +0% |
| 16 | 14 | 7% | 13 (93%) | 25% of 12 | -8% |
| 18 | 26 | 15% | 22 (85%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 1.2 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
