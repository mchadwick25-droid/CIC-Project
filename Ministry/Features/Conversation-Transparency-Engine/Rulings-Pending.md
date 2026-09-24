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

### R41 — G5, R39-audit: should a modern/anachronistic word be answered by the Representative itself, or always intercepted by the Facilitator first?
**Status:** RULED — 2026-09-23, via the reviewer thread's standing
authorization. Not strictly (a) or (b) below: Mark asked first for the
risks of letting the Representative handle a modern word directly
(definition leak, a false mapping of the modern term onto the world's
nearest concept, dating the term from outside the record, the seam
hidden inside the Representative's own turn, loss of per-term control),
then ruled on those risks. **The Representative acknowledges the
participant's own word and answers from its record only - it never
defines the modern word.** The Facilitator's modern-sense explanation
moves out of a spoken turn entirely, into the term's hover card. **The
bridge route stays exactly as built until a measurement shows the risks
above are near zero** - see R41-A below for the framing this sits
inside, and the follow-up measurement queued after 7b in this program's
own build order.

**Found by the reviewer's own R39-audit retrofit brief:** `pronoun_rule` (`_fleet.voice.
fleet.md` line 31) and the bridge route (`turn.py`, the `bridge_turn`
action) instruct two different answers to the same question, and are
never both live on the same turn - for any term actually on the fleet's
own `anachronistic_term_ids` registry, routing sends the turn to the
bridge route before the voice ever sees it, so `pronoun_rule`'s own
clause (below) can never fire for that term in practice. This is a
governance/methodology question - how the voice and the Facilitator
divide this kind of moment - one of CLAUDE.md's own standing escalation
categories, not a default either thread should pick on its own. Full
file:line evidence and both mechanisms quoted verbatim: Decision-Log.md
Entry 59 (this PR).

**`pronoun_rule`'s own clause, verbatim:** *"when a participant's own
question brings it, we name it as theirs - 'the later word
transubstantiation you are calling it' - and answer from what we
actually had; that stays exactly as it is."* One turn, one speaker: the
Representative names the modern word as the participant's own, then
answers from what the world actually held, all in its own voice.

**The bridge route, as actually built:** the reader detects a
registered term, routes to `bridge_turn`; the Facilitator composes and
speaks a message naming the modern word and its modern sense in the
Facilitator's own etic voice, then hands the Representative only a
term-free rephrasing of the underlying question - the voice never sees
or utters the participant's original word at all.

**(a) Let `pronoun_rule` govern.** Stop routing a term already covered
by `pronoun_rule`'s own clause to the bridge route (or narrow which
terms the bridge route actually intercepts). What a participant reads:
one continuous turn - the Representative's own answer opens by naming
the word as the participant's own, then answers from what the world
actually held, no separate Facilitator message before it.

**(b) Keep the bridge route as the one actually exercised for
registered terms.** `pronoun_rule`'s own clause describes an ideal that
is unreachable for any term on the registry as things stand - routing
overrides it before the voice ever runs. What a participant reads: two
turns, two speakers - a Facilitator message, openly outside any world's
voice, naming the modern word and its modern sense, then a separate
Representative turn answering only the translated, term-free question,
with no trace of the participant's original word in it at all, not even
an acknowledgment it was asked.

No code changes to either mechanism have been made under this entry;
both stay exactly as built until Mark's R41 ruling above takes effect
in a future build (queued after 7b - see R41-A immediately below for
what that build must cover).

### R41-A — the participant-facing frame R41's ruling sits inside, and three build-proposal requirements
**Status:** RULED — 2026-09-23, via the reviewer thread's standing
authorization, amending R41. **The participant-facing framing is a
universal translator.** The about text will say, once, that everything
a Representative says reaches the participant through a translator, and
that a modern word with no equivalent in the Representative's world
comes through untranslated: the Representative names it as the
participant's own word and answers from what its world had.
`pronoun_rule`'s own clause (quoted above) is therefore load-bearing
and stays exactly as written - it is the translator declaring "no
equivalent." The modern sense of the word lives on the term's hover
card, in no one's voice. **Mark writes the about-page wording
himself** - no participant-facing words for this are to be drafted
here. The Facilitator bridge turn retires once the R41 measurement
(definitions, false mappings, dating claims, out of twenty - see R41's
own queued follow-up) comes back near zero.

**Three additions required of the eventual R41 build proposal**, not
of this entry: (a) where the about text lives in the frontend and how
it is loaded, so Mark's wording drops in without a code change; (b)
the bridge route's own retirement path - routing no longer sends
registered terms to `bridge_turn`, the term-free rewrite goes away,
`bridge_turn` itself stays in code, unreachable, until a later cleanup;
(c) confirmation that the hover card already shows the modern sense
for registered terms via `term_glosses`, or a plain statement of what
is missing if it doesn't. All three land when the R41 build itself is
proposed (queued after 7b), not before.

### R42 — R27 detector precision follow-up: which of the three options?
**Status:** RULED — 2026-09-23, via the reviewer thread's standing
authorization. Mark's own follow-up question to G1's null result
(Entry 60, this PR): the precision of the `uncited_claims` detector
behind that entry's own 95.5% raw flag rate. Measured in Entry 61 (this
PR) - 40 sentences sampled across all 11 worlds from a fresh 22-probe
run, hand-read against each world's own freshly compiled records: **0
of 40 genuinely unsupported, 14 of 40 real record-supported claims the
voice simply never tagged, 26 of 40 interpretive or connective prose
the citation contract already exempts.**

**Ruled: option (i).** R27 stays report-only; the citation contract
stands as written; enforcement is off. `CIC_R27_ENFORCE` remains
default off in `engine/api/config.py`, and Mark is turning it off on
staging himself. The detector is kept as a measured instrument, its
precision on record here rather than assumed. Candidates (ii) (the
contract adopts the paragraph rule, with enforcement returning once a
generation-side change moves the raw rate) and (iii) (rebuild the
detector around "unsupported" only) are closed.

**Follow-up, queued after 7b, not before - a generation-side item, not
a check:** the 14 of 40 sentences that were true but carried no tag are
a citation-completeness gap on the generation side. Propose one
report-only directive line asking the voice to tag any sentence that
draws on a record even when it names no person, number, or quote;
measure it on the same 22-probe run by the same hand-read method (count
of true-but-untagged before and after); report the two counts and the
cost. No enforcement follows from the number either way - this is a
generation-side improvement or nothing. Note for whoever runs this:
with G6's fix (this PR) now merged, R27's detector examines withheld
sentences too, so any battery numbers quoted after this merge are not
directly comparable to Entry 56's own pre-G6 numbers - say so wherever
they're quoted.


### R38 — A fabricated clause rode a real citation match past the net: what general rule closes it?
**Status:** RULED — 2026-09-23, via the reviewer thread's standing
authorization. A SIBLING question the same worked example raised -
whether the PIVOT itself (steering to "the lapsed" on a Donatist
question at all) was legitimate - is R37, RULED separately; see R37
immediately below. Found on Mark's own staging look
(`CIC_R27_ENFORCE=1`, first result), full detail in Decision-Log.md
Entry 63.

**Ruled: self-revision at generation** - not candidate (a) or (b) (the
lexical-remainder net rules, CLOSED: they withhold honest paraphrase to
catch a class with 0 of 6 precision) and not candidate (c) (the live
support-check reader) as the primary mechanism - (c) stays the fallback
only, and is not needed: the real, measured leak rate under self-
revision is 0 of 20, at or under the bar Mark set ("if leaks are 0 or 1
of 20, propose the build").

**What self-revision is:** after the voice drafts its turn, a second
voice call - same model, same system prompt - is given its own draft
plus the exact, full text of every record it tagged, and told: for each
tagged sentence, keep only what that record says or exactly paraphrases;
trim any detail the record does not give, even if believed true; do not
add, do not re-tag, do not change any untagged sentence; return the
revised turn. The revised turn is what `apply_net` sees and the
participant reads - generation, not correction: no withhold, no
Facilitator, no regeneration loop. Scoped to `other_tradition`-routed
turns only, where the leak class lives.

**Measured** (`engine/m4/reports/r38_self_revision_measure.py` +
`r38-self-revision-measure-2026-09-23.json`, this PR): the Theon/
Donatists worked example, 20 runs, proposed directive (Entry 65) plus
self-revision, unconditional on every run (not gated on a pre-check of
which drafts need it - matches how it would actually run in
production). **Real cost: $0.5207, 40 calls** (20 drafts + 20 revision
passes). The revision pass changed the text in 20 of 20 runs - real
work, not a no-op most of the time. **Real leak rate: 0 of 20** - all 8
draft occurrences of the traditor/scripture-surrender detail ("handed
over the scriptures"/"the Scriptures", the same unsupported clause
named in Entries 57/59/60) were removed in revision; none reached the
final, participant-facing text. Hand-read for over-trimming (a true,
record-supported detail lost, not just the known leak shape) on a
representative sample of the 20 pairs - no case found; every trim
checked removed either the fabricated clause itself or a separate
unsupported interpretive elaboration ("we thought the church had
authority to forgive what Christ forgave" - a real theological gloss,
but not the record's own words or a fair paraphrase of them), and real
supported detail the draft had omitted was sometimes correctly restored
too ("The strict party demanded they stay out" - genuine record text,
absent from one draft, present after revision). Full per-run pairs:
Decision-Log.md Entry 67.

**Candidate C's own numbers stand as measured** (Entry 63: 2/6
own-clause precision, non-deterministic, 14.5% raw flag rate dominated
by false positives) but are not needed as the primary mechanism given
self-revision's own 0/20 - C remains available as a documented fallback
if a larger sample later shows self-revision's real rate above 0.

**Built** - PR #445 (`engine/m4/self_revision.py`), exactly as proposed
below: same call site, same scope, same kill-switch shape as `r27_
enforce`'s own parameter-threading. `CIC_SELF_REVISION`, default ON.
Real per-turn cost/latency from a live run are not available yet (not
deployed live); PR #445 closes the cost-separation gap this entry
names below by logging the revision call under its own `call_kind=
"self_revision"`, distinct from the draft call's `"voice_generation"`.

**Proposed build** (per Mark's own ask - propose since leaks are ≤1/20):
- **Where it sits:** `engine/m4/turn.py`, inside `_run_ordinary_voice_
turn`, immediately after the draft's own `stream_voice_turn` call
succeeds and before `apply_net(raw_text, ...)` runs - the revised text
replaces `raw_text` going into `apply_net`, so the entire existing
downstream pipeline (net check, citation resolution, transparency plan)
runs on the revised text unchanged, with no new caller-side branching.
- **Scope:** gated on `is_other_tradition_first_ask=True` only (the
same flag `_other_tradition_directive` already gates on) - an ordinary
turn never pays the extra call.
- **Cost:** this measurement did not log draft-call and revision-call
cost separately (a real gap - a follow-up run should), so the number
here is the blended average across both call shapes: **~$0.013/call**
($0.5207 / 40). The marginal cost of self-revision (the one new call
per `other_tradition` turn) is of that same order - roughly doubling
the AI cost of an already-rare turn class, not the fleet's average
turn cost.
- **Latency:** not logged per call either; the real, measured wall-
clock for the whole 40-call sequential run was ~330 seconds, ~8.25s/
call average end to end. Self-revision adds one more sequential call of
that same order to an `other_tradition` turn - roughly doubling that
turn's own latency before anything reaches the participant.
- **Streaming (7b/R30):** R30's own ruling already holds the opening
paragraph until the guard has checked it, then streams from a point
already known clean. Self-revision fits the same shape without a new
mechanism: the draft-then-revise pair completes as one atomic pre-
stream step - the guard check (and streaming) never starts on the
DRAFT text, only on the already-revised one. This makes the "hold"
phase longer specifically for `other_tradition` turns (the rare class
this measurement scopes to), consistent with, not competing against,
R30's own rule that the opening is never released before it is known
clean.

**The worked example:** interview, Theon on the Donatists. The R26
opener fired correctly; the answer that followed included, tagged to
`alx.dw.church-failure`: *"Under persecution, some gave way - they
sacrificed to the gods, or they handed over the sacred books."* The
record's own text supports "many gave way. Some sacrificed to the
gods." - nothing in `records/alx` supports handing over books
(traditores) - and the added clause is specifically the Donatist
traditor charge, the very tradition the opener said this world's own
record does not cover. `alx.dw.church-failure` is not touched by
anything here; its text is correct.

**The mechanism, verified against the real code (not assumed from the
first report of it):** the sentence carries no literal quote marks, so
it never reaches the quoted-span window check
(`engine.m4.grounding_net._span_in_records`) at all. It has no proper
noun/number/enumeration, so `verdict_for_sentence` routes it into its
own "TAG IS THE CLAIM" branch - gated on ANY nonzero content-word
overlap with the tagged record, no ratio floor. Five of the sentence's
eight content words are in the record's own vocabulary; three (books,
handed, sacred) are not, and nothing in this branch ever examines that.
Full detail and the correction to the reviewer's own first diagnosis
(which named a different branch): Decision-Log.md Entry 63.

**The measurement** (report-only, `engine/m4/reports/
net_remainder_measure.py` + `net-remainder-measure-2026-09-23.json`,
this PR): 311 tag-bearing sentences across the real Corpus A pool
(34 turns, 529 sentences scanned, re-run against current packages) were
marked grounded via a real grounding decision. Remainder (content words
absent from the tagged records' own vocabulary) distribution: 0 words -
150; 1 - 43; 2 - 27; 3 - 21; 4 - 14; 5+ - 56. 6 of the 311 have a
remainder that forms one coordinating clause of its own (3+ content
words, all unmatched) - the worked example's own shape; every one of
those six carries a remainder of 3 or more words.

**None of the six is a fabrication** (named and checked individually,
Decision-Log.md's own entry has all six) - one Origen paraphrase, one
"Old Testament and New alike" framing clause, descriptive geography, an
honest-limit scaffold sentence in substance, an apatheia paraphrase,
and pure first-person framing. **On this corpus, the own-clause shape
has 0 of 6 precision** - the only confirmed fabrication anywhere in
this entry is the staging worked example itself, which is not in this
corpus at all. Lexical remainder cannot tell "handed over the sacred
books" from "the whole of Scripture is one voice"; both candidates
below withhold real, honest paraphrase to catch a class with zero
confirmed real instances here. Candidate (c) below is proposed for
exactly this reason.

**Three candidates, numbers from the measurement, none built:**
(a) **Full coverage** - remainder must be 0, and a quoted span over six
words must be covered end-to-end, not by one internal window. Closes
every gap found, including the quoted-span branch's own separate one
(a >6-word quote today only needs one true 6-word window inside it).
Cost: 161 of 311 (51.8%) of currently-grounded sentences would newly
withhold - roughly half, and most of that half reads as ordinary,
honest paraphrase on inspection, not fabrication.
(b) **Bounded remainder, N=2** - a sentence is grounded only if its
remainder is 2 content words or fewer (0, 1, or 2 passes; 3 or more
withholds). Catches all six known own-clause cases (including the
worked example, remainder 3) while leaving harmless single-word
paraphrase untouched. Cost: 91 of 311 (29.3%, the 3/4/5+ remainder
buckets) would newly withhold. Needs its own rule for the quoted-span branch
(most naturally (a)'s own full-span-coverage requirement, applied to
that branch alone).
(c) **A live Haiku 4.5 reader support check** - real record: does the
tagged record's own text support every claim in the sentence, naming
the unsupported clause. Real cost $0.6391/312 calls ($0.00205/sentence,
estimated before running, within the pre-estimate). **Catches the
worked example exactly** (`partly_supported`, names "they handed over
the sacred books"). Full 311: 45 (14.5%) not fully supported - less
aggressive than (a)/(b). **Own-clause precision: 2 of 6** - not
meaningfully better than (a)/(b) on the six known-honest cases; four of
six, including a real theological gloss and the `desert` honest-limit
sentence, get flagged too. **Not deterministic** - the same sentence
against the same record, checked twice minutes apart, returned two
different verdicts; a real structural cost (a)/(b) do not carry. Full
numbers: Decision-Log.md's own entry.
**No recommendation between the three** - (a) is simple and closes the
whole family at the cost of roughly half of today's honest paraphrase;
(b) is more surgical but leaves a small, permanent unexamined residue by
construction; (c) is the only one that names what's unsupported and
catches the real fabrication precisely, but is non-deterministic and no
more precise than (a)/(b) on the six known-honest cases. Any of the
three needs its own live re-battery before an enforcement number is
trusted, same discipline R36 itself was built on.

**Separately, the R26 leak class** (also Decision-Log.md Entry 63):
`engine.m4.uncited_claims.find_uncited_claims` skips every TAGGED
sentence outright, so a correctly-cited-but-partially-fabricated
sentence is invisible to the entire R26/R27 apparatus - checks citation
presence, never citation accuracy. Confirmed no check anywhere in the
pipeline (including the pre-generation "reader," which never sees what
the voice actually writes) looks at a tagged sentence's own content
once it clears the net. Proposed, not built: for an `other_tradition`
turn, test a tagged sentence's own remainder against the DISCLAIMED
tradition's own vocabulary specifically - needs cross-world lookup this
module does not have today, a real added piece. Note: candidates (a)/(b)
above would already catch this specific worked example without any
cross-world lookup at all (the clause fails on remainder alone,
regardless of which tradition it belongs to) - whether the narrower,
tradition-aware check is still worth building on top is part of what
this ruling needs to settle.

**R39, Mark's own principle** (relayed 2026-09-23): *"our goal is to
generate the right conversation, not correct it... checks are fine but
ideally unused because the engine generates it correctly."* Amends R38
above, ahead of choosing between (a)/(b)/(c): the real cause (the tag
promises the ADDRESS is real, never that non-quoted CONTENT stays
inside the record - `_other_tradition_directive` never anticipated
topic-adjacent outside knowledge bleeding into a tagged sentence about
the SPEAKER'S OWN record) and a proposed generation-side directive fix
(tag-is-a-promise + R37's own knowledge scope), measured live: 20
regenerations of the worked example under the current directive versus
20 under the proposed one. Hand-read, not lexical remainder or candidate
C's own raw flags (R38's own precision problem applies to C too - most
of its 23/73 and 27/89 raw flags are honest paraphrase on inspection).
**Real leak rate: 3 of 20 runs before, 2 of 20 after** - a real but
partial improvement; the exact traditor detail ("handed over the
scriptures") recurred twice under the fixed directive, once alongside
the libellatici detail this project's own build already removed once
by hand from `alx.dw.church-failure`. Candidate (c) is the better-
aligned backstop of the three (tracks the real leak rate, not lexical
mismatch on honest content); its own expected fire rate once the
directive fix ships is in the 10-15% neighborhood, not the "near zero"
Mark asked for and not what its own currently-measured 14.5% raw rate
shows either (that rate mixes real leaks with (c)'s own false
positives). Full detail: Decision-Log.md Entry 65.

**R39 follow-up** (the reviewer's own next ask, 2026-09-23): two more
conditions on the same worked example - D1, the proposed directive
plus `alx.dw.church-failure` offered in the evidence block with its
real, full text (the retrieval fix); D2, D1 plus one explicit line
("tag only records offered in this turn's own ground"). **Real cost
$0.5062, 40 calls. D1: 2 of 20 - identical to the directive-alone
condition above.** Offering the record's real full text made no
measurable difference over the directive fix alone. **D2: 4 of 20 -**
not an improvement, numerically worse than D1 (not a confirmed
regression at n=20, but a real, hand-verified count). Neither addition
tested here beats R39's own directive fix alone; the residual leak is
not a retrieval problem and is not closed by stating the ground/prompt
distinction explicitly either, on this sample. Candidate (c)'s own
expected fire rate on top of the best condition (10% real leak rate,
tied between the directive-alone condition and D1): roughly one in
three of real leaks, per its own 2/6 own-clause precision (R38 above)
- expected to catch on the order of 3-4% of turns' real leaks, leaving
roughly 6-7% uncaught even with the net running as backstop. Full
detail: Decision-Log.md Entry 66.

### R37 — When may a Representative's pivot draw on outside knowledge of a named-but-uncovered tradition?
**Status:** RULED — 2026-09-23, 12:47Z; R37-A the same day; R37-B
2026-09-24. **BUILT** — Decision-Log.md Entry 69 (the design brief,
carried forward from PR #438, now closed as superseded) and Entry 70
(the build). All three via the reviewer thread's standing authorization.

**Mark's own words (R37):**
> "only if it would have known in its own time, or if something what
> revealed in the facilitators introduction or user, but limited only
> to what was told to them in the conversation"

R37 refines R26 (above, "The representative should only know its own
sources unless they would have known the sources from another in
reality").

**Origin:** Mark's own staging look (`CIC_R27_ENFORCE=1`, first
result): interview, Theon on the Donatists. The R26 opener fired
correctly ("Our record doesn't mention that Christian tradition."), and
the answer then steered to Theon's own lapsed controversy - even though
alx's records never mention Donatism by name. A separate question from
whether the answer's own content was fabricated (R38, above): not
whether the fabricated clause should have streamed, but whether Theon
was allowed to steer toward "the lapsed" at all.

**Ruled, stated in full:** when a question names a tradition outside
the Representative's own record, the Representative may use knowledge
of that tradition to choose which part of its own record to answer
from only under two conditions. **(a)** It would have known of that
tradition in its own time. **(b)** It was revealed in this
conversation, and then only what was actually said, nothing beyond it.
Outside those two, the pivot must come from the question's own words
alone. **In every case, content about the other tradition still never
enters the answer from outside the record** - that stays R38's
question. Under (a), Theon (alx, window 150-400) steering to his own
lapsed on a Donatist question is allowed; "handed over the sacred
books" remains a leak either way (R38).

**R37-A — the asymmetric window reading (2026-09-23).** A
Representative may know of any tradition that arose before or during
its own window; only a tradition that had NOT yet arisen by the
window's end sits outside condition (a). The test: the named
tradition's `time_window` start is at or before the speaking world's
own `time_window` end. On the design brief's battery this makes 11 of
11 other-tradition probes defensible (9 of 11 under the symmetric
reading R37-A declined).

**R37-B — another Representative (2026-09-24).** Mark's own words:
> "add or what another representitive revials in the conversation R37"

Condition (b)'s sources are therefore three: the Facilitator's
introduction, the participant, and another Representative - each only
for what was actually said in this conversation.
