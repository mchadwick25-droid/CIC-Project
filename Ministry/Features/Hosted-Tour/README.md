# Hosted Tour (Phase One)

> **Status: Descoped to Phase 2+ (2026-07-22).** Per Mark's direct decision, tour
> work is out of the current build cycle — not part of this launch. Everything
> below is kept as an accurate historical/status record of what was built and
> designed; it is not being touched, and no further tour integration proceeds
> until this is explicitly reprioritized.

**What this is:** a built, self-contained immersive demo — the Representative walks a
participant through a reconstructed moment of their world (a gathering, a shared
meal) rather than only answering questions. Built and verified for one world
(Chloe/House-Churches) as a reference implementation of the full pipeline: an
interactive HTML demo, a flow slideshow, and a GIF walkthrough, with verified
public-domain images and source-text audio readings.

**Not the same feature as `Tour-Experience-Module-Phase2/`** — that's a separate,
unbuilt Phase Two concept. The two were historically referred to almost
interchangeably in prose; keeping them in separate folders with distinct names is the
fix for that.

**Current state:** demo self-verified, not integrated into `cic-poc`, nothing merged.
Holding for Mark's voice review and the front-end integration queue.

**Where deliverables land once integrated:** `cic-poc/frontend/` (as a new
conversation mode) plus new per-world data alongside each world's existing lexicon
chunks in `cic-poc/backend/data/`.
