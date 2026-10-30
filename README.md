# solana-rug-watcher (GitHub Actions batch scanner)

Public, free GitHub Actions version of the Solana rug/risk **batch** scanner (`fast_scan.py`).
Runs every ~10 minutes (GitHub cron may be delayed) and on manual dispatch.

- The Helius API key must be stored as the encrypted repo secret `HELIUS_API_KEY`. It is never committed.
- Latest results: `alerts/latest.md` (committed each run) and the `scan-output` artifact.
- Limitation: the live websocket watcher (`realtime.py`) is **not** included; Actions can't hold a live connection, so this catches things minutes late, not seconds.
- Output is information and risk only, not advice. A low score means fewer red flags, not safe.

## Modes and budget (added 2026-10-30)
- `actions_mode.py decide`: if the box `heartbeat.json` (pushed by `/workspace/scorecard/sync_lists.sh`) is < 20 min old, the run is **free-only** (DEX Screener / pump.fun / GeckoTerminal, no Helius, results labelled UNVERIFIED). If it is missing/stale, Helius scoring runs until `actions_budget.json` reaches 3,000 credits for the ET day, then free-only again.
- `.cache/` (HTTP + score cache) persists across runs via actions/cache; `scored.json` records mint -> last score time/liq/holders. A coin is re-scored only if its last score is > 60 min old or liquidity moved > 30%.
- `HELIUS_EARLY_STOP=1`: the funder trace stops paging history once the creator (or its first funder) is a rug-list wallet (rug-funder FAIL already decided).
- If GeckoTerminal is down, the scan uses DEX Screener fields only and the report says DEGRADED.
- Every run writes `alerts/actions_heartbeat.json` (mode, helius_used, credits today).

## Heartbeat comparison (for the monitoring routine)
- Box: `heartbeat.json` `ts_epoch` (only advances while the realtime daemon is healthy). Actions: `alerts/actions_heartbeat.json` `ts_epoch`.
- Either older than 30 min = that watcher is dark. Box dark + Actions fresh = backup is covering (mode should be `helius` until budget spent). Both dark = alert.
- Box side: run `/workspace/scorecard/sync_lists.sh` every ~10 min (heartbeat each time; rug lists only when changed, same commit).
