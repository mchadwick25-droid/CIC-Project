# Phase D — Live Deep Interview, Gallic Monastic-Ascetic Christianity

**Mechanism:** `engine.m4.live_turn_run`, real live Bedrock
generation (`LiveModelAnswerer`, same voice model as M3: `us.anthropic.claude-sonnet-4-5-20250929-v1:0`),
against the actual admitted package (`manifest_hash
sha256:9a1dd6d23305d2fc3790ae3bc7e9cfac7ccd640536c44a26049a5617b14f2632`).
Six real, threaded, unscripted questions, one session, history carried
turn to turn (matching Cappadocian's own §38 precedent exactly, following
the process document's own Phase D requirement for genuine interview
dynamics, not a thinned copy of the sealed battery). Report:
`engine/m4/reports/live-turn-report-gallic.json`.

**This is not a pass/fail mechanism.** Unlike M3, nothing here gates
admission (already granted). The point is a human read — the project
lead's own, per this build's standing discipline — of what a real participant would
actually receive, catching things the sealed battery's own narrower checks
are not built to catch. Two real findings surfaced this way, reported
honestly below rather than smoothed over.

## The six questions and what came back

1. **"Who are you, and what does your life actually look like, day to day?"**
   Clean identity/register baseline. Used the one sanctioned exception
   correctly ("I am a representative of the monasteries of Gaul"), then
   held strict we-voice throughout; both nodes given their own concrete,
   place-marked daily texture (Marseilles' hours and cell discipline;
   Tours' saint-centered record); the reception discipline held (the
   twelve psalms "came from an angel the fathers of Egypt received it
   from, not from us"). 12 citations, all real record ids.

2. **"People sometimes say you have to choose — either God does everything
   ... or you have to earn it yourself. What would you say to that?"**
   The core grace-and-effort tension (G3), handled as this world's own
   texts hold it — both halves commanded, "not I, but the grace of God
   with me," the husbandman-and-rain field answer, ending exactly where
   the fathers stopped rather than resolving the tension. **One real
   fluency defect found:** a paraphrase of the Paesius-and-John anecdote
   came out grammatically broken ("The hermit answered, nor me angry") —
   an incomplete conversion from a quoted-Latin-flavored source phrase
   into smooth indirect English. Minor, not a fabrication or a discipline
   violation, but a real rough edge a participant would actually read.

3. **"Did those two houses ever write to each other, or hear news of one
   another?"** — the single highest-risk discipline this world's own
   build has repeatedly guarded (no documented traffic between Tours and
   Lérins-Marseilles). Answered correctly and directly: "They did not,"
   then carefully attributes the shared "capture" shape to this voice's
   own analytical vantage rather than to either house's own awareness of
   the other — a real, correct handling of a genuine subtlety, under
   direct pressure to claim otherwise.

4. **"What was life like for the women in your communities — did any of
   them leave behind their own words?"** Honest, plain, un-hedged: "Not
   one word of theirs was kept... not even the one our record praised
   most, and she is praised for not being seen." Exactly the "honest
   thinness beats invented depth" discipline, naturally extending into
   the material-remains limit as well.

5. **"I keep picturing you as Martin himself, or maybe Cassian. Which one
   are you?"** — the identity-collision cell this world's own B-7 build
   flagged as *required* to get right. **The most significant finding of
   this interview:** under this direct pressure, the voice broke strict
   we-voice four times in its closing paragraph — "both their witness is
   **mine** to carry," "So **I am** not Martin...", "**I am** not
   Cassian...", "**I am** the witness for both nodes together..." — none
   of which is the one sanctioned self-naming line. The *content* stayed
   correct throughout (it never claimed to be Martin or Cassian, never
   invented detail, correctly attributed each man's own material in the
   third person) — this is a register failure, not a factual or identity
   one — but it is a real, participant-facing violation of this world's
   own strictest standing rule, caught by the runtime's own
   `output_defects` pronoun check and confirmed here by direct read of
   the actual delivered text (this check decorates the event for audit;
   it does not alter or block what a participant receives). **Cappadocian's
   own equivalent interview (ledger §38) reports this exact discipline
   held with zero breaks** — so this is a genuine, worse-than-precedent
   result for Gallic on its own single most-anticipated risk, not a
   universal, expected soft spot.

6. **"Would you say you were Catholic, in the way we'd use that word
   today?"** Sophisticated, correct handling of the later-word/living-tradition
   discipline: answers the substance in the world's own terms (Vincent's
   universality/antiquity/consent test), distinguishes "Pope"/"Apostolic
   See" as this world's own usage from the later denominational sense,
   and never refuses or adopts the modern label outright — exactly the
   Construction Notes' own "later-sounding label" handling, executed live.

## A second, smaller finding: three unresolvable citation tags — safely contained, not participant-facing

Direct inspection of `grounding` verdicts (not just `output_defects`) found
three sentences across turns 1–2 tagged by the model with record ids that
do not exist: `gallic.term.the-angel-and-the-twelve-psalms` (the real
record is `gallic.story.the-angel-and-the-twelve-psalms`, correctly cited
elsewhere in the same turn), `gallic.limit.record-thinnest` (the real
record is `gallic.demo.record-thinnest`), and `gallic.dw.faith-alone` (the
real record is `gallic.demo.faith-alone`) — the model guessing the wrong
`record_type` prefix for an otherwise-correct topical slug, three times.

**Verified directly against `engine/m4/turn.py`'s own `apply_net()`
docstring and code before characterizing severity, rather than assumed:**
the checks gate decoration only, never the text (a foundation-audit
finding, cited in the function's own docstring, that deleting failed
sentences orphaned surrounding content 25–39% of the time and was
reversed) — so the sentence text still reaches the participant, but an
unresolvable tag is dropped from the citations list entirely rather than
shown as a broken or invented citation. **No participant ever sees a false
or dangling citation from this** — the safety net worked exactly as
designed. Worth naming as a real, if contained, precision gap in how the
model self-tags claims with record ids; not a fabrication risk.

All 40 distinct record ids the model DID successfully cite across the six
turns were independently verified to resolve to real files in
`records/gallic/` (0 hallucinated ids reached an actual citation).

## Verdict

This is genuine, valuable evidence Phase D exists to produce — not a clean
sweep, and not treated as one. Five of six turns held every discipline
this world's own build named as load-bearing, under real, unscripted
pressure, including the hardest ones (no-node-traffic, honest limits,
later-word handling). One turn — on the single cell this world's own
build flagged as requiring the most care — broke the strict we-voice rule
four times in its closing lines, worse than Cappadocian's own equivalent
result. A separate, smaller, safely-contained tagging-precision gap was
also found and disclosed.

**Not decided here:** whether this register finding warrants a Permanent
Prompt reinforcement (e.g., strengthening the identity-collision guard
specifically under direct "which one are you" pressure) before this is
considered fully closed, or whether it is judged an acceptable, disclosed
limitation given the underlying content stayed accurate throughout. That
judgment belongs to the project lead, per this build's own standing
discipline that a live read like this one is his to make, not the build
thread's to resolve unilaterally.
