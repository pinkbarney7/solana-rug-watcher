# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 07:24 UTC. Labeled coins: 180 (73 dead/pulled, 107 still alive). Base dead rate 40.6%. Forward 24h samples so far: 103.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 164 | 44% | 92 (56%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 43% of 168 | -41% |
| 3 | 76 | 34% | 50 (66%) | 45% of 104 | -6% |
| 5 | 121 | 52% | 58 (48%) | 17% of 59 | +12% |
| 6 | 29 | 10% | 26 (90%) | 47% of 150 | -30% |
| 7 | 115 | 46% | 62 (54%) | 33% of 58 | +6% |
| 8 | 135 | 53% | 63 (47%) | 2% of 45 | +13% |
| 9 | 87 | 33% | 58 (67%) | 47% of 93 | -7% |
| 10 | 94 | 66% | 32 (34%) | 13% of 86 | +25% |
| 11 | 180 | 41% | 107 (59%) | n/a | +0% |
| 12 | 180 | 41% | 107 (59%) | n/a | +0% |
| 13 | 180 | 41% | 107 (59%) | n/a | +0% |
| 14 | 180 | 41% | 107 (59%) | n/a | +0% |
| 15 | 180 | 41% | 107 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 138 | -5% |
| 18 | 180 | 41% | 107 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=76)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=87)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=94)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
