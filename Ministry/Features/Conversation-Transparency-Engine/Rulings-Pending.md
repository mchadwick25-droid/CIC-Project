# Rulings Pending — Conversation & Transparency Engine

One at a time, per `CLAUDE.md`'s own ground rules: real options, honest
tradeoffs, a recommendation — never a flat conclusion. Nothing in Stages
6–9 of `Build-Plan.md` proceeds until its ruling lands here. Update the
**Status** line when Mark rules; append the outcome to `Decision-Log.md`
in the same edit.

**Scope note (2026-09-19):** every ruling that proposed new Facilitator
safety machinery is closed below as resolved, per `Decision-Log.md` entry
3 — Mark's direct ruling that the mechanism is a single fixed step
(recognize a signal → check in → encourage seeking real human help) and
is not open design space. What remains open below is conversation/
transparency engine work only: retrieval, the library connection,
citation and confidence display.

Full reviewable version (written before the scope correction, read
alongside `Decision-Log.md` entry 3): `https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`

---

### R1 — If the safety call itself fails, answer anyway or fail toward check-in?
**Status:** CLOSED (`Decision-Log.md` entry 3) — the existing fail path
stands; no async reclassification or operator paging is built.

### R2 — Escalation priority, message decay, and the interim continuation text
**Status:** CLOSED (`Decision-Log.md` entry 3) — no escalation-tier logic,
no decay timer. The already-merged fix (PR #306) is the whole mechanism.

### R3 — Item 16's replacement: what, if anything, should the safety classifier be told about recent turns?
**Status:** CLOSED (`Decision-Log.md` entry 3) — nothing. The classifier
stays fully memoryless; no replacement mechanism of any kind is built.

### R4 — How often does the non-acute reminder repeat, and does the voice ever see it fired?
**Status:** CLOSED (`Decision-Log.md` entry 3) — one check-in, once. No
frequency tuning beyond what already exists.

### R5 — A real "interrupt the round" affordance in Table mode
**Status:** RULED (a) — 2026-09-21. See Decision-Log.md Entry 29.
This is general Table-mode UX (a participant leaving a multi-Representative
round mid-way), not a safety-mechanism question; unaffected by the scope
correction.
(a) A participant message sent mid-round simply closes that round
server-side and the new message proceeds — no new UI control needed.
(b) A dedicated, explicit Interrupt button. (c) Both.
**Recommend (a)** — reuses the existing message path rather than adding a
new one.

### R6 — Register-drift scope, and whether numbers ever gate a build
**Status:** RULED (a) and (iii) — 2026-09-21. See Decision-Log.md Entry 29.
Scope: (a) only the source's own original words are exempt from register
screening; our own retellings are screened. (b) all story/quote fields
stay exempt. (c) exempt everything except a `tellable_as` length/shape
check. Numbers: (i) record-layer readability numbers gate a build, and
the new register profile joins them. (ii) advisory forever, per the
existing "numbers never gate" rulings. (iii) advisory for one cycle, then
promoted to a gate.
**Recommend (a) and (iii)** — the drift is real (measured, not assumed)
and the ceilings proposed will be the fleet's own exemplars, not an
arbitrary number.

**Stage 2c ceiling proposal (2026-09-21):** `engine.m1.bar_screen` and now
`engine.m1.cross_world observe_register_profile` (report-only, per-world
per-field median words / longest sentence / fragment ratio / dash
density) give the real numbers this ruling needs. `alx` and `hal` read as
the fleet's own best-behaved worlds on every field; their own worst
values set the exemplar baseline. Not every voice-diet field is the same
shape, though: `story.tellable_as` and `term.quick_meaning` are short,
label-like fields (`tellable_as` is literally what `StoryMark.tsx` shows
as a hover-card title) — a genuinely different shape from a prose field
like `story.text` or `doctrinal_witness.text`, which the Register Bar's
own "100-150 words a turn... pressure, never a cap" already treats as
allowed to run long. This proposal is scoped to the two label-shaped
fields only; a prose-field ceiling isn't measured here and isn't part of
this proposal.

- **`story.tellable_as` longest sentence ≤ 30 words** (hal's own worst is
  27). 5 of 11 built worlds exceed it: cappadocian (33), don (54), gallic
  (53), rzg (36), witt (65).
- **`story.tellable_as` median words ≤ 25** (cappadocian, the least-drifted
  of the worlds over the line, sits exactly at 25). 5 of 11 exceed it:
  don (34), gallic (42), pahc (36), rzg (35), witt (50).
- **`term.quick_meaning` longest sentence ≤ 20 words** (ijc and syr sit
  exactly at the line). 3 of 11 exceed it: gallic (28), pahc (24), rzg
  (25).
- **`term.quick_meaning` median words ≤ 16** (hal's own worst is 14). 4 of
  11 exceed it: gallic (28), pahc (19), rzg (24), syr (20).

gallic is the worst offender on every one of the four numbers above,
consistent with R7's own framing of it as the fleet's already-drifted
world. These are proposed absolute ceilings for R6 to rule on — not
applied anywhere, not gating anything; `observe_register_profile` stays
OBSERVATION until R6 actually rules, per this stage's own "Gate promotion
... only after R6" bar.

### R7 — Fixing the fleet's already-drifted `tellable_as` text
**Status:** RULED (a) — 2026-09-21. See Decision-Log.md Entry 29. Was
blocked on R6, now cleared by R6's own ruling in the same session.
(a) A Sonnet thread does a capped-round pass per affected world. (b)
Fixed by hand. (c) Full regeneration.

### R8 — CLAUDE.md names a confidence level ("Not Attested") the code doesn't have
**Status:** RULED (c) — 2026-09-21. See Decision-Log.md Entry 29.
(a) Add a sixth confidence enum value to match. (b) Amend CLAUDE.md down
to the code's real five. (c) Amend CLAUDE.md to say what's actually true:
"Not Attested" describes an absent claim (already modeled elsewhere as an
honest-limit or absent-detail record), not a confidence rating on a claim
that exists.
**Recommend (c)** — it's not really a sixth confidence level, it's a
different kind of thing, and (a)/(b) both paper over that.

### R9 — A distinct mark for contested or thin-evidence claims
**Status:** RULED (a) — 2026-09-21. See Decision-Log.md Entry 29. Was a
sequencing gate on the Stage 1 measurement plus R16/R17, all now cleared;
proceeding with the design already agreed: a quiet, non-alarming hollow
glyph — not a new color, not a new verb.

### R10 — Where a story's citation mark lands: first sentence or end of the telling
**Status:** RULED (c) — 2026-09-21. See Decision-Log.md Entry 29. Unblocked
Stage 3c's renderer switch-on; label copy (its own remaining step) landed
Entry 41, and the switch-on itself — `VITE_TRANSPARENCY_ANCHOR_RENDERER`
defaulting on — landed Entry 49, closing this out in full.
(a) End of the telling, as built today. (b) First sentence, uniformly.
(c) First sentence for a witness quote, end-of-run for a story. A
repeated re-citation gets the lighter "ibid" glyph under any of the
three.
**Recommend (c)** — but either (b) or (c) equally fixes the dropout bug;
the real fix is the completeness guarantee underneath, not which option
gets picked here.

### R11 — Split the dead retrieval-exclusion field into a real guard record type
**Status:** RULED (a) — 2026-09-21. Stage 4a unblocked; see Decision-Log.md.
(a) Split it, as designed: a redirect half and a separate honesty-guard
half. (b) Leave the field as-is, rely only on the existing exclusion-list
fix.
**Recommend (a)** — a one-line confirmation, not really a groan-zone
decision; D1 makes the honesty half load-bearing rather than cosmetic.

**Stage 1 D1 measurement (2026-09-21):** confirmed concretely, not just in
principle. Of 714 `do_not_retrieve_when` lines fleet-wide, only 13 (1.8%)
are genuine honesty-guard clauses (a barred proposition, e.g. Brictio's
succession) — the other 701 are ordinary retrieval-scoping notes ("ask
about X instead, retrieve that record"), a different purpose entirely. The
field really is dead for the honesty purpose today: one shared field
quietly carrying two unrelated jobs, the smaller one almost invisible
inside the larger. Separately (see Decision-Log.md's own Stage 1 entry):
even those 13 real guard clauses, fabricated as flat assertions and
tagged to their own record, were caught by `check_turn()` only 2 times in
13 — both catches rode on a proper noun the fabrication introduced, not on
the guard clause itself being read at all. A structural split (this
ruling) makes the honesty half a real, addressable field; it does not by
itself make the checker enforce it — that is further engineering, not
this ruling's own scope.

### R12 — What "library accessed live" should actually mean
**Status:** RULED (live resolution only) — 2026-09-21. See Decision-Log.md
Entry 29.
Live full-text access to the vendored sources during a conversation (a
real architectural change), or live resolution of citations/evidence
only, as already built.
**Recommend live resolution only** — just fix the topology sentence that
currently overclaims this, no engineering change needed.

### R13 — Should the new "unused source" holdings check block a world from shipping?
**Status:** RULED (report-only for one cycle, then promote) — 2026-09-21.
See Decision-Log.md Entry 29. **Cycle 1 started 2026-09-21** — fleet-wide
baseline captured, see Decision-Log.md Entry 30. Promotion to blocking is
keyed to the next world admitted after this date; not yet built.
Report-only for one build cycle, then promoted to blocking for new
worlds — or blocking starting day one.
**Recommend report-only for one cycle first** — lets Mark see the real
distribution before deciding where the bar sits.

### R14 — May an output-side safety check ever remove a sentence from the Representative's answer, not just report it?
**Status:** CLOSED (`Decision-Log.md` entry 3) — never, in any form. The
mechanism reports only, exactly as it does today. Not revisited later.

### R15 — A distinct message when someone discloses risk about a third party, not themselves
**Status:** CLOSED (`Decision-Log.md` entry 3) — one message, no branching
by disclosure type.

### R16 — Every record fleet-wide is still marked "draft" — what does that mean for confidence display?
**Status:** RULED, corrected — 2026-09-22. See Decision-Log.md Entry 42
(supersedes the 2026-09-21 wording immediately below, which is Entry 29's
own original ruling text, kept intact per this file's convention — not an
edit to Entry 29 itself). **Promote by admission now, fleet-wide**: a
record is ready once it sits in an admitted world's currently pinned
package and passes every M1 gate — no longer deferred to each world's
next real touch. `status` stays pure workflow bookkeeping; confidence
display draws only from `formation_confidence`, never `status` (Entry
29's part (b), unaffected).
(a) Define what "ready" actually means and run a per-world promotion pass
keyed to review rounds already on record. (b) Rule that `status` is pure
workflow bookkeeping and confidence display should draw only from the
separate confidence field, never from `status`. (c) Both — rule (b) now
so nothing is blocked indefinitely, and do (a) as each world comes up for
its next real touch.
**Recommend (c)** — confidence display for a given world only goes live
once that world has actually been through its promotion pass.

### R17 — A hard budget on how many new transparency elements can stack on one screen
**Status:** RULED (approved as house rule) — 2026-09-21. See
Decision-Log.md Entry 29. Both halves of the read-through this ruling
itself required — the automated cap test (Entry 38, PR #399) and Mark's
own seeker read-through, on both sides (Entry 46 mine, Entry 48 Mark's
own, verdict: promote) — are done; gate fully closed.
Proposal on the table: at most a small, capped number of inline marks per
turn (scaling gently with sentence count), one collapsed references line
instead of a scattered list, no new mark types beyond the one
contested-claim variant under discussion, and the unverified-claims count
never rendering to a participant at all.
**Recommend approving the cap as a house rule**, enforced by an automated
test so no future change can silently stack past it — plus Mark's own
read-through as a seeker with no background before Stage 6 ever ships.

### R18 — The onboarding text overclaims what the honesty check actually does
**Status:** RULED (a), text corrected — 2026-09-22. See Decision-Log.md
Entry 44 (the exact ruled `SYSTEM_NATURE`/`about.html` replacement text,
superseding PR #383's same-day-earlier reword below — not an edit to
Entry 29 itself).
Today's line tells a participant every claim is "checked against the
record it came from" — true only in the sense of word-overlap, not
truth-verification. (a) Reword now to describe what the mechanism
actually does. (b) Leave it and wait for the (currently blocked) display
affordance that would make the current wording accurate.
**Recommend (a)** — this is a participant-facing honesty gap in its own
right, independent of anything else in this workstream, and doesn't need
to wait on Stage 1's measurement to fix.

### R19 — Should every world's own voice carry the same distress-minimization guard clause?
**Status:** RULED and RETROFITTED — 2026-09-21. See Decision-Log.md
Entries 28 and 32. All 10 gap worlds' `voice_craft.guard` now carry the
addition; package recompile is the one remaining mechanical step.
Note: this is a Representative-voice authoring question — the guard is a
prohibition on the Representative comparing or minimizing a participant's
own disclosed distress against the world's own historical suffering ("not
the same weight as our martyrs"), staying entirely in the world's own
voice and period. It does not direct a Representative toward outside help
or any language outside its world/time — that stays Facilitator-only,
governed outside any world's own voice, per Safety comes first
(CLAUDE.md). This ruling is not part of the closed Facilitator-mechanism
scope above, and does not touch it. (Earlier drafts of this entry called
it a "don't recommend outside help" guard clause — that was the wrong
name for what the mechanism actually does and has been corrected here.)

**Ruled: extend fleet-wide, each world's own voice, folded into the
standing build-cycle discipline, existing gap worlds retrofitted.** Not
identical text — every world resolves the question in its own idiom; what's
decided once is that every world must have *some* honest version of it.
Three-part scope, enforcement mechanism, and open engineering question
(the keyword-scan check's own reliability across worlds with genuinely
different wording) — full detail in Decision-Log.md Entry 28. Retrofit of
the **10** gap worlds (alx, cappadocian, desert, gallic, hal, ijc, pahc,
rzg, syr, witt — corrected from 9, see Decision-Log.md Entry 31) is now
done — see Decision-Log.md Entry 32 for the final text per world and how
it was reached. Folding the requirement into the standing build-cycle
discipline for future worlds is still outstanding.

**Stage 0e observation pass (2026-09-21), `engine.m1.cross_world`'s new
`observe_outside_help_guard`** (report-only, keyword scan, not a semantic
judgment — see its own docstring): of the 11 built worlds, only **don**
carries don-style distress-comparison language ("measured against" /
whole-word "weigh"/"weighs"/"weighed"/"weighing" / "not the same weight")
in `voice_craft.guard`. The other 10 do not: **alx, cappadocian, desert,
gallic, hal, ijc, pahc, rzg, syr, witt**. This is the concrete list R19's
ruling needs. (An earlier version of this scan matched "weigh" as a bare
substring, which false-positived on rzg's own "felt weight" — a
doctrine-thinness phrase, not a distress comparison — and wrongly counted
rzg as already covered. Fixed word-boundary, per Decision-Log.md Entry
31; rzg moved from "carries" to the gap list here.) Editing any
`voice_craft.guard` field is a Representative-voice change (`Build-Plan.md`'s
own escalation category), so no world's guard text is touched here.

### R26 — May a Representative speak about another tradition, or claim a doctrine its own world's records don't hold?
**Status:** RULED — 2026-09-22. Mark's own words, via the reviewer
thread's standing authorization (see Decision-Log.md Entry 50):
> "The representative should only know its own sources unless they would
> have known the sources from another in reality."

**Ruled shape:** on a first ask about another Christian tradition — if
the asked world's own records hold nothing on it, the voice answers
*"Our record doesn't mention that Christian tradition."* and then
answers the rest of the question from its own records. If the records
do hold something, the voice speaks only from those records, cited. The
Facilitator's existing `other_tradition` etic turn stays as the
mechanism for a second press.

**Origin, the real staging defect this closes:** `cic-engine-staging`,
Theon/alx asked "what was your relationship with the donatists"; alx
holds zero records mentioning Donatists (grep-confirmed). The voice
described Donatist history uncited, and attributed to Alexandria itself
a sacramental doctrine no alx record holds ("what the sacrament does,
it does by Christ's power, not the minister's purity"; "even a broken
priest could not block his grace") — Augustine's own doctrine, a
century later, not alx's.

R26's two violation shapes (a neighbour tradition named without
citation; a doctrine belonging to a different world asserted as the
answering world's own, inside an `other_tradition` turn) are not a
separate guard — they are violation classes inside R27's own check.

**Built, 2026-09-23 (R39's own audit found the gap; no new ruling
needed — this closes an implementation gap against R26's own already-
ruled words above, "if the records do hold something, the voice speaks
only from those records, cited," which the shipped code never actually
branched on):** `_other_tradition_directive` (`engine/m4/turn.py`) used
to say the fixed honest-limit sentence unconditionally, regardless of
whether the speaking world's own records already named the tradition
asked about — provably false for `ijc` on Donatism, whose own records
(`ijc.quote.compelled-to-come-in`, `ijc.story.emperor-builds-another-
basilica`) genuinely do. Now conditional: `engine.m4.uncited_claims.
match_named_tradition`/`world_records_mention_tradition` detect real
evidence in the speaking world's own package before the directive is
built; a world with real evidence gets the record ids as its own
ground instead of the honest-limit sentence, a world with none gets the
sentence exactly as it always was. Full detail, the real per-world
count (4 of 11 built-fleet worlds flip), and tests: Decision-Log.md's
new entry.

### R27 — A hard requirement: every declarative claim sentence carries a citation
**Status:** RULED (option A) — 2026-09-22. Via the reviewer thread's
standing authorization (see Decision-Log.md Entry 50).

**Ruled:** every declarative claim sentence in a voice turn must carry a
citation, or be one of a short, closed list of allowed uncited kinds:
(1) an honest-limit sentence — R26's own form above, and the world's
existing honest-limit forms; (2) a question back to the participant;
(3) first-person framing that makes no historical or doctrinal claim.
Deterministic check, no new model call (Constraint A holds — see
Decision-Log.md Entry 51 for the exact detection design).

**Rollout, report-only first:** ships report-only for one week to
measure the real per-world uncited-claim rate, then enforced with the
seat-guard's own shape (regenerate once with the violations named, then
the Facilitator takes the turn). Mark sets the enforcement threshold
once the measured rate is in (build order item 4, Decision-Log.md Entry
51). Full build order, engineering detail, and the R26 first-ask
directive wiring: Decision-Log.md Entry 51.

### R27-A — Amendment: the unit of enforcement is the paragraph, not the sentence
**Status:** RULED — 2026-09-22. Mark chose this from three options put
to him after PR #419's own live numbers (Decision-Log.md Entry 52's own
data: 86% raw sentence-level rate, 84% residual after one regeneration).
Via the reviewer thread's standing authorization.

**Ruled shape:** a paragraph must carry at least one citation. The
grounding net checks every sentence in that paragraph against the union
of that paragraph's own cited records, not only the tagged sentence — an
untagged sentence inside a cited paragraph is checked against that
paragraph's own citations, the same way a tagged sentence already is. A
wholly uncited paragraph fails, unless every sentence in it is one of
R27's own allowed-uncited kinds (question back, honest-limit,
first-person no-claim). R26's two classes — `neighbour_named` and
`own_doctrine_in_other_tradition_turn` — stay per-sentence hard
failures; the paragraph unit is R27's own base check only.

**Rollout unchanged from R27 itself:** report-only with rates first,
Mark sets the threshold, then flag-gated enforcement with the same
seat-guard shape (regenerate once with the failures named, then the
Facilitator takes the turn). Full build order (design entry, report-only
module change, tests, battery, enforcement): Decision-Log.md's own R27-A
entry.

### R30 — Stage 7 streaming, E1: what a participant sees on a mid-stream guard catch
**Status:** RULED (option c) — 2026-09-22. Via the reviewer thread's
standing authorization.

**Ruled:** hold the opening paragraph until the guard has checked it,
then stream sentence by sentence from a point already known to be clean.
A mid-stream catch after that point follows the seat-guard shape already
ruled (regenerate once, then the Facilitator takes the turn) — the 7b
design entry states exactly what the participant sees in that residual
case, and anything other than the Facilitator closing the turn with the
sentences already shown left in place escalates to Mark before it is
built.

### R31 — Stage 7 streaming, E2: when a citation mark attaches during a stream
**Status:** RULED (option a) — 2026-09-22. Via the reviewer thread's
standing authorization.

**Ruled:** a citation mark attaches with each sentence as it clears. An
R17 cap demotion at turn end moves an already-shown mark to the
references line — it never removes a sentence or a claim.

### R31-A — Amendment: marks are per distinct grounded element, not per sentence; how should more than one on the same sentence be told apart?
**Status:** RULED (option a) — 2026-09-23. Via the reviewer thread's
standing authorization. Mark's own correction, relayed verbatim, of the
reviewer's first framing of a staging defect report: *"i am not sure
why we can only have 1 mark per sentence, i get not overloading, but if
a quote and a lexicon word are in the same sentence they should both
marked."* Found on Mark's own staging Table look, full detail in
Decision-Log.md Entry 58.

**Ruled (the count question):** a mark is per distinct grounded
element — a story, a witness quote, a term — never reduced to one per
sentence. Theon's own turn (*"...long before any emperor cared.✲✲"*)
showing two marks stacked on one sentence is not a bug under this
reading; it is what today's renderer already does whenever a
story/quote record and a `doctrinal_witness` record both finish their
citing run at the same sentence.

**Ruled (the readability question): option (a), mark placed at its own
element.** Each mark sits at the element it marks — a quote's mark
follows the quoted words, a term's mark follows the term, a claim's
mark ends the sentence. One mark per distinct grounded element, none
duplicated. The three options weighed, one-paragraph-each with cost:
(a) **Mark placed at its own element (RULED)** — each mark moves to sit
after the specific span inside the sentence it actually grounds, not at
the sentence's end. Reads most like ordinary punctuation; needs new
span-level placement data the anchors don't carry today - the design
brief for this build is queued after the G1-G7 retrofit PR, before
Stage 7b, since 7b's own per-sentence marks must be built to this rule.
(b) **One glyph per kind** — marks stay at the sentence boundary, but
the story mark and the witness mark get visually distinct glyphs
instead of two identical ✲. Smallest change of the three; adds a
second glyph to the fleet's "one grammar, five applications" rule. Not
chosen.
(c) **Single mark, tap/hover card listing all elements** — collapse
however many marks land on one sentence into one glyph; tapping opens
a card listing everything it covers. Cleanest on a phone screen; hides
the "there were two things here" signal a participant gets today
without tapping. Not chosen.

**Also unresolved:** which two real records produced Theon's own two
marks was not confirmed — the exact sentence has no saved report, pool
file, or transcript this repository can read, and pinning it needs
either a live regeneration against the original prompt or persisting
`apply_net`'s own per-sentence citations for staging turns going
forward. The two records named as the likely (not confirmed) pairing
in Decision-Log.md Entry 58 are real alx records on the same topic,
offered honestly as the best evidence available, not as fact.

### R36 — R27-A's own enforcement threshold: which paragraph classes are enforced
**Status:** RULED — 2026-09-23. Mark chose this from three options put
to him after PR #427's own live numbers (Decision-Log.md Entry 54's own
data: 22 interview probes, 55% would-regenerate at the paragraph unit
[12/22], 42% of those [5/12] would still reach the Facilitator after one
regeneration; the net's own inherited-check verdicts split 81 ok / 50
withhold). Via the reviewer thread's standing authorization.

**Ruled:** enforcement (item 5) covers `wholly_uncited_paragraph` only,
for now. `inherited_ungrounded` stays report-only until the hand-sort
of the withheld inherited sentences shows the inherited check measures
substance rather than mere word overlap — Mark rules on it separately
once that question is settled (see the hand-sort finding below).
`neighbour_named` stays a per-sentence hard failure, unchanged from
R27-A's own base ruling. `own_doctrine_in_other_tradition_turn`, already
narrowed per Entry 55 to fire only on a real paragraph-level failure,
therefore fires in practice only through a `wholly_uncited_paragraph`
finding while `inherited_ungrounded` stays report-only — its own
narrowing rule is unchanged, only which paragraph classes actually
reach it in practice.

**The hand-sort finding this threshold rests on** (reported to the
reviewer thread 2026-09-23, from #427's own report): of the 50 raw
"withhold" inherited-check tallies, only 28 correspond to an actual
reported `inherited_ungrounded` offense with recoverable sentence text
(the other 22 were sentences whose own base verdict was already
`withhold` for reasons unrelated to paragraph inheritance, e.g. an
untagged quoted span — verified directly with a synthetic repro, not
assumed). Of those 28: 3 genuinely unsupported, 19 supported in
substance but failing on word overlap (narrative frame, paraphrase,
pronoun reference), and 6 that should have been exempt under R27's own
allowed-uncited kinds (a question, an honest-limit sentence, a hedge —
one of the 6 is R26's own fixed honest-limit sentence, near-verbatim)
but weren't, because `find_uncited_paragraphs`'s `inherited_ungrounded`
branch never applies the question/honest-limit/first-person exemptions
its own `wholly_uncited_paragraph` branch already does. That exemption
asymmetry is a real bug, not a measurement artifact, and inflates the
`inherited_ungrounded` numbers a threshold would be set against — hence
report-only until it's fixed and re-measured.

**Rollout:** flag-gated, default off (`CIC_R27_ENFORCE` or equivalent),
nothing changes for any participant until Mark flips it after a staging
look. Same regenerate-once-then-Facilitator shape as R27/R27-A's own
base ruling. Full build order: Decision-Log.md's own R36 entry.

**The enforced-run baseline** (PR #432, real, billed, region us-east-1,
flag actually on): interview, 7 of 22 turns regenerated, 2 of those 7
reached the Facilitator. Table (alx/don/rzg), 7 of 10 voice turns
regenerated, 4 of those 7 reached the Facilitator - see Decision-Log.md
Entry 56's own note on what that Table rate means and the likeliest
cause. This is the baseline number set Mark looks at on
`cic-engine-staging` (`CIC_R27_ENFORCE=1`) before the flag is flipped
anywhere real.
