# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 09:12 UTC. Labeled coins: 258 (124 dead/pulled, 134 still alive). Base dead rate 48.1%. Forward 24h samples so far: 184.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 238 | 50% | 118 (50%) | 17% of 18 | +2% |
| 2 | 16 | 0% | 16 (100%) | 51% of 242 | -48% |
| 3 | 92 | 38% | 57 (62%) | 54% of 166 | -10% |
| 5 | 178 | 63% | 66 (37%) | 15% of 80 | +15% |
| 6 | 36 | 8% | 33 (92%) | 55% of 221 | -40% |
| 7 | 174 | 56% | 77 (44%) | 38% of 69 | +8% |
| 8 | 200 | 61% | 78 (39%) | 3% of 58 | +13% |
| 9 | 106 | 37% | 67 (63%) | 56% of 152 | -11% |
| 10 | 151 | 71% | 44 (29%) | 16% of 107 | +23% |
| 11 | 258 | 48% | 134 (52%) | n/a | +0% |
| 12 | 258 | 48% | 134 (52%) | n/a | +0% |
| 13 | 258 | 48% | 134 (52%) | n/a | +0% |
| 14 | 258 | 48% | 134 (52%) | n/a | +0% |
| 15 | 258 | 48% | 134 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 212 | -13% |
| 18 | 258 | 48% | 134 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 48%, n=92)
- check #6: lower weight: flagged coins die no more often than average (precision 8% vs base 48%, n=36)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=151)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
