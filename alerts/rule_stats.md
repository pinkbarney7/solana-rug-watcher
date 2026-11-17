# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 09:51 UTC. Labeled coins: 110 (30 dead/pulled, 80 still alive). Base dead rate 27.3%. Forward 24h samples so far: 72.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 97 | 30% | 68 (70%) | 0% of 11 | +3% |
| 2 | 8 | 0% | 8 (100%) | 29% of 102 | -27% |
| 3 | 45 | 16% | 38 (84%) | 35% of 65 | -12% |
| 5 | 65 | 37% | 41 (63%) | 13% of 45 | +10% |
| 6 | 22 | 14% | 19 (86%) | 31% of 87 | -14% |
| 7 | 73 | 33% | 49 (67%) | 19% of 31 | +6% |
| 8 | 77 | 39% | 47 (61%) | 0% of 33 | +12% |
| 9 | 50 | 16% | 42 (84%) | 37% of 60 | -11% |
| 10 | 58 | 47% | 31 (53%) | 6% of 52 | +19% |
| 11 | 110 | 27% | 80 (73%) | n/a | +0% |
| 12 | 110 | 27% | 80 (73%) | n/a | +0% |
| 13 | 110 | 27% | 80 (73%) | n/a | +0% |
| 14 | 110 | 27% | 80 (73%) | n/a | +0% |
| 15 | 110 | 27% | 80 (73%) | n/a | +0% |
| 16 | 39 | 28% | 28 (72%) | 27% of 71 | +1% |
| 18 | 110 | 27% | 80 (73%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=50)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 27%, n=39)
