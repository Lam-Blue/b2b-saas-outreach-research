# Collection Status

Updated: 2026-06-23

## Status Key

- Collected: real retained source file exists in `research/`.
- Not retained: attempted or considered, but no usable source record was kept in `research/`.
- Not queued: no transcript was approved for this expert because the area was better served by supporting material.

## Area Status

| Area | Expert | LinkedIn status | Deep-source status | Supporting-source status | Notes |
| --- | --- | --- | --- | --- | --- |
| Area 1 — Commercial Fit, ICP, and Problem Context | Kyle Vamvouris | Not retained | Not queued | Collected | Public LinkedIn unavailable; supporting article retained. |
| Area 2 — Target Account Prioritisation and Account Research | Adam Schoenfeld | Not retained | Collected | Collected | Supadata transcript plus ICP/account-fit supporting sources retained. |
| Area 3 — Stakeholder Mapping and Buying-Committee Strategy | Nate Nasralla | Not retained | Not queued | Collected | Use for Area 3 only; do not count as Area 10. |
| Area 4 — Contact Data, Enrichment, and Verification | Jesse Ouellette | Not retained | Not queued | Collected | Preserve human-approved caveat on direct operator-role proof. |
| Area 5 — Timing and Trigger Signals | Todd Busler | Not retained | Collected | Collected | Supadata transcript plus trigger-signal supporting source retained. |
| Area 6 — Deliverability and Sender Infrastructure | Peter Goldstein | Not retained | Not queued | Collected | Technical sender-authentication foundations only; not cold-email ramping. |
| Area 7 — Messaging and Conversation Entry | Will Allred | Not retained | Collected | Collected | Supadata transcript plus benchmark supporting source retained. |
| Area 8 — Cadence and Channel Orchestration | Jason Bay | Not retained | Collected | Collected | Supadata transcript retained after live validation succeeded. |
| Area 9 — Live Conversation and Objection Handling | Armand Farrokh | Not retained | Collected | Collected | Supadata transcript plus episode-page context retained. |
| Area 10 — Reply Handling, Qualification, and Handoff | Harris Kenny | Not retained | Collected | Collected | Supadata transcript plus OutboundSync context retained. |

## Transcript Run Log

2026-06-23:

- First live validation initially failed before an API request because the script reported `SUPADATA_API_KEY is missing. Copy .env.example to .env and add your key.`
- A later approved Supadata run succeeded for the Jason Bay queue item. That transcript was retained and not refetched.
- The remaining approved queue items for Todd Busler, Will Allred, Armand Farrokh, Harris Kenny, and Adam Schoenfeld were fetched successfully through `scripts/fetch_youtube_transcript.py`.
- No random replacement videos were used.
- Prior failures and LinkedIn access constraints are recorded in `output-by-AI/collection/access-and-failure-log.md`.
