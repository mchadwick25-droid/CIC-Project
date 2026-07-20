# Level-2 Mobile Popover Fix

**What this is:** closing a real, pre-existing gap found during the
Increment 1 build — on phone, tapping a lexicon term or citation marker
skips the intended Level-2 preview step and opens Level-3 directly. Not a
regression, not broken, just short of the spec'd two-step grammar.

**Current state:** launch prompt written 2026-07-20, not yet dispatched.

**Where deliverables land once integrated:** `cic-poc/frontend/src/
components/LexiconHighlight.tsx` and `CitationMarker.tsx`, directly — small
enough that this likely doesn't need its own branch/merge-timing debate the
way Increment 1 did, but confirm before merging regardless.
