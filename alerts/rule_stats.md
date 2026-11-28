# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-28 08:11 UTC. Labeled coins: 257 (123 dead/pulled, 134 still alive). Base dead rate 47.9%. Forward 24h samples so far: 180.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 238 | 50% | 118 (50%) | 12% of 17 | +3% |
| 2 | 16 | 0% | 16 (100%) | 51% of 241 | -48% |
| 3 | 91 | 37% | 57 (63%) | 54% of 166 | -10% |
| 5 | 178 | 63% | 66 (37%) | 14% of 79 | +15% |
| 6 | 35 | 9% | 32 (91%) | 54% of 221 | -39% |
| 7 | 173 | 56% | 76 (44%) | 36% of 69 | +8% |
| 8 | 199 | 61% | 77 (39%) | 2% of 58 | +13% |
| 9 | 106 | 37% | 67 (63%) | 56% of 151 | -11% |
| 10 | 151 | 71% | 44 (29%) | 15% of 106 | +23% |
| 11 | 257 | 48% | 134 (52%) | n/a | +0% |
| 12 | 257 | 48% | 134 (52%) | n/a | +0% |
| 13 | 257 | 48% | 134 (52%) | n/a | +0% |
| 14 | 257 | 48% | 134 (52%) | n/a | +0% |
| 15 | 257 | 48% | 134 (52%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 51% of 211 | -13% |
| 18 | 257 | 48% | 134 (52%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=91)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 48%, n=35)
- check #9: lower weight: flagged coins die no more often than average (precision 37% vs base 48%, n=106)
- check #10: consider treating WARN like FAIL: strong lift (precision 71% vs base 48%, n=151)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 48%, n=46)
