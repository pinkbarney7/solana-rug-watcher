# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 05:12 UTC. Labeled coins: 212 (90 dead/pulled, 122 still alive). Base dead rate 42.5%. Forward 24h samples so far: 139.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 195 | 46% | 106 (54%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 46% of 197 | -42% |
| 3 | 82 | 37% | 52 (63%) | 46% of 130 | -6% |
| 5 | 139 | 58% | 59 (42%) | 14% of 73 | +15% |
| 6 | 33 | 9% | 30 (91%) | 49% of 178 | -33% |
| 7 | 136 | 49% | 69 (51%) | 35% of 62 | +7% |
| 8 | 159 | 56% | 70 (44%) | 2% of 53 | +14% |
| 9 | 93 | 37% | 59 (63%) | 47% of 119 | -6% |
| 10 | 118 | 65% | 41 (35%) | 14% of 94 | +23% |
| 11 | 212 | 42% | 122 (58%) | n/a | +0% |
| 12 | 212 | 42% | 122 (58%) | n/a | +0% |
| 13 | 212 | 42% | 122 (58%) | n/a | +0% |
| 14 | 212 | 42% | 122 (58%) | n/a | +0% |
| 15 | 212 | 42% | 122 (58%) | n/a | +0% |
| 16 | 44 | 34% | 29 (66%) | 45% of 168 | -8% |
| 18 | 212 | 42% | 122 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 42%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 42%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 42%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 42%, n=118)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 42%, n=44)
