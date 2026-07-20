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

**Current state:** the map itself is live and working on the public site
(`cic-website/atlas.html`, `world-map.html`, `world-atlas-list.html`). Deeper
integration into the actual conversational app (`cic-poc/`) — letting the map hand a
participant directly into a Table session — is built and tested but **not merged**,
gated on an undecided Tier A/B scope question (does the map stay a secondary
orientation view, or become the primary world-selector?).

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
