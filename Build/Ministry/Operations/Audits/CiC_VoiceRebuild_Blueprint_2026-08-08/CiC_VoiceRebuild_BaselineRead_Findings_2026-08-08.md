# CiC Voice Rebuild — Baseline Read Findings (logged, not actioned)

**Source:** Mark's own read of the pre-rebuild baseline transcripts,
2026-08-08, ahead of the formal Objective-3 scored read. Two system-level
findings, logged here per Mark's own instruction: work at the system
level, don't chase individual phrases, and if the fix belongs to Phase 1A
that's fine — log it and keep moving.

## Finding 1: story/demonstration reuse has no within-session self-awareness

**Evidence:** Albina's 8-turn baseline probe uses the Paula story as its
primary illustration twice — turn 5 ("Is there someone in your household
whose life shows what this looked like when it was lived out fully?") and
turn 7 ("What would people today get most wrong...?") — retelling nearly
the same biographical beats (senatorial birth, wealth given away, her
daughter's accusation, learning Hebrew late in life, building the
Bethlehem household) with no acknowledgment of having already told it a
few turns earlier.

**Diagnosis:** the demonstration selector (Phase 0.1,
`wrs/views/segments/demonstrations.py`) picks the best-scoring
demonstration per turn by trait relevance to that turn's question. It has
no within-session reuse-tracking — a strong, high-scoring demonstration
can resurface untouched whenever a later question's traits also favor it,
because nothing in the selector knows it already spoke.

**Scope call (not made here):** this is a selector/session-state gap, not
a prose fix. Two directions worth weighing when Phase 1A or Phase 2 scope
this: (a) track already-used demonstrations this session and deprioritize
repeats in favor of the next-best-scoring one, or (b) where the same
example is genuinely the right answer twice, require an explicit callback
framing ("as I said a moment ago...") rather than a fresh, unaware
retelling. Left open — not decided here.

## Finding 2: quotes and referencing — a visibility gap and a coverage question, bundled together

**The visibility half (fixed in the read tool today):** the app already
has a real, mature sourcing system — `CitationMarker`/`CitationModal`,
built per "Article 30 Three-Level Transparency," backed by a full Source
Registry with confidence and boundary tags per entry. It wasn't visible
in the original baseline read materials because the `citations` field was
stripped out the same way `glosses_used` was — both are now wired into
the read tool (a "Sources for this turn" pill under any probe turn that
has one).

**The coverage half (an open question, not a defect):** even counting
generously, only 20 of 96 baseline probe turns (~21%) fired a citation at
all, and turns where the Representative quotes primary-source text
verbatim in their own spoken words are rarer still — 4 of 96 turns
baseline-wide carry any quotation marks at all. The citation system as
built mostly documents what *supports* a claim (source, confidence,
registry) rather than surfacing an actual quoted line to the participant
inside the conversation itself.

**Open question for whoever scopes Phase 1A:** does "we need quotes and
referencing" mean (a) making the existing sourcing system reliably
visible and consistently firing across turns — the cheaper, more
mechanical fix — or (b) increasing how often Representatives quote
primary sources verbatim in their own speech, which is a voice-craft/
authoring decision with real cost, not a wiring fix — or both. Logged
here rather than guessed at.

**Also logged, not fixed:** `sustained_disagreement_battery.py` did not
capture citation data at generation time (only the 8-turn probe script
did), so none of the six sustained-disagreement transcripts can show a
sourcing panel even where one existed at run time. A gap in that specific
battery script, not in the app. Not worth a costly re-run to fix right
now; logged for whenever that battery next runs for real.

## What this does NOT block

The Objective-3 baseline read itself (packets and interactive tool,
committed and published earlier today) is unaffected by either finding —
Mark and Susan's independent scores are still the next actual action, and
still what unblocks Phase 1A's own checkpoint bar.
