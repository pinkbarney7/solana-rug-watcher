# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-18 10:29 UTC. Labeled coins: 123 (40 dead/pulled, 83 still alive). Base dead rate 32.5%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 108 | 36% | 69 (64%) | 0% of 13 | +4% |
| 2 | 8 | 0% | 8 (100%) | 35% of 115 | -33% |
| 3 | 50 | 28% | 36 (72%) | 36% of 73 | -5% |
| 5 | 75 | 44% | 42 (56%) | 15% of 48 | +11% |
| 6 | 22 | 14% | 19 (86%) | 37% of 100 | -19% |
| 7 | 82 | 37% | 52 (63%) | 29% of 35 | +4% |
| 8 | 89 | 45% | 49 (55%) | 0% of 34 | +12% |
| 9 | 57 | 28% | 41 (72%) | 36% of 66 | -4% |
| 10 | 65 | 57% | 28 (43%) | 5% of 58 | +24% |
| 11 | 123 | 33% | 83 (67%) | n/a | +0% |
| 12 | 123 | 33% | 83 (67%) | n/a | +0% |
| 13 | 123 | 33% | 83 (67%) | n/a | +0% |
| 14 | 123 | 33% | 83 (67%) | n/a | +0% |
| 15 | 123 | 33% | 83 (67%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 33% of 83 | -0% |
| 18 | 123 | 33% | 83 (67%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 28% vs base 32%, n=50)
- check #9: lower weight: flagged coins die no more often than average (precision 28% vs base 32%, n=57)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 32%, n=65)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 32%, n=40)
