# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-23 20:12 UTC. Labeled coins: 171 (71 dead/pulled, 100 still alive). Base dead rate 41.5%. Forward 24h samples so far: 92.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 156 | 45% | 86 (55%) | 0% of 13 | +3% |
| 2 | 12 | 0% | 12 (100%) | 45% of 159 | -42% |
| 3 | 71 | 37% | 45 (63%) | 45% of 100 | -5% |
| 5 | 114 | 54% | 53 (46%) | 18% of 57 | +12% |
| 6 | 28 | 11% | 25 (89%) | 48% of 142 | -31% |
| 7 | 111 | 46% | 60 (54%) | 36% of 53 | +4% |
| 8 | 127 | 55% | 57 (45%) | 2% of 44 | +14% |
| 9 | 82 | 35% | 53 (65%) | 47% of 89 | -6% |
| 10 | 92 | 65% | 32 (35%) | 14% of 79 | +24% |
| 11 | 171 | 42% | 100 (58%) | n/a | +0% |
| 12 | 171 | 42% | 100 (58%) | n/a | +0% |
| 13 | 171 | 42% | 100 (58%) | n/a | +0% |
| 14 | 171 | 42% | 100 (58%) | n/a | +0% |
| 15 | 171 | 42% | 100 (58%) | n/a | +0% |
| 16 | 42 | 36% | 27 (64%) | 43% of 129 | -6% |
| 18 | 171 | 42% | 100 (58%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 37% vs base 42%, n=71)
- check #9: lower weight: flagged coins die no more often than average (precision 35% vs base 42%, n=82)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 42%, n=92)
- check #16: lower weight: flagged coins die no more often than average (precision 36% vs base 42%, n=42)
