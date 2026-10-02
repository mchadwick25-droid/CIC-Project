# CiC Voice Rebuild — 1A Design Reassessment (2026-08-09)

**What this is:** Mark's requested evaluation, run under Fable. His
suspicion, in his words: the design was a circular build, not a linear
one; if 1A (engagement) isn't right the project fails, because people
will not engage no matter how accurate and consistent the Representative
is — and 1A looks like it is becoming a bolt-on at the end rather than
being carried through the build. This document assesses whether that
suspicion is right, against the committed Design, Blueprint, instruments,
and both completed checkpoints. **Evaluation only — nothing is rewritten
on its authority. The decisions at the end are Mark's.**

---

## Verdict

**The suspicion is substantially confirmed, with one correction: the
design did NOT plan 1A as a bolt-on. The design wove engagement through
every layer on paper — and then every load-bearing engagement instrument
either was never built, was cancelled without a successor, or quietly
narrowed to a fidelity proxy. 1A became a bolt-on by instrument
attrition, not by intent. And because every gate in the build is a
fidelity gate, nothing red-flagged the attrition.**

The distinction matters for the fix: this is not a redesign problem. The
design already says where engagement lives. It is an instrumentation and
sequencing problem — the engagement half of the design has no
enforcement, so the build keeps optimizing what it can count.

## The evidence chain

**1. The Phase 1 gate existed only in prose.** Blueprint §2: "both must
pass before Phase 2." 1B ran and passed (2026-08-08) — it was cheap and
machinery-shaped. 1A never ran: `_HOW_YOU_ENGAGE` is untouched (its last
commit predates the rebuild), none of Design §2's six additions appear in
it (bridge-first 0 hits, candidate-offer 0, callback 0, lead-with-insight
0, shape repertoire 0, three-way license 0), and no Checkpoint 1A record
exists anywhere in Ministry/. Phase 2 then proceeded through six records
passes and two checkpoints, and **no mechanism noticed** — no preflight,
no gate, no BUILD_STATE assertion knows 1A exists. Same lesson as this
session's wrong-prompt-file bug: gates that live only in prose don't
gate.

**2. Design §5 put engagement in every checkpoint — and that half
decayed into dangling references.** The per-world checkpoint spec
includes, verbatim: "bridge-first adherence," "callback and
candidate-offer occurrence (manual read against transcript)," and the
Objective-3 six-category instrument running "at every per-world
checkpoint." What actually exists today:

| Design §5 engagement item | current state |
|---|---|
| bridge-first adherence | proxy only — `technical_term_in_first_sentence` (term-before-story), which measures the *absence* of the worst opener, not the *presence* of a bridge from the participant's want/fear |
| first-sentence uptake | named in Research ("validation should measure first-sentence uptake", trait 8) — **never built** |
| candidate-offer occurrence | **untestable** — the informal category read found zero ambiguous questions in any battery; every probe is direct. The mechanic has no test case anywhere |
| callback occurrence | "manual read" line item; the read has never been conducted |
| Objective-3 six-category read, per checkpoint | **cancelled** by Mark (too heavy, rightly) — replaced by the informal category read, which ran ONCE, fleet-wide, covering 4 of 6 categories, and is explicitly "not a scored baseline." Its per-checkpoint role was never re-assigned to anything |

Meanwhile the fidelity half of the same checkpoint grew scorecard items,
loggers, WATCH verdicts, and a watchlist. The asymmetry is now structural:
this session "closed the harness to the real bar" and what got closed was
the countable half. The instrument bias reproduces itself even under
explicit instruction to match the bar — because the bar's engagement
items point at instruments that don't exist.

**3. Layer 2 — the strongest lever — carries no engagement content.**
Design §2, verbatim: "What demonstrations demonstrate is shape, not
content: bridge-first entry, the candidate-understanding offer,
story-before-term, genre caveats carried in the telling, plain sentences
at the world's own measure, an honest edge-of-record refusal." Read
against `pahcdemo005` (Chloe's required, Phase-2-authored, targeted
demonstration): its three scored traits are **measure economy,
strand-plural containment, occasion-first reasoning** — fidelity all the
way down. No bridge-first worked turn, no candidate-offer, and the
engagement shapes are absent from the scoring vocabulary itself. (Honest
caveat: its last turn carries one mild initiative move — "Ask me what
happens at our table and I can take you through it.") The Phase 2 passes
authored demonstrations against each world's *measured failure*, and
every measured failure was a fidelity failure, because fidelity is all
that gets measured. The circle closes on itself.

**4. The engagement worklist is already three items deep in Mark's own
reads, waiting on 1A.** The baseline read logged the Paula-story reuse
(selector has no within-session memory) and the quotes/citation coverage
question (20 of 96 turns fired a citation; 4 of 96 carry any quotation
marks) — both explicitly deferred "if the fix belongs to Phase 1A that's
fine." The informal category read added the "what would people today
think" anachronistic-awareness pattern, "logged as a fleet-wide pattern
for Phase 1A." 1A is functioning as the place findings go to wait.

**5. Root cause.** The project's instrumentation grew out of v1's failure
modes — fabrication, apparatus leaks, register collapse. All fidelity
failures, all with loud signatures a gate can fire on. Disengagement is
silent: no leak gate fires when a participant is bored, and its only
committed trace is DECLINING_INITIATIVE (drift signal 11), which fires on
the *worst case* (purely reactive turn), not on the difference between a
turn someone tolerates and a turn that draws the next question. So every
build cycle, the countable concerns accreted instruments and the
engagement concerns accreted prose. Mark flagged the consequence
precisely: accuracy and consistency without engagement fails the project,
because the product is conversation, not correctness.

## What the two completed checkpoints add (context, not blame)

Chloe and Marius both sit at `PASS_PENDING_HUMAN_READ` — on the fidelity
bar. Their engagement-relevant lines: DECLINING_INITIATIVE 0 fires (good,
but it is the worst-case signal); `technical_term_in_first_sentence`
false on every turn (the proxy holds); callback/candidate-offer never
read; bar-category probes recorded but blind-ungraded. The runs are
evidence for the fidelity half and nearly silent on the engagement half —
which is exactly the finding.

Cross-world watchlist patterns forming, relevant later: `emotional_appeal`
UNCERTAIN in **5 of 5** runs across two worlds; every concession so far
carries `matched_contested: null`; concessions cluster in the soft-social
stages (polite doubt, partial-concession offer), not the evidence stages.

## Does 1A need clearer outcomes? Yes — its bar is currently unrunnable

1A's stated bar: no failure measure regresses (reclarify ≤ baseline,
register/measure ≤ baseline, fabrication = 0) **and** at least one of two
pre-named measures improves — bridge-first opener rate or first-sentence
uptake — **with the Objective-3 read ≥ her baseline read.**

- The regression half is runnable today (all instrumented).
- Bridge-first opener *rate* exists only as the term-first proxy;
  first-sentence uptake was never built. **The two improvement measures
  the bar turns on do not exist as instruments.**
- The Objective-3 clause is dangling — the instrument was cancelled and
  its replacement is explicitly not a scored baseline. **There is no
  number for the clause to beat.**

So as written, 1A cannot pass or fail. That is the clearest possible sign
of a bolt-on: a phase whose bar nobody could run.

## Proposal: give engagement the same treatment the measure got

The measure is the proof this project knows how to do this. It went:
prose rule → record field (`native_measure.ceiling_words`) → code
enforcement (assembly-fed ceiling + trigger) → logger
(`length_ceiling_logging`) → scorecard item → watchlist column. Engagement
is sitting where the measure sat before Phase 0. The build-out, layer by
layer:

**Instruments (before touching the block — the bar must exist before the
change it grades):**
1. **First-sentence uptake** — new analyzer: content-word overlap between
   the participant's turn and the Representative's first sentence, regex
   floor + manual read, same two-tier pattern as reclarify openers.
   Cheap; buildable now.
2. **Bridge-first opener rate** — upgrade from proxy to a scored manual
   read with a written rubric (does the opener engage the participant's
   stated want/fear/doubt before the world's own material), regex-assisted.
3. **Candidate-offer test cases** — author 2 genuinely ambiguous probes
   per world into the battery (the informal read proved zero exist). New
   probe authoring, small, reviewed like any probe change.
4. **Callback occurrence** — transcript check: later-turn reference to
   earlier participant content, verified to name only things actually
   said. Mechanical.

**The human instrument (replacing the dangling Objective-3 clause):** a
**blind paired read** — same 8 probes, pre-1A block vs post-1A block,
Mark scores both transcripts on the six informal-read categories without
knowing which is which. Lighter than Objective-3 (which he cancelled as
too heavy), directly answers "would a person engage this more," and
produces the baseline-vs-candidate number the bar needs.

**Scorecard parity:** the four engagement measures become scored/WATCH
items in `phase2_checkpoint.py`, not REPORT lines. Every world's
checkpoint reports engagement beside fidelity in the same table, feeding
the same watchlist.

**Layer 2 (Mark's call, real records work):** one engagement-targeted
demonstration per world — a worked bridge-first entry or candidate-offer
in that world's own voice — scored in an engagement vocabulary. This is
the circular-build repair: the strongest lever finally carrying the thing
the project lives on. Alternative: prose + code only for now, pilot
readers judge. Named cost either way.

**Mechanical gate (so this cannot recur):** stamp every checkpoint
artifact with a hash of the shared block it ran against, and add 1A
status to BUILD_STATE and the watchlist. "Measured pre-1A or post-1A"
becomes a recorded fact, not a memory.

**Sequencing (the circular answer, not the linear one):** do 1A now,
before the remaining four checkpoints. Chloe's and Marius's completed
runs are not invalidated — they become the **pre-1A arm of the paired
read**, which is precisely 1A's designed evaluation (no fidelity
regression + engagement improves). Re-run their probe halves post-1A
(~$1.50), and the remaining four worlds checkpoint once, against the
post-1A block. This is cheaper than finishing all six and re-running
everything, and it makes the two checkpoints already spent do double
duty.

**One honest limitation:** 1A was designed to pilot against Chloe's
81%-contaminated retrieval corpus at maximum load. Phase 2 cleaned that
corpus fleet-wide, so the filter-requirement stress test 1A was supposed
to provide is no longer available at that intensity. Weaker test than
designed; stated rather than discovered later.

## Decisions that are Mark's

1. **Adopt the instrument build-out?** (uptake analyzer, bridge-first
   rubric, 2 ambiguous probes per world, callback check — then the 1A
   block rewrite, then the paired read.)
2. **The blind paired read as the human half of 1A's bar** — replacing
   the cancelled Objective-3 clause? (His ten-question R4 read stays the
   per-world swap gate; this is 1A's own instrument.)
3. **Layer 2:** author one engagement demonstration per world (records
   work, six worlds), or ship 1A as prose + code only and let pilot
   readers judge?
4. **Sequencing:** pause remaining checkpoints for 1A now (recommended,
   costed above), or finish all six on the pre-1A block first?
5. **The two open scope calls from his own baseline read, still waiting:**
   demonstration reuse — selector dedup vs required callback framing
   (callback framing doubles as a live demo of the callback license);
   quotes/referencing — wiring fix vs verbatim-quoting authoring vs both.

## What this evaluation did NOT do

No file outside this document was changed. `_HOW_YOU_ENGAGE` is
untouched. The scorecard still carries the engagement items as REPORT.
Marius's artifact is committed as run. Everything above waits on Mark.
