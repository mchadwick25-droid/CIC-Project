# Built-World Voice Alignment

**Charter (Mark, 2026-09-17):** every touchpoint a participant meets
between browsing the site and sitting down to talk with a Representative
should speak in one consistent, human, participant-facing voice — plain,
modern English focused on what the participant needs to decide or feel,
never internal project language, scholarly explanation, or complex
wording. Mark's own words: *"everything on the website and pathways to
the features needs to be human voice."*

This is a pickup from three prior threads whose work touches this same
ground but never converged on one voice: the Copy-editor / voice-craft
analysis work (`Ministry/Technology/CiC_Prose_Craft_Analysis.md`,
`CiC_Marks_Voice_Analysis.md`), the Website V2 design thread
(`Ministry/Features/Website-V2/`), and the Atlas prose review thread
(branch `claude/atlas-era1-prose-review`, PR #246). None of those threads
is being redone — this one covers the built-world voice end to end,
which none of them alone does.

## Scope

For the 8 currently built/live worlds, and every world that reaches
"Built & Live" after them:

1. **Homepage card blurb** — `entry.tile` in
   `cic-website/data/world-census.json`, rendered on `cic-website/index.html`.
2. **Atlas click-through panel** — `entry.longDescription` in the same
   census file, duplicated inline in `cic-website/atlas-v3.html`.
3. **"More information" page** — `cic-website/traditions/*.html`.
4. **The Arrival screen** (revised from the launch charter's original
   guess of a per-world "opening line" — see Decision-Log 2026-09-17) —
   `doorway_description` and `thinness_statement` in
   `records/worlds/<code>.yaml`, rendered by
   `cic-poc/frontend/src/components/Arrival.tsx`, plus the Facilitator's
   own DOOR/TABLE_DOOR template in `engine/m4/facilitator_turns.py`,
   which names the world by registry `card_name` (fixed 2026-09-17 — see
   log).

**Out of scope:** the ~285 remaining unbuilt/atlas-only traditions —
that ground belongs to the Atlas/Church Family Tree thread (PR #246).
The `doctrine` field PR #246 adds to 6 of the 8 built worlds' Atlas
entries stays Atlas-owned for now (Mark's ruling, 2026-09-17 — see log).

## The eight built worlds

| Code | Card name | Representative |
|---|---|---|
| `pahc` | The Scattered Households | Chloe |
| `alx` | Alexandrian Christianity | Theon |
| `syr` | Syriac Christianity | Mar Yausep |
| `desert` | Desert Fathers and Mothers | Papnoute |
| `cappadocian` | The Cappadocian Churches | Chilo |
| `ijc` | Church and Empire | Marius |
| `hal` | The Bethlehem Circle | Albina |
| `gallic` | The Monk-Bishops of Gaul | Renatus |

Confirmed against `records/worlds/*.yaml` (`state: admitted`,
`kind: formation`) — the real deployment source of truth, cross-checked
against `world-census.json`'s own `Built & Live` count.

## Status

Touchpoint 4 done (2026-09-17). Touchpoints 1–3 next: an audit across
all 8 worlds against the existing craft rules
(`CiC_Prose_Craft_Analysis.md`) and this project's own accessible/
rigorous bar (CLAUDE.md), before any replacement copy is drafted.

Decisions land in `Decision-Log.md` here, dated, per the project's
standing discipline.
