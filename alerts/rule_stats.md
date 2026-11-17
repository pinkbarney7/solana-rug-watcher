# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 04:44 UTC. Labeled coins: 99 (24 dead/pulled, 75 still alive). Base dead rate 24.2%. Forward 24h samples so far: 64.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 87 | 26% | 64 (74%) | 0% of 10 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 91 | -24% |
| 3 | 44 | 16% | 37 (84%) | 31% of 55 | -8% |
| 5 | 57 | 32% | 39 (68%) | 14% of 42 | +7% |
| 6 | 22 | 14% | 19 (86%) | 28% of 76 | -11% |
| 7 | 63 | 29% | 45 (71%) | 20% of 30 | +4% |
| 8 | 68 | 35% | 44 (65%) | 0% of 31 | +11% |
| 9 | 45 | 13% | 39 (87%) | 33% of 54 | -11% |
| 10 | 51 | 41% | 30 (59%) | 6% of 48 | +17% |
| 11 | 99 | 24% | 75 (76%) | n/a | +0% |
| 12 | 99 | 24% | 75 (76%) | n/a | +0% |
| 13 | 99 | 24% | 75 (76%) | n/a | +0% |
| 14 | 99 | 24% | 75 (76%) | n/a | +0% |
| 15 | 99 | 24% | 75 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 23% of 61 | +2% |
| 18 | 99 | 24% | 75 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 24%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 13% vs base 24%, n=45)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
