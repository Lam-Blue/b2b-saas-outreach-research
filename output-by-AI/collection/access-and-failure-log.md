# Access and Failure Log

Date: 2026-06-23

## LinkedIn Access Constraints

Public LinkedIn post searches were attempted for all 10 approved experts during the Task 99 collection run. No LinkedIn post was retained because no accessible public post with visible date, full usable text, and clear relevance to the assigned area was captured.

These failed or unavailable LinkedIn attempts are not retained as research sources. The placeholder `availability.md` files were removed from `research/linkedin-posts/`.

Affected experts:

- Kyle Vamvouris
- Adam Schoenfeld
- Nate Nasralla
- Jesse Ouellette
- Todd Busler
- Peter Goldstein
- Will Allred
- Jason Bay
- Armand Farrokh
- Harris Kenny

## Transcript Attempts

Initial transcript attempt:

- Source: Jason Bay, `https://www.youtube.com/watch?v=JX1UNIJwcCY`
- Prior status: failed before a live Supadata request because the script reported `SUPADATA_API_KEY is missing. Copy .env.example to .env and add your key.`
- Recovery status: a later manual Supadata run succeeded for this same approved source. The generated transcript was retained and its metadata was corrected to the approved queue title and YouTube publication date.

Sandbox DNS/network retries:

- Todd Busler and Armand Farrokh initially hit sandbox DNS resolution errors. The same approved queue items were retried through the permitted network path and succeeded.

## Cleanup

Removed from `research/` because they were access/failure notes rather than retained source material:

- `research/linkedin-posts/*/availability.md`
- `research/linkedin-posts/README.md`
- `research/youtube-transcripts/README.md`
- `research/other/README.md`

Removed from `research/other/` because attribution did not meet the retained-source standard:

- `research/other/peter-goldstein/2026-05-19--email-hosting-infrastructure.md`: the page covered email-hosting infrastructure but was not attributable to Peter Goldstein in the captured source record. It was not used in `research/sources.md` or `FINAL.md`.
