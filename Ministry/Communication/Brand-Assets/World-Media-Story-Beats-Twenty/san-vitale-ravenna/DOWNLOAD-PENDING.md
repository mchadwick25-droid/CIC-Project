# Download pending — the one file not yet retrieved

19 of this set's 20 images downloaded successfully once the sandbox's network
allowlist was widened to include Wikimedia's image domains directly. This one
did not, for a different reason than the original network block:

- The Wayback Machine stopgap (used as a workaround before the allowlist
  change, and re-checked after) returned a clean HTTP 404 for this exact file
  — it was never crawled/archived, unlike most of this set.
- A direct fetch from `upload.wikimedia.org` hit Wikimedia's own edge rate
  limiter (HTTP 429) after this session's earlier burst of requests during
  testing. That limiter should clear with time; a plain retry later should
  succeed.

**Direct URL to fetch:**
https://upload.wikimedia.org/wikipedia/commons/6/68/Ravenna_Basilica_di_San_Vitale_-_mosaici.JPG

(Or the thumbnail form, which is friendlier to Wikimedia's servers and plenty
for web use: append `/thumb` after `/commons` and `/1600px-Ravenna_Basilica_di_San_Vitale_-_mosaici.JPG`
after the filename.)

License, author, and full sourcing already verified — see
`../story-beats-twenty-sources.json` and `../README.md`. Once downloaded,
save the file at `san-vitale-mosaici.jpg` in this folder and delete this
placeholder.
