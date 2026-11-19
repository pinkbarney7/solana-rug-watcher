# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-19 08:14 UTC. Labeled coins: 127 (44 dead/pulled, 83 still alive). Base dead rate 34.6%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 112 | 38% | 69 (62%) | 0% of 13 | +4% |
| 2 | 10 | 0% | 10 (100%) | 38% of 117 | -35% |
| 3 | 51 | 31% | 35 (69%) | 37% of 76 | -3% |
| 5 | 78 | 47% | 41 (53%) | 14% of 49 | +13% |
| 6 | 23 | 13% | 20 (87%) | 40% of 103 | -22% |
| 7 | 85 | 36% | 54 (64%) | 33% of 36 | +2% |
| 8 | 92 | 48% | 48 (52%) | 0% of 35 | +13% |
| 9 | 58 | 31% | 40 (69%) | 38% of 69 | -4% |
| 10 | 68 | 57% | 29 (43%) | 8% of 59 | +23% |
| 11 | 127 | 35% | 83 (65%) | n/a | +0% |
| 12 | 127 | 35% | 83 (65%) | n/a | +0% |
| 13 | 127 | 35% | 83 (65%) | n/a | +0% |
| 14 | 127 | 35% | 83 (65%) | n/a | +0% |
| 15 | 127 | 35% | 83 (65%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 36% of 87 | -2% |
| 18 | 127 | 35% | 83 (65%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 31% vs base 35%, n=51)
- check #7: lower weight: flagged coins die no more often than average (precision 36% vs base 35%, n=85)
- check #9: lower weight: flagged coins die no more often than average (precision 31% vs base 35%, n=58)
- check #10: consider treating WARN like FAIL: strong lift (precision 57% vs base 35%, n=68)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 35%, n=40)
