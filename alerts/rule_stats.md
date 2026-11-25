# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 11:43 UTC. Labeled coins: 208 (85 dead/pulled, 123 still alive). Base dead rate 40.9%. Forward 24h samples so far: 135.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 191 | 44% | 107 (56%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 44% of 193 | -41% |
| 3 | 82 | 33% | 55 (67%) | 46% of 126 | -8% |
| 5 | 137 | 55% | 62 (45%) | 14% of 71 | +14% |
| 6 | 33 | 9% | 30 (91%) | 47% of 174 | -32% |
| 7 | 132 | 48% | 68 (52%) | 32% of 62 | +8% |
| 8 | 156 | 54% | 72 (46%) | 2% of 52 | +13% |
| 9 | 93 | 33% | 62 (67%) | 47% of 115 | -8% |
| 10 | 116 | 64% | 42 (36%) | 12% of 92 | +23% |
| 11 | 208 | 41% | 123 (59%) | n/a | +0% |
| 12 | 208 | 41% | 123 (59%) | n/a | +0% |
| 13 | 208 | 41% | 123 (59%) | n/a | +0% |
| 14 | 208 | 41% | 123 (59%) | n/a | +0% |
| 15 | 208 | 41% | 123 (59%) | n/a | +0% |
| 16 | 44 | 34% | 29 (66%) | 43% of 164 | -7% |
| 18 | 208 | 41% | 123 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 41%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 41%, n=116)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=44)
