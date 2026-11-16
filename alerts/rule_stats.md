# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 06:26 UTC. Labeled coins: 84 (19 dead/pulled, 65 still alive). Base dead rate 22.6%. Forward 24h samples so far: 52.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 73 | 25% | 55 (75%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 25% of 76 | -23% |
| 3 | 39 | 18% | 32 (82%) | 27% of 45 | -5% |
| 5 | 44 | 30% | 31 (70%) | 15% of 40 | +7% |
| 6 | 21 | 14% | 18 (86%) | 26% of 62 | -8% |
| 7 | 53 | 25% | 40 (75%) | 23% of 26 | +2% |
| 8 | 56 | 34% | 37 (66%) | 0% of 28 | +11% |
| 9 | 39 | 15% | 33 (85%) | 29% of 45 | -7% |
| 10 | 43 | 37% | 27 (63%) | 7% of 41 | +15% |
| 11 | 84 | 23% | 65 (77%) | n/a | +0% |
| 12 | 84 | 23% | 65 (77%) | n/a | +0% |
| 13 | 84 | 23% | 65 (77%) | n/a | +0% |
| 14 | 84 | 23% | 65 (77%) | n/a | +0% |
| 15 | 84 | 23% | 65 (77%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 20% of 46 | +4% |
| 18 | 84 | 23% | 65 (77%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 6.9 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 23%, n=39)
- check #9: lower weight: flagged coins die no more often than average (precision 15% vs base 23%, n=39)
