# Level-2 Mobile Popover Fix

**What this is:** closing a real, pre-existing gap found during the
Increment 1 build — on phone, tapping a lexicon term or citation marker
skips the intended Level-2 preview step and opens Level-3 directly. Not a
regression, not broken, just short of the spec'd two-step grammar.

**Current state:** built and verified 2026-07-20 — see Decision-Log.md.
Tap now shows the Level-2 popover (with a real "Full entry →" button)
instead of skipping straight to Level-3; desktop hover→click is
unchanged. Landed directly on `main` (`cic-poc/frontend/src/
components/LexiconHighlight.tsx`, `CitationMarker.tsx`, and the
tooltip-footer rules in `styles/table.css`) — small enough it didn't need
its own branch/merge-timing debate the way Increment 1 did.

**Where deliverables land once integrated:** `cic-poc/frontend/src/
components/LexiconHighlight.tsx` and `CitationMarker.tsx`, directly.
