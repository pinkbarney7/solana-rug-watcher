# solana-rug-watcher (GitHub Actions batch scanner)

Public, free GitHub Actions version of the Solana rug/risk **batch** scanner (`fast_scan.py`).
Runs every ~10 minutes (GitHub cron may be delayed) and on manual dispatch.

- The Helius API key must be stored as the encrypted repo secret `HELIUS_API_KEY`. It is never committed.
- Latest results: `alerts/latest.md` (committed each run) and the `scan-output` artifact.
- Limitation: the live websocket watcher (`realtime.py`) is **not** included; Actions can't hold a live connection, so this catches things minutes late, not seconds.
- Output is information and risk only, not advice. A low score means fewer red flags, not safe.
