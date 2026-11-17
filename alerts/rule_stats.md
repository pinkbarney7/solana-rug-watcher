# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 10:19 UTC. Labeled coins: 113 (31 dead/pulled, 82 still alive). Base dead rate 27.4%. Forward 24h samples so far: 74.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 98 | 31% | 68 (69%) | 0% of 13 | +3% |
| 2 | 8 | 0% | 8 (100%) | 30% of 105 | -27% |
| 3 | 45 | 16% | 38 (84%) | 35% of 68 | -12% |
| 5 | 67 | 37% | 42 (63%) | 13% of 46 | +10% |
| 6 | 22 | 14% | 19 (86%) | 31% of 90 | -14% |
| 7 | 76 | 33% | 51 (67%) | 19% of 31 | +5% |
| 8 | 79 | 39% | 48 (61%) | 0% of 34 | +12% |
| 9 | 52 | 17% | 43 (83%) | 36% of 61 | -10% |
| 10 | 61 | 46% | 33 (54%) | 6% of 52 | +18% |
| 11 | 113 | 27% | 82 (73%) | n/a | +0% |
| 12 | 113 | 27% | 82 (73%) | n/a | +0% |
| 13 | 113 | 27% | 82 (73%) | n/a | +0% |
| 14 | 113 | 27% | 82 (73%) | n/a | +0% |
| 15 | 113 | 27% | 82 (73%) | n/a | +0% |
| 16 | 40 | 28% | 29 (72%) | 27% of 73 | +0% |
| 18 | 113 | 27% | 82 (73%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 17% vs base 27%, n=52)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 27%, n=40)
