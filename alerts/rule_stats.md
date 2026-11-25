# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 11:31 UTC. Labeled coins: 206 (84 dead/pulled, 122 still alive). Base dead rate 40.8%. Forward 24h samples so far: 133.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 189 | 44% | 106 (56%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 44% of 191 | -41% |
| 3 | 82 | 32% | 56 (68%) | 47% of 124 | -9% |
| 5 | 137 | 54% | 63 (46%) | 14% of 69 | +13% |
| 6 | 33 | 9% | 30 (91%) | 47% of 172 | -32% |
| 7 | 132 | 48% | 68 (52%) | 31% of 62 | +8% |
| 8 | 156 | 53% | 73 (47%) | 2% of 50 | +12% |
| 9 | 93 | 32% | 63 (68%) | 48% of 113 | -9% |
| 10 | 114 | 64% | 41 (36%) | 12% of 92 | +23% |
| 11 | 206 | 41% | 122 (59%) | n/a | +0% |
| 12 | 206 | 41% | 122 (59%) | n/a | +0% |
| 13 | 206 | 41% | 122 (59%) | n/a | +0% |
| 14 | 206 | 41% | 122 (59%) | n/a | +0% |
| 15 | 206 | 41% | 122 (59%) | n/a | +0% |
| 16 | 44 | 34% | 29 (66%) | 43% of 162 | -7% |
| 18 | 206 | 41% | 122 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 41%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 41%, n=114)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=44)
