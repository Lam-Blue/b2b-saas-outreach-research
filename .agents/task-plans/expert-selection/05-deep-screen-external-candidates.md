# Task 05 — Deep-Screen External Candidates

## Purpose

Research only external candidates marked `Queue for deep screen`.

Apply the same evidence standard used for the initial candidate list so every candidate can be compared fairly.

## Required skills

Use the expert-screening and public-material collection skills.

## Inputs

* `output-by-AI/discovery/external-candidate-leads.md`
* `output-by-AI/discovery/coverage-gap-brief.md`
* `output-by-AI/research-log.md`
* `output-by-AI/source-library.md`
* `research/sources.md`
* repository rules
* workflow README
* this task file

## Scope

Research only candidates marked:

```text
Queue for deep screen
```

Do not research `Reserve` or `Rejected` candidates.

Do not discover additional candidates during this task.

## Research workflow

For every queued candidate:

1. Create a candidate dossier in:

```text
output-by-AI/candidate-dossiers/[candidate-slug]/
```

2. Set:

```text
Origin: External discovery
```

3. Apply the full workflow from Task 02:

   * resolve identity
   * verify direct practitioner evidence
   * capture useful public material
   * create source records
   * update source library
   * update research log
   * map the narrowest proven area
   * record material available for later retrieval
   * assign a provisional status

4. Compare the candidate specifically against the gap or challenge brief that caused their discovery.

In the dossier, add this section:

```md
## Comparison relevance

- Discovery brief addressed:
- Why this candidate may improve the initial pool:
- Evidence supporting that possibility:
- Remaining limitations:
```

## Completion condition

This task is complete only when every queued external candidate has:

* a full dossier or an explicit research failure record
* source records where material is retained
* an updated research-log row
* a provisional status
* a clear comparison note against the relevant discovery brief

Do not build the final shortlist in this task.

Do not edit `research/sources.md`.
