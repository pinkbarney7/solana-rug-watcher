# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 11:54 UTC. Labeled coins: 185 (76 dead/pulled, 109 still alive). Base dead rate 41.1%. Forward 24h samples so far: 111.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 169 | 44% | 94 (56%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 173 | -41% |
| 3 | 77 | 34% | 51 (66%) | 46% of 108 | -7% |
| 5 | 125 | 53% | 59 (47%) | 17% of 60 | +12% |
| 6 | 29 | 10% | 26 (90%) | 47% of 155 | -31% |
| 7 | 119 | 47% | 63 (53%) | 32% of 59 | +6% |
| 8 | 140 | 54% | 65 (46%) | 2% of 45 | +12% |
| 9 | 88 | 33% | 59 (67%) | 48% of 97 | -8% |
| 10 | 98 | 66% | 33 (34%) | 13% of 87 | +25% |
| 11 | 185 | 41% | 109 (59%) | n/a | +0% |
| 12 | 185 | 41% | 109 (59%) | n/a | +0% |
| 13 | 185 | 41% | 109 (59%) | n/a | +0% |
| 14 | 185 | 41% | 109 (59%) | n/a | +0% |
| 15 | 185 | 41% | 109 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 143 | -5% |
| 18 | 185 | 41% | 109 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=77)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=88)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=98)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
