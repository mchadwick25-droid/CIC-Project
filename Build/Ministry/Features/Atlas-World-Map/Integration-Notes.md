# Integration Notes — Atlas / World Orientation Map

This is the single most consequential file in this feature's folder — the whole
point of this reorg is that "is this actually live" should be a one-file answer.

## Live today

Three surfaces, one shared data file (`cic-website/data/world-census.json`):

- **`cic-website/atlas.html`** and **`cic-website/index.html`** — the Story view
  (vertical, era-by-era, the landing surface on all devices per the 2026-07-20
  decision below). Each fetches the shared census independently; they carry the
  same rendering code as two separate files, not a shared include (the site has no
  templating layer), so a future content/behavior change to the Story still needs
  applying in both places.
- **`cic-website/world-atlas.html`** — the Wall Chart and the Research Table, as one
  document with a view toggle (`#chart` / `#table`, default `#chart`), consolidated
  2026-07-22 from the two files below. Both views fetch the same shared census at
  runtime; the wall chart keeps only its own presentation-only data locally
  (per-entry start/end years for the timeline, era medallions, figure lifelines,
  relationship edges) — no census-truth field (status, name, why, sourcing, ...) is
  duplicated anywhere anymore.

**Archived 2026-07-22** (moved, not deleted, per this project's no-silent-deletion
convention — see `Drafts-Archive/`): the two files world-atlas.html replaces —
`CiC_World_Map_html_Superseded_2026-07-22.html` (was `cic-website/world-map.html`,
the "Concept Demo V0.3" wall chart) and
`CiC_World_Atlas_List_html_Superseded_2026-07-22.html` (was
`cic-website/world-atlas-list.html`, the research browser). Reason: both carried
their own independently-stale embedded copy of the census — the exact "N vs N+1
live worlds" drift class this feature exists to kill — and merging them into one
document reading the shared JSON removes the duplication at its root instead of
patching each stale copy again next time a world goes live. All in-site links
(`atlas.html`, `index.html`) repointed to `world-atlas.html#chart` /
`world-atlas.html#table`; no other site page linked to the old files directly (only
`atlas.html` in nav bars, per the prior version of this note).

7 site pages link to `atlas.html` in their nav bar only.

As of 2026-10-09, `cic-poc/frontend/src/App.tsx` parses the deep-link grammar
`?worlds=<id,id>&mode=<interview|table>` (lines 22-43), the one contract between the
discovery surfaces and the app. The two branches below no longer exist on the remote
(checked 2026-10-09); which of their other changes reached `main` was not checked.

## Historical — integration code that existed on two branches (2026-07-22; both gone from the remote by 2026-10-09)

- **`claude/world-map-integration-exploration`** (tip `de11233`, 2026-07-16) —
  exploratory: map as a supplementary/optional selection view, plus a
  `/?worlds=<id,id>&mode=<interview|table>&role=<...>` URL handoff contract.
- **`claude/world-map-merge-into-main`** (tip `c277ca8`, 2026-07-19,
  "Merge World Map integration (Tier A: optional orientation view + handoff)") — a
  112-file, +803/-4501-line diff against `main`, including a new
  `cic-poc/frontend/public/world-map/index.html` and edits to `WorldSelector.tsx`,
  `TheTable.tsx`, `useConversation.ts`, `types/conversation.ts`, `MessageBubble.tsx`
  — the actual bidirectional app↔map handoff.
- This branch was previously checked out in a sibling directory outside this repo
  (`C:\Users\mchad\Documents\CiC-Project-worldmap-merge`) — **that directory no
  longer exists** (confirmed 2026-07-22; presumably cleaned up already). The branch
  itself is still here, `2` commits behind `main` as of 2026-07-22 — not badly
  stale, a straightforward rebase away. Verified live against real dev servers in
  both directions per the Website decision log, but held back pending the Tier A/B
  scope decision below.

## The Tier A/B decision — DECIDED 2026-07-20, supersedes the framing below

This section originally asked whether the Atlas stays a secondary orientation view or
becomes the primary world-selector, as an either/or. **That framing is stale.** The
2026-07-20 Usability Redesign Study (`Design/CiC_World_Map_Usability_Redesign_Study_2026-07-20.md`,
Part 6) reframed it as two linked surfaces rather than one either/or choice, and Mark
ruled on it the same day (`Decision-Log.md`, 2026-07-20): **the Story is the website's
exploration surface; Choose a Tradition is the in-app selection surface — neither
replaces the other.** (The Story half was superseded 2026-08-02 by "only one atlas,
done right", and the river map has been the website's one atlas since 2026-09-03; the
two-surface split, website explores and app selects, stands.) The `world-map-merge-into-main` branch's existing handoff
contract (`/?worlds=<id,id>&mode=<interview|table>`) is exactly what Choose a
Tradition builds against, so that branch is not obsolete — it's one input to the
now-decided design, not a proposal still waiting on the gating question.

## Known-stale item, resolved twice now — watch for a third time

The live site's world statuses (which worlds show "Built & Live" vs. "Selected - Not
Yet Built") drift from `world_manifest.py` each time a world goes live, because
`world_manifest.py` isn't the thing that renders the site — someone has to notice and
update the census. Alexandria/Theon was the first instance (fixed per the census
file's own `meta.notes`, see
`Build/Ministry/Technology/CiC_Website_Alexandria_Status_Fix_Thread_Launch_2026-07-20.md`);
Church and Empire/Marius (installed 2026-07-22) was the second, fixed in this same
session alongside the world-atlas.html consolidation above. The consolidation should
make a third instance less likely for the Wall Chart and Research Table specifically
(one shared JSON now, not three), but the Story view's own two copies (`atlas.html`,
`index.html`) and `world_manifest.py` itself are still three independently-updated
places — there is no automated check that they agree. Worth a look whenever a new
world goes live.

## What to do when the Tier A/B decision lands

The Tier A/B decision already landed 2026-07-20 (see above) — the next concrete step
is building Choose a Tradition against the `claude/world-map-merge-into-main`
branch's existing `/?worlds=<id,id>&mode=<interview|table>` handoff contract (rebase
first; it's only 2 commits behind `main` as of 2026-07-22). Update this file once
that work starts.

## Boundary with the In-App Icons & Graphics thread — verified clean 2026-07-22, keep it this way

Mark's direct instruction, System Hub: these two threads are both essential and should
not cross over into each other's work. Checked directly, not assumed: **Marius's
icon (`empire.svg`) is built exactly once**, by the Icons & Graphics thread, locked as
`Build/Ministry/Communication/Brand-Assets/World-Icons/_working-base/marius_LOCKED_v1_0.svg`
— this thread's own "icon copied from Brand-Assets" note above means literally that,
confirmed via `diff` as byte-identical to `cic-website/assets/world-icons/empire.svg`,
not an independently invented copy. **The rule going forward: this thread (Atlas)
owns the Story/Wall-Chart/Research-Table surfaces and copies whatever icon/graphic
assets it needs from `Brand-Assets/` once they exist there — it does not design or
lock a new Representative icon itself.** The Icons & Graphics thread owns the
canonical asset (design, source-verification, locking) in `Brand-Assets/World-Icons/`.
Same split applies to the era-ground color palette (values canonical in the icon
spec, §7) — this thread renders with them, doesn't redefine them. If a new world's
icon isn't built yet when this thread needs it, that's a real blocker to flag back to
System Hub, not something to work around by drawing a placeholder here.
