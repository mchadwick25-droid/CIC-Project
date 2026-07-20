# Integration Notes — Front-End Integration Strategy

**Live in `cic-poc/frontend/` today:** the citation-UI migration (`CitationModal.tsx`,
`CitationMarker.tsx`) — verified conflict-free against this strategy's own
"nothing renders over the transcript" rule (it's participant-summoned detail, not an
unprompted contextual card, same class as the already-accepted `LexiconModal`).

**Not yet integrated:** table-bar consolidation and the whole-screen five-count
budget check for Increment 1 — blocked on Full-UX-Design's first concrete deliverable
at the time this was last checked.

**Dependency chain this strategy established** (see Decision-Log.md for the full
reasoning): Increment 1 (budget compliance) → Increment 2 (role selection, gated by
Representative Modes' Battery A) → Increment 3 (Guided Questions UI, gated by
Increment 2 landing) → Increment 4 (World Map Tier A merge).

**No branch of its own** — this thread's own output is documents, not code; the code
it specifies lands via whichever feature actually builds each increment.
