# Hosted Tour (Phase One)

> **Status: SUPERSEDED (2026-08-03).** This demo's whole premise — the
> Representative hosting a participant live, inside an encounter, with the
> product's caption-strip UI layered around that live narration — was built
> around the same live-hosted assumption Tours is now being rebuilt away
> from. See `Tour-Experience-Module-Phase2/README.md` and
> `Front-End-Integration-Strategy/CiC_FrontEnd_Decision_Log.md` (2026-08-03
> entry) for the full reasoning. **Nothing here is deleted** — the stop-by-
> stop source-cartouche pattern (citation + tier + confidence, hover-short/
> click-full), the "what we cannot show you" honest-decline stop, and the
> parchment/ink/gold presentation conventions are real, reusable design work
> that a fully-authored, map-launched tour can likely still use; they need
> re-fitting to a no-live-generation, no-live-encounter-gate premise, not
> assuming the demo's flow still applies as built.
>
> **Superseded the following, kept below as historical record:** the
> 2026-07-22 "Descoped to Phase 2+" status (tour work was already on hold;
> this supersedes *why* it's on hold, not just confirms the hold).

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
