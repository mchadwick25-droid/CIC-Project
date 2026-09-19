# Rulings Pending — R1 through R19

One at a time, per `CLAUDE.md`'s own ground rules: real options, honest
tradeoffs, a recommendation — never a flat conclusion. Nothing in Stages
5–9 of `Build-Plan.md` proceeds until its ruling lands here. Update the
**Status** line when Mark rules; append the outcome to `Decision-Log.md`
in the same edit.

Full reviewable version: `https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`

---

### R1 — If the safety call itself fails, answer anyway or fail toward check-in?
**Status:** PENDING
(a) Keep today's fail-open toward the voice; build async reclassification
+ operator paging. (b) Fail toward the softer check-in question instead.
(c) One retry in the failure path, then (b). (d) (c), plus degraded-turn
counts surfaced in the weekly digest, paging deferred.
**Recommend (d)** — caution over resilience, and the added cost lands
only on turns that are already failing, never on the ordinary turn.

### R2 — Escalation priority, message decay, and the interim continuation text
**Status:** PENDING
(a) Keep "already fired always wins." (b) A rising level wins — a plan
disclosed after an earlier, milder disclosure gets the stronger message.
(c) (b), plus decay: the softer continuation only applies within the same
session and a bounded time window; after that, a fresh full message
either way. (d) Always the full message; retire the softer continuation
entirely. Also needs a plain yes/no: is the shipped interim continuation
text ("I'm still right here with you... Please reach out to someone
real...") the version that stands, or does it need Mark's own wording?
**Recommend (c)**, with the shipped text approved as final unless Mark
wants it reworded.

### R3 — Item 16's replacement: what, if anything, should the safety classifier be told about recent turns?
**Status:** PENDING
(a) Nothing new — leave it fully memoryless. (b) Conditional context, only
on the single turn right after a check-in fires: a fixed marker plus the
check-in text plus what got withheld; every other turn stays empty exactly
as today. (c) (b), plus the same after any crisis-track fire. (d) Handle
the reply deterministically in code instead of changing what the
classifier sees at all.
**Recommend (b)** — it only changes input shape on an already-rare
follow-up turn, never the ordinary one, so it clears Constraint A.
Requires its own small test battery before it ships either way.

### R4 — How often does the non-acute reminder repeat, and does the voice ever see it fired?
**Status:** PENDING
(a) Full text every time it fires in a session. (b) Full text once per
session; a short, separately-approved reminder after that. (c) Full text
once; later fires logged only, nothing shown. Separately: should the
Representative's own voice ever see, in its own turn history, that the
Facilitator spoke?
**Recommend (b)**, and **never** — in either conversation mode — for the
second question.

### R5 — A real "interrupt the round" affordance in Table mode
**Status:** PENDING
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

### R7 — Fixing the fleet's already-drifted `tellable_as` text
**Status:** PENDING
(a) A Sonnet thread does a capped-round pass per affected world. (b)
Fixed by hand. (c) Full regeneration.
**Recommend (a)** — matches how every other fleet-wide readability pass
this project has run has actually gone. Blocked on R6.

### R8 — CLAUDE.md names a confidence level ("Not Attested") the code doesn't have
**Status:** PENDING
(a) Add a sixth confidence enum value to match. (b) Amend CLAUDE.md down
to the code's real five. (c) Amend CLAUDE.md to say what's actually true:
"Not Attested" describes an absent claim (already modeled elsewhere as an
honest-limit or absent-detail record), not a confidence rating on a claim
that exists.
**Recommend (c)** — it's not really a sixth confidence level, it's a
different kind of thing, and (a)/(b) both paper over that.

### R9 — A distinct mark for contested or thin-evidence claims
**Status:** PENDING — sequencing gate, not a real decision yet
Comes back for a real ruling only after the Stage 1 measurement is in
front of Mark and R16/R17 are settled — the display design itself is
already agreed, this is purely a sequencing gate.
**Provisional** recommendation once unblocked: a quiet, non-alarming
variant of the existing mark — not a new color, not a new verb.

### R10 — Where a story's citation mark lands: first sentence or end of the telling
**Status:** PENDING
(a) End of the telling, as built today. (b) First sentence, uniformly.
(c) First sentence for a witness quote, end-of-run for a story. A
repeated re-citation gets the lighter "ibid" glyph under any of the
three.
**Recommend (c)** — but either (b) or (c) equally fixes the dropout bug;
the real fix is the completeness guarantee underneath, not which option
gets picked here.

### R11 — Split the dead retrieval-exclusion field into a real guard record type
**Status:** PENDING
(a) Split it, as designed: a redirect half and a separate honesty-guard
half. (b) Leave the field as-is, rely only on the existing exclusion-list
fix.
**Recommend (a)** — a one-line confirmation, not really a groan-zone
decision; D1 makes the honesty half load-bearing rather than cosmetic.

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
**Status:** PENDING
(a) Report-only, forever — never touch the text. (b) Report-only now;
revisit once the real fire rate is measured. (c) Withhold just the
flagged sentence (breaks the "gate decorates, never edits" rule the whole
system otherwise holds to). (d) Withhold the whole turn and substitute a
code-owned Facilitator message instead — the Representative's words are
never partially edited, only wholly declined.
**Recommend (b)**, with explicit intent to move to **(d)** once the
measured false-positive rate is near zero. **Never (c)** — mid-sentence
editing of generated text is exactly the class of thing this project's
own rules forbid.

### R15 — A distinct message when someone discloses risk about a third party, not themselves
**Status:** PENDING
(a) Reuse the same first message. (b) A distinct template, same redirect
underneath. (c) Route to the softer check-in instead.
**Recommend (b)** — the routing already exists; only the wording is open.

### R16 — Every record fleet-wide is still marked "draft" — what does that mean for confidence display?
**Status:** PENDING
(a) Define what "ready" actually means and run a per-world promotion pass
keyed to review rounds already on record. (b) Rule that `status` is pure
workflow bookkeeping and confidence display should draw only from the
separate confidence field, never from `status`. (c) Both — rule (b) now
so nothing is blocked indefinitely, and do (a) as each world comes up for
its next real touch.
**Recommend (c)** — confidence display for a given world only goes live
once that world has actually been through its promotion pass.

### R17 — A hard budget on how many new transparency elements can stack on one screen
**Status:** PENDING
Proposal on the table: at most a small, capped number of inline marks per
turn (scaling gently with sentence count), one collapsed references line
instead of a scattered list, at most one Facilitator interjection per
turn, no new mark types beyond the one contested-claim variant under
discussion, and the unverified-claims count never rendering to a
participant at all.
**Recommend approving the cap as a house rule**, enforced by an automated
test so no future change can silently stack past it — plus Mark's own
read-through as a seeker with no background before Stage 6 ever ships.

### R18 — The onboarding text overclaims what the honesty check actually does
**Status:** PENDING
Today's line tells a participant every claim is "checked against the
record it came from" — true only in the sense of word-overlap, not
truth-verification. (a) Reword now to describe what the mechanism
actually does. (b) Leave it and wait for the (currently blocked) display
affordance that would make the current wording accurate.
**Recommend (a)** — this is a participant-facing honesty gap in its own
right, independent of anything else in this redesign, and doesn't need
to wait on Stage 1's measurement to fix.

### R19 — Should every world's own voice carry the same "don't recommend outside help" guard clause?
**Status:** PENDING
Once the observation pass (Stage 0e) names which worlds are missing don's
own categorical clause: extend it fleet-wide as one packaged decision, or
word it per world individually.
**Recommend extending fleet-wide** once the observation names the gap —
this is exactly the kind of cross-world consistency question CLAUDE.md
already asks to be decided once, not world by world.
