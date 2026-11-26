# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-26 08:29 UTC. Labeled coins: 220 (95 dead/pulled, 125 still alive). Base dead rate 43.2%. Forward 24h samples so far: 146.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 203 | 46% | 109 (54%) | 0% of 15 | +3% |
| 2 | 15 | 0% | 15 (100%) | 46% of 205 | -43% |
| 3 | 85 | 38% | 53 (62%) | 47% of 135 | -6% |
| 5 | 145 | 59% | 60 (41%) | 13% of 75 | +15% |
| 6 | 34 | 9% | 31 (91%) | 50% of 185 | -34% |
| 7 | 141 | 50% | 71 (50%) | 38% of 64 | +6% |
| 8 | 165 | 57% | 71 (43%) | 2% of 55 | +14% |
| 9 | 97 | 38% | 60 (62%) | 47% of 123 | -5% |
| 10 | 123 | 65% | 43 (35%) | 15% of 97 | +22% |
| 11 | 220 | 43% | 125 (57%) | n/a | +0% |
| 12 | 220 | 43% | 125 (57%) | n/a | +0% |
| 13 | 220 | 43% | 125 (57%) | n/a | +0% |
| 14 | 220 | 43% | 125 (57%) | n/a | +0% |
| 15 | 220 | 43% | 125 (57%) | n/a | +0% |
| 16 | 45 | 33% | 30 (67%) | 46% of 175 | -10% |
| 18 | 220 | 43% | 125 (57%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 43%, n=85)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 43%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 43%, n=97)
- check #10: consider treating WARN like FAIL: strong lift (precision 65% vs base 43%, n=123)
- check #16: lower weight: flagged coins die no more often than average (precision 33% vs base 43%, n=45)
