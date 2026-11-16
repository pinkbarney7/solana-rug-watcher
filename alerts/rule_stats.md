# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 09:44 UTC. Labeled coins: 85 (20 dead/pulled, 65 still alive). Base dead rate 23.5%. Forward 24h samples so far: 52.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 74 | 26% | 55 (74%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 77 | -24% |
| 3 | 39 | 18% | 32 (82%) | 28% of 46 | -6% |
| 5 | 45 | 31% | 31 (69%) | 15% of 40 | +8% |
| 6 | 21 | 14% | 18 (86%) | 27% of 63 | -9% |
| 7 | 54 | 26% | 40 (74%) | 23% of 26 | +2% |
| 8 | 57 | 35% | 37 (65%) | 0% of 28 | +12% |
| 9 | 39 | 15% | 33 (85%) | 30% of 46 | -8% |
| 10 | 44 | 39% | 27 (61%) | 7% of 41 | +15% |
| 11 | 85 | 24% | 65 (76%) | n/a | +0% |
| 12 | 85 | 24% | 65 (76%) | n/a | +0% |
| 13 | 85 | 24% | 65 (76%) | n/a | +0% |
| 14 | 85 | 24% | 65 (76%) | n/a | +0% |
| 15 | 85 | 24% | 65 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 21% of 47 | +3% |
| 18 | 85 | 24% | 65 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 24%, n=39)
- check #9: lower weight: flagged coins die no more often than average (precision 15% vs base 24%, n=39)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
