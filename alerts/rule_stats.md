# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-16 11:09 UTC. Labeled coins: 86 (21 dead/pulled, 65 still alive). Base dead rate 24.4%. Forward 24h samples so far: 52.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 75 | 27% | 55 (73%) | 0% of 9 | +2% |
| 2 | 8 | 0% | 8 (100%) | 27% of 78 | -24% |
| 3 | 39 | 18% | 32 (82%) | 30% of 47 | -6% |
| 5 | 46 | 33% | 31 (67%) | 15% of 40 | +8% |
| 6 | 21 | 14% | 18 (86%) | 28% of 64 | -10% |
| 7 | 55 | 27% | 40 (73%) | 23% of 26 | +3% |
| 8 | 58 | 36% | 37 (64%) | 0% of 28 | +12% |
| 9 | 39 | 15% | 33 (85%) | 32% of 47 | -9% |
| 10 | 45 | 40% | 27 (60%) | 7% of 41 | +16% |
| 11 | 86 | 24% | 65 (76%) | n/a | +0% |
| 12 | 86 | 24% | 65 (76%) | n/a | +0% |
| 13 | 86 | 24% | 65 (76%) | n/a | +0% |
| 14 | 86 | 24% | 65 (76%) | n/a | +0% |
| 15 | 86 | 24% | 65 (76%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 23% of 48 | +2% |
| 18 | 86 | 24% | 65 (76%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 18% vs base 24%, n=39)
- check #9: lower weight: flagged coins die no more often than average (precision 15% vs base 24%, n=39)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 24%, n=38)
