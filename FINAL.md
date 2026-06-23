# B2B SaaS Cold Outreach Playbook

## Scope and Evidence

This playbook is built from the human-approved expert selection in `research/sources.md` and the local collection inventory under `research/`. It is organized by ten outreach areas, from commercial fit through reply handling.

Evidence caveats:

- Supadata transcript collection was attempted but blocked because `scripts/fetch_youtube_transcript.py` reported a missing `SUPADATA_API_KEY`; no transcript files were created.
- Public LinkedIn posts were not collected; each expert has an availability record in `research/linkedin-posts/`.
- Jesse Ouellette is a human-approved provisional Area 4 selection. Dated LeadMagic material is attributable to him and strongly fits Area 4, but direct operator-role proof was not captured in the research workspace.
- Peter Goldstein is used only for technical sender-infrastructure foundations, such as email authentication, DKIM, domains, and deliverability infrastructure.

## 1. Commercial Fit, ICP, and Problem Context

Start by deciding whether outbound is commercially sensible for the problem, market, and sales motion. Kyle Vamvouris's sales-playbook material supports documenting the target customer, sales process, and operating expectations before reps start executing outreach.

Practical rule: define the problem context, ICP hypothesis, buyer maturity, sales motion, and disqualifiers before building lists or writing messages. A cold-outreach system should reject weak-fit accounts early instead of letting them become poor personalization inputs later.

Local evidence: `research/other/kyle-vamvouris/2026-03-13--sales-playbook.md`

## 2. Target Account Prioritisation and Account Research

After ICP definition, prioritize accounts by fit and research value. Adam Schoenfeld's Keyplay and PeerSignal material supports account intelligence, ICP modelling, and account-fit scoring as a distinct step from timing or trigger interpretation.

Practical rule: tier accounts before researching contacts. The research depth should match the expected value of the account: high-fit accounts deserve deeper context, while low-fit accounts should not receive expensive manual effort.

Local evidence: `research/other/adam-schoenfeld/2026-04-08--keyplay-inflection.md`; `research/other/adam-schoenfeld/undated--build-an-icp-model.md`

## 3. Stakeholder Mapping and Buying-Committee Strategy

Nate Nasralla's material supports mapping who matters inside an account and how champions influence internal buying conversations. This area is about stakeholder strategy, not downstream reply handling.

Practical rule: identify likely users, champions, economic buyers, blockers, and internal storytellers. Outreach should respect that one person may open the door while another person controls budget, risk, or implementation.

Local evidence: `research/other/nate-nasralla/2022-05-11--enterprise-sales-playbook.md`

## 4. Contact Data, Enrichment, and Verification

Jesse Ouellette's LeadMagic material supports contact-data workflows: list building, enrichment, email verification, B2B data accuracy, and Clay-related workflows. Because direct operator-role proof was not captured, use this area with the explicit human-approved caveat.

Practical rule: turn stakeholder hypotheses into reliable contact records through enrichment, verification, deduplication, and source conflict checks. Bad data contaminates later steps: deliverability, personalization, and reply routing all depend on correct identity and contact fields.

Local evidence: `research/other/jesse-ouellette/2026-06-08--leadmagic-source-index.md`

## 5. Timing and Trigger Signals

Todd Busler's Champify material supports using signals such as job changes and existing relationship data to decide why an account deserves outreach now. Area 5 is owned by Todd Busler, not Adam Schoenfeld.

Practical rule: a trigger is useful only when it changes the next action. Treat each signal as a workflow: signal observed, priority adjusted, account or person selected, outreach message or sequence changed.

Local evidence: `research/other/todd-busler/2022-11-16--growing-beyond-net-new.md`

## 6. Deliverability and Sender Infrastructure

Peter Goldstein's material is used only for sender-infrastructure foundations: email hosting, authentication, DKIM, sender identity, domains, and infrastructure hygiene. Do not treat this source as cold-email ramping or mailbox-rotation guidance.

Practical rule: verify the technical basis for sending before scaling outreach. Authentication, sender identity, domain setup, and bounce controls are prerequisites for a responsible outbound motion.

Local evidence: `research/other/peter-goldstein/2026-05-19--email-hosting-infrastructure.md`

## 7. Messaging and Conversation Entry

Will Allred's Lavender benchmark material supports message-quality decisions: relevance, personalization, structure, and reply-oriented writing.

Practical rule: a cold email should convert known account, stakeholder, and timing context into a clear reason to talk. Avoid generic personalization; the opening should show why this company and person are being contacted now.

Local evidence: `research/other/will-allred/2026-03-30--cold-email-benchmark.md`

## 8. Cadence and Channel Orchestration

Jason Bay's 30MPC episode page supports cadence and meeting-booking guidance, though transcript-level evidence was not collected in this run.

Practical rule: design sequences around channel roles and stopping rules. Email, calls, and LinkedIn touches should not repeat the same ask; each touch should add context, reduce friction, or close the loop.

Local evidence: `research/other/jason-bay/2026-04-16--cold-email-masterclass-page.md`

## 9. Live Conversation and Objection Handling

Armand Farrokh's 30MPC source supports live cold-call structure, opening language, and objection handling, though transcript-level evidence was not collected in this run.

Practical rule: live calls should separate reflex resistance from substantive objections. The goal is not to overpower the prospect; it is to earn enough permission to test relevance and identify a useful next step.

Local evidence: `research/other/armand-farrokh/2025-01-08--perfect-cold-call-pitch-page.md`

## 10. Reply Handling, Qualification, and Handoff

Harris Kenny's OutboundSync material supports CRM sync, routing, and outbound operations context for moving replies and engagement data into the right follow-up path.

Practical rule: reply handling is an operations workflow, not just inbox triage. Classify replies, route ownership, update CRM fields, preserve context, and define when a response becomes a qualified sales conversation.

Local evidence: `research/other/harris-kenny/2026-06-22--outboundsync-blog-index.md`

## Workflow

1. Define the commercial fit and ICP.
2. Prioritize accounts by fit and expected value.
3. Map stakeholders and buying-committee roles.
4. Build and verify contact records.
5. Add timing signals that change outreach priority.
6. Confirm sender infrastructure is technically sound.
7. Write messages that connect context to a conversation entry.
8. Sequence touches across channels with spacing and stopping rules.
9. Handle live conversations with clear opening and objection language.
10. Classify, qualify, route, and hand off replies.

## Trade-Offs and Caveats

The strongest collected evidence is in Areas 1, 2, 3, 5, 6, and 7. Areas 8, 9, and 10 have usable fallback records but would benefit from transcript-level collection after Supadata configuration is available. Area 4 remains usable because it is human-approved with a transparent caveat.

The playbook intentionally separates adjacent decisions: Adam Schoenfeld covers account prioritisation, Todd Busler covers timing signals, Nate Nasralla covers stakeholder strategy only, and Harris Kenny covers reply handling and handoff.

## Source Map

| Area | Expert | Primary local evidence |
|---:|---|---|
| 1 | Kyle Vamvouris | `research/other/kyle-vamvouris/2026-03-13--sales-playbook.md` |
| 2 | Adam Schoenfeld | `research/other/adam-schoenfeld/2026-04-08--keyplay-inflection.md` |
| 3 | Nate Nasralla | `research/other/nate-nasralla/2022-05-11--enterprise-sales-playbook.md` |
| 4 | Jesse Ouellette | `research/other/jesse-ouellette/2026-06-08--leadmagic-source-index.md` |
| 5 | Todd Busler | `research/other/todd-busler/2022-11-16--growing-beyond-net-new.md` |
| 6 | Peter Goldstein | `research/other/peter-goldstein/2026-05-19--email-hosting-infrastructure.md` |
| 7 | Will Allred | `research/other/will-allred/2026-03-30--cold-email-benchmark.md` |
| 8 | Jason Bay | `research/other/jason-bay/2026-04-16--cold-email-masterclass-page.md` |
| 9 | Armand Farrokh | `research/other/armand-farrokh/2025-01-08--perfect-cold-call-pitch-page.md` |
| 10 | Harris Kenny | `research/other/harris-kenny/2026-06-22--outboundsync-blog-index.md` |

