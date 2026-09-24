# Atlas / World Orientation Map

**What this is:** an interactive, zoomable/pannable map of ~178 historical Christian
movements across 9-10 eras, letting a participant orient themselves before choosing a
world/Representative to talk with. Also called "World Atlas." (Was briefly misnamed
"Christian Movement Scrolling Atlas" early on — corrected; use "World Orientation
Map" or "Atlas.")

**This was the single worst-scattered feature found in the 2026-07-20 filing audit**
— 8 locations across the repo before this migration, including a live-tested
integration branch checked out in its own sibling directory entirely outside the
repo. See `Integration-Notes.md` for exactly what's live vs. unmerged.

**Current state:** the map itself is live and working on the public site, at
`cic-website/atlas-v3.html` — "Church in History." `atlas.html` and `world-atlas.html`
are dead redirect stubs kept only for old bookmarks/links, from before the "Story"
surface and the earlier Wall Chart + Research Table directions merged into this one
page (2026-08-03 "ship flip"); `world-map.html`/`world-atlas-list.html` never shipped
under those names. Deeper integration into the actual conversational app (`cic-poc/`)
— letting the map hand a participant directly into a Table session — is built and
tested but **not merged**, gated on an undecided Tier A/B scope question (does the map
stay a secondary orientation view, or become the primary world-selector?).

## Module map (WO-3, 2026-09-16 — one home to find every real location from)

The design/decision documents below live in one place, as intended; the live page,
its data, and their generators do not and should not — Cloudflare deploys
`cic-website/` verbatim, so a file's path there *is* its live URL, and moving one
means breaking a link, not a repo-hygiene win. This section exists so nobody goes
hunting: every real location, current as of the survey that produced it.

| what | where | notes |
|---|---|---|
| **Live page** | `cic-website/atlas-v3.html` | the whole thing: HTML/CSS/JS/SVG, no build step, committed as a finished static artifact |
| Dead redirect stubs | `cic-website/atlas.html`, `cic-website/world-atlas.html` | keep old bookmarks working; not the real page |
| Preview image | `cic-website/assets/atlas-preview.jpg` | OG/share preview |
| **Census data** (hand-authored) | `cic-website/data/world-census.json` | loaded directly by the live page; the one file to hand-edit |
| Census → registry sync | `engine/m6/census_sync.py`, `engine/m6/cli.py` | "the Atlas connection" — copies a narrow field set from `records/worlds/<code>.yaml` into the census for Built-&-Live worlds only; `cli.py check` is the CI gate |
| Corpus-assignment targets (generated) | `cic/corpus-map/ATLAS-TARGETS.md` | regenerated from the census by `cic/engine/atlas_targets.py` — do not hand-edit |
| Adjacent, not the census | `cic-website/data/corpus-coverage.json` | corpus-coverage stats, produced by `cic/engine/corpus_coverage.py`; easy to confuse with the census, is not it. **Not yet wired into `atlas-v3.html`'s own rendering** (per `cic/corpus-map/README.md`'s own note) — generated and correct, but the live page does not read it yet; a future front-end task, not yet scoped or scheduled |
| **Validator** | `tools/validate-census.mjs` | `node tools/validate-census.mjs cic-website/data/world-census.json`; wired into CI's `validate-census` job |
| **Design/decisions** | this directory (`Decision-Log.md`, `Design/`, `Launch-Prompts/`, `Integration-Notes.md`, `Drafts-Archive/`) | the one place to look — see below for what stays outside it and why |
| Not moved here, and correctly so | `Ministry/Features/Website-V2/Sandbox/D1-directions/02-atlas-first-spatial/` (and its D2 counterpart) | an "Atlas-first homepage" *direction* explored inside Website-V2's own sandbox — that workstream's content, not this module's, even though it discusses the Atlas |
| Runtime API | none | the map is purely static; `engine/api/app.py`'s `/api/worlds` is the session-doorway endpoint for choosing a world to talk to, unrelated and unread by the map |

**`Drafts-Archive/`** holds two scratch drafts explicitly superseded by the real
`cic-website/` implementation, plus census spreadsheet versions V0.2-V0.12 (V0.13 is
current, in `Design/`).

**Where deliverables live once integrated:** `cic-website/` (already live) and
`cic-poc/frontend/` (pending the Tier A/B decision).

**Active as of 2026-07-20 — new usability/branding study (Fable), launched directly
by Mark:** studying how other scrolling/interactive maps handle usability, applying
findings to make this map more usable on-screen while incorporating this project's
own DECIDED visual identity (palette/type from Full UX Design / the Messaging &
Branding Kit — see `../Full-UX-Design/`). No launch doc filed; tracked in the System
Hub Decision Log's thread roster. **Its output belongs in `Design/` when it lands** —
this is the one place to look for it, per the whole point of this folder existing.
