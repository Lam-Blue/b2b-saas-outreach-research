# Task 04 — Discover External Candidate Leads

## Purpose

Find promising external candidates who could fill a documented coverage gap or outperform a borderline initial candidate.

This is lightweight discovery, not full candidate research.

## Required skill

Use the expert-screening skill for minimum evidence checks.

## Inputs

* `output-by-AI/discovery/coverage-gap-brief.md`
* `output-by-AI/research-log.md`
* `research/sources.md`
* repository rules
* workflow README
* this task file

## Required output

Create:

```text
output-by-AI/discovery/external-candidate-leads.md
```

Use this structure:

| Candidate | Target area | Discovery purpose | Initial practice signal | Material signal | Canonical links | Initial assessment | Status | Reason |
| --------- | ----------- | ----------------- | ----------------------- | --------------- | --------------- | ------------------ | ------ | ------ |

Allowed statuses:

* `Queue for deep screen`
* `Reserve`
* `Rejected`

## Discovery method

For each brief in `coverage-gap-brief.md`:

1. Search for relevant practitioners.
2. Verify a minimum direct-practice signal.
3. Verify a minimum public-material signal.
4. Record the canonical links supporting those signals.
5. Decide whether the candidate merits deep screening.

Do not create a full candidate dossier yet.

Do not add the candidate to `source-library.md` yet.

The discovery log itself is the evidence record for candidates who do not progress.

## Minimum threshold for a deep-screen queue

Queue an external candidate for deep screening only when there is at least:

* one credible signal of direct practice relevant to the target area
* one public source suggesting usable original material
* a plausible connection to B2B SaaS cold outreach or the precise gap being addressed

A candidate with only a polished bio, audience size, or generic advice must not enter the queue.

## Scope control

For each discovery brief:

* identify up to five credible leads
* queue only the smallest number needed for meaningful comparison
* normally queue no more than three candidates per brief
* record `No viable lead found` where targeted discovery fails

Do not endlessly expand the longlist.

Do not start full research inside this task.

## Completion condition

This task is complete only when:

* every gap or challenge brief has either viable leads or an explicit no-lead outcome
* every lead has canonical supporting links
* every queued candidate has a specific reason for deep screening
* no candidate dossier has been created for an unqueued lead
* `research/sources.md` remains unchanged
