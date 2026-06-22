# Task 07 — Publish the Human-Approved Expert Selection

## Purpose

Write the human-approved final expert selection into `research/sources.md`.

This task is allowed only after explicit human approval.

## Required approval input

The user must provide:

* the final approved candidate names
* any changes from `expert-selection-review.md`
* any special wording or inclusion decisions

Do not infer approval from silence or from a previous provisional recommendation.

## Inputs

* `research/sources.md`
* `output-by-AI/selection/selection-matrix.md`
* `output-by-AI/selection/expert-selection-review.md`
* relevant candidate dossiers
* explicit human-approved candidate list
* repository rules
* workflow README
* this task file

## Allowed changes

Edit only:

```text
research/sources.md
```

Do not conduct new research.

Do not alter:

* the selection criteria
* the existing criteria table
* the approved candidate list
* the final areas decided by the human

## Publishing method

Use the existing final-candidate or selection section in `research/sources.md`.

When no such section exists, add one concise section directly after the criteria section:

```md
## Selected Experts
```

For every approved expert, include only:

* name
* narrowest approved area
* concise reason for selection
* evidence references using source IDs or local dossier paths
* concise note on useful material available for the next phase

Do not paste long source excerpts into `research/sources.md`.

Do not copy the full internal review package into the final source file.

## Validation before completion

Verify:

* every published candidate appears in the human-approved list
* no unapproved candidate appears in the final section
* every meaningful claim traces back to a stored source record
* selection criteria remain unchanged
* only the final-selection section was added or updated
* no working artifact outside `research/sources.md` was modified

## Completion report

```md
## Published

### Final candidates written
- [candidate]

### Updated section
- [section name in research/sources.md]

### Evidence references used
- [source IDs or dossier paths]

### Not changed
- Selection criteria
- Working research artifacts
```
