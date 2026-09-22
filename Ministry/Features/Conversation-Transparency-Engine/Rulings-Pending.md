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
**Status:** RULED (c) — 2026-09-21. See Decision-Log.md Entry 29. Unblocks
Stage 3c's renderer switch-on (label copy is still a separate step).
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
Decision-Log.md Entry 29.
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
