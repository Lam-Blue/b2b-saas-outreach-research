---
name: synthesize-outbound-source-notes
description: Turn stored expert evidence into concise, source-backed B2B SaaS cold outreach research notes. Use after relevant source records already exist and a task plan defines the target area and output file. Do not use to collect new sources, select experts, or produce unsupported industry claims.
---

# Synthesize Outbound Source Notes

## Purpose

Convert existing evidence files into useful working notes without losing provenance, nuance, or disagreement.

This skill turns source material into research insight. It does not replace source collection or candidate screening.

## Required reading

Before starting:

1. Read all files in `.agents/rules/`.
2. Read `research/sources.md`.
3. Read the active task plan.
4. Read all source files named by the task plan.

Do not search for extra sources unless the task plan explicitly instructs it.

## Workflow

### 1. Map evidence to a research area

Assign each insight to the relevant area already defined in `research/sources.md`.

Do not create broad new categories unless the task plan explicitly asks for them.

### 2. Extract atomic insights

Each insight should answer one practical question.

Use this format unless the task plan defines another:

```md
### [Short operational insight]

- Area:
- Claim:
- Supporting evidence:
- Source references:
- Practical implication:
- Limits or disagreement:
```

### 3. Preserve attribution

Use careful language:

* “X argues…”
* “X’s framework suggests…”
* “Across these sources, a recurring pattern is…”
* “Evidence is limited because…”

Do not write “best practice,” “proven,” or “industry standard” unless the available evidence genuinely supports that level of confidence.

### 4. Separate agreement from disagreement

When experts disagree:

* present both positions
* cite each source record
* explain the scope in which each position may apply
* do not force a single conclusion

### 5. Preserve operational usefulness

A good synthesis note should clarify:

* what the practitioner recommends
* when it applies
* what evidence supports it
* what could make it fail
* how it connects to the outbound system

Do not turn notes into generic summaries or long profiles of the expert.

## Quality gate

Before completing the synthesis, verify:

* Every insight points to one or more stored source records.
* No personal opinion became an unsupported industry fact.
* Duplicates were merged or removed.
* Disagreement and uncertainty remain visible.
* The output uses the task-plan target file only.
* No new material was invented or silently introduced.

## Final response

Use the repository’s standard completion report.
