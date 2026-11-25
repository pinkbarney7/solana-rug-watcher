# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-25 08:11 UTC. Labeled coins: 195 (81 dead/pulled, 114 still alive). Base dead rate 41.5%. Forward 24h samples so far: 124.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 178 | 45% | 98 (55%) | 0% of 15 | +3% |
| 2 | 13 | 0% | 13 (100%) | 45% of 182 | -42% |
| 3 | 80 | 32% | 54 (68%) | 48% of 115 | -9% |
| 5 | 132 | 54% | 61 (46%) | 16% of 63 | +12% |
| 6 | 32 | 9% | 29 (91%) | 48% of 162 | -32% |
| 7 | 128 | 48% | 67 (52%) | 32% of 60 | +6% |
| 8 | 149 | 54% | 69 (46%) | 2% of 46 | +12% |
| 9 | 91 | 33% | 61 (67%) | 49% of 104 | -9% |
| 10 | 106 | 66% | 36 (34%) | 12% of 89 | +24% |
| 11 | 195 | 42% | 114 (58%) | n/a | +0% |
| 12 | 195 | 42% | 114 (58%) | n/a | +0% |
| 13 | 195 | 42% | 114 (58%) | n/a | +0% |
| 14 | 195 | 42% | 114 (58%) | n/a | +0% |
| 15 | 195 | 42% | 114 (58%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 153 | -6% |
| 18 | 195 | 42% | 114 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 32% vs base 42%, n=80)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 42%, n=32)
- check #9: lower weight: flagged coins die no more often than average (precision 33% vs base 42%, n=91)
- check #10: consider treating WARN like FAIL: strong lift (precision 66% vs base 42%, n=106)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=42)
