# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 14:05 UTC. Labeled coins: 189 (80 dead/pulled, 109 still alive). Base dead rate 42.3%. Forward 24h samples so far: 112.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 173 | 46% | 94 (54%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 45% of 177 | -42% |
| 3 | 77 | 34% | 51 (66%) | 48% of 112 | -9% |
| 5 | 129 | 54% | 59 (46%) | 17% of 60 | +12% |
| 6 | 29 | 10% | 26 (90%) | 48% of 159 | -32% |
| 7 | 123 | 49% | 63 (51%) | 32% of 59 | +6% |
| 8 | 144 | 55% | 65 (45%) | 2% of 45 | +13% |
| 9 | 88 | 33% | 59 (67%) | 50% of 101 | -9% |
| 10 | 102 | 68% | 33 (32%) | 13% of 87 | +25% |
| 11 | 189 | 42% | 109 (58%) | n/a | +0% |
| 12 | 189 | 42% | 109 (58%) | n/a | +0% |
| 13 | 189 | 42% | 109 (58%) | n/a | +0% |
| 14 | 189 | 42% | 109 (58%) | n/a | +0% |
| 15 | 189 | 42% | 109 (58%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 44% of 147 | -7% |
| 18 | 189 | 42% | 109 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 42%, n=77)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 42%, n=88)
- check #10: consider treating WARN like FAIL: strong lift (precision 68% vs base 42%, n=102)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=42)
