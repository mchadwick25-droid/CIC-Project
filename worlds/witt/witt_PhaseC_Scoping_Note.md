# Phase C Scoping Note — Lutheran Wittenberg & Its Congregations (witt)

**Date:** 2026-09-19. **Status:** Phase C recon complete. Two genuine content
defects found and fixed directly (both self-inflicted during this build's
own B-4 and Answer-the-Canon authoring passes). Four small, disclosed,
precedented `ACCEPTED_OPEN` entries added. The bulk of "deployment wiring"
is confirmed structurally deferred until after a Representative portrait is
decided and M3 admission happens, per real fleet precedent — not a
build-thread task to force now.

## What the governing process document says, and why it doesn't apply as written

`reference/method/CiC_Record_Native_World_Build_Process_V1.5.md` §4 ("Phase
C — Deployment wiring") describes: an `app/world_manifest.py` entry, two
hand-synced frontend points (`SpeakerName` union, `MessageBubble.tsx`
`REPRESENTATIVE_NAMES`), vector indices built at Docker build time, a
Dockerfile audit, `HARD_CEILING_WORLDS` (`app/graph/nodes.py`),
`POST_HISTORY_GUARD` wiring (`wrs/views/segments/guards.py`), and a live
smoke test against a Docker/Render-deployed site.

**None of this exists in the current repository** — confirmed directly:
`app/` does not exist anywhere in this tree; `cic-poc/backend/` is gone.
This is the identical class of finding Gallic's own Phase C note already
made (`gallic_PhaseC_Scoping_Note.md`), independently re-checked here
rather than assumed to transfer: a repo-wide search for `app/world_manifest.py`
and `wrs/glosses/` returns nothing; only `cic-poc/README.md` and
`cic-poc/frontend/` remain.

## What the CURRENT live architecture actually requires, confirmed by direct inspection

The live path is `engine/api/`, which reads `records/worlds.yaml` (now
`records/worlds/*.yaml`) directly. Admission gating is already automatic:
`engine/api/wiring.py`'s `_check_admission()` gates on `state in {"admitted",
"open"}`, so witt's current `state: built` already correctly keeps it
invisible to `create_session`/`list_worlds` under admission enforcement —
nothing further needs to be built for this.

The real remaining wiring surface, per `engine/m1/cross_world.py`'s own
"stage 5: the frontends" checks, run directly against witt:

- `cic-poc/frontend/src/data/worlds.ts` — `WORLD_ORDER` array and
  `WORLD_ASSETS` object (portrait image path + accent colour per world).
- `cic-website/traditions/lutheran-wittenberg-and-its-congregations.html`
  — a per-world site page carrying the Representative's portrait image.

witt's own `census_id` is already set in `records/worlds/witt.yaml`
(`lutheran-wittenberg-and-its-congregations`) — unlike Gallic at the
identical stage of its own build, which had none yet. Only the
portrait-dependent frontend and site pages are outstanding.

## Why the frontend/portrait work is not actionable as a build-thread task right now

The `WORLD_ASSETS` entry needs a Representative portrait image, which does
not exist for Nikolaus. Deciding and commissioning a Representative
portrait is exactly the shape of decision this build's own standing
discipline treats as a real identity decision (CO-022's first escalation
category), not something to invent a placeholder for or decide
unilaterally here — matching Gallic's own identical finding for Renatus.

**Conclusion: there is no genuine, safe frontend/census "Phase C" task to
do ahead of that portrait decision and M3 admission**, beyond the fixes and
disclosures below.

## Two genuine content defects found and fixed directly (not just disclosed)

Running `engine.m1.cross_world` against witt surfaced two `_defect`-level
findings — distinct from the frontend-deferral class above, and distinct
from Gallic's own Phase C recon (which found none of this kind for
Gallic). Both were self-inflicted during this build's own earlier passes
(B-4 figure authoring; the Answer-the-Canon quote authoring), not
pre-existing corpus defects:

1. **`ui-field-leak/witt`** — two figure records'
   `dates.display` field (a participant-facing field the doorway's Level-3
   panel prints verbatim) carried a raw internal reference inline in its
   own prose: `witt.figure.luther.dates.display` cited
   `(witt.core.witt.thinness)`, and
   `witt.figure.brussels-martyrs-john-and-henry.dates.display` cited "the
   date Doc_09 and this record both follow." Both were rewritten to state
   the same dating claim without the internal reference, with a dated
   correction note added to each record's own body. Substance unchanged;
   both records' underlying dating claims were not touched.
2. **`quote-speaker-label/witt`** — five of the seven `quote` records
   authored at the Answer-the-Canon step (`witt.quote.article-ii-of-original-sin`,
   `.article-ix-of-baptism`, `.christs-return-to-judgment`,
   `.congregation-of-saints`, `.nothing-that-varies`) named
   `witt.story.diet-of-augsburg-1530` as a raw record id inside their own
   `speaker_or_author` field — a field both the Level-3 citation card and
   the compiled prompt's quote index print verbatim to a participant, and
   which the label resolvers only unwrap for `figure` ids, not `story`
   ids. Each was rewritten to describe the Diet of Augsburg in plain prose
   (e.g. "read before the Emperor at the 1530 Diet of Augsburg") with a
   dated correction note added to each record's own body. Substance
   unchanged.

**Independently re-verified after both fixes:** `engine.m1.gates.run_all()`
re-run against `load_world_records('witt')` + `load_fleet_records()` +
`load_registry()` — 0 findings, all 18 gates pass, record count unchanged
at 251. `engine.m1.cross_world` re-run — neither `ui-field-leak/witt` nor
`quote-speaker-label/witt` appears any longer.

## What WAS done directly, as ordinary Doc_02/cross-world-maintenance (not escalated)

Four `ACCEPTED_OPEN` entries added to `engine/m1/cross_world.py`, matching
the exact precedent pahc, cappadocian, gallic, and don already established
for the identical pattern:

1. **`figure-dates-keys/witt`** — all 6 witt figure records key
   `figure.dates` as `display` (contested/partial dating that doesn't
   reduce cleanly to born/died/floruit — e.g. Luther's own record gives no
   birth date; the Brussels martyrs record corrects a printed heading's
   own misprint and states no birth date survives for either man).
2. **`app-world-assets/witt`**, **`app-world-order/witt`**,
   **`site-portrait/witt`** — the frontend/site portrait-wiring trio,
   deferred pending the Representative-portrait decision, structurally
   expected for a world at `state: built` awaiting M3 admission, matching
   Gallic's own identical in-between-window finding.

## Verdict

Phase C is **scoped, not completed** — correctly, per fleet precedent — with
two real content defects caught and fixed along the way, not merely
disclosed. The real deployment-wiring work (frontend registration, site
portrait page) has no safe path forward until either (a) the Representative
portrait is decided — a real identity decision requiring the project
lead's own grounded-options treatment, the same as name/role received — or
(b) M3 admission happens, which is itself a separate real stop requiring
the project lead's explicit spend authorization. Neither is a routine next
step to take unprompted; both are put to the project lead directly, as
this build's own standing discipline requires.
