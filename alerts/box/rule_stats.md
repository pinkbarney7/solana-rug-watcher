# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-01 18:18 EST. Labeled coins: 1075 (830 dead/pulled, 245 still alive). Base dead rate 77.2%. Forward 24h samples so far: 43.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 871 | 76% | 208 (24%) | 57% of 51 | -1% |
| 2 | 21 | 19% | 17 (81%) | 77% of 918 | -58% |
| 3 | 315 | 71% | 91 (29%) | 77% of 613 | -6% |
| 4 | 143 | 69% | 45 (31%) | 76% of 786 | -9% |
| 5 | 757 | 82% | 140 (18%) | 50% of 183 | +4% |
| 6 | 73 | 51% | 36 (49%) | 76% of 808 | -27% |
| 7 | 395 | 70% | 117 (30%) | 78% of 460 | -7% |
| 8 | 417 | 68% | 133 (32%) | 76% of 391 | -9% |
| 9 | 711 | 80% | 144 (20%) | 60% of 218 | +3% |
| 10 | 738 | 84% | 115 (16%) | 39% of 188 | +7% |
| 11 | 531 | 89% | 60 (11%) | 60% of 431 | +11% |
| 12 | 875 | 79% | 180 (21%) | 41% of 87 | +2% |
| 13 | 589 | 76% | 143 (24%) | 76% of 373 | -1% |
| 14 | 393 | 78% | 86 (22%) | 75% of 569 | +1% |
| 15 | 463 | 73% | 126 (27%) | 79% of 499 | -4% |
| 16 | 85 | 79% | 18 (21%) | 76% of 877 | +2% |
| 18 | 670 | 84% | 110 (16%) | 59% of 292 | +6% |
| 19 | 348 | 79% | 74 (21%) | 73% of 531 | +2% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=871)
- check #3: lower weight: flagged coins die no more often than average (precision 71% vs base 77%, n=315)
- check #4: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=143)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 77%, n=73)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 77%, n=395)
- check #8: lower weight: flagged coins die no more often than average (precision 68% vs base 77%, n=417)
- check #9: lower weight: flagged coins die no more often than average (precision 80% vs base 77%, n=711)
- check #12: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=875)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 77%, n=589)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 77%, n=393)
- check #15: lower weight: flagged coins die no more often than average (precision 73% vs base 77%, n=463)
- check #16: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=85)
- check #19: lower weight: flagged coins die no more often than average (precision 79% vs base 77%, n=348)
