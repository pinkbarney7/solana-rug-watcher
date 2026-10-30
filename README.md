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

## Free hardening (Oct 30)
- `outcomes.py`: 1h/6h/24h price+liq after first score via DEX Screener (no Helius) -> `alerts/outcomes.md|jsonl`.
- Public RPC fallback (`helius_checks.py`): `getTokenLargestAccounts`, `getAccountInfo`, `getMultipleAccounts`, `getTokenSupply`, `getBalance` try `solana-rpc.publicnode.com` first (<=4 req/s, 60s cool-off on error), then Helius. History/tx calls (`getTransactionsForAddress`, signatures, parsed txs) stay on Helius. `scorecard.py` getAccountInfo already used publicnode.
- Exit liquidity uses Jupiter lite-api quotes only (no Helius).
- `telegram_alert.py`: backup alerts only when Actions is in helius mode or box heartbeat >20 min stale; standing bar; 24h dedup in `sent_alerts.json`; no-op if `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID` secrets unset. Liquidity pulls are never sent from Actions (single source).
- `status.md`: heartbeat ages + today's Actions Helius spend.

## Profit gates (added 2026-10-30, info/risk only)
- Copycat ticker family mute: 24 h after a confirmed pull/rug (`family_mute.json`, synced from the box).
- Jupiter sellability hard gate: non-SKIP coins that fail a $25 buy+sell quote are downgraded to SKIP.
- Smart pile-ins (box daemon): 2+ *proven* smart wallets on the same mint within 6 h, with sellability noted.
- Cheap filter + hourly Helius pacing (box daemon): plain launches with liq < $20k, liq/mcap < 1%, a muted ticker, or over the paced hourly allowance (15% of the day reserved for 00-08 ET) are not scored.
- PumpPortal free launch feed alongside the pump.fun API; Helius create-log stays the fallback.
- RugCheck as a second liquidity source when GeckoTerminal is down.
- `alerts/outcome_digest.md`: hit rates by verdict; suggested bar changes go to `bar_changes.jsonl` and are never auto-applied.
