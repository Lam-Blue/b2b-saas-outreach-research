# Content Collection and Final Synthesis — Task List

## Workflow principle

Collection is driven by the assigned research area and a concrete playbook question.

Do not collect content merely because an expert has a recent post or video.

Every collected item must answer:

1. Which area does this support?
2. What practical question can it help answer?
3. Why is this source more useful than a generic post or video?
4. Can it later support a claim in `FINAL.md`?

`research/sources.md` is the inventory of selected experts and collected materials.

`FINAL.md` is the final evidence-backed practical synthesis.

`README.md` is written last and explains the project approach, workflow, tooling, and repository structure.

---

## Task 00 — Create the Area Collection Plan

### Purpose

Translate the approved 10 experts into a collection plan before collecting any posts or transcripts.

### Create

```text
output-by-AI/collection/area-collection-plan.md
output-by-AI/collection/collection-status.md
```

### For each area, define

* area name
* assigned expert
* playbook question
* preferred short-form source
* preferred deep source
* fallback source type
* source-selection reason
* collection status

### Example

```text
Area 5 — Timing and Trigger Signals
Expert: Todd Busler
Question: Which trigger signals should change account priority or outreach cadence?
Short-form target: recent post about champion changes, closed-lost accounts, or event triggers.
Deep-source target: article, podcast, or talk showing signal → prioritisation → outreach action.
Do not collect: generic pipeline motivation or broad intent-data claims.
```

### Completion condition

Every selected expert has an assigned area, a research question, and a planned source path.

Do not collect source material yet.

---

## Task 01 — Collect Targeted LinkedIn Material: Areas 1–5

### Scope

Collect recent, area-relevant LinkedIn material for:

1. Kyle Vamvouris
2. Adam Schoenfeld
3. Nate Nasralla
4. Jesse Ouellette
5. Todd Busler

### Required output

```text
research/linkedin-posts/[expert-slug]/
```

For each expert:

* collect one recent relevant LinkedIn post where publicly accessible
* create one Markdown file per retained post
* include original URL, publication date, collection date, area, and annotation
* explain why the post matters for the playbook

If no public LinkedIn post can be collected:

```text
research/linkedin-posts/[expert-slug]/availability.md
```

Record:

* where the search was attempted
* why no usable public post was retained
* the fallback source type chosen in the area collection plan

### Important rule

“Latest” means the most recent relevant public material found.

Do not retain an irrelevant recent post merely because it is newer.

---

## Task 02 — Collect Targeted LinkedIn Material: Areas 6–10

### Scope

Collect recent, area-relevant LinkedIn material for:

6. Peter Goldstein
7. Will Allred
8. Jason Bay
9. Armand Farrokh
10. Harris Kenny

### Required output

Same structure and metadata rules as Task 01.

### Completion condition for Tasks 01 and 02

Every selected expert has either:

* at least one retained LinkedIn post, or
* an explicit availability record and documented fallback path.

---

## Task 03 — Select Deep Sources and Build the Transcript Queue

### Purpose

Choose the exact long-form sources worth collecting before any transcript API call.

### Create

```text
output-by-AI/collection/transcript-queue.md
```

### Required selection

Choose approximately 5–6 high-value YouTube videos or podcast videos.

Prioritise sources that give operational depth for the areas most likely to become the final playbook backbone:

* Area 2 — account prioritisation
* Area 5 — trigger signals
* Area 7 — messaging
* Area 8 — cadence
* Area 9 — live conversation
* Area 10 — reply handling and handoff

Use `research/other/` rather than forcing a YouTube transcript for areas where video is not the best format, especially:

* Area 4 — data, enrichment, and verification
* Area 6 — sender infrastructure

### Queue format

| Expert | Area | Video or podcast title | URL | Published | Why this source is worth fetching | Transcript mode |
| ------ | ---- | ---------------------- | --- | --------- | --------------------------------- | --------------- |

Default transcript mode:

```text
native
```

Use `auto` only for a source that is explicitly valuable enough to justify fallback transcription.

### Completion condition

Every queued transcript has a specific area, question, URL, date, and reason.

Do not fetch a transcript before it appears in the queue.

---

## Task 04 — Fetch Approved Transcripts Through Supadata

### Purpose

Use the prepared script and Supadata API to collect transcripts for the approved queue.

### Tooling

```text
scripts/fetch_youtube_transcript.py
.env
```

### Output

```text
research/youtube-transcripts/[expert-slug]/
```

### Rules

* Run the script only for sources listed in `transcript-queue.md`.
* Store the generated Markdown output without manually stripping transcript metadata.
* Keep transcript timestamps.
* Do not retry with random videos when a transcript is unavailable.
* If a transcript fails, record the failure in the collection plan and use a pre-approved fallback source.

### Completion condition

At least five API-fetched transcripts are stored, or every unavailable transcript has a documented fallback source.

---

## Task 05 — Collect Supporting Material in `research/other/`

### Purpose

Fill depth gaps with first-party articles, newsletters, podcast pages, case studies, or public talks.

### Priorities

Prioritise material for:

* Jesse Ouellette: enrichment, verification, data quality, Clay workflows
* Peter Goldstein: DKIM, sender authentication, domain trust, infrastructure
* any expert whose LinkedIn post is useful but too shallow to support a practical playbook section

### Output

```text
research/other/[expert-slug]/
```

### Required metadata per file

* expert
* source type
* original URL
* published date
* collected date
* collection method
* relevant area
* why this matters
* limitations or caveats

### Completion condition

Every area has enough usable material to support a practical section in `FINAL.md`.

---

## Task 06 — Audit Collection Coverage and Update `research/sources.md`

### Purpose

Turn the collected material into a clean inventory without writing the final synthesis yet.

### Update

```text
research/sources.md
```

### Required format per expert

* name
* assigned primary area
* expert/profile link
* collected LinkedIn materials
* collected transcript materials
* collected supporting materials
* date for each item
* one-sentence annotation for each item
* local file path where relevant

### Audit checks

* all 10 approved experts appear
* all 10 areas have material
* every source has a canonical URL
* every retained source has a date or an explicit undated label
* every transcript says `Collection method: Supadata API`
* no source was kept only because it was easy to find
* no source claim exceeds what its material supports

### Create

```text
output-by-AI/collection/collection-audit.md
```

This file should list:

* coverage by area
* missing or weak material
* inaccessible LinkedIn sources
* failed transcript jobs
* fallback material used
* sources best suited for `FINAL.md`

---

## Task 07 — Write `FINAL.md`

### Purpose

Write the final evidence-backed B2B SaaS cold outreach playbook.

### Output

```text
FINAL.md
```

### Required structure

```text
# B2B SaaS Cold Outreach Playbook

## Scope and evidence base

## 1. Commercial fit, ICP, and problem context
## 2. Account prioritisation and account research
## 3. Stakeholder mapping and buying-committee strategy
## 4. Contact data, enrichment, and verification
## 5. Timing and trigger signals
## 6. Deliverability and sender infrastructure
## 7. Messaging and conversation entry
## 8. Cadence and channel orchestration
## 9. Live conversation and objection handling
## 10. Reply handling, qualification, and handoff

## End-to-end operating workflow
## Trade-offs and caveats
## Source map
```

### Writing rules

* Write as a practical playbook, not ten mini-biographies.
* Synthesize across evidence.
* Attribute ideas through source IDs or local file paths.
* State when advice is conditional or context-specific.
* Keep Peter Goldstein scoped to technical sender infrastructure.
* Keep Jesse Ouellette’s selection caveat transparent where relevant.
* Do not invent universal “best practices” from one expert’s opinion.
* Use clear, natural English. Avoid generic AI-style marketing language.

### Completion condition

Every substantive recommendation in `FINAL.md` can be traced to collected material.

---

## Task 08 — Commit and Push Research + Final Synthesis

### Commit scope

```text
research/
FINAL.md
output-by-AI/collection/
```

### Suggested commit message

```text
research: collect expert materials and add outreach playbook
```

Push after confirming:

```bash
git status
git diff --check
```

---

## Task 09 — Write the Final `README.md`

### Purpose

Document how the project was designed and executed.

### README should explain

* research topic and objective
* why the expert selection is practitioner-led
* area-based collection method
* why sources were selected rather than collected randomly
* LinkedIn collection approach
* Supadata transcript API tooling
* source organization
* evidence and limitation rules
* repository structure
* link to `FINAL.md`

### README should not

* repeat the full playbook
* repeat every source annotation
* pretend all work was fully automated
* hide caveats or fallback collection methods

---

## Task 10 — Final Commit and Push

### Commit scope

```text
README.md
.agents/
scripts/
.env.example
.gitignore
```

### Suggested commit message

```text
docs: document research workflow and collection tooling
```

Push after confirming the repository is clean.
