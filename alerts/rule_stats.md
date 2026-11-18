# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-18 18:59 UTC. Labeled coins: 124 (42 dead/pulled, 82 still alive). Base dead rate 33.9%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 109 | 38% | 68 (62%) | 0% of 13 | +4% |
| 2 | 8 | 0% | 8 (100%) | 36% of 116 | -34% |
| 3 | 50 | 30% | 35 (70%) | 36% of 74 | -4% |
| 5 | 76 | 46% | 41 (54%) | 15% of 48 | +12% |
| 6 | 22 | 14% | 19 (86%) | 39% of 101 | -20% |
| 7 | 83 | 37% | 52 (63%) | 31% of 35 | +3% |
| 8 | 90 | 47% | 48 (53%) | 0% of 34 | +13% |
| 9 | 57 | 30% | 40 (70%) | 37% of 67 | -4% |
| 10 | 66 | 58% | 28 (42%) | 7% of 58 | +24% |
| 11 | 124 | 34% | 82 (66%) | n/a | +0% |
| 12 | 124 | 34% | 82 (66%) | n/a | +0% |
| 13 | 124 | 34% | 82 (66%) | n/a | +0% |
| 14 | 124 | 34% | 82 (66%) | n/a | +0% |
| 15 | 124 | 34% | 82 (66%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 35% of 84 | -1% |
| 18 | 124 | 34% | 82 (66%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 34%, n=50)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 34%, n=57)
- check #10: consider treating WARN like FAIL: strong lift (precision 58% vs base 34%, n=66)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 34%, n=40)
