# Transcript Collection Tooling

## Purpose

`fetch_youtube_transcript.py` fetches one pre-approved YouTube transcript through Supadata and saves it in:

```text
research/youtube-transcripts/[expert-slug]/
```

This script is not for bulk downloading a channel.

Use it only after the collection plan has chosen a specific video because it directly supports an assigned research area.

## Setup

From the repository root:

```bash
cp .env.example .env
```

Add the Supadata key to `.env`:

```text
SUPADATA_API_KEY=your_key_here
```

Do not commit `.env`.

No package installation is required. The script uses Python's standard library.

## Basic usage

```bash
python3 scripts/fetch_youtube_transcript.py \
  --expert "Jason Bay" \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --title "Cold Email Cadence Masterclass" \
  --published "2026-03-18" \
  --areas "Area 8 — Cadence and Channel Orchestration" \
  --why "Explains how channel sequencing connects cold email, replies, and booked meetings."
```

The script saves a Markdown file such as:

```text
research/youtube-transcripts/jason-bay/2026-03-18--cold-email-cadence-masterclass--VIDEO_ID.md
```

## Transcript modes

Default:

```text
--mode native
```

Use this first. It fetches existing captions only.

Use this only when the selected source is important enough to justify AI fallback:

```text
--mode auto
```

Do not use `--mode generate` unless the task specifically requires generated transcription.

## Failure rules

* If the transcript is unavailable, do not switch to a random video.
* Record the failed source in the relevant task output, then choose the next approved source for that area.
* If an output file already exists, the script stops rather than fetching the same transcript again.
* Use `--overwrite` only when deliberately replacing a bad or incomplete saved file.

## Metadata standard

Every generated transcript file includes:

* expert
* original URL
* published date
* collection date
* collection method
* requested transcript mode
* relevant area
* why the source matters
* transcript language
* timestamped transcript content
