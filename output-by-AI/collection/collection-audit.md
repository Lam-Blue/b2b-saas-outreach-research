# Collection Audit

Date: 2026-06-23

## Fixed Expert Selection

The approved 10 experts in `research/sources.md` were treated as fixed. No expert selection was reopened and no replacement experts were introduced.

## Coverage Result

| Area | Expert | Local source coverage | Assessment |
|---:|---|---|---|
| 1 | Kyle Vamvouris | LinkedIn availability record; fallback article in `research/other/` | Adequate for FINAL.md claims about ICP and sales playbook setup. |
| 2 | Adam Schoenfeld | LinkedIn availability record; dated first-person post; supporting ICP guide | Adequate for account prioritisation and ICP-fit claims. |
| 3 | Nate Nasralla | LinkedIn availability record; enterprise sales playbook | Adequate for stakeholder/champion/buying-committee claims; not Area 10. |
| 4 | Jesse Ouellette | LinkedIn availability record; LeadMagic source index | Usable with required caveat: direct operator-role proof was not captured. |
| 5 | Todd Busler | LinkedIn availability record; Champify trigger-signal article | Adequate for trigger-to-prioritisation-to-outreach claims. |
| 6 | Peter Goldstein | LinkedIn availability record; technical email-hosting article | Usable only for technical sender-infrastructure foundations. |
| 7 | Will Allred | LinkedIn availability record; cold-email benchmark report | Adequate for messaging and conversation-entry claims. |
| 8 | Jason Bay | LinkedIn availability record; 30MPC episode page | Weaker than transcript-level evidence because Supadata collection was blocked. |
| 9 | Armand Farrokh | LinkedIn availability record; 30MPC episode page | Weaker than transcript-level evidence because Supadata collection was blocked. |
| 10 | Harris Kenny | LinkedIn availability record; OutboundSync blog/source context | Adequate for reply routing/CRM handoff at process level; weaker without transcript. |

## Transcript Audit

Queued transcript sources were created in `output-by-AI/collection/transcript-queue.md`.

First live validation:

- Source: Jason Bay, `https://www.youtube.com/watch?v=JX1UNIJwcCY`
- Script: `scripts/fetch_youtube_transcript.py`
- Result: Failed before a live Supadata API request.
- Exact script error: `SUPADATA_API_KEY is missing. Copy .env.example to .env and add your key.`

Because the failure was configuration-wide, no remaining queued source was fetched in this run. The documented fallback path was used: source records were created under `research/other/`, and unavailable LinkedIn records were created under `research/linkedin-posts/`.

## Weaker Evidence and Gaps

- No Supadata transcript files were collected because the API key was unavailable to the script at runtime.
- Public LinkedIn posts were not collected for any expert; each expert has an availability record and fallback.
- Jason Bay, Armand Farrokh, and Harris Kenny would benefit most from transcript-level collection once Supadata configuration is available.
- Jesse Ouellette remains a human-approved provisional Area 4 selection with a transparent evidence caveat.
- Peter Goldstein must remain limited to technical sender-infrastructure foundations.

