# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 18:53 UTC. Labeled coins: 211 (88 dead/pulled, 123 still alive). Base dead rate 41.7%. Forward 24h samples so far: 138.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 194 | 45% | 107 (55%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 45% of 196 | -42% |
| 3 | 82 | 34% | 54 (66%) | 47% of 129 | -8% |
| 5 | 139 | 56% | 61 (44%) | 14% of 72 | +14% |
| 6 | 33 | 9% | 30 (91%) | 48% of 177 | -33% |
| 7 | 135 | 50% | 68 (50%) | 32% of 62 | +8% |
| 8 | 159 | 55% | 72 (45%) | 2% of 52 | +13% |
| 9 | 93 | 34% | 61 (66%) | 47% of 118 | -7% |
| 10 | 118 | 65% | 41 (35%) | 12% of 93 | +24% |
| 11 | 211 | 42% | 123 (58%) | n/a | +0% |
| 12 | 211 | 42% | 123 (58%) | n/a | +0% |
| 13 | 211 | 42% | 123 (58%) | n/a | +0% |
| 14 | 211 | 42% | 123 (58%) | n/a | +0% |
| 15 | 211 | 42% | 123 (58%) | n/a | +0% |
| 16 | 44 | 34% | 29 (66%) | 44% of 167 | -8% |
| 18 | 211 | 42% | 123 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 42%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 42%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 34% vs base 42%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 42%, n=118)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 42%, n=44)
