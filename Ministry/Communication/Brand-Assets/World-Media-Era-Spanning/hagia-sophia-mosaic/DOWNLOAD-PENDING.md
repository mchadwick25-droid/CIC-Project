# Download pending — network egress blocked

This folder's image file has not been downloaded yet. `upload.wikimedia.org`
is blocked by this sandbox's network egress policy (confirmed via direct
curl and WebFetch, both returned an explicit egress-block error, not a
transient rate limit) — the same class of restriction `CLAUDE.md` already
notes for the patristic text hosts, just extended to Wikimedia's own image
CDN. `commons.wikimedia.org` is blocked the same way, which is also why
license verification for these images had to go through en.wikipedia.org's
own federated MediaWiki API instead (see the folder README one level up).

**Direct URL to fetch:**
https://upload.wikimedia.org/wikipedia/commons/a/a2/Christ_Pantocrator_Deesis_mosaic_Hagia_Sophia.jpg

License, author, and full sourcing already verified — see
`../era-spanning-media-sources.json` and `../README.md`. Once downloaded,
save the file at the path this folder's own JSON entry names and delete
this placeholder.
