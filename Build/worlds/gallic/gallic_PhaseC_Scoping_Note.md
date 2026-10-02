# Phase C Scoping Note — Gallic Monastic-Ascetic Christianity

**Status:** Phase C recon complete. Two small, disclosed,
precedented fixes made directly (ACCEPTED_OPEN entries in
`engine/m1/cross_world.py`). The bulk of "deployment wiring" is confirmed
structurally deferred until after M3 admission, per real fleet precedent —
not a build-thread task to force now. One genuine, new test-suite gap
surfaced and disclosed, not silently patched.

## What the governing process document says, and why it doesn't apply as written

`Build/reference/method/CiC_Record_Native_World_Build_Process_V1.5.md` (moved
there by the later repo reorganization; path since corrected) §4
("Phase C — Deployment wiring") describes: an `app/world_manifest.py` entry,
two hand-synced frontend points (`SpeakerName` union, `MessageBubble.tsx`
`REPRESENTATIVE_NAMES`), vector indices built at Docker build time,
a Dockerfile audit, `HARD_CEILING_WORLDS` (`app/graph/nodes.py`),
`POST_HISTORY_GUARD` wiring (`wrs/views/segments/guards.py`), and a live
smoke test against a Docker/Render-deployed site.

**None of this exists in the current repository.** `app/` does not exist
anywhere in this tree; `cic-poc/backend/` (which held the equivalent
tooling) was deleted, per the same commit (`bc6601b8`) B-8's own
recon already found ("the links moved to cic-engine"). This is the
identical class of finding B-6, B-7a, B-8, and B-9 each already made for
their own process-document rows — a row describing infrastructure that no
longer exists, for any world, not only this one.

## What the CURRENT live architecture actually requires, confirmed by direct inspection

The live path is `engine/api/` (`wiring.py`, `app.py`, `table_wiring.py`),
which reads `records/worlds.yaml` directly:

- **Admission gating is already automatic, by design.** `engine/api/wiring.py`'s
  `_check_admission()` and `list_worlds()` both gate on `entry.get("state") in
  {"admitted", "open"}` when `Settings.enforce_admission` is on. A `state:
  built` world (Gallic's own current state, set at B-8) is already correctly
  invisible to `create_session`/`list_worlds` under admission enforcement —
  nothing further needs to be *built* for this; it is a property of the
  registry `state` field, which only M3 admission changes.
- **The real remaining "wiring" surface, confirmed by direct inspection of
  `engine/m1/cross_world.py`'s own "stage 5: the frontends" checks:**
  - `cic-poc/frontend/src/data/worlds.ts` — `WORLD_ORDER` array and
    `WORLD_ASSETS` object (portrait image path + accent colour per world).
  - `cic-website/traditions/<census_id>.html` — a per-world site page
    carrying the Representative's portrait image, keyed by `census_id`.
  - `records/worlds.yaml`'s own `census_id` field, linking this world to
    its Atlas census entry.

## Why none of this is actionable as a build-thread task right now

1. **Census linking is real, later, post-admission work — not skipped, deferred, per direct fleet precedent.** Cappadocian's own ledger (`CAPPADOCIAN_BUILD_LEDGER.md` §30, "Atlas/census entry: linked and renamed, NOT flipped live") did this AFTER M3 admission (§26-27), not before. `check_site_portraits` itself only fires for a world with a `census_id` set (`if not cid: continue`) — the site-portrait check is structurally inert for Gallic until that later step.
2. **The frontend `WORLD_ASSETS` entry needs a Representative portrait image, which does not exist.** Every existing entry (`cappadocian: { portraitImage: '/images/portraits/cappadocian.jpg', ... }`) points to a real image file. Renatus has no portrait — this world's own build record already carries this forward as "a separately-deferred second fabrication, not yet built" (alongside the name/role fabrication). Deciding and commissioning a Representative portrait is exactly the shape of decision this build's own standing discipline treats as a real identity decision (CO-022's first escalation category), not something to invent a placeholder for or decide unilaterally here.

**Conclusion: there is no genuine, safe "Phase C" content-building task to do ahead of M3 admission**, beyond the small disclosures made below. Attempting to force frontend/census wiring now would mean either inventing a portrait unilaterally (an identity-decision overreach) or census-linking before admission (contrary to every precedent in this fleet).

## What WAS done directly, as ordinary Doc_02/cross-world-maintenance (not escalated)

1. **`figure-dates-keys/gallic` added to `ACCEPTED_OPEN`** (`engine/m1/cross_world.py`). All 5 of this world's own figure records key `figure.dates` as `display` (contested/hedged prose — e.g. Martin's own dates resting on "lived sixteen years after the Treves affair by Gallus's own reckoning," Vincent's Lérins entry "undated... Inferential-Thin") rather than `born`/`died`/`floruit`, for the identical legitimate reason `pahc` and `cappadocian` already disclosed the same pattern for. Disclosed, not rewritten — matching both precedents' own disposition exactly.
2. **Four more `ACCEPTED_OPEN` entries added**, disclosing that Gallic is the fleet's first world ever registered (B-8) at `state: built` without also being census-linked and frontend-wired in the same pass — every prior world's B-8 happened close enough to its own M3 admission that this in-between window was never actually exercised against these checks before: `registry-null-field/gallic.census_id`, `census-id/gallic`, `app-world-assets/gallic`, `app-world-order/gallic`.
3. **Full re-verification**: `python -m engine.m1.cross_world` now reports 0 new defects (17 accepted-open, up from 13); `python -m pytest engine/m1/ engine/m2/` re-run in full.

## A genuine, new, unresolved test-suite gap — disclosed, not patched

`engine/m1/tests/test_cross_world.py::test_the_desert_deep_link_defect_is_caught`
now fails: its final assertion (`assert not {f.key for f in
cross_world.check_census_link(registry=registry, worlds=worlds)}`) calls
`check_census_link` directly, bypassing `ACCEPTED_OPEN` entirely, and
asserts that the *real, unmodified* registry produces zero census-linkage
findings for any real formation world. This is the first time in this
fleet's history a world has sat in the registry at `state: built` without
also being census-linked, so this specific hard assumption — that every
registered formation world has a census_id — was never actually exercised
before now.

**This is not fixed here.** Loosening or restructuring this test's own
assumption is a real methodology/test-design decision about a shared,
non-world-build file (`engine/m1/tests/test_cross_world.py`), which this
build's own standing discipline (CO-022) assigns to a coach thread, not a
build thread scoped to its own world's folder — the same discipline already
respected at B-6/B-7a/B-8/B-9 whenever a stale-but-shared file was found,
rather than silently corrected. Flagged here, and to the project lead,
rather than patched.

## Verdict

Phase C is **scoped, not completed** — correctly, per fleet precedent. The
two small disclosures above are genuine, precedented, low-risk maintenance,
committed directly. The real deployment-wiring work (frontend registration,
site portrait page, census link) has no safe path forward until either (a)
the Representative portrait is decided — a real identity decision requiring
the project lead's own grounded-options treatment, the same as name/role
received — or (b) M3 admission happens, which is itself a separate real
stop requiring the project lead's explicit spend authorization. The
disclosed test-suite gap is a third, independent item for the project lead
or a coach thread, not blocking either of the above.
