# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 15:53 EST. Labeled coins: 1125 (872 dead/pulled, 253 still alive). Base dead rate 77.5%. Forward 24h samples so far: 70.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 917 | 77% | 213 (23%) | 55% of 56 | -1% |
| 2 | 24 | 17% | 20 (83%) | 77% of 966 | -61% |
| 3 | 338 | 74% | 89 (26%) | 77% of 641 | -4% |
| 4 | 150 | 70% | 45 (30%) | 77% of 830 | -8% |
| 5 | 790 | 82% | 139 (18%) | 50% of 201 | +5% |
| 6 | 78 | 49% | 40 (51%) | 78% of 837 | -29% |
| 7 | 417 | 70% | 124 (30%) | 81% of 472 | -7% |
| 8 | 438 | 70% | 133 (30%) | 76% of 420 | -8% |
| 9 | 742 | 81% | 142 (19%) | 59% of 238 | +3% |
| 10 | 775 | 85% | 116 (15%) | 40% of 202 | +8% |
| 11 | 554 | 88% | 65 (12%) | 62% of 459 | +11% |
| 12 | 918 | 80% | 181 (20%) | 39% of 95 | +3% |
| 13 | 621 | 76% | 147 (24%) | 77% of 392 | -1% |
| 14 | 413 | 77% | 93 (23%) | 76% of 600 | -0% |
| 15 | 492 | 72% | 138 (28%) | 81% of 521 | -6% |
| 16 | 88 | 77% | 20 (23%) | 76% of 925 | -0% |
| 18 | 703 | 84% | 112 (16%) | 59% of 310 | +7% |
| 19 | 367 | 78% | 80 (22%) | 74% of 559 | +1% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=917)
- check #3: lower weight: flagged coins die no more often than average (precision 74% vs base 78%, n=338)
- check #4: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=150)
- check #6: lower weight: flagged coins die no more often than average (precision 49% vs base 78%, n=78)
- check #7: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=417)
- check #8: lower weight: flagged coins die no more often than average (precision 70% vs base 78%, n=438)
- check #12: lower weight: flagged coins die no more often than average (precision 80% vs base 78%, n=918)
- check #13: lower weight: flagged coins die no more often than average (precision 76% vs base 78%, n=621)
- check #14: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=413)
- check #15: lower weight: flagged coins die no more often than average (precision 72% vs base 78%, n=492)
- check #16: lower weight: flagged coins die no more often than average (precision 77% vs base 78%, n=88)
- check #19: lower weight: flagged coins die no more often than average (precision 78% vs base 78%, n=367)
