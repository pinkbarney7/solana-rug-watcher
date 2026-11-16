# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 03:15 UTC. Labeled coins: 82 (19 dead/pulled, 63 still alive). Base dead rate 23.2%. Forward 24h samples so far: 50.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 71 | 25% | 53 (75%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 74 | -23% |
| 3 | 38 | 18% | 31 (82%) | 27% of 44 | -5% |
| 5 | 43 | 30% | 30 (70%) | 15% of 39 | +7% |
| 6 | 20 | 15% | 17 (85%) | 26% of 61 | -8% |
| 7 | 51 | 25% | 38 (75%) | 23% of 26 | +2% |
| 8 | 54 | 35% | 35 (65%) | 0% of 28 | +12% |
| 9 | 38 | 16% | 32 (84%) | 30% of 44 | -7% |
| 10 | 43 | 37% | 27 (63%) | 8% of 39 | +14% |
| 11 | 82 | 23% | 63 (77%) | n/a | +0% |
| 12 | 82 | 23% | 63 (77%) | n/a | +0% |
| 13 | 82 | 23% | 63 (77%) | n/a | +0% |
| 14 | 82 | 23% | 63 (77%) | n/a | +0% |
| 15 | 82 | 23% | 63 (77%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 20% of 44 | +3% |
| 18 | 82 | 23% | 63 (77%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 6.8 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 23%, n=38)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 23%, n=38)
