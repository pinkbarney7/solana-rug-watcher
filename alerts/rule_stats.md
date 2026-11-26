# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 00:38 UTC. Labeled coins: 211 (90 dead/pulled, 121 still alive). Base dead rate 42.7%. Forward 24h samples so far: 138.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 194 | 46% | 105 (54%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 46% of 196 | -43% |
| 3 | 82 | 37% | 52 (63%) | 47% of 129 | -6% |
| 5 | 139 | 58% | 59 (42%) | 14% of 72 | +15% |
| 6 | 33 | 9% | 30 (91%) | 49% of 177 | -34% |
| 7 | 135 | 50% | 68 (50%) | 35% of 62 | +7% |
| 8 | 159 | 56% | 70 (44%) | 2% of 52 | +13% |
| 9 | 93 | 37% | 59 (63%) | 47% of 118 | -6% |
| 10 | 118 | 65% | 41 (35%) | 14% of 93 | +23% |
| 11 | 211 | 43% | 121 (57%) | n/a | +0% |
| 12 | 211 | 43% | 121 (57%) | n/a | +0% |
| 13 | 211 | 43% | 121 (57%) | n/a | +0% |
| 14 | 211 | 43% | 121 (57%) | n/a | +0% |
| 15 | 211 | 43% | 121 (57%) | n/a | +0% |
| 16 | 44 | 34% | 29 (66%) | 45% of 167 | -9% |
| 18 | 211 | 43% | 121 (57%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 43%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 43%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 43%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 43%, n=118)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 43%, n=44)
