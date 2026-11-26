# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 06:32 UTC. Labeled coins: 215 (92 dead/pulled, 123 still alive). Base dead rate 42.8%. Forward 24h samples so far: 144.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 198 | 46% | 107 (54%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 46% of 200 | -43% |
| 3 | 83 | 39% | 51 (61%) | 45% of 132 | -4% |
| 5 | 140 | 59% | 58 (41%) | 13% of 75 | +16% |
| 6 | 34 | 9% | 31 (91%) | 49% of 180 | -34% |
| 7 | 138 | 49% | 71 (51%) | 39% of 62 | +6% |
| 8 | 160 | 57% | 69 (43%) | 2% of 55 | +14% |
| 9 | 94 | 38% | 58 (62%) | 46% of 121 | -4% |
| 10 | 120 | 64% | 43 (36%) | 16% of 95 | +21% |
| 11 | 215 | 43% | 123 (57%) | n/a | +0% |
| 12 | 215 | 43% | 123 (57%) | n/a | +0% |
| 13 | 215 | 43% | 123 (57%) | n/a | +0% |
| 14 | 215 | 43% | 123 (57%) | n/a | +0% |
| 15 | 215 | 43% | 123 (57%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 45% of 170 | -9% |
| 18 | 215 | 43% | 123 (57%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 39% vs base 43%, n=83)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 43%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 43%, n=94)
- check #10: consider treating WARN like FAIL: strong lift (precision 64% vs base 43%, n=120)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 43%, n=45)
