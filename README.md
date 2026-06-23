# B2B SaaS Cold Outreach Research

This project researches how a B2B SaaS cold-outreach motion should work from end to end: from deciding which companies are worth pursuing to handling a reply once it arrives.

The final output is a practical playbook, but the project is built around the research process behind it: expert selection, evidence collection, source validation, and synthesis.

* Read [`FINAL.md`](./FINAL.md) for the finished cold-outreach playbook.
* Read [`research/sources.md`](./research/sources.md) for the retained evidence library.
* Read this file for the project design, workflow, tooling, and repository structure.

The final library contains:

* 10 approved practitioners, each assigned to one part of the outbound workflow;
* 6 YouTube transcripts collected through the Supadata API;
* 12 retained supporting sources;
* no retained LinkedIn posts, because the accessible material did not meet the project’s evidence standard.

## Research design

Cold outreach is often reduced to writing better emails. This project takes a wider view.

A message cannot fix poor account fit. A good account does not automatically have a reason to buy now. Valid contact data does not guarantee delivery. A reply is not automatically a qualified opportunity.

For that reason, the research was divided into ten separate decision areas covering:

* commercial fit and ICP;
* account prioritisation;
* stakeholder mapping;
* contact data and verification;
* timing signals;
* sender infrastructure;
* messaging;
* sequencing;
* live conversation;
* reply handling and handoff.

The aim was not to collect generic sales advice. Each area needed an expert whose work clearly matched that part of the workflow.

Expert selection was kept separate from collection and synthesis:

```text id="r50pft"
Expert selection
→ source collection
→ evidence audit
→ final synthesis
```

This prevented the expert list from drifting once research had started.

## Expert and source standards

The project prioritised practitioners over commentators.

Each expert was screened against three questions:

1. Do they have credible operating, product, or practitioner evidence in the assigned area?
2. Is there attributable material that can support a later claim?
3. Does their expertise add distinct coverage rather than duplicate another expert?

A retained source also needed to be useful, traceable, and specific enough to support the final synthesis.

Each source record includes:

* expert and assigned area;
* source type and canonical URL;
* publication date or an explicit date limitation;
* collection method;
* a concise note on why the source matters;
* bounded evidence such as an excerpt, timestamp, or source note;
* relevant caveats.

The project did not keep material simply because it was easy to find.

For example, LinkedIn posts were only retained when the full text was accessible, the date was visible, and the content directly supported the expert’s assigned area. No LinkedIn source met those conditions, so no placeholder post records remain in `research/`.

Access limitations and failed collection attempts are kept separately:

```text id="mrdfxc"
output-by-AI/collection/access-and-failure-log.md
```

A failed search is not evidence.

## Collection workflow and tooling

Long-form video material was collected through the Supadata API.

The collection utility is located at:

```text id="v1sjru"
scripts/fetch_youtube_transcript.py
```

It reads `SUPADATA_API_KEY` from a local `.env` file, fetches approved YouTube transcripts, and stores them as Markdown with source metadata and timestamps.

```text id="tjqgfh"
.env              # local only; never committed
.env.example      # committed placeholder
```

Transcript collection was controlled through a queue. A video had to be selected for a specific research area before it could be fetched. This avoided pulling transcripts first and trying to justify them later.

The planning and audit trail lives in:

```text id="sfgydm"
output-by-AI/collection/
```

## Evidence recovery

The initial collection pass created too many availability records for inaccessible LinkedIn content. Those files made the folder structure look complete, but they were not useful research artifacts.

The collection process was corrected before final synthesis:

* placeholder availability files were removed from `research/`;
* access constraints were moved into a separate log;
* the Supadata workflow was validated with a live request;
* six approved long-form transcripts were collected;
* weak or incorrectly attributed sources were removed;
* `research/sources.md` and `FINAL.md` were rebuilt using retained evidence only.

This was an important quality-control step. A complete-looking folder structure is not the same thing as a usable source library.

## Repository structure

```text id="zfddo1"
.
├── .agents/
│   ├── rules/                         # Evidence, collection, and repository-writing rules
│   ├── skills/                        # Reusable research and synthesis guidance
│   └── task-plans/                    # Sequenced plans used during the project
│
├── scripts/
│   ├── fetch_youtube_transcript.py    # Supadata transcript collection utility
│   └── README.md                      # Script usage notes
│
├── research/
│   ├── sources.md                     # Retained expert and source inventory
│   ├── linkedin-posts/                # Retained public LinkedIn posts, when available
│   ├── youtube-transcripts/           # Supadata-fetched transcript records
│   └── other/                         # Articles, guides, and supporting sources
│
├── output-by-AI/
│   └── collection/                    # Collection plans, queue, audits, and access logs
│
├── FINAL.md                           # Final B2B SaaS cold-outreach playbook
├── .env.example                       # Environment variable placeholder
└── .gitignore
```

## How to inspect the work

The repository can be read in three layers.

### 1. Start with the final synthesis

Open:

```text id="sdr6gc"
FINAL.md
```

This is the practical output: an end-to-end cold-outreach playbook built from the retained evidence.

### 2. Trace claims to their source material

Open:

```text id="5f8x70"
research/sources.md
```

It lists each selected expert, their assigned area, retained materials, canonical URLs, dates, annotations, and local paths.

### 3. Inspect the working method

Review:

```text id="ahwz4v"
.agents/
scripts/
output-by-AI/collection/
```

These folders show how the work was planned, collected, audited, and separated from inaccessible or unsupported material.

## Limitations

This is practitioner-led research, not a controlled study of outbound effectiveness.

The source library includes transcripts, first-party articles, company materials, and technical documentation. These sources are useful for understanding how experienced operators frame decisions and build workflows, but they should not be treated as proof that one tactic will work in every market.

A few limitations are especially relevant:

* Jesse Ouellette’s Area 4 material is relevant and attributable, but direct operator-role proof was not captured.
* Peter Goldstein’s Area 6 source supports sender-authentication foundations only. It is not used for current cold-email scaling advice.
* Transcript captions may contain minor imperfections, so they are used for operating insight rather than polished direct quotation.
* No LinkedIn posts were retained because the available material did not meet the evidence standard.

The project is designed to be inspectable and extendable. New sources can be added, weak evidence can be replaced, and the playbook can be updated without losing the reasoning behind earlier decisions.
