# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 12:23 UTC. Labeled coins: 186 (77 dead/pulled, 109 still alive). Base dead rate 41.4%. Forward 24h samples so far: 112.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 170 | 45% | 94 (55%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 174 | -41% |
| 3 | 77 | 34% | 51 (66%) | 47% of 109 | -8% |
| 5 | 126 | 53% | 59 (47%) | 17% of 60 | +12% |
| 6 | 29 | 10% | 26 (90%) | 47% of 156 | -31% |
| 7 | 120 | 48% | 63 (52%) | 32% of 59 | +6% |
| 8 | 141 | 54% | 65 (46%) | 2% of 45 | +13% |
| 9 | 88 | 33% | 59 (67%) | 49% of 98 | -8% |
| 10 | 99 | 67% | 33 (33%) | 13% of 87 | +25% |
| 11 | 186 | 41% | 109 (59%) | n/a | +0% |
| 12 | 186 | 41% | 109 (59%) | n/a | +0% |
| 13 | 186 | 41% | 109 (59%) | n/a | +0% |
| 14 | 186 | 41% | 109 (59%) | n/a | +0% |
| 15 | 186 | 41% | 109 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 144 | -6% |
| 18 | 186 | 41% | 109 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=77)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=88)
- check #10: consider treating WARN like FAIL: strong lift (precision 67% vs base 41%, n=99)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
