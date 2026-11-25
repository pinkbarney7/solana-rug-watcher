# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 11:18 UTC. Labeled coins: 203 (84 dead/pulled, 119 still alive). Base dead rate 41.4%. Forward 24h samples so far: 130.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 186 | 45% | 103 (55%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 45% of 188 | -41% |
| 3 | 82 | 32% | 56 (68%) | 48% of 121 | -10% |
| 5 | 137 | 54% | 63 (46%) | 15% of 66 | +13% |
| 6 | 33 | 9% | 30 (91%) | 48% of 169 | -32% |
| 7 | 132 | 48% | 68 (52%) | 31% of 62 | +7% |
| 8 | 156 | 53% | 73 (47%) | 2% of 47 | +12% |
| 9 | 93 | 32% | 63 (68%) | 49% of 110 | -9% |
| 10 | 111 | 66% | 38 (34%) | 12% of 92 | +24% |
| 11 | 203 | 41% | 119 (59%) | n/a | +0% |
| 12 | 203 | 41% | 119 (59%) | n/a | +0% |
| 13 | 203 | 41% | 119 (59%) | n/a | +0% |
| 14 | 203 | 41% | 119 (59%) | n/a | +0% |
| 15 | 203 | 41% | 119 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 161 | -6% |
| 18 | 203 | 41% | 119 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 41%, n=33)
- check #9: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=111)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
