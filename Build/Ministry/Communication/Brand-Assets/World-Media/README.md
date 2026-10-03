# World Media — historical site photographs

**Hold lifted, 2026-09-16.** Pulled from live use 2026-07-24 pending a rights
question (see history below); Mark reviewed the reasoning and cleared these for
use, with attribution displayed on any page they appear on. First live use:
a homepage filmstrip on `cic-website/index.html`, cropped copies at
`cic-website/assets/history/`.

**How it was resolved, stated plainly rather than overclaimed:** this thread's
own license research found all 5 non-public-domain files verified CC BY-SA via
the Wikimedia API directly — free to use with attribution, not payment — against
Mark having been told 5 of the 6 needed permission and payment. A live re-check
this session could not reach `commons.wikimedia.org` or `api.wikimedia.org`
(both blocked by this environment's network egress), so the license text itself
was **not independently re-fetched**. The case for lifting the hold instead rests
on structural reasoning: Wikimedia Commons has no paid-license tier at
all — everything on it is CC-licensed or public domain by the platform's own
design — so a "requires payment" claim couldn't have come from actually reading
these Commons pages, and the per-file metadata (different CC BY-SA versions,
named individual photographers) is consistent with a genuine lookup, not a
fabricated blanket claim. Mark accepted this reasoning and lifted the hold
knowingly, not from a full independent re-verification. If these are ever
scrutinized, re-fetch each `source_url` from an unblocked network first.

**Original hold, for the record:** Mark was told 5 of these 6 photos need
permission and payment to use. That's not what this thread's own license
research found (all 5 were verified CC BY-SA via the Wikimedia API directly —
free to use with attribution, not payment), so this was either a real licensing
wrinkle this research missed, or someone/something conflating "requires
attribution" with "requires payment." At the time: removed from
`cic-poc/frontend/public/images/world-media/` and un-wired from
`worldMedia.ts`/`WorldSelector.tsx` (portraits are unaffected — those are
AI-generated, no third-party rights question applies). Whether these are
re-wired into the app itself, beyond the website homepage, is a separate,
still-open question.

One real, historically-matched architectural/artifact photo per world, for use as
each World Selector tile's background (per Mark's design: architecture/artifact fills
the tile, the Representative's profile portrait sits in the upper-right corner —
profile portraits live in `../Representative-Portraits/`).

All six were sourced from Wikimedia Commons, verified individually for a genuine
regional/period match and an actual open license — not stock imagery. Full reasoning
for each: `Build/Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`.

## Files

| Folder | Image | World |
|---|---|---|
| `house-churches/` | `ephesus-terrace-houses.jpg` | House-Churches |
| `alexandria/` | `kom-el-shoqafa-catacombs.jpg` | Alexandria Catechetical School |
| `syriac/` | `dura-europos-church.jpg` | Syriac Christianity |
| `empire/` | `hagia-irene.jpg` | Church and Empire |
| `desert/` | `monastery-saint-macarius.jpg` | Desert Monasticism |
| `bethlehem/` | `grotto-of-st-jerome.jpg` | Bethlehem Circle |

## Sourcing metadata — `world-media-sources.json`

One JSON object per world, keyed by the same `world_id` used everywhere else in this
project. Each entry has `title`, `location`, `period`, `story` (why this specific
site/artifact connects to that world — the text for a "click the photo to learn more"
feature), `source_url`, `author`, `license`, and a ready-to-use `attribution` string.

**License note — every image requires visible attribution except one.** All six are
CC BY-SA (2.0 through 4.0) except Hagia Irene, which is public domain. CC BY-SA
requires crediting the photographer and linking the license on the page the image
appears on — the `attribution` field in the JSON has the exact text to show. None of
these are CC0/fully unrestricted; don't strip the credit when these go live.

## Honest caveats, carried over from the sourcing research

A few of these show the right historical *site*, not necessarily fabric physically
dating to the world's own exact years — noted per-entry in the JSON `period`/`story`
fields, and worth keeping visible if this ever gets scrutinized (e.g. the Macarius
monastery's standing buildings are later rebuilds on the original ground; the Grotto
of St. Jerome's altars are later Franciscan-era additions to an authentic cave). This
matches the project's standing discipline of not overclaiming accuracy.
