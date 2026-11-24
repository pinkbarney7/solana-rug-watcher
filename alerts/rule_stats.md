# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 11:10 UTC. Labeled coins: 183 (75 dead/pulled, 108 still alive). Base dead rate 41.0%. Forward 24h samples so far: 108.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 167 | 44% | 93 (56%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 171 | -41% |
| 3 | 76 | 34% | 50 (66%) | 46% of 107 | -7% |
| 5 | 123 | 53% | 58 (47%) | 17% of 60 | +12% |
| 6 | 29 | 10% | 26 (90%) | 47% of 153 | -31% |
| 7 | 118 | 47% | 63 (53%) | 33% of 58 | +6% |
| 8 | 138 | 54% | 64 (46%) | 2% of 45 | +13% |
| 9 | 87 | 33% | 58 (67%) | 48% of 96 | -8% |
| 10 | 97 | 66% | 33 (34%) | 13% of 86 | +25% |
| 11 | 183 | 41% | 108 (59%) | n/a | +0% |
| 12 | 183 | 41% | 108 (59%) | n/a | +0% |
| 13 | 183 | 41% | 108 (59%) | n/a | +0% |
| 14 | 183 | 41% | 108 (59%) | n/a | +0% |
| 15 | 183 | 41% | 108 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 141 | -5% |
| 18 | 183 | 41% | 108 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=76)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=87)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=97)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
