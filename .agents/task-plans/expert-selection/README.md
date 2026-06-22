# Expert Selection Workflow

## Goal

Build an evidence-backed recommendation for the best 10 experts for the B2B SaaS cold outreach research project.

The workflow must:

1. screen the initial candidate list in `research/sources.md`
2. preserve useful public material for later insight retrieval
3. identify weak coverage, overlap, and candidate gaps
4. discover and screen stronger external alternatives where needed
5. produce a human-reviewable recommendation package
6. update `research/sources.md` only after explicit human approval

## Final decision authority

The human makes the final selection decision.

The agent may recommend, compare, and flag uncertainty. It must not publish candidate decisions into `research/sources.md` until the human explicitly approves a final list.

## Required reading before every task

Read, in this order:

1. All applicable files in `.agents/rules/`
2. The relevant file in `.agents/skills/`
3. `research/sources.md`
4. This workflow file
5. The active task file
6. Required outputs from earlier completed tasks

`research/sources.md` is the source of truth for:

* selection criteria
* candidate names in the initial list
* area definitions
* review fields
* final output structure

Do not recreate or alter those criteria elsewhere.

## Workspace ownership

The human creates only this root folder:

```text
output-by-AI/
```

Task 01 creates every required file and subfolder inside it.

All research working files must remain inside `output-by-AI/`.

Do not create research artifacts elsewhere in the repository.

## Task sequence

Run these tasks in order:

1. `01-initialize-workspace.md`
2. `02-research-initial-candidates.md`
3. `03-map-coverage-and-gaps.md`
4. `04-discover-external-candidates.md`
5. `05-deep-screen-external-candidates.md`
6. `06-build-selection-package.md`

After Task 06, stop and wait for human review.

Run this task only after explicit human approval:

7. `07-publish-approved-selection.md`

## Working output structure

Task 01 creates this structure:

```text
output-by-AI/
  README.md
  research-log.md
  source-library.md

  candidate-dossiers/
    [candidate-slug]/
      dossier.md
      sources/
        [source-id].md

  discovery/
    coverage-gap-brief.md
    external-candidate-leads.md

  selection/
    selection-matrix.md
    expert-selection-review.md
```

Not every folder or file needs content immediately. Create detailed candidate folders only when a candidate is actually researched.

## Shared operating rules

* Work sequentially through the tasks without asking for human review between Tasks 01 and 06.
* Update persistent outputs as work progresses so the workflow can resume after interruption.
* Do not edit `research/sources.md` before Task 07.
* Do not add candidates directly to the final selection.
* Do not use candidate reputation, audience size, or generic content as proof of practitioner credibility.
* Do not create a second version of the selection criteria.
* Do not copy full third-party transcripts, posts, or articles into the repository.
* Save only the excerpts, timestamps, and summaries needed for verification and later retrieval.
* A task may add narrower constraints, but may not weaken a repository rule.

## Standard progress report

At the end of every task, report:

```md
## Completed

### Files created or updated
- [path]

### Work completed
- [candidate, source, or output]: [result]

### Evidence gaps or limitations
- [item]: [specific gap]

### Next task
- [task file]
```
