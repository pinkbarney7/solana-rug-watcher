# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 20:36 UTC. Labeled coins: 94 (22 dead/pulled, 72 still alive). Base dead rate 23.4%. Forward 24h samples so far: 61.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 82 | 26% | 61 (74%) | 0% of 10 | +2% |
| 2 | 8 | 0% | 8 (100%) | 26% of 86 | -23% |
| 3 | 42 | 17% | 35 (83%) | 29% of 52 | -7% |
| 5 | 52 | 31% | 36 (69%) | 14% of 42 | +7% |
| 6 | 22 | 14% | 19 (86%) | 27% of 71 | -10% |
| 7 | 61 | 26% | 45 (74%) | 21% of 28 | +3% |
| 8 | 63 | 35% | 41 (65%) | 0% of 31 | +12% |
| 9 | 43 | 14% | 37 (86%) | 31% of 51 | -9% |
| 10 | 48 | 40% | 29 (60%) | 7% of 46 | +16% |
| 11 | 94 | 23% | 72 (77%) | n/a | +0% |
| 12 | 94 | 23% | 72 (77%) | n/a | +0% |
| 13 | 94 | 23% | 72 (77%) | n/a | +0% |
| 14 | 94 | 23% | 72 (77%) | n/a | +0% |
| 15 | 94 | 23% | 72 (77%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 21% of 56 | +3% |
| 18 | 94 | 23% | 72 (77%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 17% vs base 23%, n=42)
- check #9: lower weight: flagged coins die no more often than average (precision 14% vs base 23%, n=43)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 23%, n=38)
