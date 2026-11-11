# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-11 10:48 UTC. Labeled coins: 43 (5 dead/pulled, 38 still alive). Base dead rate 11.6%. Forward 24h samples so far: 27.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 36 | 11% | 32 (89%) | 0% of 6 | -1% |
| 2 | 7 | 0% | 7 (100%) | 14% of 36 | -12% |
| 3 | 19 | 11% | 17 (89%) | 12% of 24 | -1% |
| 5 | 14 | 21% | 11 (79%) | 7% of 29 | +10% |
| 6 | 16 | 12% | 14 (88%) | 12% of 26 | +1% |
| 7 | 28 | 18% | 23 (82%) | 0% of 12 | +6% |
| 8 | 20 | 25% | 15 (75%) | 0% of 23 | +13% |
| 9 | 13 | 15% | 11 (85%) | 10% of 30 | +4% |
| 10 | 20 | 25% | 15 (75%) | 0% of 23 | +13% |
| 11 | 43 | 12% | 38 (88%) | n/a | +0% |
| 12 | 43 | 12% | 38 (88%) | n/a | +0% |
| 13 | 43 | 12% | 38 (88%) | n/a | +0% |
| 14 | 43 | 12% | 38 (88%) | n/a | +0% |
| 15 | 43 | 12% | 38 (88%) | n/a | +0% |
| 16 | 24 | 8% | 22 (92%) | 16% of 19 | -3% |
| 18 | 43 | 12% | 38 (88%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 2.1 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
