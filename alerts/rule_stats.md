# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 09:58 UTC. Labeled coins: 111 (30 dead/pulled, 81 still alive). Base dead rate 27.0%. Forward 24h samples so far: 73.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 97 | 30% | 68 (70%) | 0% of 12 | +3% |
| 2 | 8 | 0% | 8 (100%) | 29% of 103 | -27% |
| 3 | 45 | 16% | 38 (84%) | 35% of 66 | -11% |
| 5 | 66 | 36% | 42 (64%) | 13% of 45 | +9% |
| 6 | 22 | 14% | 19 (86%) | 31% of 88 | -13% |
| 7 | 74 | 32% | 50 (68%) | 19% of 31 | +5% |
| 8 | 78 | 38% | 48 (62%) | 0% of 33 | +11% |
| 9 | 51 | 16% | 43 (84%) | 37% of 60 | -11% |
| 10 | 59 | 46% | 32 (54%) | 6% of 52 | +19% |
| 11 | 111 | 27% | 81 (73%) | n/a | +0% |
| 12 | 111 | 27% | 81 (73%) | n/a | +0% |
| 13 | 111 | 27% | 81 (73%) | n/a | +0% |
| 14 | 111 | 27% | 81 (73%) | n/a | +0% |
| 15 | 111 | 27% | 81 (73%) | n/a | +0% |
| 16 | 39 | 28% | 28 (72%) | 26% of 72 | +1% |
| 18 | 111 | 27% | 81 (73%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=45)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=51)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 27%, n=39)
