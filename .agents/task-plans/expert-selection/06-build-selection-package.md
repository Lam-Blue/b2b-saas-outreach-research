# Task 06 — Build the Expert Selection Package

## Purpose

Compare all deep-screened candidates and create the human-review package.

This is the final task before human review.

It must recommend the strongest 10 candidates, explain why others were not selected, and preserve enough evidence for the next research stage.

Do not edit `research/sources.md`.

Do not conduct new research.

## Required skill

Use the expert-screening skill and the synthesis skill.

## Inputs

* `research/sources.md`
* `output-by-AI/research-log.md`
* `output-by-AI/source-library.md`
* all candidate dossiers
* `output-by-AI/discovery/coverage-gap-brief.md`
* `output-by-AI/discovery/external-candidate-leads.md`
* repository rules
* workflow README
* this task file

## Required outputs

Create or update:

```text
output-by-AI/selection/selection-matrix.md
output-by-AI/selection/expert-selection-review.md
```

## 1. `selection-matrix.md`

Create one row for every deep-screened candidate, including both initial and external candidates.

Use the exact criteria and decision logic from `research/sources.md`.

Do not invent a second score, ranking formula, or alternative criterion framework.

Use this structure:

| Candidate | Origin | Proven area | Practitioner evidence | B2B SaaS relevance | Recent usable material | Key source IDs | Strengths | Gaps or risks | Recommendation |
| --------- | ------ | ----------- | --------------------- | ------------------ | ---------------------- | -------------- | --------- | ------------- | -------------- |

Allowed recommendations:

* `Recommended`
* `Strong alternative`
* `Not selected`
* `Needs human decision`

## 2. `expert-selection-review.md`

Write this file for direct human review.

Use this structure:

```md
# Expert Selection Review

## Recommendation summary

State the number of candidates recommended.

Do not force the list to contain 10 people if fewer than 10 candidates meet the required standard.

## Recommended experts

For each recommended expert:

### [Name]

- Proven area:
- Why this person meets the criteria:
- Direct practitioner evidence:
- Key source IDs:
- Useful material for later retrieval:
- Why this person was selected over close alternatives:
- Remaining limitations:

## Coverage map

Map the recommended experts against the areas defined in `research/sources.md`.

State:

- strong coverage
- acceptable overlap
- unresolved gaps
- areas with only one viable expert

## Strong alternatives

List candidates who were close to selection and explain:

- where they fit
- why they were not selected
- when they may be preferable instead

## Not selected or not advanced

Group candidates by reason, such as:

- insufficient practitioner evidence
- weak B2B SaaS relevance
- insufficient recent usable material
- excessive overlap
- outperformed by another candidate
- unresolved identity or evidence gap

## Human decisions required

List only decisions that require human judgment.

For each decision, state:

- the competing options
- relevant evidence
- trade-off
- recommended default
```

## Selection rules

* Select based on evidence, not prior reputation.
* Use the exact criteria in `research/sources.md`.
* Do not select weak candidates merely to force coverage or reach 10 names.
* Prefer the narrowest proven operating area over broad positioning.
* Preserve source IDs for every meaningful recommendation.
* Treat useful public material as a meaningful criterion because it supports the next research phase.
* Explain close calls and exclusions clearly.
* Do not hide gaps.

## Stop condition

After creating the selection package:

* stop
* do not begin Task 07
* do not edit `research/sources.md`
* wait for explicit human approval
