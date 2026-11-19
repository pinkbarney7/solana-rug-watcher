# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-19 17:26 UTC. Labeled coins: 131 (44 dead/pulled, 87 still alive). Base dead rate 33.6%. Forward 24h samples so far: 82.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 116 | 37% | 73 (63%) | 0% of 13 | +3% |
| 2 | 10 | 0% | 10 (100%) | 36% of 121 | -34% |
| 3 | 54 | 30% | 38 (70%) | 36% of 77 | -4% |
| 5 | 81 | 46% | 44 (54%) | 14% of 50 | +12% |
| 6 | 26 | 12% | 23 (88%) | 39% of 104 | -22% |
| 7 | 86 | 36% | 55 (64%) | 31% of 39 | +2% |
| 8 | 96 | 46% | 52 (54%) | 0% of 35 | +12% |
| 9 | 61 | 30% | 43 (70%) | 37% of 70 | -4% |
| 10 | 69 | 57% | 30 (43%) | 8% of 62 | +23% |
| 11 | 131 | 34% | 87 (66%) | n/a | +0% |
| 12 | 131 | 34% | 87 (66%) | n/a | +0% |
| 13 | 131 | 34% | 87 (66%) | n/a | +0% |
| 14 | 131 | 34% | 87 (66%) | n/a | +0% |
| 15 | 131 | 34% | 87 (66%) | n/a | +0% |
| 16 | 40 | 32% | 27 (68%) | 34% of 91 | -1% |
| 18 | 131 | 34% | 87 (66%) | n/a | +0% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #3: lower weight: flagged coins die no more often than average (precision 30% vs base 34%, n=54)
- check #7: lower weight: flagged coins die no more often than average (precision 36% vs base 34%, n=86)
- check #9: lower weight: flagged coins die no more often than average (precision 30% vs base 34%, n=61)
- check #10: consider treating WARN like FAIL: strong lift (precision 56% vs base 34%, n=69)
- check #16: lower weight: flagged coins die no more often than average (precision 32% vs base 34%, n=40)
