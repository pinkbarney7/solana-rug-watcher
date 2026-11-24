# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-24 07:59 UTC. Labeled coins: 181 (74 dead/pulled, 107 still alive). Base dead rate 40.9%. Forward 24h samples so far: 104.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 165 | 44% | 92 (56%) | 0% of 14 | +3% |
| 2 | 12 | 0% | 12 (100%) | 44% of 169 | -41% |
| 3 | 76 | 34% | 50 (66%) | 46% of 105 | -7% |
| 5 | 122 | 52% | 58 (48%) | 17% of 59 | +12% |
| 6 | 29 | 10% | 26 (90%) | 47% of 151 | -31% |
| 7 | 116 | 47% | 62 (53%) | 33% of 58 | +6% |
| 8 | 136 | 54% | 63 (46%) | 2% of 45 | +13% |
| 9 | 87 | 33% | 58 (67%) | 48% of 94 | -8% |
| 10 | 95 | 66% | 32 (34%) | 13% of 86 | +25% |
| 11 | 181 | 41% | 107 (59%) | n/a | +0% |
| 12 | 181 | 41% | 107 (59%) | n/a | +0% |
| 13 | 181 | 41% | 107 (59%) | n/a | +0% |
| 14 | 181 | 41% | 107 (59%) | n/a | +0% |
| 15 | 181 | 41% | 107 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 42% of 139 | -5% |
| 18 | 181 | 41% | 107 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 34% vs base 41%, n=76)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 41%, n=87)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=95)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
