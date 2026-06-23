# B2B SaaS Cold Outreach Research

This repository contains a source-backed B2B SaaS cold outreach playbook.

The current final artifact is `FINAL.md`. It uses the human-approved 10-expert selection already published in `research/sources.md`; expert selection is closed unless a future human instruction explicitly reopens it.

## Approved Expert Map

| Area | Expert | Focus |
|---:|---|---|
| 1 | Kyle Vamvouris | Commercial Fit, ICP, and Problem Context |
| 2 | Adam Schoenfeld | Target Account Prioritisation and Account Research |
| 3 | Nate Nasralla | Stakeholder Mapping and Buying-Committee Strategy |
| 4 | Jesse Ouellette | Contact Data, Enrichment, and Verification |
| 5 | Todd Busler | Timing and Trigger Signals |
| 6 | Peter Goldstein | Deliverability and Sender Infrastructure |
| 7 | Will Allred | Messaging and Conversation Entry |
| 8 | Jason Bay | Cadence and Channel Orchestration |
| 9 | Armand Farrokh | Live Conversation and Objection Handling |
| 10 | Harris Kenny | Reply Handling, Qualification, and Handoff |

Required caveats:

- Jesse Ouellette is human-approved with a transparent evidence caveat: dated LeadMagic material is attributable to him and strongly fits Area 4, but direct operator-role proof was not captured in the research workspace.
- Peter Goldstein covers technical sender-infrastructure foundations only, such as email authentication, DKIM, domains, and deliverability infrastructure. He should not be described as a cold-email ramping or mailbox-rotation expert.
- Nate Nasralla covers Area 3 only. Area 10 is Harris Kenny.
- Adam Schoenfeld is Area 2 primary. Area 5 is Todd Busler.

## Repository Structure

- `FINAL.md` — final playbook organized by Areas 1 through 10.
- `research/sources.md` — source of truth for research areas, fixed expert selection, and collected-material inventory.
- `research/linkedin-posts/` — public LinkedIn availability records and collected LinkedIn material if available.
- `research/youtube-transcripts/` — Supadata transcript outputs. This run produced no transcript files because the script reported a missing API key.
- `research/other/` — collected fallback and supporting materials.
- `output-by-AI/collection/` — collection plan, transcript queue, status log, and audit.
- `scripts/fetch_youtube_transcript.py` — approved Supadata transcript-fetching entry point.
- `scripts/README.md` — transcript tooling notes.

## Collection Status

The collection run used the fixed expert list and gathered local fallback/source records for all 10 areas.

Public LinkedIn posts were not collected because no accessible public post with usable date, text, and area relevance was retained. Each expert has an availability record under `research/linkedin-posts/`.

The transcript queue is in `output-by-AI/collection/transcript-queue.md`. The first live validation attempted Jason Bay's queued video with `scripts/fetch_youtube_transcript.py`, but the script stopped before a live Supadata request because `SUPADATA_API_KEY` was missing. No random replacement videos or alternate transcript providers were used.

## Safe Transcript Usage

Use Supadata only through:

```bash
python3 scripts/fetch_youtube_transcript.py --help
```

Before fetching, add the exact approved YouTube source to `output-by-AI/collection/transcript-queue.md`. Do not fetch random videos. Do not print, edit, commit, or expose `.env` or API keys.

Generated transcripts should remain under `research/youtube-transcripts/[expert-slug]/`.

## Evidence Strength

The strongest local evidence is in Areas 1, 2, 3, 5, 6, and 7.

Areas 8, 9, and 10 have usable fallback records but would benefit from transcript-level collection once Supadata configuration is available.

Area 4 is usable with the explicit Jesse Ouellette evidence caveat.
