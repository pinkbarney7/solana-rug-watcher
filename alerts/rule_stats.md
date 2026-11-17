# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-17 07:54 UTC. Labeled coins: 105 (26 dead/pulled, 79 still alive). Base dead rate 24.8%. Forward 24h samples so far: 69.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 92 | 27% | 67 (73%) | 0% of 11 | +2% |
| 2 | 8 | 0% | 8 (100%) | 27% of 97 | -25% |
| 3 | 44 | 16% | 37 (84%) | 31% of 61 | -9% |
| 5 | 60 | 33% | 40 (67%) | 13% of 45 | +9% |
| 6 | 22 | 14% | 19 (86%) | 28% of 82 | -11% |
| 7 | 69 | 29% | 49 (71%) | 20% of 30 | +4% |
| 8 | 72 | 36% | 46 (64%) | 0% of 33 | +11% |
| 9 | 47 | 13% | 41 (87%) | 34% of 58 | -12% |
| 10 | 54 | 43% | 31 (57%) | 6% of 51 | +18% |
| 11 | 105 | 25% | 79 (75%) | n/a | +0% |
| 12 | 105 | 25% | 79 (75%) | n/a | +0% |
| 13 | 105 | 25% | 79 (75%) | n/a | +0% |
| 14 | 105 | 25% | 79 (75%) | n/a | +0% |
| 15 | 105 | 25% | 79 (75%) | n/a | +0% |
| 16 | 38 | 26% | 28 (74%) | 24% of 67 | +2% |
| 18 | 105 | 25% | 79 (75%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 16% vs base 25%, n=44)
- check #9: lower weight: flagged coins die no more often than average (precision 13% vs base 25%, n=47)
- check #16: lower weight: flagged coins die no more often than average (precision 26% vs base 25%, n=38)
