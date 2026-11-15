# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-15 19:02 UTC. Labeled coins: 81 (19 dead/pulled, 62 still alive). Base dead rate 23.5%. Forward 24h samples so far: 48.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 70 | 26% | 52 (74%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 73 | -23% |
| 3 | 37 | 19% | 30 (81%) | 27% of 44 | -5% |
| 5 | 42 | 31% | 29 (69%) | 15% of 39 | +7% |
| 6 | 20 | 15% | 17 (85%) | 27% of 60 | -8% |
| 7 | 50 | 26% | 37 (74%) | 23% of 26 | +3% |
| 8 | 53 | 36% | 34 (64%) | 0% of 28 | +12% |
| 9 | 37 | 16% | 31 (84%) | 30% of 44 | -7% |
| 10 | 42 | 38% | 26 (62%) | 8% of 39 | +15% |
| 11 | 81 | 23% | 62 (77%) | n/a | +0% |
| 12 | 81 | 23% | 62 (77%) | n/a | +0% |
| 13 | 81 | 23% | 62 (77%) | n/a | +0% |
| 14 | 81 | 23% | 62 (77%) | n/a | +0% |
| 15 | 81 | 23% | 62 (77%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 21% of 43 | +3% |
| 18 | 81 | 23% | 62 (77%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 6.5 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 19% vs base 24%, n=37)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 24%, n=37)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
