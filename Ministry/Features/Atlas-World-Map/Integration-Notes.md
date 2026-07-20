# Integration Notes — Atlas / World Orientation Map

This is the single most consequential file in this feature's folder — the whole
point of this reorg is that "is this actually live" should be a one-file answer.

## Live today

`cic-website/atlas.html`, `cic-website/world-map.html`, `cic-website/world-atlas-list.html`
— the real, committed, interactive map and its list-view fallback. Last touched
2026-07-19 (commit `e292713`, "Replace the Atlas page's placeholder slideshow with
the real interactive World Orientation Map"). 7 more site pages link to `atlas.html`
in their nav bar only.

`cic-poc/frontend` has **zero** references to "atlas" or "world-map" as of this
writing — confirmed by direct search. The deep app-integration below has not reached
`main`.

## Not merged — real, tested integration code exists on two branches

- **`claude/world-map-integration-exploration`** (tip `de11233`, 2026-07-16) —
  exploratory: map as a supplementary/optional selection view, plus a
  `/?worlds=<id,id>&mode=<interview|table>&role=<...>` URL handoff contract.
- **`claude/world-map-merge-into-main`** (tip `c277ca8`, 2026-07-19,
  "Merge World Map integration (Tier A: optional orientation view + handoff)") — a
  112-file, +803/-4501-line diff against `main`, including a new
  `cic-poc/frontend/public/world-map/index.html` and edits to `WorldSelector.tsx`,
  `TheTable.tsx`, `useConversation.ts`, `types/conversation.ts`, `MessageBubble.tsx`
  — the actual bidirectional app↔map handoff.
- **This second branch is checked out in its own sibling directory outside this
  repo entirely: `C:\Users\mchad\Documents\CiC-Project-worldmap-merge`.** Easy to
  forget exists since it isn't nested inside `CiC-Project/` at all. Verified live
  against real dev servers in both directions per the Website decision log, but held
  back pending the Tier A/B scope decision below.

## The one open decision gating the merge

Does the Atlas stay a secondary orientation view a participant can optionally visit,
or become the primary world-selector replacing the current in-app world picker? Not
yet decided as of the last check. This single decision is what the whole
`world-map-merge-into-main` branch is waiting on.

## Known-stale item, being fixed separately

The live site's world statuses (which worlds show "Built & Live" vs. "Selected - Not
Yet Built") drift from `world_manifest.py` — see
`Ministry/Technology/CiC_Website_Alexandria_Status_Fix_Thread_Launch_2026-07-20.md`
for the active fix thread covering this.

## What to do when the Tier A/B decision lands

Merge `claude/world-map-merge-into-main` (or a rebased equivalent, given how far
behind `main` it may be by then), remove the sibling worktree directory once merged,
and update this file to reflect the new live state.
