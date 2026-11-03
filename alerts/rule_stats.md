# Rule stats - outcome learning (info/risk only, not advice)
Updated 2026-11-03 18:44 UTC. Labeled coins: 0 (0 dead/pulled, 0 still alive). Base dead rate 0.0%. Forward 24h samples so far: 0.

**Caveats:** history labels are 'dead now vs alive now' plus the liquidity-pull watch, which mostly watched SKIP coins, so precision is biased upward for SKIP-heavy rules. Clean 1h/6h/24h forward samples need ~a week before thresholds should move. Nothing here changes alerting automatically.

| check # | flagged (FAIL/WARN) n | dead when flagged (precision) | false positives (flagged, alive) | dead when PASS | lift vs base |
|---|---|---|---|---|---|

## Suggested bar changes (logged to bar_changes.jsonl, need Barney's yes; not applied)
_Data span 0.0 days of forward-tracked + historical coins; treat as provisional until ~7 days of forward samples._
- none yet (needs n>=30 flagged and n>=30 passing per check)
