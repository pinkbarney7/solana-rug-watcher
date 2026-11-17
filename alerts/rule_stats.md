# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 09:01 UTC. Labeled coins: 108 (29 dead/pulled, 79 still alive). Base dead rate 26.9%. Forward 24h samples so far: 70.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 95 | 29% | 67 (71%) | 0% of 11 | +3% |
| 2 | 8 | 0% | 8 (100%) | 29% of 100 | -27% |
| 3 | 44 | 16% | 37 (84%) | 34% of 64 | -11% |
| 5 | 63 | 37% | 40 (63%) | 13% of 45 | +10% |
| 6 | 22 | 14% | 19 (86%) | 31% of 85 | -13% |
| 7 | 72 | 32% | 49 (68%) | 20% of 30 | +5% |
| 8 | 75 | 39% | 46 (61%) | 0% of 33 | +12% |
| 9 | 49 | 16% | 41 (84%) | 36% of 59 | -11% |
| 10 | 57 | 46% | 31 (54%) | 6% of 51 | +19% |
| 11 | 108 | 27% | 79 (73%) | n/a | +0% |
| 12 | 108 | 27% | 79 (73%) | n/a | +0% |
| 13 | 108 | 27% | 79 (73%) | n/a | +0% |
| 14 | 108 | 27% | 79 (73%) | n/a | +0% |
| 15 | 108 | 27% | 79 (73%) | n/a | +0% |
| 16 | 39 | 28% | 28 (72%) | 26% of 69 | +1% |
| 18 | 108 | 27% | 79 (73%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 16% vs base 27%, n=49)
- check #16: lower weight: flagged coins die no more often than average (precision 28% vs base 27%, n=39)
