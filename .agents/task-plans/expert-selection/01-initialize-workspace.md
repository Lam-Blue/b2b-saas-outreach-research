# Task 01 — Initialize the Expert Research Workspace

## Purpose

Create the working structure inside `output-by-AI/` and register the initial candidate list without conducting research or changing any candidate assessment.

## Required skill

Read the relevant screening and source-capture skills before starting.

## Inputs

* `research/sources.md`
* `research/other/initial-landscape-overview.md`
* `.agents/rules/`
* `.agents/skills/`
* `.agents/task-plans/expert-selection/README.md`

## Allowed changes

Create or update files only inside:

```text
output-by-AI/
```

Do not edit `research/sources.md`.

Do not browse for sources during this task.

## Required outputs

Create these folders:

```text
output-by-AI/candidate-dossiers/
output-by-AI/discovery/
output-by-AI/selection/
```

Create these files:

```text
output-by-AI/README.md
output-by-AI/research-log.md
output-by-AI/source-library.md
```

## Output requirements

### 1. `output-by-AI/README.md`

Write a concise workspace guide containing:

* project purpose
* statement that `research/sources.md` remains frozen until final publish
* explanation of the role of each working file and folder
* the task sequence from the workflow README
* a reminder that source records must be reusable for later insight retrieval

Do not copy the full selection criteria into this file.

### 2. `output-by-AI/research-log.md`

Create a dashboard with one row for every initial candidate currently listed in `research/other/initial-landscape-overview.md`.

Use this structure:

| Candidate | Origin | Research stage | Practitioner evidence | Proven area | Usable material | Source IDs | Key gaps | Provisional status |
| --------- | ------ | -------------- | --------------------- | ----------- | --------------- | ---------- | -------- | ------------------ |

Initial values:

* Origin: `Initial list`
* Research stage: `Not started`
* All evidence, area, material, source ID, gap, and status cells: `—`

Allowed provisional statuses later:

* `Potentially advance`
* `Needs verification`
* `Do not advance`

These are working statuses only. They are not final selection decisions.

### 3. `output-by-AI/source-library.md`

Create an empty, searchable source index using this structure:

| Source ID | Expert | Origin | Source type | Published | Tags | Use | Canonical URL | Local record | Retrieval note |
| --------- | ------ | ------ | ----------- | --------- | ---- | --- | ------------- | ------------ | -------------- |

Allowed values for `Use`:

* `Practitioner verification`
* `Later insight retrieval`
* `Both`

### 4. Candidate name extraction

Extract the initial candidate names exactly as they appear in `research/other/initial-landscape-overview.md`.

Do not:

* infer alternative spellings
* add new candidates
* assign an area
* rank candidates
* create candidate dossiers yet

## Completion condition

This task is complete only when:

* all required workspace files and folders exist
* every initial candidate has one row in `research-log.md`
* no research has been performed
* `research/sources.md` remains unchanged
