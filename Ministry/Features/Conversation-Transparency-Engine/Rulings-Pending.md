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
**Status:** PENDING — this is general Table-mode UX (a participant leaving
a multi-Representative round mid-way), not a safety-mechanism question;
unaffected by the scope correction.
(a) A participant message sent mid-round simply closes that round
server-side and the new message proceeds — no new UI control needed.
(b) A dedicated, explicit Interrupt button. (c) Both.
**Recommend (a)** — reuses the existing message path rather than adding a
new one.

### R6 — Register-drift scope, and whether numbers ever gate a build
**Status:** PENDING
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
**Status:** PENDING
(a) A Sonnet thread does a capped-round pass per affected world. (b)
Fixed by hand. (c) Full regeneration.
**Recommend (a)** — matches how every other fleet-wide readability pass
this project has run has actually gone. Blocked on R6.

### R8 — CLAUDE.md names a confidence level ("Not Attested") the code doesn't have
**Status:** RULED 2026-09-21 — amend the rules to the code's five, and say
what "Not Attested" really is. `CLAUDE.md`'s stated confidence vocabulary
becomes the five the schema enforces (Documented / Widely Accepted /
Dominant Modern Reconstruction / Contested / Inferential-Thin), adding
Documented. One sentence records that "Not Attested" is the disposition
of a claim the sources do not make — already modeled as honest-limit and
absent-detail records — not a confidence rating on a claim that exists.
No schema change, no migration. The `CLAUDE.md` edit is a governance
change authorized by this ruling. See Decision-Log.md.
(a) Add a sixth confidence enum value to match. (b) Amend CLAUDE.md down
to the code's real five. (c) Amend CLAUDE.md to say what's actually true:
"Not Attested" describes an absent claim (already modeled elsewhere as an
honest-limit or absent-detail record), not a confidence rating on a claim
that exists.
**Recommend (c)** — it's not really a sixth confidence level, it's a
different kind of thing, and (a)/(b) both paper over that.

### R9 — A distinct mark for contested or thin-evidence claims
**Status:** RULED 2026-09-21 — a quiet variant of the existing mark, for
both Contested and Inferential-Thin. Same mark family, one subtle cue
(hollow/open form or light dashed underline — the renderer thread
proposes the exact form for Mark's pick), on any sentence citing a
record whose `formation_confidence` is Contested or Inferential-Thin.
Tap reveals the world's emic hedge and the plain confidence phrase at
Level 2. No new color, no new verb, no inline label. Counts inside the
R17 cap as a mark, not a new kind. Source of truth is the record's
confidence tag, never the runtime grounding check (Stage 1 measured
contested claims spoken as settled at 100% fooled). See Decision-Log.md.
Comes back for a real ruling only after the Stage 1 measurement is in
front of Mark and R16/R17 are settled — the display design itself is
already agreed, this is purely a sequencing gate.
**Provisional** recommendation once unblocked: a quiet, non-alarming
variant of the existing mark — not a new color, not a new verb.

### R10 — Where a story's citation mark lands: first sentence or end of the telling
**Status:** RULED (c) 2026-09-21 — first sentence for a witness quote, end
of the run for a story; a repeated re-citation gets the lighter "ibid"
glyph. The anchor renderer (Stage 3c, behind
`VITE_TRANSPARENCY_ANCHOR_RENDERER`) may switch on once its label copy
is worded by Mark — the build thread proposes the copy in its PR;
nothing participant-facing merges until Mark words it. See
Decision-Log.md.
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
**Status:** PENDING
Live full-text access to the vendored sources during a conversation (a
real architectural change), or live resolution of citations/evidence
only, as already built.
**Recommend live resolution only** — just fix the topology sentence that
currently overclaims this, no engineering change needed.

### R13 — Should the new "unused source" holdings check block a world from shipping?
**Status:** PENDING
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
**Status:** RULED 2026-09-21 — promote by admission now, and split the
fields. `ready` is defined mechanically: a record is `ready` when it sits
in an admitted world's currently pinned package and passes every m1
gate; `frozen` remains Mark's alone. A Haiku pass applies this across all
eleven admitted worlds. Confidence display reads only
`formation_confidence`, never `status`. Rationale: admission is already
a stronger gate than any per-record review; this restores the label's
integrity in a day and unblocks Stage 6 fleet-wide at once. See
Decision-Log.md.
(a) Define what "ready" actually means and run a per-world promotion pass
keyed to review rounds already on record. (b) Rule that `status` is pure
workflow bookkeeping and confidence display should draw only from the
separate confidence field, never from `status`. (c) Both — rule (b) now
so nothing is blocked indefinitely, and do (a) as each world comes up for
its next real touch.
**Recommend (c)** — confidence display for a given world only goes live
once that world has actually been through its promotion pass.

### R17 — A hard budget on how many new transparency elements can stack on one screen
**Status:** RULED 2026-09-21 — the cap is a house rule, enforced by test.
Inline marks per turn: one per two sentences, floor 3, ceiling 8 (set at
the busiest tenth of 195 logged turns; median turn untouched). Over the
cap, marks drop in a fixed order — glosses, then figures, then stories,
never witness quotes — and every dropped mark still appears in the
single collapsed references line. One references line, not a scattered
list. At most one Facilitator interjection per turn. No new mark kinds
beyond the quiet contested variant (R9). The unverified-claims count
never renders. Enforced by an M7 instrument counting Level-1 elements
per turn and a renderer fixture test asserting the cap. Mark's own
seeker read-through precedes Stage 6 shipping. See Decision-Log.md.
Proposal on the table: at most a small, capped number of inline marks per
turn (scaling gently with sentence count), one collapsed references line
instead of a scattered list, no new mark types beyond the one
contested-claim variant under discussion, and the unverified-claims count
never rendering to a participant at all.
**Recommend approving the cap as a house rule**, enforced by an automated
test so no future change can silently stack past it — plus Mark's own
read-through as a seeker with no background before Stage 6 ever ships.

### R18 — The onboarding text overclaims what the honesty check actually does
**Status:** RULED (a) 2026-09-21 — reword now to what the check does;
Mark worded the text himself. `SYSTEM_NATURE`
(`engine/m4/facilitator_turns.py`), middle sentence, becomes: "Before you
see an answer, each claim in it is checked to make sure its words come
from the record it names. The record itself was checked against the
sources when the world was built. Where the record is silent, the voice
is built to say so, not to fill the gap." The rest of the turn is
unchanged. `cic-website/about.html` "How It Works" sentence becomes: "We
check every quotation and claim in that record directly against those
sources, and label each for how well it's attested." Any other surface
making the runtime-truth claim (check `support.html` around line 125)
gets the same tightening; none gets a limitation disclaimer. Wording
ruled; the code/copy edit itself is separate follow-on work. See
Decision-Log.md.
Today's line tells a participant every claim is "checked against the
record it came from" — true only in the sense of word-overlap, not
truth-verification. (a) Reword now to describe what the mechanism
actually does. (b) Leave it and wait for the (currently blocked) display
affordance that would make the current wording accurate.
**Recommend (a)** — this is a participant-facing honesty gap in its own
right, independent of anything else in this workstream, and doesn't need
to wait on Stage 1's measurement to fix.

### R19 — Should every world's own voice carry the same "don't recommend outside help" guard clause?
**Status:** PENDING
Once the observation pass (Stage 0e) names which worlds are missing don's
own categorical clause: extend it fleet-wide as one packaged decision, or
word it per world individually. Note: this is a Representative-voice
authoring question (does the world's own voice defer to outside help
appropriately), not part of the closed Facilitator-mechanism scope above.
**Recommend extending fleet-wide** once the observation names the gap —
this is exactly the kind of cross-world consistency question CLAUDE.md
already asks to be decided once, not world by world.

**Stage 0e observation pass (2026-09-21), `engine.m1.cross_world`'s new
`observe_outside_help_guard` (report-only, keyword scan, not a semantic
judgment — see its own docstring): of the 11 built worlds, only **don**
and **rzg** carry don-style distress-comparison language
("measured against" / "weigh" / "not the same weight" / "weighing") in
`voice_craft.guard`. The other 9 do not: **alx, cappadocian, desert,
gallic, hal, ijc, pahc, syr, witt**. This is the concrete list R19's
ruling needs — still unruled; editing any `voice_craft.guard` field is a
Representative-voice change (`Build-Plan.md`'s own escalation category),
so no world's guard text is touched here.
