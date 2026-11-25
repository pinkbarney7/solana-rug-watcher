# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 10:38 UTC. Labeled coins: 198 (82 dead/pulled, 116 still alive). Base dead rate 41.4%. Forward 24h samples so far: 127.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 181 | 45% | 100 (55%) | 0% of 15 | +3% |
| 2 | 13 | 0% | 13 (100%) | 44% of 185 | -41% |
| 3 | 82 | 32% | 56 (68%) | 48% of 116 | -10% |
| 5 | 135 | 53% | 63 (47%) | 16% of 63 | +12% |
| 6 | 32 | 9% | 29 (91%) | 48% of 165 | -32% |
| 7 | 129 | 48% | 67 (52%) | 31% of 62 | +7% |
| 8 | 152 | 53% | 71 (47%) | 2% of 46 | +12% |
| 9 | 93 | 32% | 63 (68%) | 50% of 105 | -9% |
| 10 | 107 | 66% | 36 (34%) | 12% of 91 | +25% |
| 11 | 198 | 41% | 116 (59%) | n/a | +0% |
| 12 | 198 | 41% | 116 (59%) | n/a | +0% |
| 13 | 198 | 41% | 116 (59%) | n/a | +0% |
| 14 | 198 | 41% | 116 (59%) | n/a | +0% |
| 15 | 198 | 41% | 116 (59%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 156 | -6% |
| 18 | 198 | 41% | 116 (59%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=82)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 41%, n=32)
- check #9: lower weight: flagged coins die no more often than average (precision 32% vs base 41%, n=93)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 41%, n=107)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 41%, n=42)
