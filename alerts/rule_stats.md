# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-22 23:24 UTC. Labeled coins: 157 (54 dead/pulled, 103 still alive). Base dead rate 34.4%. Forward 24h samples so far: 88.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 142 | 37% | 89 (63%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 37% of 145 | -34% |
| 3 | 69 | 30% | 48 (70%) | 38% of 88 | -4% |
| 5 | 101 | 45% | 56 (55%) | 16% of 56 | +10% |
| 6 | 28 | 11% | 25 (89%) | 40% of 128 | -24% |
| 7 | 99 | 39% | 60 (61%) | 27% of 51 | +5% |
| 8 | 114 | 46% | 61 (54%) | 2% of 43 | +12% |
| 9 | 79 | 29% | 56 (71%) | 40% of 78 | -5% |
| 10 | 81 | 58% | 34 (42%) | 9% of 76 | +24% |
| 11 | 157 | 34% | 103 (66%) | n/a | +0% |
| 12 | 157 | 34% | 103 (66%) | n/a | +0% |
| 13 | 157 | 34% | 103 (66%) | n/a | +0% |
| 14 | 157 | 34% | 103 (66%) | n/a | +0% |
| 15 | 157 | 34% | 103 (66%) | n/a | +0% |
| 16 | 41 | 34% | 27 (66%) | 34% of 116 | -0% |
| 18 | 157 | 34% | 103 (66%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 34%, n=69)
- check #9: lower weight: flagged coins die no more often than average (precision 29% vs base 34%, n=79)
- check #10: consider treating WARN like FAIL: strong lift (precision 58% vs base 34%, n=81)
- check #16: lower weight: flagged coins die no more often than average (precision 34% vs base 34%, n=41)
