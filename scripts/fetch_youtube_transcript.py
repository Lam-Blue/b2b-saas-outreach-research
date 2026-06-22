
"""
Fetch one approved YouTube transcript from Supadata and save it as Markdown.

Run from the repository root:

python3 scripts/fetch_youtube_transcript.py 
--expert "Jason Bay" 
--url "https://www.youtube.com/watch?v=VIDEO_ID" 
--title "Cold Email Cadence Masterclass" 
--published "2026-03-18" 
--areas "Area 8 — Cadence and Channel Orchestration" 
--why "Explains how sequencing connects cold email, replies, and booked meetings."
"""

from **future** import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urlencode, urlparse
from urllib.request import Request, urlopen

API_BASE = "https://api.supadata.ai/v1"
REPO_ROOT = Path(**file**).resolve().parents[1]

def load_env_file(path: Path) -> None:
"""Load simple KEY=VALUE pairs without requiring python-dotenv."""
if not path.exists():
return

```
for raw_line in path.read_text(encoding="utf-8").splitlines():
    line = raw_line.strip()

    if not line or line.startswith("#") or "=" not in line:
        continue

    key, value = line.split("=", 1)
    key = key.strip()
    value = value.strip().strip("'").strip('"')

    if key:
        os.environ.setdefault(key, value)
```

def slugify(value: str) -> str:
value = value.lower().strip()
value = re.sub(r"[^a-z0-9]+", "-", value)
value = value.strip("-")
return value or "source"

def extract_youtube_video_id(url: str) -> str:
parsed = urlparse(url)
host = parsed.netloc.lower().replace("[www](http://www).", "").replace("m.", "")

```
if host == "youtu.be":
    video_id = parsed.path.strip("/").split("/")[0]
elif host in {"youtube.com", "youtube-nocookie.com"}:
    query_id = parse_qs(parsed.query).get("v", [""])[0]
    path_parts = [part for part in parsed.path.split("/") if part]

    if query_id:
        video_id = query_id
    elif len(path_parts) >= 2 and path_parts[0] in {"embed", "shorts", "live"}:
        video_id = path_parts[1]
    else:
        video_id = ""
else:
    video_id = ""

if not re.fullmatch(r"[A-Za-z0-9_-]{6,}", video_id):
    raise ValueError(
        "Could not extract a valid YouTube video ID. "
        "Use a normal YouTube watch, short, live, embed, or youtu.be URL."
    )

return video_id
```

def api_get(path: str, params: dict[str, str], api_key: str) -> dict[str, Any]:
query = urlencode(params)
endpoint = f"{API_BASE}{path}"
url = f"{endpoint}?{query}" if query else endpoint

```
request = Request(
    url,
    headers={
        "x-api-key": api_key,
        "Accept": "application/json",
        "User-Agent": "b2b-outreach-research-transcript-tool/1.0",
    },
    method="GET",
)

try:
    with urlopen(request, timeout=90) as response:
        status_code = response.getcode()
        body = response.read().decode("utf-8")
        data = json.loads(body) if body else {}

except HTTPError as error:
    error_body = error.read().decode("utf-8", errors="replace")
    raise RuntimeError(
        f"Supadata returned HTTP {error.code}: {error_body}"
    ) from error

except URLError as error:
    raise RuntimeError(f"Could not reach Supadata: {error.reason}") from error

except json.JSONDecodeError as error:
    raise RuntimeError("Supadata returned invalid JSON.") from error

if status_code == 206:
    raise RuntimeError(
        "Transcript unavailable from Supadata. "
        "Record this source as unavailable instead of selecting a random replacement."
    )

if status_code not in {200, 202}:
    raise RuntimeError(f"Unexpected Supadata status code: {status_code}")

return data
```

def fetch_transcript(
video_url: str,
api_key: str,
language: str,
mode: str,
poll_seconds: float,
max_polls: int,
) -> dict[str, Any]:
response = api_get(
"/transcript",
{
"url": video_url,
"lang": language,
"text": "false",
"mode": mode,
},
api_key,
)

```
job_id = response.get("jobId") or response.get("job_id")

if not job_id:
    return response

for _ in range(max_polls):
    time.sleep(poll_seconds)

    result = api_get(
        f"/transcript/{quote(str(job_id), safe='')}",
        {},
        api_key,
    )

    status = result.get("status")

    if status == "completed":
        return result

    if status == "failed":
        raise RuntimeError(
            f"Supadata transcript job failed: {result.get('error', 'Unknown error')}"
        )

raise RuntimeError(
    "Supadata transcript job did not complete before the polling limit. "
    "The job may still exist, but this script did not save an incomplete result."
)
```

def format_timestamp(milliseconds: Any) -> str:
try:
total_seconds = max(0, int(float(milliseconds) / 1000))
except (TypeError, ValueError):
total_seconds = 0

```
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

if hours:
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

return f"{minutes:02d}:{seconds:02d}"
```

def render_transcript(content: Any) -> str:
if isinstance(content, str):
text = content.strip()

```
    if not text:
        raise RuntimeError("Supadata returned an empty transcript.")

    return text + "\n"

if isinstance(content, list):
    rendered_segments: list[str] = []

    for segment in content:
        if not isinstance(segment, dict):
            continue

        text = str(segment.get("text", "")).strip()

        if not text:
            continue

        timestamp = format_timestamp(segment.get("offset", 0))
        rendered_segments.append(f"**[{timestamp}]** {text}")

    if not rendered_segments:
        raise RuntimeError("Supadata returned no usable transcript segments.")

    return "\n\n".join(rendered_segments) + "\n"

raise RuntimeError("Supadata returned an unsupported transcript format.")
```

def build_markdown(
args: argparse.Namespace,
response: dict[str, Any],
transcript_text: str,
) -> str:
language = response.get("lang") or args.lang
available_languages = response.get("availableLangs") or []
collected_at = datetime.now().astimezone().isoformat(timespec="seconds")

```
available_languages_text = (
    ", ".join(str(item) for item in available_languages)
    if available_languages
    else "Unknown"
)

return f"""# {args.title}
```

* Expert: {args.expert}
* Source type: YouTube video transcript
* Original URL: {args.url}
* Published: {args.published}
* Collected: {collected_at}
* Collection method: Supadata API
* Transcript mode: {args.mode}
* Transcript language: {language}
* Available transcript languages: {available_languages_text}
* Relevant areas: {args.areas}
* Why this matters: {args.why}

## Transcript

{transcript_text}"""

def parse_args() -> argparse.Namespace:
parser = argparse.ArgumentParser(
description="Fetch one approved YouTube transcript through Supadata."
)

```
parser.add_argument("--expert", required=True, help="Expert name.")
parser.add_argument("--url", required=True, help="Public YouTube video URL.")
parser.add_argument("--title", required=True, help="Video title.")
parser.add_argument(
    "--published",
    required=True,
    help="Video publish date in YYYY-MM-DD format.",
)
parser.add_argument(
    "--areas",
    required=True,
    help="Relevant project area(s).",
)
parser.add_argument(
    "--why",
    required=True,
    help="Short explanation of why this video matters for the playbook.",
)
parser.add_argument(
    "--lang",
    default="en",
    help="Preferred transcript language. Default: en.",
)
parser.add_argument(
    "--mode",
    choices=["native", "auto", "generate"],
    default="native",
    help="Supadata transcript mode. Default: native.",
)
parser.add_argument(
    "--poll-seconds",
    type=float,
    default=1.0,
    help="Seconds between async job polls. Default: 1.",
)
parser.add_argument(
    "--max-polls",
    type=int,
    default=300,
    help="Maximum async job polls. Default: 300.",
)
parser.add_argument(
    "--overwrite",
    action="store_true",
    help="Replace an existing transcript file.",
)

return parser.parse_args()
```

def main() -> int:
load_env_file(REPO_ROOT / ".env")
args = parse_args()

```
try:
    date.fromisoformat(args.published)
except ValueError:
    print("--published must use YYYY-MM-DD.", file=sys.stderr)
    return 2

api_key = os.getenv("SUPADATA_API_KEY")

if not api_key or api_key == "replace_with_your_key":
    print(
        "SUPADATA_API_KEY is missing. Copy .env.example to .env and add your key.",
        file=sys.stderr,
    )
    return 2

try:
    video_id = extract_youtube_video_id(args.url)
except ValueError as error:
    print(str(error), file=sys.stderr)
    return 2

expert_slug = slugify(args.expert)
title_slug = slugify(args.title)

output_path = (
    REPO_ROOT
    / "research"
    / "youtube-transcripts"
    / expert_slug
    / f"{args.published}--{title_slug}--{video_id}.md"
)

if output_path.exists() and not args.overwrite:
    print(
        f"Output already exists: {output_path.relative_to(REPO_ROOT)}\n"
        "Use --overwrite only when intentionally replacing it.",
        file=sys.stderr,
    )
    return 1

try:
    response = fetch_transcript(
        video_url=args.url,
        api_key=api_key,
        language=args.lang,
        mode=args.mode,
        poll_seconds=args.poll_seconds,
        max_polls=args.max_polls,
    )

    transcript_text = render_transcript(response.get("content"))
    markdown = build_markdown(args, response, transcript_text)

except RuntimeError as error:
    print(f"Transcript collection failed: {error}", file=sys.stderr)
    return 1

output_path.parent.mkdir(parents=True, exist_ok=True)

temporary_path = output_path.with_suffix(".tmp")
temporary_path.write_text(markdown, encoding="utf-8")
temporary_path.replace(output_path)

print(f"Saved: {output_path.relative_to(REPO_ROOT)}")
return 0
```

if **name** == "**main**":
raise SystemExit(main())
