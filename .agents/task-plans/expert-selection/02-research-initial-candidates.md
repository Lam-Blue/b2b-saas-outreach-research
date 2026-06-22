# Task 02 — Research the Initial Candidate List

## Purpose

Research every candidate from the initial list, verify practitioner credibility, preserve useful public material, and create a reusable candidate dossier.

This task does not select final experts.

## Required skill

Use the expert-screening and public-material collection skills.

## Inputs

* `research/sources.md`
* `output-by-AI/research-log.md`
* `output-by-AI/source-library.md`
* `.agents/rules/`
* `.agents/skills/`
* workflow README
* this task file

## Scope

Research only candidates whose `Origin` is `Initial list` in `output-by-AI/research-log.md`.

Process them one by one.

Do not add or research external candidates in this task.

## Candidate research workflow

For each candidate:

### 1. Resolve identity

Confirm that the public profile, company, content, or source belongs to the correct person.

Record meaningful ambiguity in the dossier.

Do not assume two people with similar names are the same person.

### 2. Verify practitioner credibility

Look for direct evidence that the candidate practises, operates, advises on, or has directly built work relevant to B2B SaaS cold outreach.

Prioritise:

* current or recent operating roles
* founder or agency work with clear outbound relevance
* direct first-hand process explanations
* case studies or documented systems
* credible public discussion of work personally performed

Do not treat follower count, podcast appearances, polished branding, or generic sales advice as sufficient proof.

### 3. Capture useful material

During practitioner verification, also save public material that could be useful in a later research phase.

Examples include:

* original LinkedIn posts
* YouTube videos
* podcast appearances
* newsletters
* case studies
* first-party company pages
* interviews with direct statements from the candidate

Capture material only when it is relevant to one or more project areas defined in `research/sources.md`.

Prefer original, operational, and recent material.

### 4. Create or update the candidate dossier

Create:

```text
output-by-AI/candidate-dossiers/[candidate-slug]/
```

Create:

```text
output-by-AI/candidate-dossiers/[candidate-slug]/dossier.md
output-by-AI/candidate-dossiers/[candidate-slug]/sources/
```

Use this dossier structure:

```md
# [Candidate Name]

- Origin: Initial list
- Identity status:
- Current or recent verified role:
- Research stage:
- Provisional status:

## Practitioner evidence

Summarise only evidence supported by saved source records.

## Criterion assessment

Assess the candidate using the exact criteria and area definitions in `research/sources.md`.

Do not invent new criteria or scoring systems.

## Narrowest proven area

State one primary area and, only where evidence supports it, one secondary area.

Do not assign broad labels without proof.

## Useful material for later retrieval

List source IDs and explain what each source may contribute later.

## Evidence gaps and uncertainty

List missing proof, unclear role details, missing dates, inaccessible material, or weak B2B SaaS relevance.

## Research conclusion

State one provisional status:

- Potentially advance
- Needs verification
- Do not advance
```

### 5. Create source records

Create one source record for every source worth retaining.

Use this naming format:

```text
[candidate-slug]-[source-type]-[number].md
```

Examples:

```text
jason-bay-li-01.md
becc-holland-pod-01.md
will-allred-web-02.md
```

Store each record inside the candidate’s `sources/` folder.

Use this structure:

```md
# [Source ID] — [Candidate] — [Short Source Title]

- Candidate:
- Origin:
- Source type:
- Canonical URL:
- Published:
- Accessed:
- Tags:
- Use: Practitioner verification / Later insight retrieval / Both
- Source status: Accessible / Partially accessible / Inaccessible

## Evidence

> Exact relevant excerpt.

For video or podcast material:

- Timestamp:
- Exact relevant excerpt:

## What this shows

Explain precisely what the source proves or contributes.

## Later retrieval note

State the specific framework, example, insight, or angle worth revisiting later.

## Limits

State missing date, partial access, unsupported claims, overlap with another source, or other uncertainty.
```

Do not save full transcripts, full LinkedIn posts, or copied articles.

### 6. Update shared working files

For every saved source:

* add one row to `output-by-AI/source-library.md`
* link to the local source record
* add searchable area tags
* write a concise retrieval note

After each candidate:

* update that candidate’s row in `output-by-AI/research-log.md`
* update the dossier research stage
* add source IDs
* state gaps honestly

## Research depth standard

Aim for enough evidence to make a provisional assessment, not to collect everything the candidate has ever published.

Normally retain two to five high-signal sources per candidate.

Retain more only when each additional source contributes a distinct project area or valuable later insight.

When evidence remains insufficient after targeted research, record the gap and move on.

Do not force a negative conclusion merely because evidence is unavailable.

## Completion condition

This task is complete only when every initial candidate has:

* a dossier or an explicit documented evidence gap
* at least one saved source record or a clear statement that no reliable source was found
* an updated research-log row
* a provisional status
* source references where relevant

Do not begin external discovery during this task.

Do not edit `research/sources.md`.
