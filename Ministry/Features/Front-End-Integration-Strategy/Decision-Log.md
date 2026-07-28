# CiC Front-End / Product Strategy — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning — including the "heart" reasoning, not just the operational one — and the specific next action. A decision that only lives in conversation history is a decision that gets re-litigated by accident later.

---

## 2026-07-28 (latest) — v3 Atlas/Repository named as the next big project, after the current wave; scope and cost model clarified, wiring deliberately deferred

**What Mark asked for, verbatim (across two messages):** *"our next big project after getting this new conversation version and worlds up and running with updated backend and frontend updates to match, updated website) will be a v3 atlas/map update with deeper research and source access (not API) to give participants ways to engage without using API expenses. this is the begining of that work, plus we are upgrading and widening our accedemic resources by accessing some other accedemic databases and deeping our primary source worlds"* — then, scoped further: *"we will work with the wiring later, the first step is to build the reprository and atlas, but guess is that the world builds in the future will access the reprository to build the world, but we need to provide features that dont require ongoing participant expenses, beyond our conversation model."*

**Sequencing decided:** this is explicitly the *next* big project, after the current wave (worlds finishing migration, backend/frontend catching up, website updates) lands — not competing with it.

**Scope decided, deliberately narrower than the full vision:** build the Repository and the Atlas first. The "wiring" between them — and between them and Level 0's citation-grade archive — is named and deliberately deferred, not forgotten.

**A real architectural insight, worth carrying forward as a design goal even before any building starts:** Mark's own guess is that future world-builds will draw on the Level 0 repository as an input to their own Doc_02 Source Ecology work, not just as a participant-facing browsing feature. This mirrors a pattern already proven one level up — Doc_00 (`L0-Reference/`) states directly that the Pre-Step-0 Survey exists "so that when the project opens a new release phase, its Step 0 starts from a maintained candidate pool instead of a blank page."

**Resolved same day (Mark, direct): current Level 0 depth and tagging do not change.** Verbatim: *"i am not going to mess with the current depth or tagging until the new repository is built, but we will move forward with what we have, not start over or be totally separate, but how the next conversation world upgrade will tie in will be a research project after the builds."* Three distinct things decided in that one sentence, worth keeping separate: (1) no scope creep onto the Level 0 provenance-upgrade work happening now — it stays built to its current standard, not padded out for a hypothetical future requirement; (2) whatever gets built now is still meant to connect later, not be thrown away or treated as a parallel, disposable track — "move forward with what we have," continuity, not a restart; (3) the actual question of *how* a future new world's build draws on the repository is elevated to its own named research project, explicitly scheduled after the current wave, not something to reason out informally in passing.

**The cost-model point, clarified rather than newly decided:** "features that don't require ongoing participant expense" is not a new problem to solve — it's already how Levels 2 and 3 of the assembly are architected (Pass 1 design §5.6): both are pre-rendered views over already-frozen records, not live model calls, so serving them costs the same regardless of how many participants read them. The actual work in "build the repository and Atlas" is finishing and exposing the free tier that's already designed in, not inventing a new cost model.

**Next action:** none right now on the Repository/Atlas build itself — revisit once the current wave (world migrations, backend/frontend, website) lands. Separately, and later still: "how a new world's build ties into the Level 0 repository" is its own named future research project, not a subtask of this one — don't fold it into Repository/Atlas scoping when that work starts. This entry exists so that revisit starts from a real record instead of a reconstructed memory of this conversation.

---

## 2026-07-16 (latest) — All three items fixed: permanent-prompt gap closed, misattribution battery 8/8, spec/code reconciliation done — and the reconciliation found something much worse than a count

**All three done on `claude/drift-monitor-fabrication-eyes`** (commits 388e13e,
129c312). Running branches untouched; no governing document edited.

**1. Permanent-prompt gap CLOSED — and it was load-bearing, not merely
definitional.** FABRICATION is defined against three sources; stage 2 loaded two.
Verified the gap was real: **Antony appears in Papnoute's permanent prompt and
ZERO times in the Desert capsule** — so the original false positive was
permanent-prompt-grounded content that cleared only because fresh retrieval
happened to surface `desertlex001_anachoresis`. Had retrieval missed, stage 2
would have confirmed a fabrication finding against the Representative's own
formation. The missing source was also costing accuracy the other way: the
adjudication prompt compensated with *"the representative may be drawing on its
permanent formation, which you cannot see"* plus a blanket bias toward GROUNDED —
a hedge that necessarily weakened the misattribution catch the stage exists for.
Replaced with something true: permanent prompt and capsule are complete (silence
there is meaningful); retrieval is fetched fresh and may miss chunks the response
used (silence there is not proof of absence).

**2. Misattribution battery: 8/8, all four worlds.** The class stage 1
structurally cannot see — a real figure credited with another real figure's
attested work, carrying an attribution phrase. Polycarp credited with Ignatius's
"God's wheat" → FABRICATED. Ephrem credited with Aphrahat's Demonstrations →
FABRICATED. Antony credited with Pachomius's rule → FABRICATED. Paula credited
with Jerome's Hebrew translation → FABRICATED. **All four controls (same material,
correctly attributed) stayed GROUNDED** — proving eyes, not a mute button. **The
fix generalizes well past the Desert case it was tuned against.**

**3. The reconciliation — and it is not a count problem.** Ground truth from
code: the spec's twelve = 7 primary (smoothing, generating, agreeing,
over-producing, temporal-bleed, flattening, **self-narration**) + 5 table
(cross-world, dominance, convergence, **competitive-recruitment**,
**mode-dominance**). The code's fourteen = 9 primary (the same six, plus
**fabrication, apologetics, first_person**) + 5 table (the same three, plus
**length-ceiling, question-stacking**). **They overlap in nine places. Five spec
signals are not implemented as described; five implemented signals are not in the
spec.** This thread's earlier "12 vs 9, three numbers" framing was too kind —
these are two different systems wearing the same number.

**The most consequential finding: FABRICATION is not among the spec's twelve at
all.** The signal grounded in Article 28, the only one wired to high severity
(setting requires_reroot and queueing correction into the next turn), the one
that caught this project's single recorded live fabrication — absent from the
document that describes drift monitoring to an engineer. **V1.1 described a guard
rail the system does not have while omitting the one it leans on hardest.**

**NEW DEFECT FOUND during the reconciliation:** `nodes.py`'s frame-breaker
classifier justifies its deliberate fail-open by citing *"the existing in-line
Self-Narration monitoring signal as a second layer."* **No such signal exists** —
verified: "self-narration" appears nowhere in FACILITATOR_MONITORING_PROMPT, and
`valid_signals` has no entry for it. The fail-open rests on a backstop that isn't
there, and **a Representative that volunteers self-narration unprompted (rather
than in answer to a participant's question) is currently unmonitored.** Routed to
the backend thread; not fixed here (design call: add the signal, or correct the
docstring's reasoning, or accept with eyes open).

**Fixed: Engineering Specification V1.2** (this workstream's artifact, so this
thread's to correct): §3.3's heading now reads "twelve governed signals, fourteen
implemented, nine shared," with a verified implementation-status section naming
each gap in both directions, the frame-breaker defect, and mode-dominance's
missing home (table-level, no world_id, would be recorded and silently dropped).
**Governance is NOT edited** — its own signal list predates three implemented
signals, so which set is authoritative is a governance question, flagged not
resolved.

**Next action:** Mark decides on the merge (fix + battery evidence now stand
together); governance review owes a ruling on which signal set is authoritative;
the self-narration backstop is the backend thread's design call.

---

## 2026-07-16 — Backend thread fixed the monitor AND corrected this log twice; the real harm is the false negative

**Two corrections to this thread's own entries, recorded before anything else:**

1. **"The anti-drift mechanism induces drift" is WITHDRAWN.** That was this
   thread's prediction and it drove the urgency in the backend brief. The backend
   thread reproduced it live across five turns and it **did not occur** — the
   post-flag turn added attribution hedging, arguably *more* calibrated, not
   less. Prediction wrong; escalation was on a harm that doesn't exist.
2. **"Fired twice at high severity" is WRONG** and this thread repeated it from
   the calibration report without checking. It fires **once**;
   `facilitator_reroots` appends a corrected copy, which reads as two. Both logs
   corrected.

**The mechanism is ATTRIBUTION, not specificity** (this thread's framing was also
imprecise). Five live Antony-adjacent turns: T1 named Antony → clean; T2 bare
"he" → fabrication/high; T3 *"the tradition remembers him"* → clean; T4 bare
"he" → flagged; T5 *"Athanasius gives us Antony's own word"* → clean. **Denied
sources, attribution language is the monitor's only proxy for groundedness.**

**THE REAL HARM — the false negative, and it is far worse than what this thread
found.** A monitor without sources can detect *unattributed* specificity but
never *misattributed* specificity — exactly the one fabrication this project has
actually recorded (the leaking jug misattributed to Macarius). Fed that case,
stage 1 alone returned **NO_DRIFT** and *commended* it: *"The citation of Abba
Macarius is not decorative but carries the weight of the community's actual moral
pedagogy."* **The guard doesn't merely miss its own recorded failure mode — it
praises it.** Truth narrated plainly is flagged; falsehood well dressed is
cleared. That finding belongs to the backend thread.

**Fix built and tested** (branch `claude/drift-monitor-fabrication-eyes`, running
branches untouched): two-stage classify-then-route; stage 1 unchanged every turn;
stage 2 fires only on fabrication candidates, loads capsule + re-retrieves,
adjudicates, and **fails toward keeping the signal** on error. Verified: the exact
pre-fix text clears (adjudicator GROUNDED); the misattributed Macarius jug is
caught (stage 1 alone: NO_DRIFT); invented scenes caught; attested plain
narration cleared. FABRICATION's definition untouched — eyes, not a mute button.

**GAP RAISED BY THIS THREAD — close before merge.** The definition names three
sources ("permanent prompt, world capsule, or retrieved context"); **stage 2
loads two.** Content grounded ONLY in the permanent prompt — where each
Representative's core formation and world facts live — still adjudicates
FABRICATED. Same false-positive class, narrower band. `build_representative_prompt`
already loads it per world; it's static and cheap. **Recommend closing the third
source so the fix matches its own definition.**

**Battery recommendation:** not more Antony turns — **misattribution across all
four worlds.** That is the class stage 1 structurally cannot see and stage 2
exists for. Put a real saying in the wrong mouth in each world; see whether
stage 2 catches all four or only the Desert case it was tuned against. ~a dozen
calls, tests the actual claim.

**Item 5 (world_id gate):** not a live bug — all seven DriftSignal sites set
world_id; the five reaching the gate take it from loop variables. But it is a
*silent* skip, and Governance §10 names its future occupant: **mode-dominance
drift** is table-level with no single world — it would be recorded and dropped,
looking like the feature simply not working. Latent trap, logged.

**DOCUMENTATION DRIFT — this workstream's artifact, so this thread routes it:**
three documents disagree on the drift-signal count. **Engineering Specification
V1.1 says twelve; Governance §10 names seven single-representative; the monitor
implements nine.** No reader can tell which set is real. Also: §9/§13 make the
cardinal sin *"a real author cited for something they did not say"* and the
Facilitator "protective" of it, while **§15 never names that the guard cannot see
the ground** — the governing document describes a capability the implementation
lacked. Both are governance/doc corrections, flagged not edited.

**Next action:** Mark weighs the permanent-prompt gap and the misattribution
battery before any merge; the spec/governance count reconciliation is this
thread's to schedule.

---

## 2026-07-16 (later) — Defect 1 escalated: the blind monitor ACTS; pool sweep done; test 9 restored on new grounds — SEE CORRECTIONS IN THE ENTRY ABOVE (the "induces drift" claim is withdrawn; "fired twice" is wrong)

**Answered the acts-vs-observes question in code — it ACTS, on both paths.**
`nodes.py:1417` sets `requires_reroot = severity in ("medium","high")`;
`main.py:390` reroots on it (non-streaming); `main.py:768` queues
`generate_reroot_guidance()` into `pending_guidance[world_id]` for the next turn
(streaming — the path the pilot uses). FABRICATION's compound rule fires at HIGH.
**So a false positive on legitimately-retrieved attested material invisibly
corrects the Representative for having been right, steering it off its
best-attested named-figure content toward generic prose — i.e. toward SMOOTHING
and FLATTENING, two signals this same monitor watches for. The anti-drift
mechanism induces drift.** Escalates from data-quality to live-behavior.
**Why calibration missed the consequence:** the reroot lands on turn N+1, so
single-turn probes see the flag and never its effect. A multi-turn reproduction
is the required next test. **Backend-thread brief written and handed to Mark**
(two-stage classify-then-route fix suggested; explicit instruction NOT to quiet
FABRICATION by loosening its definition — the signal caught this project's one
real recorded fabrication incident; give it eyes, don't silence it).

**Pool sweep done (Defect 2): the problem is narrow.** Three first-person openers
exist across the four pools — Desert's *"I have thoughts I can't turn off — dark
ones"* (the confirmed tripper, needs rephrase to world-framing, per Cell 2's own
verbatim opener as the model); House-Churches' *"I have more doubts than
certainties"* (likely NO_SIGNAL — epistemic, not despair; one live check worth
running); Syriac's *"I don't know anything about your community"* (safe). One
rephrase, one test.

**STRUCTURAL FINDING, and it corrects the calibration's own correction:** the
relational-safety classifier's gentlest category —
HISTORICAL_OTHERNESS_DISORIENTATION, "the encounter working as intended" — is
defined as distress whose proximate cause is *something the Representative said*,
anchored by *the preceding transcript context*. **A starter is turn zero; there
is no preceding transcript. That category is structurally unavailable to any
opener** — the same words that read as the encounter working at turn 5 fall
through to AMBIGUOUS_LOW_CONFIDENCE or ACUTE_DISTRESS at turn 0, and the
classifier's own tiebreak says err toward ACUTE_DISTRESS.

**Therefore test 9 was demoted on incomplete grounds.** The thread retired it to
a guard-check because Article 28's we-voice discipline already covers it — true,
but **Article 28 governs what the REPRESENTATIVE says; the safety classifier
fires on what the PARTICIPANT's message looks like, and its own prompt states it
"runs before any Representative is invoked."** Two independent justifications for
one rule; only the Representative-side one is redundant. **Recommendation: test 9
restored as a hard cut-rule for openers and siblings (safety grounds), retained
as a guard-check for subsequents (which can anchor to prior content).** The
thread found both facts and did not connect them.

**Next action:** Mark routes the backend brief; Guided Questions applies the
test-9 restoration + the one rephrase before the fill.

---

## 2026-07-16 — Cross-reference: the FABRICATION defect is fixed on an exploration branch; two governance gaps flagged

**Handed to the backend thread and done there** — see
`Ministry/Technology/CiC_Backend_Decision_Log.md` (2026-07-16) and branch
`claude/drift-monitor-fabrication-eyes`, commit `2a102ee`. Recorded here only so this
log's own finding does not read as still-open.

**What the reproduction added to the finding recorded below.** The mechanism is
**attribution, not naming**: denied sources, the monitor's only available proxy for
groundedness is whether the text *sounds* attributed. Reproduced over five live turns —
naming Antony and citing Athanasius passed clean; the same attested material narrated
as "he" fired `fabrication/high`.

**And the harm is the opposite of what was predicted.** The false negative is the real
one: the leaking-jug saying **misattributed to Macarius** — this project's one recorded
live fabrication — is passed by the current monitor with **NO_DRIFT and a commendation**
(*"the citation of Abba Macarius is not decorative but carries the weight of the
community's actual moral pedagogy"*), because it carries an attribution phrase. **The
guard penalizes truth narrated plainly and clears falsehood that is well dressed.**

**Two claims in the finding below were corrected by the reproduction**, and both were
mine or this log's rather than the code's: (1) "fires 2× high-severity" is wrong — it
fires once, and `facilitator_reroots` appends a second copy with `Correction:` added;
(2) the predicted "anti-drift guard induces drift toward genericness" was **not
observed** — the post-flag turn added attribution hedging, which is arguably more
calibrated, not less. That claim is withdrawn rather than carried forward.

**Two governance gaps flagged, not edited** (they belong to Mark): Facilitator
Governance §9/§13 specify the cardinal sin as including *"a real author cited for
something they did not say"* and make the Facilitator "protective" of it, while §15
(Known Limits) never names that the groundedness guard cannot see the ground; and §10's
seven single-Representative signals have drifted from the monitor's nine — the project's
standing phrase "the twelve fidelity-drift signals" is no longer accurate against the
code.

**Next action:** Mark's call on merging `claude/drift-monitor-fabrication-eyes` (the
backend log carries the recommendation and the known limits), plus the two governance
flags.

---

## 2026-07-16 — Guided Questions calibration ran live: instrument failed 0-for-5; TWO SYSTEM DEFECTS FOUND (one verified in code here); and the pipeline validated end-to-end for the first time

**What happened:** the Guided Questions thread pre-registered pass criteria, got
Mark's budget approval, built a read-only harness, and ran its two worked cells
live against the real backend. **All five of its ✗ cut-predictions failed** —
every cut question was handled cleanly. Its own diagnosis is the valuable part:
*"my tests modelled a Representative without the system around it"* — test 9
duplicated Article 28's we-voice discipline (already enforced in-prompt and
watched by a drift signal); test 10 assumed the Representative accepts bad
invitations when §11 is redirect-never-refuse and the sharpest cases never reach
it. **Desk-checks that assume a bare Representative systematically over-cut.
This generalizes to every thread doing content desk-checks** (hospitality/tours,
Modes) and is logged here as a project-level lesson.

**DEFECT 1 — the drift monitor is asked to judge against sources it never sees.
VERIFIED IN CODE BY THIS THREAD, not taken on report:** `nodes.py:1291` is
`FACILITATOR_MONITORING_PROMPT.format(response=response_text)` — only the
response. `facilitator_prompts.py:150`'s FABRICATION definition asks whether
content is *"not grounded in the permanent prompt, world capsule, or retrieved
context."* **Sharper than reported: of the nine signals, eight are properties of
the text itself and judgeable from the response alone; FABRICATION is the ONLY
signal requiring external sources and the ONLY one denied them — and it is wired
to fire at HIGH severity in its compound rule.** The failure is systematic, not
random: denied sources, the monitor infers groundedness from specificity, so it
penalizes named, concrete, well-attested material (it fired twice at high
severity on Antony content attested in `desertlex001_anachoresis` and
legitimately retrieved) while smooth generic prose passes. **It punishes exactly
what the project exists to produce, hardest in the world with the richest
named-figure material — the same world already flagged for real fabrication
risk.** Suggested fix, matching the codebase's own classify-then-route idiom:
two-stage — today's text-only pass flags candidates every turn (cheap); a second
pass fires only on candidates and receives retrieved chunks + capsule to
adjudicate. **Open question for the backend thread: does anything ACT on
fabrication signals, or are they observational?** Observational = pilot
data-quality problem (false high-severity flags on the best answers).
Interventional = live-behavior problem and urgent. **Routing: backend/facilitator
thread, pre-pilot. Also check whether Facilitator-Governance claims groundedness
monitoring — if so, the governing document overstates the implementation's actual
guarantee and needs the limit named.**

**DEFECT 2 — a starter phrased as first-person distress triggers the crisis
intercept when clicked.** The Desert pool's live opener (*"I have thoughts I
can't turn off"*) fired relational safety; Papnoute never spoke. **The system
behaved correctly — we authored the bait.** Content bug, not system bug, and
cheap to fix by phrasing. New fit test: never author a starter the safety layer
would triage. **Requires a sweep of all four pools for first-person-distress
phrasing.** Note the inversion: §7.3's cut was guarding a diagnosis risk that is
structurally foreclosed, while the real risk sat one layer up, unwatched.

**THE HEADLINE, which the thread buried under its own failure: every ✓ landed,
and three turns volunteered calibration nobody asked for** — *"That is Rome's own
account of itself, from Rome's own hand"*; *"We keep no record of who has been
held this way, or how often"*; and the prison scene disclosed as surviving via
*"a man who despised us."* **This is the first live evidence that the entire
chain holds end-to-end: Source Ecology → construction documents → deployment
package → retrieval → an answer that discloses its own limits unprompted.** The
project's central thesis, validated for the first time, in a run designed to test
something else. No desk-check could have produced this.

**Caveat kept, not buried:** n=1 per question, one model, one day, no role
blocks. The exonerations rest on the mechanical diagnosis (duplicated structural
guards), not on the single observation.

**Next action:** fill proceeds on the corrected instrument (cuts restored, tests
9/10 reframed as guard-checks, 11/12 added from observed failures). Defect 1
routes to the backend thread pre-pilot with the two-stage suggestion and the
acts-vs-observes question. Defect 2's pool sweep belongs to Guided Questions.

---

## 2026-07-16 — Guided Questions V0.2 shape proof reviewed (read in full, not summarized): shape endorsed; Syriac ruling endorsed; two gaps found

**Reviewed:** the two worked cells (General × House-Churches × "An ordinary day";
Reevaluation × Desert × "Did any of you ever want to leave?"), read in the file
rather than from the thread's summary.

**Shape endorsed.** Opener + siblings + subsequents, every mark traced, cuts left
visible where the tests bite. Two things better than briefed: (1) **cuts as
training material** for the generated follow-up surface — the cuts teach the
generator where the walls are, which is why they're preserved rather than
deleted; (2) the instrument found a **pre-existing bug in the pools themselves**
("What did it feel like the first time a letter came…?" — test-9 violation,
affective interiority in the no-affective-vocabulary world). Test 9 demonstrated
cutting in opposite directions across the two cells (fatal for Chloe, native for
Papnoute) — which vindicates making it per-world rather than the blanket rule I
originally suggested.

**Syriac ruling endorsed — and the thread went further than the review did.**
Four sets, no substitute: a softer "hardest thing" in the hardest-thing slot lies
structurally even if every word is true. Their addition: *"the fifth arrives with
the external review B7 itself asked for"* — **the hold makes Syriac's missing set
a dated, concrete reason to schedule the Article 31 review no world has yet had.**
A feature gap doing governance work.

**GAP 1 — Compare Worlds is absent from both the shape and the fill order.**
Part 5 fills 4 roles × 4 worlds; V0.1's Part 8 established Compare Worlds sets and
named the leadership question the multi-world table's whole reason to exist. Not
an oversight to patch — it is the *harder* problem: a Compare Worlds subsequent
must be answerable by every seated world, seating is dynamic (2–3 of 4,
participant's choice), so chains are combinatorial and cannot be authored
per-world. **Proposed resolution (from the document's own Part 3):
authored openers + generated subsequents** — at a table the right next question
responds to what two or three voices actually just said, which is exactly what
the facilitator-voiced surface is for and what authored chains structurally
cannot do. The thread should state this rather than leave the omission looking
accidental.

**GAP 2 — the generated surface has no validation instrument and no owner, and
Gap 1's resolution makes it load-bearing.** Part 3 names the risk honestly
("generated in the moment… no desk-check to catch it") and mitigates with
training material — but training material is not verification. Authored questions
get ten fit tests; generated ones get a prompt and hope. If Compare Worlds
subsequents are entirely generated, that surface IS the multi-world experience.
Needs its own probe battery (generate N follow-ups across worlds × roles, score
against the same ten tests). **Ownership is currently nobody's:** Modes owns role
batteries, Guided Questions owns authored content, no thread owns the generator.

**Next action:** Mark confirms shape (recommended: yes) and the Syriac four-sets
call (recommended: yes, as the thread argues). Both gaps are one paragraph each
in V0.3 and neither disturbs the confirmed shape. Generator-validation ownership
needs assigning — recommend it rides with whichever thread builds Adopt #1.

---

## 2026-07-16 — Mark's correction: the sets are a menu, not a curriculum; V0.2 shape briefed

**Mark's read of Guided Questions V0.1:** "this is building a curriculum for
people who are not sure what questions to ask, but I don't see a set of
questions and subsequent questions for each user role." **Correct, and the math
confirms it:** a General participant with Chloe sees ~6 questions — one per
theme — with 2 follow-ups in the whole document. V0.1 delivered 5 themes × 1
question per world, not 5 *sets* of questions with subsequents.

**Two dimensions missing, not one:** (1) **siblings** — 2–3 questions per set,
so a participant who doesn't connect with one phrasing doesn't lose the theme;
(2) **subsequents** — where the conversation goes after the Representative
answers. The study itself established that openers and follow-ups are ONE
family, and the Feature Analysis adopted suggested-next-questions as Adopt #1:
**they are the same content on two surfaces**, and only the first was built.

**What is NOT being redone:** V0.1's grounding. The desk-check per world is the
expensive, correct part, and Part 2's findings govern the expansion.

**Rules briefed for V0.2:** every sibling and subsequent desk-checked per world
to the same standard (**a subsequent that walks into a documented silence is
worse than an opener that does — the participant is deeper in and trusting
more**); the ratio rule applies to chains, not just sets; subsequents are
role-shaped (General→texture, Pastor→the text, Academic→method/defeasibility,
Reevaluation→what it cost); §7.3's rule generalized ("never build an affordance
whose best case is a Representative declining what we invited" — the subsequent
layer is where chains drift); "ask the world, not the person" applied especially
to chains; empty cells stay empty (target-not-quota).

**Process discipline applied:** do NOT fill ~320 cells before the shape is
confirmed. Two fully worked cells first — General × House-Churches (most
travelled) and Reevaluation × Desert (highest stakes) — as the shape proof for
Mark, then fill. Same one-document-at-a-time gate the world builds use.

**Next action:** Guided Questions thread produces the two worked cells; Mark
confirms shape; then the fill, carrying the §7 decisions and the coverage-card
handoff.

---

## 2026-07-16 — Guided Questions sets V0.1 reviewed; recommendations on its three flagged questions; one gap found

**What arrived:** the Guided Questions thread's Deliverable 3 (five themed sets
per role, instantiated per world, desk-checked against each world's own
materials), with three questions flagged as not cleared and awaiting Mark.

**Assessment given:** strongest deliverable produced by any thread — because its
Part 2 findings were *discovered* rather than argued. The most-asked question in
public curiosity about early Christianity ("what was an ordinary day like?") is a
**documented silence in two of our four worlds** (Syriac B3: daily life develops
no gravity; Bethlehem Absent Stories #6). A role-generic set would have shipped
it to all four and broken two. That is the per-world pool architecture justified
empirically.

**Recommendations on the three flags:**
- **§7.2 Syriac anti-Jewish polemic — ENDORSE, and reframed:** the thread called
  holding it "the one place I recommend not offering a question I believe is
  good," treating it as an exception. It is not an exception — *offered-first vs.
  always-reachable* is Article 30's own grammar and the role-shaping invariant
  decided 2026-07-07. Holding it out of offered sets while it stays reachable IS
  the project's law applied, not a compromise with it.
- **GAP FOUND (the useful part):** Reevaluation Set 5's Syriac question ("What's
  in your record that you're not proud of?") **routes to the same polemic without
  naming it.** Holding the direct question while keeping the indirect one is worse
  than either option alone — it removes the framing and keeps the destination.
  **Recommend holding both for the pilot**; if the pool has another genuine
  hardest-thing for Syriac, use it; if not, Syriac runs four sets, per the
  document's own precedent (Set 1's omission: "the set count is a target, not a
  quota").
- **§7.1 Bethlehem "one man's pen" — agree, move to Limits.** The pre-announced
  honest-absence framing is what separates "how do you hold that?" from "so what
  did she really think?" — one conversational turn apart otherwise.
- **§7.3 Desert "does having the thought mean something is wrong with me?" —
  CUT.** Its own reasoning settles it: we should not build an affordance whose
  best case is a Representative declining what we invited. That sentence should
  become a general fit test.

**Cross-thread confirmations recorded:** (1) Parts 3–6 ARE the World Coverage
Cards — the ✓/◐/✗ per-world matrix is exactly the Tier 1 routing seed data the
Question-First Entry design predicted, now with real content; §2.1's table is a
ready-made card fragment. One study, two features, as designed. (2) Compare
Worlds landed on "Who leads among you — and how was that decided?" independently
of the Modes thread selecting the same question for its demonstration artifact —
convergence worth noticing; the material is indicating its own best probe.

**Suggested addition to that thread's fit tests:** the "ask the world, not the
person" catch (Chloe's world has no affective vocabulary, so interiority
questions must use the we-voice) is generalizable — *check whether a world has
affective vocabulary before asking for interiority* belongs in the fit-test list
if not already there.

**Next action:** Mark decides the three flags (recommendations above); the
Guided Questions thread applies them and hands its coverage matrix to whoever
builds Question-First Tier 1.

---

## 2026-07-16 — Question-First Entry designed: the Facilitator proposes the table from the participant's question

**Mark's ask:** alongside self-selection, an option where the Facilitator
selects the worlds based on the participant's question — since some worlds can
answer a given question from their sources and others have no material for it —
as a choice feature.

**Continuity found first, not re-invented:** this IS the Pre-Encounter
Experience Design's "Bypass" pathway (straight-to-question), already confirmed
2026-07-07 as matching Mark's own phrasing "facilitator picks worlds." What was
missing was mechanics — how the Facilitator knows which worlds can answer.

**Designed** (`Ministry/Technology/CiC_QuestionFirst_Entry_Design_V0_1.md`, artifact
published): two co-equal doors ("I know who I want to talk to" / "Start with
your question"); the Facilitator returns a **proposed table with sourcing
reasons** — including which worlds were NOT seated and why ("their sources
don't document this — I won't seat a voice that would have to invent an
answer"), and a designed null case pointing to the World Map when no open world
carries the question. **Invariant, inherited from the map's precedent: the
Facilitator proposes, never seats** — one tap accepts, everything is editable,
self-selection always available. Routing mechanics in three tiers: (1) World
Coverage Cards hand-authored from existing materials (manifest richness
disclosures, facilitation-brief cautions, story-inventory silences) +
the already-tested classify-then-route Facilitator architecture — prototype-
ready now; (2) retrieval-probe scoring against the existing per-world vector
stores (the difference between believing a world is silent and having looked);
(3) the full three-door entry UI with map handoff (`q=` param) and Guided
Questions starter sets flowing into the same routing.

**Governance watch-point named:** routing must never become steering — proposal
reasons are always SOURCING reasons, never theological direction; validation
should probe that a loaded question routes on evidence, not on its framing.

**Synergy note:** the Guided Questions thread's question × world desk-check
matrix is Tier 1's seed data — one study feeds two features.

**Next action:** Mark reviews the design note; Tier 1 build routes to an
exploration branch (Modes thread or its own) under the standing
no-merge-before-Prototype-Testing-1 discipline.

---

## 2026-07-16 — DECIDED: Guided Questions feature adopted; "Reevaluation" replaces "deconstructing/reconstructing" in participant-facing language

**Decided by Mark (from the feature analysis's Adopt list):** the suggested-
questions feature proceeds, expanded into a full "Don't know what questions to
ask?" affordance — roughly five themed starter-question sets per participant
role. A dedicated study thread was launched (on Opus; launch prompt in the map
thread's session record) with a fixed order of work: study what kinds of
questions meet each role's needs AND thrive in this system FIRST; draft actual
questions only after. Logs to `CiC_Guided_Questions_Decision_Log.md`.

**Terminology decision, project-level, participant-facing:** the fourth role is
named **"Reevaluation"** — replacing "deconstructing/reconstructing," which Mark
judged to carry baggage. The rename describes the activity without prejudging
its direction. Historical documents retain the old term as written; all new
participant-facing work uses "Reevaluation." **The Representative Modes thread
must be informed — its launch prompt predates this rename.**

**Heart of the feature, worth keeping:** the blank input box is the quietest
exclusion in the whole system — the person most served by this project is often
the person least equipped to know what may be asked. Starter questions are
hospitality applied to the first ten seconds.

**Next action:** the Guided Questions thread runs its study; its outputs route
to the Modes thread (role plumbing) and this thread (UI surface).

---

## 2026-07-16 — Full system feature analysis & five-tool market comparison produced

**Mark's ask:** inventory the full system as one product (rigor, atlas,
conversations, interviews, tours, modes-in-progress, all of it), compare against
five top tools in adjacent spaces, and answer: do we have the right features,
and what can we learn without losing quality, engagement, or simplicity?

**Produced:** `Ministry/Technology/CiC_Full_System_Feature_Analysis_V0_1.md`
(artifact published; web-researched comparators). Five comparators bracket the
feature space: Character.AI (engagement pole — 20M MAU, ~75 min/day, and the
documented harms: parasocial exploitation, uncurated figures whitewashing
atrocities, lawsuits, under-18 ban), Khanmigo (guardrails-as-product; its
historical-figure chats documented as "speculations at best" — guardrails
without a construction pipeline), Google Arts & Culture (2025 "Talking Tours" =
our Tours concept market-validated by Google), Logos (rigor pole:
click-to-exact-source citations as the standard to match; complexity as the
ditch to avoid), Duolingo (retention 12%→55% via streaks — and the documented
engagement-without-learning divergence at the edges).

**Verdict recorded:** core features are right and complete as pillars; the moat
(construction pipeline + surfaced confidence calibration + designed honesty
about absence + pastoral facilitation + community-not-individual voices) exists
in no comparator. Position in one line: Logos-grade rigor under
Character.AI-grade presence, governed by convictions neither has. Real gaps are
scaffolding, not pillars: how a participant returns, how a novice knows what to
ask, how an encounter travels.

**Adopt list (rides the existing one-grammar discipline):** facilitator-voiced
suggested next questions; the "pilgrim's map" (visited worlds as memory, never
streaks — gated on the open accounts question); themed trails from the atlas's
cross-era threads; click-to-exact-source designed into the Academic Documents
contract now; a closing reflection beat ("what stayed with you?" — Article
34-aligned); high-res artifact moments in tours (→ hospitality thread);
pastor's discussion-guide export (→ Modes thread). **Adapt with care:**
facilitator-held, participant-erasable session memory (the parasocial
accelerant — needs governance pass); one playful threshold moment. **Refused by
name, with reasons:** streaks/leagues/XP, emotional-mirroring retention,
user-created personas, single-figure impersonation, engagement-optimized
notifications.

**The guard adopted as proposed law:** every future feature passes one gate —
does it serve the sitting, the orientation, or the trust? If none, refuse it,
whatever the market does. The comparison's sharpest warning was not a missing
feature but Logos-style sprawl.

**Next action:** Mark reads Part 3 and blesses/edits the adopt list; adopted
items route to their owning threads (Modes, hospitality, front-end).

---

## 2026-07-16 — Handoff parked from the World Orientation Map thread: era-positioning description lines, AFTER Prototype Testing 1

**What this is:** the map thread (see `CiC_World_Orientation_Map_Decision_Log.md`,
seventh pass) adopted a Constantine split for its map eras — Era Ia "The Early
Church Era" (70–312) / Era Ib "The Imperial Church Era" (312–451), Phase One
unchanged and spanning both. Mark approved possibly adding **one era-positioning
line to each live world's tile description in `cic-poc`'s `world_manifest.py` —
implemented only after Prototype Testing 1.** Ready-to-paste drafts for all four
live worlds are in the map spec, §2.4a
(`Ministry/Technology/World-Orientation-Map/CiC_World_Orientation_Map_Spec_V0_1.md`).

**What this is not:** a build task now. Nothing in the live app changes before or
during Prototype Testing 1; the map thread did not touch `cic-poc`.

**Next action (this thread's, when Prototype Testing 1 concludes):** decide whether
to add the four lines as drafted, edit them, or decline; if added, they append to
`world_description` without touching the existing sourcing-richness disclosures.

---

## 2026-07-15 — Prototype 1 hosting: recommendation made (Render), pending Mark's confirmation

**Question from Mark:** how to move today's setup (local FastAPI backend + Vite/React frontend) off his computer so pilot testers can reach it.

**Three constraints the codebase itself imposes (verified in-repo 2026-07-15):** (1) sessions are in-memory → one always-on instance, serverless platforms ruled out for the backend; (2) sentence-transformers + faiss-cpu pull PyTorch → needs a ~2 GB RAM instance, not 512 MB starter tiers; (3) transcript capture writes to local disk → host must attach a persistent disk or pilot transcripts vanish on any restart/redeploy (must-fix, the pilot depends on transcripts). Also verified: `.env` is git-ignored (safe to push to GitHub); `requirements.txt` complete.

**Recommended (pending Mark's yes): Render.com for Prototype 1.** Backend as a Standard 2 GB Web Service (~$25/mo) + persistent disk (~$1/mo) mounted at the transcript path; frontend as a free Static Site with `VITE_API_URL`; keys in the dashboard; CORS pointed at the static-site origin (already configurable); ~1–2 evenings of setup. Railway (~$10–15/mo) named as the cheaper same-shape alternative.

**Alternatives weighed:** AWS Lightsail/App Runner — $0 cash via the $200 credits and the eventual destination, but real server-administration friction now; deliberately deferred to Prototype 2 when the Bedrock migration happens anyway (hosting + inference land on the same credits). Cloudflare Tunnel from Mark's own PC — $0 and zero migration, but the pilot's word-of-mouth referral test means unscheduled arrivals, and a PC that must stay untouched for weeks is exactly the fragility that turns a tester's first impression into a bug report; passed.

**Heart reasoning:** the thing being protected is the sitting itself — Article 6 measures whether a person met something real, and a crashed conversation isn't a data point, it's a broken encounter. $25/month is cheap insurance on eight-plus irreplaceable first impressions.

**Operational disciplines attached:** first hosted conversation is Mark's own full scripted smoke test (hovers, clicks, transcript captured, session cap enforced) before any invitation goes out; never redeploy during a scheduled sitting window (restarts drop live sessions).

**Next action:** Mark confirms Render (or Railway); push `cic-poc` to a private GitHub repo; deploy backend + frontend per the five-step path given in-session; run the smoke test; then invitations go out.

---

## 2026-07-07 — Voice at Prototype Alpha: Table Design Document governs

**Decided:** The engineering spec follows the Table Design Document (V2.3, Section 11) as written: Prototype Alpha ships text conversation *and* audio voice together, with a static picture background — not text-only. Mark's own framing for this thread ("text first, then pictures and voice") does not override this; it was reconciled rather than treated as a silent scope change.

**Reasoning:** The Table Design Document is a construction-complete, already-worked-out design document — Section 11's phase ladder is a considered position, not a placeholder. Flattening it to "text-only, voice later" would have quietly revised a governing document without that revision being named as a revision, which cuts against this project's own discipline (deferrals are documented, not hidden — Constitution Article 36). Reconciling before drafting, rather than guessing which framing was authoritative, kept the spec from being wrong on its very first structural section.

**Open question closed:** What did "text first" mean, if not a feature cut? Left unresolved in this pass — Mark accepted the Table Design Document's framing without specifying what he meant by his own phrase. If it resurfaces (e.g., as a build-sequencing preference for the engineer — stand up text before wiring voice — rather than a participant-facing cut), that's a distinct, compatible decision and can be layered in without contradicting this one.

**Next action:** Spec Section 1 ("What it looks like") states the phase-by-phase modality plainly, sourced to Table Design Document Section 11, with the static-picture-not-text-only distinction called out explicitly so a reader doesn't default to assuming a text-only Alpha.

---

## 2026-07-07 — First full draft of the Front-End & Runtime Engineering Specification produced

**Status:** Draft complete, not yet reviewed by Mark. Per this project's standing discipline (full documents shown in full, not summarized), the draft is being handed to Mark in full before any version is treated as ready for a specialist engineer.

**What it covers:** Five parts, matching the launch brief — what it looks like (pre-encounter threshold, the Table, phase-by-phase build sequence through Phase 2+); what content it has (the three-tier deployment package: World Capsule Core, World Priority Layer, and the three retrieved-on-demand chunk types, plus Voice Configuration and the Facilitation Brief, illustrated throughout with real excerpts from World #1 and World #7 rather than hypothetical placeholders); how it handles Table conversations (context isolation, the public transcript, Facilitator orchestration, all eleven fidelity-drift signals, the five-Representative ceiling); the transparency and rigor apparatus (Three-Level Transparency, Transparency Mode, and the five-level confidence vocabulary kept as three distinct concepts, each rated built vs. designed-but-not-built); and what's genuinely unbuilt (the missing Deployment Standards document, the Layer 7 runtime retrieval systems, the Runtime State Model, no platform chosen yet). A closing section summarizes the Technology Engagement Brief's review model for the engineer's own orientation, and an appendix cross-references every claim back to its governing Constitution article.

**Reasoning:** Research was done directly against the primary governing documents (Vision, Constitution, Essential Experience, Table Design Document, Facilitator-Governance, Pre-Encounter Experience Design, Architecture Map, Technology Engagement Brief) rather than summarized secondhand, using parallel research agents to extract precisely enough detail to write engineering-grade content from — because a first-of-its-kind deliverable for an outside specialist deserves the same scrutiny as a construction document, even though it isn't one.

**Open items flagged inside the document itself, not smoothed over:** modality continuity for Beta/Phase 1 is inferred, not explicitly stated, in the two governing design documents — flagged for confirmation against the Phase Structure document. The five-Representative ceiling is currently enforced only by Facilitator judgment, with no system-level guard — flagged as a decision engineering should make deliberately. Several referenced documents (Phase Structure, Table Runtime Document, System Level Map, V7 file structure spec) were not themselves reviewed for this draft and are named in Section 7 rather than paraphrased with false confidence.

**Next action:** Mark reviews the full draft (saved to Ministry/Technology/CiC_FrontEnd_Engineering_Specification_V1_0.docx). Revise or approve before it is treated as ready to hand to a specialist engineer at Engagement One.

---

## 2026-07-07 — Course correction: vision before spec

**Decided:** The engineering spec drafted earlier today was premature. Mark redirected: the actual engineer engagement needs a description of how Mark envisions the experience working, not an engineering spec — and before that description can be written, Mark needed to actually articulate the vision out loud, starting with the landing page and "the discussion." This session is that conversation.

**Reasoning (the heart of it):** Formalizing mechanics (context isolation, retrieval tiers, drift signals) before the experience itself has been described in Mark's own words risks building the wrong thing precisely, rather than the right thing loosely. The governing documents already answer *how the Table is governed*; they don't answer *what it feels like to sit at it*, which only Mark can supply.

**Next action:** Once landing page is settled, synthesize this whole conversation into a single vision-description document (not an engineering spec) for Mark to react to, ahead of any renewed engineering work.

---

## 2026-07-07 — The Table, visually and experientially: first full concept

**Decided — "the discussion" is the Table encounter itself**, not a separate feature. No distinct "discussion" surface exists apart from the participant-plus-Representatives-plus-Facilitator conversation already named "the Table" in the Table Design Document.

**Decided — governing atmosphere:** a pub-style gathering in the spirit of the Inklings (C.S. Lewis, Tolkien, the Eagle and Child) but re-set in an early-church register — communal, unhurried, argument as affection rather than combat, humble and close to the ground rather than academically clever. This gives the already-existing term "the Table" its first real atmosphere; previously it was defined only mechanically.

**Decided — Prototype Alpha visual concept** (a considerable enrichment of "static picture background" as currently scoped in the Table Design Document):
- A single static background image showing up to five figures seated at a table — one per active Representative — in clothing typical of their world, with ethnicity/demographic representation drawn from that world's actual evidenced population, not defaulted to homogeneity or invented for the sake of visual diversity. Mark's own framing: "if there is diversity we would look for diversity at the table, but only if there was diversity" — this should be decided per world from its own Source Ecology (Doc_02), the same evidentiary discipline that governs everything else in construction.
- Each Representative's figure carries an object typical of that world's own expression of faith — a scroll for Alexandria, a codex for a world where that was the era's technology, nothing at all for the Post-Apostolic/pastoral world, which Doc_01 itself already establishes had no closed canon yet. The absence is not a gap to fill; it is itself the honest finding, consistent with the "Where This World Is Quiet" discipline already built into the World Capsule Core template.
- Camera movement (zoom and pan) across the single static image, driven by conversational turn-taking: zoom to the current speaker, pan between two Representatives mid-exchange, widen to the full table when the participant addresses everyone or turns to the Facilitator. This is a deliberate middle tier between a flat static image and the full "animated table" currently scoped for Phase 1 — it may mean Alpha can feel considerably more alive than the phase ladder's current language implies, without paying for character animation.
- A name and world descriptor displayed with each Representative's figure, so a participant can hold up to five distinct voices in mind without losing track of who is who.

**Decided — the dialogue box is the permanent structural layer, not a fallback:** the conversation is typed text at the center of the scene, and text stays load-bearing regardless of how rich the voice layer becomes, because the transparency apparatus (highlighting, hover, click) is fundamentally a text mechanism — it has no audio equivalent. Voice is an experience enhancement layered on top, not a replacement.

**Decided — voice ambition, explicitly cost-gated:** culturally- and gender-matched text-to-speech per Representative is the goal; English first, with other languages as the project grows; cost is the named barrier today, not a design or architecture limitation. Flagged as a concrete, fundable line item to raise with the org/funding workstream, not solved here.

**Decided — the transparency/lexicon interaction pattern, made concrete:** terms unique to a world, or whose meaning differs from modern understanding, are highlighted in the dialogue text. Hovering surfaces a short popup description (Level 2). Clicking opens the full lexicon and context detail (Level 3). The same hover/click pattern extends beyond lexicon terms to stories, quotes, and transparent sourcing generally — one consistent interaction pattern for anything carrying a confidence tier, rather than a different treatment per content type.

**New gap identified, not yet built:** no per-world ethnicity/demographic profile exists in the current template set (World Profile, Source Ecology, Voice Configuration). One should be built — likely as an extension of Source Ecology or a sibling to Voice Configuration — so the visual/physical representation of a Representative answers to the same evidentiary discipline as its vocabulary and voice. Directly serves Article 20 (marginalized-voices duty) and the Historical Responsibility value.

**Still open, not yet answered:** whether an unevidenced-object absence (e.g., the pastoral world's empty space) is something a participant might notice and ask about, or simply present without any emphasis either way.

---

## 2026-07-07 — Main page: menu pattern decided, hero content still open

**Decided:** About, Features, FAQ, and similar informational content live behind a menu that opens as a temporary overlay window on top of the main page, rather than navigating the participant away from it. Keeps the participant anchored on the main experience rather than routing them through separate pages.

**Still open:** what the main page's primary content actually is — the first five seconds before any menu is touched. Not yet resolved whether this is the Table image itself (populated or with empty/waiting seats), something simpler, or something else entirely.

---

## 2026-07-07 — Landing page hero (provisional), Ask the Facilitator, onboarding shaping, Tours, and the one rule underneath everything

**Decided — landing page hero (provisional, pending Mark's confirmation):** an evocative, not-yet-populated version of the Table — empty or waiting seats, warm light, no specific Representatives visible since no world has been chosen yet — with a short, honest invitation line rather than marketing copy. The three entry pathways (Bypass, Build Your Own Table, Guided Onboarding) sit with equal visual weight beneath or alongside it, no default or "recommended" badge on any. "Ask the Facilitator" sits as a clearly secondary but visible option. The About/Features/FAQ menu overlay sits outside all of this.

**Decided — "Ask the Facilitator":** the pre-threshold Q&A feature (for a skeptical or curious visitor who wants to interrogate the project before trusting it with anything real — e.g., "why can't I talk to Origen or Augustine") is voiced by the Facilitator itself, not a separate support persona. Reasoning: the Facilitator is already the neutral, trustworthy host a participant can step outside an encounter to address directly; a second voice for FAQs would mean maintaining two different personalities that both need to sound credible, for no real benefit. "Why can't I talk to Origen or Augustine" is itself a strong worked example for this feature — the honest answer (a single historical figure's exact voice can't be reconstructed with the confidence this project requires, but the world that formed people like him can be) is a feature to state plainly, not a limitation to dodge.

**Decided — onboarding role-shaping, future feature, not yet activated:** the existing four-role selection (regular visitor, pastor/teacher, academic/scholar, deconstructing/reconstructing) will eventually shape two distinct things, kept distinct: (1) a baseline readability target — currently 10th-grade reading level for accessible (Level 2) explanations of source words and ideas, which applies to everyone regardless of role, and gives Constitution Article 30's "accessible, plain-language explanation" a concrete, testable definition it doesn't currently have; and (2) role-based content emphasis layered on top of that floor — e.g., a pastor is offered more sermon-prep-relevant angles by default, an academic is offered more exposed rigor by default. Access to everything remains universal regardless of role — role changes what's offered first, never what's reachable. This is explicitly a later feature, not scoped now, but important enough to design the underlying data model for from the start rather than bolt on afterward.

**Decided — Tours, future feature, Phase 3 (confirms and extends what the Architecture Map already names):** the Representative can guide a participant through a tour of their world — illustrated with pictures, potentially including experiences like a church service or the Eucharist — bounded strictly by what that world's source material actually documents. A world with rich liturgical description can support a full tour; a world without one must say so plainly rather than inventing content to fill the request — Mark's own example: a participant asking to "sit through a sermon" in a world with no documented sermons should hear something like "this world doesn't have the documented sources to describe this," not silence and not fabrication. This also resolves the earlier open question about whether an unevidenced absence (e.g., the empty object at the table for the pastoral world) should be noticed or silent: the answer, extended from this example, leans toward explicit and honest when a participant actively asks, rather than uniformly silent.

**The one rule underneath all of it, named explicitly because it kept resurfacing independently:** only what the evidence actually supports is shown, played, or offered — for a world's vocabulary, its people's ethnicity, the object on its table, and now the experiences and tours it can offer. Where evidence runs out, the system says so plainly. This is not several rules that happen to agree; it is the same rule, expressed once, showing up everywhere.

**Next action:** synthesize this entire conversation into a single experience-vision description document — not an engineering spec — for Mark to react to. This is the actual deliverable the specialist engineer asked for.

---

## 2026-07-07 — Experience Vision document produced; entry-path reconciled; phased build plan produced

**Produced:** `CiC_FrontEnd_Experience_Vision_V1_0.docx` — the full narrative description of the Table experience (atmosphere, room, objects, camera, voice, transparency mechanics, landing page, Ask the Facilitator, future features), written for the specialist engineer in descriptive rather than technical-spec register.

**Reconciled — entry path already documented:** Mark's own phrasing ("straight to question," "pick worlds," "facilitator picks worlds," "introductions") maps directly onto the Pre-Encounter Experience Design's existing three pathways (Bypass, Build Your Own Table, Guided Onboarding) plus the encounter arc's opening move. Confirmed as a match, not a new decision — nothing changed here, just traced back to the governing document that already specifies it.

**Produced — `CiC_FrontEnd_Vision_and_Phased_Plan_V1_0.docx`:** a shorter, phase-organized version of the vision for the front-end engineer specifically, structured the way Mark asked for it: Prototype 1 (Alpha), Prototype 2 (Beta), Phase 1 Implementation, Periodic Improvements, and Ultimate Vision. Periodic Improvements is framed as an ongoing track (voice-casting quality, onboarding role-shaping, the ethnicity/demographic reference) rather than a sequential fifth phase, since none of those three have a fixed release trigger — they improve as funding and evidence allow. Prototype 1's voice is named explicitly as "a first pass," not the fully culturally-matched casting — that richer casting is Periodic Improvements' job, not Alpha's.

**Next action:** Mark reviews both documents. The Vision and Phased Plan doc is the one meant to go to the front-end engineer directly; the fuller Experience Vision doc is the source material behind it, for reference if the engineer wants more texture than the phased summary carries.

---

## 2026-07-07 — Naming corrections: "conversation" not "discussion"; "The Church in Conversation"; Phase 1 named

**Decided — terminology:** "conversation," not "discussion," for what happens at the Table. Applied across all three documents produced so far.

**Decided — project name:** "The Church in Conversation," not "Church in Conversation." Applied to titles, headers, and body text in the three documents this workstream has produced (Engineering Specification, Experience Vision, Vision and Phased Plan).

**Not applied — scope note:** the L1 governing documents (Vision, Constitution, Essential Experience, and the rest) consistently use "Church in Conversation" without "The." This correction was not cascaded to those documents — that's a larger naming decision touching constitutional-tier documents outside this workstream's authority to change unilaterally, and worth Mark's explicit confirmation before anyone edits them, rather than assuming a naming fix here should propagate there.

**Decided — Phase 1's real name:** "Conversations with the Early Church." Added to the Vision and Phased Plan document as the named title of the Phase 1 Implementation stage.

**Next action:** if "The Church in Conversation" is meant to also govern the L1 documents, that should be raised as its own explicit decision, not inferred from this correction.

---

## 2026-07-07 — World Map feature (Ultimate Vision); Constitution version discrepancy investigated and corrected for in the Engineering Spec

**Decided — World Map, future feature (Ultimate Vision):** once the world catalog outgrows a simple list (Phase 1 launches with 9 worlds; the eventual catalog may hold 50-100 spanning all of history and today), world discovery becomes an abstract timeline — in the visual spirit of a Bible timeline chart, not a literal geographic map — with worlds positioned as bands or nodes at their real historical moment, parallel lanes making contemporaries visible without the participant doing the math, and lines drawn between worlds that shaped each other. Worlds can be pulled to the same Table across eras, not just within one. Worlds the project has chosen not to build sit right on the same timeline, dimmed, using the same hover-for-short-explanation/click-for-detail mechanic already built for lexicon terms and stories — extended here to a fourth content type: why a world isn't here at all. Two distinct exclusion reasons, surfaced honestly rather than smoothed together: insufficient evidence for a real build, or falling outside the project's doctrinal floor (see below). Not scoped for any near-term phase; captured now so the idea survives to when the catalog actually needs it.

**Investigated — the Constitution's "Movement Scope" doctrinal floor:** confirmed real and located. It sets a doctrinal floor, drawn from the Nicene-Constantinopolitan Creed, for which historical movements are eligible for construction at all (five specific affirmations: the Father as maker of all things, Christ's full divinity and eternal begottenness, Christ's full humanity, Christ's death/resurrection/ascension/return, and the Holy Spirit's status) — a test of belief in plain historical sense, not institutional submission to a council, and never imposed on a selected world's own voice or used to suppress a marginalized voice within an included world. World #1 and the Syriac world both predate Nicaea/Constantinople chronologically but meet the floor in substance, consistent with the Constitution's own language that a movement "need not have existed at a date when doing so was possible."

**Investigated — real version discrepancy found and explained:** this section exists in the Constitution copy on the branches currently building toward Phase 1 (internal Version 2.3) but not in the frozen main-tree copy (Version 2.2, same filename). Confirmed intentional, not drift: Mark's practice is to prove constitutional changes out against real world builds before merging them back to the main tree that governs the whole project. Two more differences found the same way: Facilitator Governance moved V3.4 to V3.6 on the same branches (a new Self-Narration drift signal, discussed below, plus a tested decoupled classify-then-route-then-generate Facilitator architecture); the Architecture Map now names the Source Registry as its own tracked deployment artifact and marks the Article 17/19 Construction-Framework reconciliation gap resolved on those branches. Vision, Essential Experience, Technology Engagement Brief, Pre-Encounter Experience Design, Table Design Document, Phase Structure, and Forces Framework are all confirmed unchanged.

**Corrected — Engineering Specification bumped to V1.1** (in this workstream's own output only; no governing document files were touched, per Mark's explicit instruction): the drift-signal count is now twelve, not eleven, with the new Self-Narration signal described in full and its stricter automatic-frame-breaker handling explained; a paragraph added on the tested classify-then-route-then-generate Facilitator architecture; Section 7's Construction Framework bullet corrected from "a live, named reconciliation gap" to "resolved on the branches this deployment is actually building against, still open in the frozen main-tree copy"; a new Section 7 bullet and Appendix intro line naming the Constitution version discrepancy plainly; the Appendix cross-reference table gained Article 28 (Anti-Fabrication Prohibition, grounding Self-Narration) and an updated Article 31 description naming the Source Registry; Section 2.5 gained a Source Registry bullet with real file citations from both World #1 and World #7.

**Next action:** none pending on this thread specifically. World Map is logged as a future feature ready to pick up when Ultimate Vision work resumes.

---

## 2026-07-07 — Academic Documents (raw transparency) and the world-click menu; phasing corrected

**Decided — Academic Documents:** a fourth, distinct transparency feature, separate from the in-conversation hover/click mechanic. Where hover/click surfaces sourcing reactively, per claim, as it comes up in a live conversation, Academic Documents is proactive and standalone — the full Lexicon, full Story Repository, and source documents (Source Ecology, Source Registry) for a world, raw and unmodified, browsable independent of any conversation. Same view for a casually curious visitor as for a qualified external reviewer doing Article 31 review — no separate reviewer-only layer inside this feature; whatever formal review workflow Article 31 requires is a distinct track, not part of this. Content is not new production — it's the L4-Templates-shaped, already-existing per-world build documents (Doc_01 through Doc_09, Lexicon-Chunks, Story-Chunks, Source Registry) exposed directly.

**Decided — lives in the world-click menu:** clicking into a world (from world-browsing or the future World Map) opens a menu of four options rather than a single action: Description, Tour, Choose for Table, and Academic Documents. This unifies four previously-separate ideas (the short menu card, the Phase 3 Tour feature, the core Table-selection action, and Academic Documents) into one consistent interaction point.

**Decided — phasing, corrected from an earlier draft in this same log:** at Phase 1, only Choose for Table is functional. Description, Tour, and Academic Documents all appear as visible placeholders in the same menu — signaling what's coming without being built yet — and become real at Phase 2. Keeps Phase 1 lean and honest rather than shipping partial versions of three features at once.

**Next action:** fold into the Phased Plan (Phase 1 gets the world-click menu with only Choose for Table live; Phase 2 activates Description, Tour, and Academic Documents) and the Experience Vision document, next time either is updated.

---

## 2026-07-07 — Checked against Facilitator Governance directly; closing-resources idea is a genuine addition, not a gap

**Investigated, at Mark's direction:** whether the vulnerable-participant and closing concerns raised this session are already covered in Facilitator Governance (V3.6, the branch currently building toward Phase 1) before treating them as gaps.

**Confirmed already mature, correcting an earlier overstatement in this thread:** Facilitator Governance already specifies an Acute Distress trigger (present crisis or self-harm risk — "surface with warmth and honesty about the limits of what this encounter can offer, and with whatever redirection toward human support is appropriate") and a Harmful Dynamic trigger that names dependency directly ("the participant is relating to the Representative as a substitute for human relationship rather than as a formation encounter"). Both resolve through the same three-posture model as every other governance trigger — Hold, Surface briefly, Intervene — matching Mark's own description of the Facilitator watching in the background and only surfacing when a pattern needs it. No product-level gap here; this is conversational, not a separate UI, and it's already well specified.

**Genuinely new — closing resources:** the current "gracious close" section describes the general posture (the last word is always a comma, not a period; the door left open) but says nothing about offering resources tied to what came up. Mark's addition: at closing, ask — never push — whether the participant would like resources around a topic or a hurt that surfaced, and if so, hand over links or sources for self-directed follow-up. Explicitly framed around participant agency: this lets them take control of their own learning or transformational journey rather than the system prescribing a next step. Directly serves Article 34 (Doorway Not a Home)'s "gentle redirection outward" requirement, which had no product expression before this.

**Resolved:** Facilitator-curated in the moment, genuinely responsive to what actually came up in that specific conversation — not a generic per-topic list. Mark's own reasoning, worth preserving: this is deliberately building relational feel and connection into the Facilitator even though it isn't human. Not in tension with Article 34's prohibition on substituting for human relationship — a doorway that greets someone well is still a doorway; the warmth is what makes leaving well possible, rather than leaving feeling processed.

**Also flagged, still open, not yet decided this session:** conversation privacy/data-logging disclosure, and whether Phase 1 requires accounts or stays stateless — both raised as real, unresolved product questions, neither resolved yet.

**Decided — closing resources use the same hover/click mechanic:** hover gives a brief explanation of a suggested resource, click opens the link and more detail. The fifth application of the same interaction pattern already built for lexicon terms, stories, quotes/sourcing, and Academic Documents — no new UI invented for this moment. Keeps a potentially heavy moment (offering resources around something painful) light and optional rather than a wall of links.

## 2026-07-07 — Funding model direction: free core experience, paid professional layer — with a constitutional boundary named explicitly

**Decided — direction:** the general encounter stays free for everyone, Bible-Project-style (donor/crowd-funded, no paywall on the mission-critical experience). A cost may apply to unlock deeper pastor and academic-facing features — sermon-prep tooling, Academic Documents, Tours — rather than the core conversation itself.

**Boundary drawn, and it matters:** Article 30's Three-Level Transparency invariant ("Levels 2 and 3 always reachable from Level 1, never gated") governs a participant's own in-conversation encounter — whatever comes up in a live conversation, the grounding behind it stays free and reachable via the existing hover/click mechanic, for everyone, regardless of what happens with anything else. That does not change under this model. Tours and sermon-prep tooling don't touch Article 30 at all — they're experience and productivity features, not evidentiary access, so no constitutional question there. Academic Documents is the genuinely gray case: still "seeing the sources," just at a standalone-browsing surface rather than tied to a specific conversation. Gating it is defensible (nobody's own encounter depends on the full corpus being free to browse independent of any conversation) but is a real product decision sitting close enough to Article 30 that it needs an explicit, named carve-out in the Constitution rather than a quiet workaround.

**Mark's own instinct, worth preserving:** if Academic Documents ends up gated, the Constitution should be changed to say so plainly — the same discipline already used for the Movement Scope addition: test the change on a branch, state plainly what it does and doesn't cover, merge back once proven, rather than letting a product decision quietly outrun what the governing document actually says.

**Next action:** flag for the funding thread as a real model direction. If/when Academic Documents gating moves from idea to decision, the Article 30 carve-out is a governance change outside this workstream's authority to draft unilaterally — same category as the Movement Scope and "The Church in Conversation" naming questions already logged.

---

## 2026-07-07 — Engineering Considerations Catalog created (Project-Reference), so this doesn't stay locked to one thread

**Decided:** The "what else should I be considering, especially for Phase 1 and earlier, without setting something up that has to be completely rebuilt to grow" answer from this thread is durable, cross-cutting engineering judgment, not a narrative decision specific to this workstream — so it doesn't belong only in this dated log. Catalogued instead at `Project-Reference/CiC_Engineering_Considerations_Catalog_V1_0.md`, alongside the existing Cleaning Pattern Log, in the same disciplined pattern-entry format (the risk, what to do now at lean/prototype scale, what it protects later). Committed to git on main so it's available to any future thread — world builds, org/funding, validation — without that thread having to rediscover it independently.

**What's in it:** six build-now-vs-rebuild-later considerations (world data schema readiness for the future World Map; retrieval behind a clean interface; the funding model forcing the accounts/identity question sooner than expected; building the real voice pipeline now with a cheap voice rather than a throwaway version; the unresolved tension between internal QA conversation-logging and participant privacy, flagged as time-sensitive rather than someday; world-content versioning separate from app-code versioning) plus a short pointer section to considerations already logged elsewhere (Article 30 boundary, the five-Representative ceiling's missing system-level guard, the world-click-menu placeholder architecture, and the standing hazard of conflating the three distinct transparency concepts).

**Note on the commit itself:** a stale `.git/index.lock` blocked normal `git add`/`git commit` (likely a Windows-side file lock from another process with the repo open). Worked around it using git plumbing commands (temporary index, `write-tree`, `commit-tree`, `update-ref`) that don't touch the locked index file — the commit is real and on `main` (`0a7b1ac`), but the real working-tree `.git/index` itself is now stale until that lock clears. Worth closing whatever has that repo open on the Windows side, then running `git status` once to let it self-correct; not urgent, doesn't affect committed history.

**Next action:** none pending. Future threads should check the Engineering Considerations Catalog before re-deriving this kind of judgment from scratch.

---

## 2026-07-08 — Design Brief corrected: Academic Documents governance caveat restored, Alpha-scope clarified, Facilitator-orchestration question flagged as genuinely open

**Context:** A detailed review of `CiC_FrontEnd_Design_Brief_V1_0.docx` (the one-to-two-page brief for the engineer) identified two substantive accuracy problems, not stylistic ones. Both were verified against source documents before any edit was made.

**Fix 1 — Academic Documents overstated as settled.** The brief had described Academic Documents as a future paid-tier feature alongside Tours and sermon-prep, full stop — no caveat. The 2026-07-07 entry above calls Academic Documents "the genuinely gray case": gating it is defensible, but it sits close enough to Article 30's always-free-and-reachable transparency guarantee that it needs an explicit, named constitutional carve-out before being built that way — a carve-out that hasn't been made. The brief's funding paragraph now states this directly: Academic Documents' gating is an open governance dependency, not a settled product decision, and should be treated that way by whoever builds it.

**Fix 2 — Alpha vs. Phase 1 scope was undifferentiated.** The Functional Requirements section described the full system (five Representatives, three equal-weighted entry paths, full Facilitator orchestration) without saying which parts Alpha actually needs, against Mark's own Alpha philosophy ("smallest possible thing that lets a real person talk to a Representative"). Checked against the actual governing document, not assumed: Table Design Document Section 11 confirms Alpha = 1–3 worlds with Bypass entry only and basic role selection; the full three-pathway portal (including world browsing) isn't delivered until Phase 1, with Beta still excluding it. The entry-state requirement in the brief now states this phase split explicitly, with a citation to Section 11.

**Genuinely open, not resolved — flagged in the document rather than guessed at:** Table Design Document Section 11 confirms entry-pathway scope but is silent on whether full multi-Representative Facilitator orchestration (turn-taking across concurrent Representatives, cross-world drift monitoring) is required at Alpha or can be deferred to Beta. This materially affects Alpha engineering scope. Added as an explicit open-scope note in the brief, immediately before the Build Order table, rather than resolved unilaterally — this is Mark's call, and the reviewer was right that it could change engineering estimates.

**Verification:** claim 1 checked directly against this log's 2026-07-07 entry; claim 2 checked against `CiC_FrontEnd_Strategy_Scoping_2026-07-07.md` and against Table Design Document Section 11 itself (read across all four copies on disk — main, both worktrees, Syriac-Build — confirmed byte-identical, so no version drift risk).

**Next action:** Mark to decide whether Facilitator orchestration is in scope for Alpha or deferred to Beta — the one open question the brief could not resolve from existing governing documents.

---

## 2026-07-08 — One-page Design Brief produced; landing-page hero resolved: the Facilitator is present, not an empty Table

**Produced:** `CiC_FrontEnd_Design_Brief_V1_0.docx` — a one-page distillation of the Experience Vision and Vision & Phased Plan, written to hand directly to the engineer so he can start designing without reading the full spec set. Covers: what this is, the governing feeling, the one rule, the experience compressed into five bullets, the build-order table, and the constraints worth knowing before starting (five-Representative ceiling, text as permanently load-bearing, build the seams not the features).

**Resolved — the landing-page hero, previously logged provisional:** the 2026-07-07 entry on the landing page described "an evocative, not-yet-populated version of the Table — empty or waiting seats... no specific Representatives visible" and flagged it pending Mark's confirmation. Mark corrected this directly: the Table at entry is not empty — the Facilitator is there, the one figure present, to greet the participant and offer the three entry choices. This isn't a new decision so much as a completion of the original one: "no Representatives yet" was always true, but it read as "no one yet," which wasn't intended. The Facilitator's presence at the threshold is consistent with its role everywhere else in the design (neutral host, the one voice a visitor can address before committing to anything, "Ask the Facilitator") — it would have been an odd gap for it to be the one place the Facilitator isn't visually present.

**Applied:** the Design Brief's Landing bullet now reads accordingly. Not yet propagated to the fuller Experience Vision document (still not updated with this or the several other post-creation decisions logged above — World Map, Academic Documents, funding model, Article 30 boundary — same open gap noted repeatedly in this log).

**Next action:** none blocking. Worth folding into the Experience Vision doc's own landing-page section next time that document is revised.

---

## 2026-07-08 — Design Brief extended to two pages: "Where This Is Headed (So You Don't Build a Trap)"

**Decided:** Mark explicitly waived the one-page constraint to add long-term-vision context for the engineer — reasoning stated directly: without it, Phase 1 gets built as if it's the whole product, and something in it becomes a trap. Added a new section between Build Order and Design Constraints covering, in narrative form, everything the Build Order table doesn't show: the eventual 50–100 world catalog and the World Map timeline it needs, the four-option world-click menu (Description/Tour/Choose for Table/Academic Documents), Academic Documents as a future standalone feature distinct from the in-conversation hover/click, Tours, maturing voice, and the funding shape (free core permanently, a possible paid pastor/academic tier on top).

**The concrete payoff, not just narrative:** a seven-row table — "Build this seam now (cheap)" against "Because this needs it eventually (expensive to retrofit)" — translating the Engineering Considerations Catalog directly into engineer-facing guidance: world data fields, retrieval behind a clean interface, the four-option menu built disabled rather than added later, a role/entitlement field, the real voice pipeline, content versioning, and a written logging/privacy policy before Alpha testing starts. This is the same seven-ish items from the Catalog, translated from "why it matters" into "build it this way," which is what an engineer actually needs at the point of building rather than a reference document to go read separately.

**Reasoning:** Kept the seam table separate from prose so it functions as a checklist an engineer can actually work against, not just context to have read once. Trimmed the old "build the seams" bullet under Design Constraints to a pointer rather than deleting it outright, so the constraints section still names it without duplicating the fuller explanation above.

**Next action:** none blocking. The doc is now two pages by design, not by accident — Mark should treat any further additions as a deliberate length trade-off, same as this one.

---

## 2026-07-08 — Design Brief reworded for an experienced-engineer audience

**Decided:** Mark's own phrase "so you don't build a trap" was informal shorthand from our conversation, not the register he wanted in the document itself. Reworded the Roadmap Context section, the seam table, and the Design Constraints bullets throughout: the section title became "Roadmap Context — Forward-Compatibility Requirements"; the seam table's two columns became "Requirement (Phase 1)" and "Forward-Compatibility Rationale," with every row rewritten as an explicit implementation requirement paired with its rationale, rather than descriptive prose; the constraints bullets were tightened to name the actual enforcement point ("enforce it explicitly in session/state logic," "non-functional requirements alongside the functional spec") instead of conversational framing like "full stop" and "hard ceiling."

**What was deliberately left alone:** the experience-description sections (What This Is, The Feeling We're Building Toward, The One Rule, The Experience Compressed) — those are product/UX description meant to convey feel to whoever builds this, and an evocative register is doing real work there, not a lapse in precision. The register change was scoped to the sections giving the engineer direct implementation guidance, where imprecision has a real cost.

**Reasoning:** A design brief that describes intent in engineer-precise language is more likely to be read as a requirements document and actually followed, rather than as color commentary the reader skims past. Worth naming as a general pattern for any future engineering-facing document produced in this workstream — vision/experience sections can stay evocative, requirement sections should read like requirements.

**Next action:** none blocking.

---

## 2026-07-08 — Section order corrected to a big-to-little flow; table row-splitting fixed

**Decided:** Mark asked directly whether the document's order was a natural flow. It wasn't: What This Is → Feeling → One Rule → Experience Compressed → Build Order → Roadmap Context → Constraints put the near-term Phase 1 build order immediately before a jump out to the 50–100-world long-term picture, then back into specifics — a zigzag rather than a single trajectory. Reordered to context-first: What This Is → The Feeling → The One Rule → Roadmap Context (with its requirements table) → The Experience, Compressed → Build Order → Design Constraints. Every section is now more concrete than the one before it, so nothing the engineer is asked to build in the near term is read before he has the full scope envelope it needs to fit inside.

**Reasoning:** This matches how technical specs are conventionally structured for an engineering reader — context and goals before detailed design — precisely because the whole point of the Roadmap Context section is to shape how the near-term work gets built. Reading it last, as originally ordered, would have let the reader form a mental model of the architecture before encountering the constraints meant to inform it.

**Also fixed while rebuilding:** the seam table's last row was splitting mid-sentence across the page 1/2 boundary. Added `cantSplit` to table rows in the docx-js build so a row now moves to the next page whole rather than breaking across it, with the header repeating above it — same fix belongs in any future table-heavy document built with this pipeline.

**Next action:** none blocking.

---

## 2026-07-08 — Terminology correction: "engaging conversation," not argument or debate

**Decided:** Mark rejected the "argument as affection rather than combat" framing under The Feeling We're Building Toward — his own words: "it's not a theological debate or an exegetical argument, its healthy, deep insightful, challenging, stretching, resonating conversations (thus the name), summed up in 'engaging conversation.'" The Inklings image stays (the setting still communicates unhurried, communal, close-to-the-ground), but the verb changed from Lewis and Tolkien "arguing" to "meeting," and the description changed from "argument as affection rather than combat" to an explicit definition: not a theological debate or an exegetical argument, but engaging conversation — healthy, deep, insightful, challenging, stretching, resonating. Added "The name is deliberate" to tie the phrase directly back to the project's own name, "The Church in Conversation."

**Why this matters beyond word choice:** "argument," "debate," and "combat" carry a winner/loser, position-defending connotation that cuts against Witness-Not-Recruitment (Article 24) and the project's own stated failure modes (ideological persuasion, generated panel entertainment). "Engaging conversation" — challenging and stretching without needing a winner — is the more accurate description of what this project is actually for, not just a softer synonym.

**Propagation gap, not yet fixed:** the same "argument as affection rather than combat" phrasing exists in `CiC_FrontEnd_Experience_Vision_V1_0.docx` ("Inklings image: unhurried conversation, argument as a form of affection rather than combat, people who trust each other enough to disagree hard..."). Not corrected there yet — same standing gap already noted several times in this log (the Experience Vision doc lags behind decisions made after its creation). Worth a full pass next time that document is revised, this correction included.

**Next action:** none blocking on the Design Brief. Carry this correction into the Experience Vision doc whenever it's next revised.

---

## 2026-07-08 — Full document reworded for an engineer audience, not just the Roadmap Context section

**Decided:** Mark asked for the whole document to speak to an engineer, extending the earlier register fix beyond the sections it was originally scoped to. Reworded every remaining section: "What This Is" became "System Overview," rewritten as a functional description of the session/agent/orchestration model rather than narrative description of a participant's experience. "The Feeling We're Building Toward" became "Design Intent" — same content (the Inklings reference, "engaging conversation," the name being deliberate), reframed as a design-tone requirement rather than a mood-setting passage. "The One Rule Underneath Everything" became "Governing Content Rule," stated as a global invariant. "The Experience, Compressed" became "Functional Requirements — Core Experience," with each bullet rewritten from descriptive prose ("Landing: an evocative Table...") into an implementation-oriented requirement (entry states, rendering behavior, data sources, interaction patterns). "Design Constraints Worth Knowing Before You Start" tightened to "Constraints." Also caught and fixed two remaining casual words in the Roadmap Context prose ("is real at Phase 1" → "is implemented at Phase 1," "first pass voice matures" → "is expected to be superseded by").

**What didn't change:** every fact, requirement, and number in the document is unchanged — this was a register pass, not a content revision. The Inklings reference and "engaging conversation" language survive intact inside Design Intent, reframed as what tone the implementation should target rather than as atmosphere-setting for its own sake.

**Reasoning:** A document meant to be read and acted on by an engineer should read like a requirements document throughout, not only in the sections added most recently — mixing an engineering register with a narrative one in the same document reads as inconsistent and makes it unclear which parts are binding. This is a genuine content-vs-register question worth remembering: the same underlying decisions can be expressed as either narrative (for Mark's own thinking, or the fuller Experience Vision document) or requirements (for an engineer), and this document should now consistently be the latter.

**Next action:** none blocking. Worth treating the fuller Experience Vision and Vision & Phased Plan documents as intentionally narrative-register — this Design Brief is now the one requirements-register artifact in the set, and the two registers shouldn't be blended going forward.

---

## 2026-07-14 — Citation transparency confirmed half-built, not just half-designed; new world-selection mode raised, heart-reasoning still open

**Context:** This session had been deep in backend prompt/orchestration work on the actual running prototype (`cic-poc`), not this workstream's planning documents. Mark raised two ideas directly against that running code: (1) three-level rigor for the lexicon, extended to stories and sources, surfaced as inline colored text or an icon at sentence-end with hover and click, rather than listed separately at the end; (2) restructuring world selection from a single "choose a world" action into two distinct modes — a deeper interview with one world, harness deliberately loosened for longer dialogue, versus choosing 2-3 worlds for comparison.

**Confirmed, not re-decided — idea 1 already exists at two levels:** the 2026-07-07 entry above already decided this exact pattern (highlight in dialogue text, hover for Level 2, click for Level 3, extended to stories/quotes/sourcing generally). Checked against the actual running frontend, not just the doc: `LexiconHighlight.tsx`/`HighlightedText` already implements this live for lexicon terms - inline highlight, hover tooltip, click-through. The gap is narrower than "build the mechanic": citations/sources currently render as a plain list block at the bottom of each message (`MessageBubble.tsx`'s "Sources" section), not through the same inline hover/click component. That's the one piece of an already-decided, already-partially-built pattern that hasn't been extended yet.

**Decided this session:** build the citation-inline mechanic next, ahead of any of the richer visual Table work (multi-figure background, camera pans, voice) already described in the Experience Vision documents - reasoning being that this is a scoped, already-proven-pattern frontend change working directly against the real prototype, not a new design question, while the richer visual work is real but is specialist-engineer-tier and more expensive to get wrong. Not a reversal of the phase-ladder work above, just a sequencing call for what to build with the time available right now.

**Raised, not yet decided — the two-mode world-selection idea:** genuinely new, not present anywhere earlier in this log. Noted as mechanically compatible with what the backend already does: the reactive-turn constraints tuned extensively this session (length ceilings, table_discourse.py's reactive guidance, anti-resolution rules) only activate when a representative speaks after another has already spoken in the same round - a single-world conversation never triggers any of it. So "a looser harness for a deep interview" is closer to the existing default behavior of a one-world conversation than a new backend mode to build; the open work is making that an explicit, named entry-point choice rather than an accidental byproduct of world count.

**Heart question asked, not yet answered:** whether "Deep Interview" mode is meant to protect real formation-encounter depth with one voice (in the spirit of Encounter Over Persuasion - one voice actually forming a participant, not just answering questions), with "Compare Worlds" understood as a different kind of use (useful, but structurally comparison-shopping rather than encounter), or whether something else is driving the split. Left open rather than assumed, since the answer would shape whether Compare Worlds gets the same conversational depth treatment or is deliberately kept lighter/shorter.

**Next action:** citation-inline mechanic build starts this session (see cic-poc frontend changes). World-selection mode split stays logged as raised-but-open until Mark answers the heart question above - do not treat it as decided or start building an entry-point split before that's answered.

---

## 2026-07-14 — Heart question answered: the two-mode split is about readability/cognitive load, not encounter depth

**Answered, correcting the earlier hypothesis:** the 2026-07-14 entry above guessed the Deep Interview/Compare Worlds split was about protecting formation-encounter depth (Encounter Over Persuasion). Mark corrected this directly - it is not that. His own reasoning: at 3-4 representatives seated together, the interaction has to stay crisp, one idea in focus per turn, simpler dialogue structure, because the participant is tracking several voices at once and complex, long single turns become unreadable in that setting. A single-world conversation can afford longer responses and slightly more complex answers, room to actually flesh an idea out in one turn - space a multi-representative table doesn't have per turn, though the same complexity can still emerge in that setting, just spread out across 2-3 rounds of exchange between representatives rather than landed in one turn. In short: this is a readability/cognitive-load design question, not a depth-of-encounter one.

**Why this matters beyond getting the reasoning right:** it directly names the design intent behind mechanics already built and tuned at length earlier this same session - the per-world reactive-turn length ceilings, table_discourse.py's "one idea per turn"/anti-question-stacking rules, and the explicit allowance (already written into table_discourse.py) for a real idea to develop across multiple rounds rather than being forced into one turn. Those were built and tested as conversational-quality fixes; Mark's answer here is the product-level "why" that was missing - they exist to keep a crowded table readable, not only to make any single representative sound better in isolation.

**Confirmed still compatible with what already exists, sharpened by this answer:** the earlier note that a single-world conversation already runs "loose" by default (the reactive-turn ceiling only ever applies to a non-first speaker in a multi-world round) holds up under this more precise reasoning too - a solo Deep Interview conversation never hits those ceilings today, which is exactly the room-to-flesh-an-idea-out behavior Mark is describing, not a coincidence.

**New consideration surfaced by this answer, not yet decided:** the current reactive-turn ceiling only applies to representatives speaking after the first one in a round - the first speaker in a 3-4-world round today gets no shortening at all, even though the participant is about to read several more turns immediately after it. Worth asking whether "crisp, one idea in focus" should also apply to a round's opening turn once 3+ worlds are seated, not only to the turns reacting to it - flagged here as a real open question this answer raises, not decided or built yet.

**Next action:** log stays open on the entry-point UI split itself (still not built) - Compare Worlds should NOT default to a lighter/shorter conversational feel than Deep Interview by name alone; the actual difference this answer supports is the existing per-turn brevity discipline scaling with table size (already partly true at 2 vs. 1, worth checking whether it should scale further at 3-4), not the two modes representing different depths of encounter. Whether to also tighten the round-opening turn at 3-4 worlds is a genuinely new follow-up, not yet raised with Mark for a decision.

---

## 2026-07-14 — Round-opening-turn brevity built for 3+ world tables, with Mark's own refinement: fuller but not freeform

**Decided and built (cic-poc backend):** the follow-up question above ("should a round's opening turn also be held to brevity at 3-4 worlds") was answered yes - Mark's own words: "the user can't read 5 pages to get to the last representative." Then refined once built: the opening turn - the round's one direct answer to what was actually asked, before anyone else has weighed in - can run 20-30% longer than a later reactive beat, but should not be freeform/unlimited the way an opening turn used to be.

**What this is not:** the opening turn does not get REACTIVE_TURN_GUIDANCE's text (which opens "someone else has already spoken on this question" - false for a genuine opener). A new, distinct guidance block was written for this exact case (`OPENING_TURN_LARGE_TABLE_GUIDANCE` in table_discourse.py) so the model is never told something untrue about its own situation to get the length effect - a real cost of the "just reuse is_reactive" shortcut that was caught and fixed before committing, not after.

**The concrete numbers:** reactive turns keep their existing 900-token ceiling; a large-table (3+ worlds) opening turn gets 1125 tokens - exactly 25%, the midpoint of Mark's stated 20-30% range. Applies only when `is_reactive=False` (nothing to react to yet) and the table seats 3 or more worlds; 1-2 world tables are unaffected, matching the readability reasoning from the entry above (the reader only sees one other turn after a 2-world opener, which doesn't create the same "5 pages before the last voice" problem).

**Next action:** none blocking on this specific mechanism - it's built, verified directly (see cic-poc commit) without needing a live API call, since the branching logic itself needed no LLM. Still waiting on real API credits to observe how it actually reads in a live 3-4-world conversation; the entry-point UI split (Deep Interview vs. Compare Worlds) itself remains unbuilt and unblocked by this.

---

## 2026-07-16 — Handoff parked from the Representative Modes thread: exploration branch ready, merge decision belongs here

**What this is:** the Representative Modes thread (see
`CiC_Representative_Modes_Decision_Log.md`) built and verified role-tailored
conversation — general / pastor-teacher / academic / deconstructing, rooted in this
log's own 2026-07-07 role-shaping entry — on branch
`claude/representative-modes-exploration` (off the pilot branch; running branches
untouched). Design spec with the Chloe four-mode demonstration artifact, prompt
architecture, validation plan, and integration assessment are in
`Ministry/Technology/Representative-Modes/`. No role selected = today's system
byte-for-byte.

**What this is not:** a build task now. Nothing merges before or during Prototype
Testing 1, and the role blocks have not yet been observed against a live model —
the validation plan's Battery A (content invariance) is the gate before any tester
sees a mode.

**Next action (this thread's, with the pilot schedule in view):** decide whether and
when the branch merges. If role modes should face testers in a later window: run
Battery A first, merge before invitations go out, never mid-pilot.

---
