# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-10-30 18:18 EDT. Labeled coins: 932 (693 dead/pulled, 239 still alive). Base dead rate 74.4%. Forward 24h samples so far: 0.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|
| 1 | 822 | 74% | 215 (26%) | 52% of 48 | -1% |
| 2 | 19 | 21% | 15 (79%) | 74% of 868 | -53% |
| 3 | 280 | 65% | 97 (35%) | 76% of 596 | -9% |
| 4 | 137 | 63% | 51 (37%) | 75% of 740 | -12% |
| 5 | 712 | 80% | 144 (20%) | 46% of 176 | +5% |
| 6 | 69 | 51% | 34 (49%) | 74% of 772 | -24% |
| 7 | 384 | 69% | 118 (31%) | 75% of 431 | -5% |
| 8 | 382 | 65% | 135 (35%) | 74% of 377 | -10% |
| 9 | 667 | 78% | 145 (22%) | 55% of 210 | +4% |
| 10 | 696 | 82% | 124 (18%) | 36% of 178 | +8% |
| 11 | 508 | 88% | 63 (12%) | 56% of 402 | +13% |
| 12 | 828 | 77% | 190 (23%) | 40% of 82 | +3% |
| 13 | 547 | 74% | 143 (26%) | 74% of 363 | -0% |
| 14 | 381 | 77% | 88 (23%) | 71% of 529 | +3% |
| 15 | 435 | 71% | 125 (29%) | 76% of 475 | -3% |
| 16 | 84 | 75% | 21 (25%) | 74% of 826 | +1% |
| 18 | 639 | 81% | 121 (19%) | 56% of 271 | +7% |
| 19 | 333 | 78% | 74 (22%) | 70% of 503 | +3% |

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
- check #1: lower weight: flagged coins die no more often than average (precision 74% vs base 74%, n=822)
- check #3: lower weight: flagged coins die no more often than average (precision 65% vs base 74%, n=280)
- check #4: lower weight: flagged coins die no more often than average (precision 63% vs base 74%, n=137)
- check #6: lower weight: flagged coins die no more often than average (precision 51% vs base 74%, n=69)
- check #7: lower weight: flagged coins die no more often than average (precision 69% vs base 74%, n=384)
- check #8: lower weight: flagged coins die no more often than average (precision 65% vs base 74%, n=382)
- check #12: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=828)
- check #13: lower weight: flagged coins die no more often than average (precision 74% vs base 74%, n=547)
- check #14: lower weight: flagged coins die no more often than average (precision 77% vs base 74%, n=381)
- check #15: lower weight: flagged coins die no more often than average (precision 71% vs base 74%, n=435)
- check #16: lower weight: flagged coins die no more often than average (precision 75% vs base 74%, n=84)
