# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-27 06:00 UTC. Labeled coins: 238 (110 dead/pulled, 128 still alive). Base dead rate 46.2%. Forward 24h samples so far: 154.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 220 | 49% | 112 (51%) | 6% of 16 | +3% |
| 2 | 15 | 0% | 15 (100%) | 49% of 223 | -46% |
| 3 | 87 | 38% | 54 (62%) | 51% of 151 | -8% |
| 5 | 162 | 61% | 63 (39%) | 14% of 76 | +15% |
| 6 | 34 | 9% | 31 (91%) | 53% of 203 | -37% |
| 7 | 157 | 54% | 72 (46%) | 36% of 66 | +8% |
| 8 | 182 | 60% | 73 (40%) | 2% of 56 | +14% |
| 9 | 101 | 38% | 63 (62%) | 53% of 137 | -9% |
| 10 | 137 | 69% | 42 (31%) | 15% of 101 | +23% |
| 11 | 238 | 46% | 128 (54%) | n/a | +0% |
| 12 | 238 | 46% | 128 (54%) | n/a | +0% |
| 13 | 238 | 46% | 128 (54%) | n/a | +0% |
| 14 | 238 | 46% | 128 (54%) | n/a | +0% |
| 15 | 238 | 46% | 128 (54%) | n/a | +0% |
| 16 | 46 | 35% | 30 (65%) | 49% of 192 | -11% |
| 18 | 238 | 46% | 128 (54%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 38% vs base 46%, n=87)
- check #6: lower weight: flagged coins die no more often than average (precision 9% vs base 46%, n=34)
- check #9: lower weight: flagged coins die no more often than average (precision 38% vs base 46%, n=101)
- check #10: consider treating WARN like FAIL: strong lift (precision 69% vs base 46%, n=137)
- check #16: lower weight: flagged coins die no more often than average (precision 35% vs base 46%, n=46)
