# Church in Conversation — Program Build Specification

**Status: LIVING DRAFT — interview in progress.** This document is being built through a design interview with Mark. Sections marked `PROVISIONAL` are the designer's recommendation awaiting Mark's ruling; sections marked `RULED` record a decision made in this interview; sections marked `EVIDENCE` are established facts from the archaeology of the existing system and do not need re-deciding. Nothing from the existing system is binding; everything in it is evidence.

- Branch: `claude/cic-redesign-spec-fcjzz6`
- Started: 2026-08-20
- Basis: full archaeology of `base/interview-v2` (sealed current interview, `e8cf6e5`), `feat/table-multivoice-spec` (separate live workstream), `main` (stale), git history (454 commits across branches), L0–L4 governance corpus, Ministry decision logs, cost tooling and measurements.

---

## 0. What this document is

A build specification someone could execute: the outcomes the system exists to produce (stated testably), the module decomposition with each module's responsibility and interfaces, ownership and measurable definition of conversation quality, the data model and where source material lives, the cost model with arithmetic, safety and retention, the build order with verification gates, and an explicit list of what could not be resolved.

It is **not** a refactor plan for the existing program. The existing program is treated as a corpus of evidence: what Mark was reaching for, what mechanisms were tried, which failed, and why.

---

## 1. What the system exists to produce — PROVISIONAL

Drafted from evidence; each outcome will be sharpened into a testable statement as the interview resolves it.

**O1 — The encounter.** A participant has a real conversation with a representative voice of an early-Christian formation world. The voice is clear, modern, accessible English **and** scholarly rigorous, bound to its source documents. Both at once; the tension is the product. (Phase 1 failed exactly here — "horrible, too simplistic and hard to read.")

**O2 — The register, made testable.** Mark's own exemplar (2026-08-18, preserved verbatim in the table workstream) is the most precise statement of the bar that exists anywhere in the project:

1. The first sentence answers the question.
2. Concrete nouns carry the content.
3. One idea per sentence.
4. The English says the meaning first; the technical term is a label attached afterward.
5. It says what it does not know, plainly ("Our record does not go further back than that").
6. There are no aphorisms — nothing shaped to be quotable.
7. Brevity is a property of the register, not of a ceiling.

**O3 — Honesty about the record.** The voice never invents a source, saying, scene, or attribution. Honest thinness beats invented depth, absolutely, under every pressure. Sourcing reaches the participant through the interface (citations, glosses, records), never through a voice that lectures.

**O4 — Distinct worlds.** Worlds sound like themselves, not like one educated generic Christian voice with a historical accent. Uniformity manufactured by enforcement is a defect (the 54/54 compliance incident is the cautionary tale).

**O5 — Safety without a clinician on staff.** Acute distress is recognized and routed; a crisis number is delivered by code, never recalled by a model; dependency dynamics are watched; the encounter's own designed intensity is never misclassified as harm. Diligence bar: comparable-program standard, with the live adversarial-testing precedent the project already set for itself.

**O6 — Anonymity and retention.** Sign-in optional, never required. Transcripts kept for learning and for a bank of standard answers; participants are told this plainly and the promise of durability is actually kept (it silently wasn't, once).

**O7 — Cost.** Target and unit to be settled in this interview (see §6 — the "$0.30/participant-hour" figure does not exist in the repo in that form; the recorded band is $0.25–1.00/hr with unresolved pacing denominators).

**O8 — Participant types.** Four audiences (General/Seeker, Reassessing, Pastor/Teacher, Graduate-level). RULED (Q3): one voice register — General/Seeker — for all users through pilot and Phase 1; the type adapts only the frame around the voice (Facilitator posture, starter questions, apparatus depth). Voice-position selection is a possible later addition the architecture keeps cheap.

**O9 — Extension paths priced in, not built.** The multi-voice table (2–5 voices) is a separate product designed in another thread; this architecture must make it cheap to add. Same for "many worlds, not the current six."

---

## 2. Standing rulings — EVIDENCE

Mark's recorded decisions. Treated as defaults for this spec unless he overturns them here. Each carries its origin.

| # | Ruling | Origin |
|---|--------|--------|
| R1 | **Length is observed, never enforced.** Ceilings did four jobs; three were covered elsewhere; enforcement manufactured uniformity and broke streaming. Removed 2026-08-17; two reintroductions reverted. | `39e86e8` and the whole cap arc |
| R2 | **Mark's reading is the instrument** for register; formulas are assistants. FK scored a register failure as success twice in three days. No invented thresholds (Goodhart rule: "a variance target would produce performed variety"). | table workstream findings |
| R3 | **Prompt = how to speak. Records = what's true.** | Mark, 2026-08-20 |
| R4 | **Modern accessible English first, world flavor second** — "not crap fake ancient talk"; lexicon order switched: plain meaning leads, the world's word is introduced after ("the two ways before the water"). | Mark, 2026-08-17/18 |
| R5 | **The model switch lands last and alone** — after everything else is verified, so a post-switch failure is a one-line revert. (The Haiku flip violated this and was reverted in a day.) | `21e6842`, render.yaml |
| R6 | **Crisis number appended by code, never asked of a model.** Option C (named resource), driven partly by CA SB 243. | `3b4769e` |
| R7 | **Witness, not recruitment** (Art. 24); **doorway, not a home** (Art. 34: never optimize for return engagement, session duration, or dependency); **three-level transparency** (Art. 30); **no AI-only validation** (Art. 31). | L1 Constitution |
| R8 | **The only sanctioned fabrications are the Representative's name and role**, made to build connection; never entered into the world record. | FLAG-003 ruling |
| R9 | **One system, with mode explicit** — the table is rebuilt out of the interview, not beside it ("a table turn is an interview turn that can see a public transcript"). Two trees make divergence the default state. | 2026-08-18 review, Mark's reset |
| R10 | **Voices never know the participant's persona; the Facilitator holds it.** | table spec D8 |
| R11 | **Keep Sonnet-class generation for the voice** — $892/yr was "the wrong price" for halving grounded citations. Sonnet 5 pricing verified flat $2/$10, no cliff. | cost review 2026-08-16 |
| R12 | **Public-domain texts only are vendored**; in-copyright editions referenced by record, never redistributed. | texts registry |
| R13 | **Fail open toward the state that existed before the guard**, with a stated per-check asymmetry direction (fabrication errs toward flagging; over-settling toward clearing; frame-breaker toward answering). | runtime discipline |
| R14 | **Build for many worlds, not the current six** — anything that must be rewritten at thirty worlds is a finding, not a detail. | Mark, 2026-08-20 |

---

## 3. What the archaeology established — EVIDENCE

Condensed. Full agent reports live in the session record; this section is what the design must answer to.

### 3.1 Measured facts (first-party Anthropic API; all to be re-measured on Bedrock)

- **$0.03103/turn measured** (48 live turns, 2026-08-16), = $0.372/hour at the *assumed* 12 turns/hour. Pacing is the largest unmeasured input: plausible real figures span $0.25–0.91/hour. "$/turn is what the architecture controls; $/hour is $/turn times how fast people talk."
- **Generation is 43.8% of spend; the monitoring/governance apparatus is 56.2%.** 13–15 Haiku calls per turn. The over-settling cluster alone (screen + adjudication + the drift call that gates it) is 29.2%.
- **Prompt caching works and pools 16×**: 61% of input tokens are cache reads; static prefix ~17.8k tokens/world, 79% of input is cacheable. Killing pooling entirely costs only +10%. The earlier "cache broken / 2.3× over" scare was a **calculator double-counting bug**, not a runtime failure.
- **Output is ~7–10% of generation cost. "Shorter answers" was never the cost lever; input is.** 89% of a turn's cost is fixed.
- **$0.30/hour is reachable ($0.223) only by deleting fabrication, over-settling, and acute-distress detection simultaneously** — under the current architecture. Mechanism-free trims land at ~$0.36.
- **The over-settling adjudicator is structurally noisy**: 30% verdict flips on frozen bytes at temperature 0; the screen fires on 82% of turns (past its own 60% break-even). Its blindness-based two-stage design was measured and its folding rejected on evidence.
- **The single-signal bottleneck fails**: a monitor carrying 11 signals with one finding slot never once reported OVER_PRODUCING across 45 turns on an arm that clearly exhibited it. Extraction into its own screen is the only pattern that made a quiet signal fire.
- **Solo turns are memoryless by design** ([system, question], no history) — that is why caching works so well and why a 12-turn interview is 12 independent answers. Conversational memory changes the economics. (The current tree later added history; the cost review flagged the economics consequence.)
- Answer bank: **serves 0% of traffic today** (no data dir, no build script in the shipping tree, no UI producing curriculum refs); honest ceiling estimate ~5.2% (range 4–16%).
- Readability instruments: FK/FRE (sentence architecture) + a top-5000 word-list vocabulary proxy (word choice) + a "wall words" check (out-of-list AND world-specific AND unglossed). They disagree, and **the disagreement is the finding** — short sentences of unfamiliar words score well on one and badly on the other; "fake-old" has a signature (FK improves while vocabulary worsens). Dale–Chall proper is computed but never thresholded. `_MIN_SCOREABLE_WORDS = 15` blind spot confirmed at `cic/engine/gates.py`: segments under 15 words return unscored and read as clean; six desert entries were rewritten that the scan never flagged. "Short is not the same as plain."

### 3.2 The failure catalog (what a clean sheet must design out, not patch)

1. **One endpoint, two products, no gate on the second.** `/api/session/start` branched on `world_id` vs `world_ids` for months; the table half had no test. Sealed only on 2026-08-17. Lesson: a product boundary must be a *contract at the entrance*, with a test that fails on a second writer.
2. **Enforcement of a proxy quantity manufactured uniformity** (54/54 length compliance, every world sounding alike), reintroduced twice, reverted twice. And the retry corrective *panicked* (told 200 words, returned 88) and traded readability for brevity.
3. **Monitoring outgrew generation** and mostly can't change the turn the participant already read — post-turn governance only queues guidance for later turns, by design.
4. **Generated views drifted silently** — 70 stale files across all six worlds; the guard existed, pointed at the wrong tree, and was red on every run ("a permanently red job that everyone learns to scroll past"). The surviving fix: regenerate-and-git-diff, explicit builder list, no per-builder `--check` modes. Still missing: any check that the *runtime* serves the deploy tree it was built from.
5. **Hand-synced registries drift** (five world registries; a signal whitelist silently relabeling detections as "smoothing"; six copied freeze batteries whose rubrics diverged). The one pattern that worked: a single source of truth everything else derives from.
6. **Gates that pass while inert**: worlds with zero quote records pass the quotation gate vacuously; 5 of 12 grounding cells inert with everything green; "a gate that never fails is checking nothing."
7. **Persona collected, never used.** Two separate "who is asking" notions (`persona`, `participant_role`), neither reaching the conversation; the lane-ceiling consumer reads a field that doesn't exist.
8. **State is process-local with a write-only Supabase mirror** — nothing survives horizontal scaling: second instance = 404s on live sessions, doubled rate limits, degraded cache pooling. The codebase names this boundary about itself.
9. **LangGraph is vestigial** — the compiled graph walks two nodes at session start; the whole live loop is a hand-written `while True`. The framework does the work of one function call.
10. **Instrumentation that lies quietly**: streaming never populates the raw usage block (the cost double-count was invisible); a 0% fire rate can't distinguish "never fires" from "wasn't deployed yet"; a stale comment claiming a gap is covered is how the gap survives.

### 3.3 What demonstrably worked (candidate carry-forwards, not obligations)

- **Records as single source of truth, everything derived** ("the migration IS the authoring"); the per-world part of a prompt as a *record*, not code — adding a world = adding rows, no new code.
- **The record schema's honesty machinery**: three-axis confidence, `divergence_note` forcing gaps to be named, absent-stories as verified limits, false-friend vocabulary category ("'knowledge' for gnosis is worse than the Greek — the Greek at least announces that something needs explaining").
- **Cache-conscious prompt assembly**: segments ordered by change frequency; one unconditional static prefix per world; conditional blocks get their own breakpoint.
- **Pre-turn routing (withholding, not instructing)**: prompt text proven unable to hold safety/frame lines; the fix that held was never showing the message to the voice.
- **Deterministic wherever possible**: crisis number appended by code; gloss/figure detection without LLM calls; regenerate-and-diff staleness checks; grounding offers from positive evidence with zero LLM calls.
- **Blind, held-out, fresh-context validation batteries** with sealed keys; "the 9/9 was worthless — the lexicon was written after reading those probes."
- **The two-instrument readability finding** and the two-move split (plain answer ≤FK10, sourced grounding ≤FK14) — with the recorded conclusion that the too-simple direction is a *content* question no formula can see.
- **Event-sourced session state** (append-only log, projection per request) — killed a real race structurally.

### 3.4 Known tensions the interview must resolve

- Four participant types (O8) vs. R10 ("a witness testifies the same regardless of audience").
- $0.25–1.00/hr band vs. unresolved pacing denominator (6 vs 12 vs 30 turns/hr) vs. per-conversation framing.
- Live per-turn quality policing vs. build-time quality + offline audit (Q1, active).
- Six-world bespoke depth vs. "build for many worlds" scalability.
- Memoryless turns (cheap, cacheable) vs. conversational continuity ("Recall What They Have Given You" was unexecutable without history).

---

## 4. The interview

### 4.1 Resolved — RULED

**Q1 — Where does conversation quality live? RULED 2026-08-20: quality is proved before a world opens its doors, then checked afterward by reading real transcripts.**

Consequences for the design:
- There is no per-turn quality-police layer at runtime. The live turn keeps only what must act in the moment: safety routing, the code-appended crisis number, and cheap deterministic checks (citation/quote/figure grounding against the deployed indexes).
- Quality is owned by two modules instead: the **world build system** (records, prompts, demonstrations, blind held-out validation batteries — a world that hasn't passed them doesn't open) and an **offline transcript audit** (every transcript reviewed after the fact, at batch rates, against the full instrument suite, feeding fixes back into the world build — never into a live patch).
- The recurring cost floor becomes generation + safety, ≈ $0.017/turn on measured figures (vs $0.031 with the live police).

**Q2 — Budget unit and number. RULED 2026-08-20: cost exists in service of access.** Mark's words: "the lower the actual cost the more people can have access, and access is a primary objective... access without compromising quality and rigor." No hard target number; the design obligation is to drive cost down wherever quality and rigor are not the price. Derived requirements:
- **The engineering unit is $/turn** (what the architecture controls); no design decision is justified by a $/hour figure.
- **The reporting unit is $/participant-hour at one declared pacing convention — 12 turns/hour — stated wherever the figure appears.** This is the fundraising number ("if this is the hour cost, then X participants cost Y") and ends the 6-vs-12-vs-30 denominator confusion; when the conversions happen doesn't matter to Mark.
- **Per-participant cost monitoring is a first-class requirement**, not an afterthought: every LLM call attributable to a session, every session to a (anonymous) participant. (Today background calls log `request_id=None, session_id=None` — that class of gap is designed out.)

**Q6 — Fabrication posture. RULED 2026-08-20: the offline catch is acceptable — "the build protection is what matters."** Confirms Q1 under the project's own cardinal sin. Consequences:
- Mechanical grounding checks stay live and deterministic: quoted text against the world's licensed quote index, citations against the turn's actual text, named figures against attested dates.
- LLM-judgment fabrication detection (invented scenes, unattributed borrowings) lives in the offline transcript review. A found fabrication is handled as: a world-build fix (records/prompt/demonstrations), plus the transcript record of exactly which participants saw it.
- The build carries the primary anti-fabrication burden and must be specified to bear it: records-bound prompting, the quote index shipped complete (including do-not-voice entries so a forbidden quote is recognizable), post-history guards, and validation batteries that include fabrication pressure with held-out probes.

**Q3 — Participant types. RULED 2026-08-20: the voice never changes; the frame does — and there is exactly ONE voice register in this design: General/Seeker, for all users, through pilot and Phase 1.** A selection to change the voice position may be added later; it is out of scope here but must stay cheap to add. Consequences:
- The register bar (§1 O2) is calibrated to General/Seeker and is *the* voice, not one lane of several. No per-type prompt variants; one static prompt per world (which is also the cache-correct shape).
- Participant type is still collected (optional) and does two jobs: feedback correlation, and **frame selection** — the Facilitator's introduction and translation posture, the offered starter questions, and how much scholarly apparatus the interface surfaces up front (a Graduate sees the source registry and confidence axes immediately; a Seeker sees plain glosses and can drill down; everyone can reach everything).
- Future voice-position selection is priced in architecturally: register is a build-time parameter of prompt assembly (a different derived prompt from the same records), never a runtime branch inside one prompt.

**Q4 — Conversational memory. RULED 2026-08-20: the voice remembers the whole session — and memory must stop the repeating of stories, quotes, and lexicon.** Consequences:
- Full-session history reaches the voice every turn, laid out cache-consciously (append-only segment; the static world prompt stays byte-identical).
- **Non-repetition is a requirement, served twice**: deterministically at retrieval (a story/lexicon/quote chunk surfaced once in a session is excluded from re-retrieval — the mechanism that already worked) and behaviorally in the voice (the same-story-twice rule is finally executable because the voice can see it already told it).
- Non-repetition is a *transcript-audit check*, not a live gate (per Q1): the offline review measures repeated stories/quotes/terms per session, with the participant explicitly asking to hear it again as the sanctioned exception.
- The invented-callback fabrication class ("when I said X" for a thing never said) is closed structurally by real history, and the audit watches for it.

**Q7 — Worlds at launch. RULED 2026-08-20: worlds open as they pass the bar — and the system is built for over 100 eventual worlds, loading only the ones in use in a conversation; the rest wait in a database.** Consequences:
- The admission bar is defined once (§5 M3); each world opens when it clears it. No fixed N-world launch date.
- **World capacity is a data problem, never a code problem**: adding a world = adding records. No world identifier may appear in code, config constants, or hand-synced registries; everything about a world derives from one registry that is itself data.
- **Runtime loads worlds lazily, per conversation**: a session seats a world → its compiled artifacts (prompt, capsule, indexes) load on demand and are released when idle. Nothing warms all worlds at startup (the current system's warm-everything design OOM'd at six worlds on a 512MB box; at 100+ it is disqualifying).
- The world-selection surface must degrade gracefully past a menu of six (curation, search, pathways — participant-surface design, Q5).
- Per-world validation must be machine-runnable at fleet scale: "at six worlds a human can hold that in their head; at six hundred the failure mode is a world that passes every gate with half its safety net inert, and nobody notices" — so gates must fail on inertness, not just on violations.

**Q8 — Answer bank. RULED 2026-08-20: keep the goal, drop the mechanism for Phase 1.** The "bank" is the audited transcript corpus: the audit (M7) surfaces recurring question clusters; vetted standard answers flow back into world builds (demonstrations, reviewed starter questions) — under the question-led canon, exactly where they belong. A runtime serving path re-enters the spec only if measured recurrence justifies it; nothing gets built on guessed demand again.

**Q9 — Transcripts. RULED 2026-08-20: keep them all, anonymous, with the deletion code.** Every transcript kept indefinitely, keyed to an anonymous session; the audit pass strips personal identifiers from free text before anything enters the shared learning corpus; the participant is told plainly at the start what is kept and why, and shown a session code at the end that lets them request deletion — control without an account. Optional sign-in buys only the participant's own continuity across visits.

*Reuse economics, settled in the same exchange:* drawing on already-generated answers is exact-tap only (never fuzzy-matched against free text — a stored answer to a slightly different question answers a question the participant didn't ask); full-session memory (Q4) limits reuse to conversation-opening/standalone answers; and post-Q1 the cost win is small (generation ≈ $0.014 of a ≈ $0.017 turn). The real value of the future bank is **consistency and reviewability** — the most-asked questions get vetted answers, identical every time — and retention is what makes it possible.

**Q10 — Safety. RULED 2026-08-20: carry the existing design as-is, with the two debts as explicit gates before public availability.** Two tracks (acute distress acts on the single message; harmful-dynamic/dependency accumulates across the session), withholding-not-instructing, the encounter-working-as-designed distinction (historical-otherness disorientation is never counted as harm; engagement length/depth never increments the accumulator), crisis resources appended by code (R6). Gates: live adversarial trials to the project's own ten-of-ten precedent, and the clinician read — informed pilot testers may precede them per Article 36; the public may not.

**Q5a — Session continuity. RULED 2026-08-20: conversations are resumable by session code.** One code per session, shown plainly, doing double duty: resume on any device, and request deletion (Q9). Sign-in stays the optional convenience tier. Article 34 compliance note: continuity honors the participant's wish to finish; nothing may *prompt* them to return.

**Q12 — Mark's role per world. RULED 2026-08-20: the four touchpoints — world/Representative identity, the living-tradition determination, the freeze, the admission read — plus one operational role: source acquisition.** Build environments cannot reach the text archives (CCEL, Archive.org, etc. are egress-blocked); Mark downloads what a build needs. Formalized so it scales: step 2 of every world build emits a **source request manifest** — exact texts, editions, URLs, expected rights status — Mark fetches and drops the files in; the texts registry then verifies rights from each file's own provenance header (never trusting the request), exactly as the existing corpus discipline does. Public-domain-only vendoring (R12) unchanged.

**Q13 — First world. RULED 2026-08-20: Alexandria.** Richest lexicon and the most substantive theological material — it exercises every canon family with real answers, stressing the pipeline exactly where the old process failed (foundations). Desert is the recommended second world, chosen to prove the opposite case: the honest-limit machinery on the project's own recorded worst-case foundations material.

**Q14 — The Facilitator. RULED 2026-08-20: kept, visible at door, thresholds, and close — and it is the single fleet-wide owner of safety, modern-term translation, and out-of-scope handling, so none of that is ever replicated in any world.**

The design, in full:

- **One gate, before every voice turn.** Every participant message passes through the Facilitator's gate — a small set of cheap, world-agnostic classifiers — which decides one of three things: *pass through* (the ordinary case; the voice answers); *Facilitator handles alone* (safety, "are you an AI?", questions about the system itself, questions about other traditions or later ages the world cannot see); or *frame, then hand inward* (the modern-term pattern: the Facilitator speaks the modern sense plainly, and the voice receives the term-free underlying subject — the participant's modern word never reaches it).
- **Safety lives here once (Q10).** The two-track mechanism, the accumulator, the code-appended crisis line — one implementation, every world, exactly as the record ruled ("the fix belongs at the Facilitator layer, once, for every world, never inside a Representative's prompt"). Mark's standing routing nuance carries: the voice may still offer its world's empathy and wisdom, but safety is governed by the Facilitator.
- **Translation lives here once.** The modern-term dictionary is Facilitator-owned, world-agnostic data; whether a term is anachronistic is *computed* per world from its time window, never authored per world.
- **The out-of-scope line — the one refinement.** Out-of-scope routing is for questions about the *system*, *later ages*, or *other traditions* — things no amount of source material could let the voice answer in character. It is **not** for questions the world's sources answer thinly: those reach the voice, and the honest-limit answer ("our record does not say") is the voice's own, in-world — that honesty is part of the testimony, not a system apology. The gate's known failure mode is over-firing (a question a world *could* answer, intercepted); every classifier fails open toward the voice answering.
- **First ask goes to the voice; the Facilitator steps in only when the participant presses (Mark's amendment, 2026-08-20).** An out-of-scope question's *first* occurrence is answered by the Representative from inside its world — in-character, honestly bounded ("I know nothing of such things" is a real fourth-century answer). Only when the participant presses the point does the Facilitator intervene with the plain etic explanation. This matches the record: total embeddedness means the first ask often doesn't even parse as a system question from inside the world, and prompt text was proven unable to hold the line only under *sustained* pressure — which is exactly where the Facilitator now takes over. **Exception: safety always intervenes immediately, on the first signal — no press-to-escalate ladder applies there.** The modern-term bridge also stays first-occurrence (it is framing that helps the answer land, not an interception).
- **Disciplines:** the Facilitator meets the same readability bar as every Representative and is measured by the same batteries (it was once the least readable voice on screen because none measured it); its threshold appearances are visible turns, never silent edits of the conversation.

**Q15 — Register statements. RULED 2026-08-20: the seven statements are the register's center of gravity, measured across transcripts — never per-turn laws.** The question may override any of them (the desert word, the story that is the answer); the audit reads tendencies, and drift from the center is a world-build conversation, not a gate. Statement 6's target is clarified: *manufactured* profundity is banned; a tradition's own licensed sayings are quotes — sourced, clickable, and welcome. Statement 1 is amended by Q16 below.

**Q16 — The question-reader. RULED 2026-08-20 (design confirmed; unified-gate shape ruled in the same exchange):**

The recorded failure this addresses (raised by Mark while exploring the register statements): when the question is unclear or two questions are asked, "the first sentence answers the question" breaks — on compound questions the last clause consumed the answer in all six worlds, and prompt instructions alone never fixed it (six edits, four runs, no movement).

**Recommendation — a silent question-reading step in the Facilitator's gate, with three rules:**
1. **The gate reads every message and names its asks** — one ask, two asks, a compound, or genuinely unclear — and hands the voice a **private directive** ("two questions: how one joined, and what it demanded; answer in that order"). One small, cheap call; it qualifies under Q1's own test because it changes *this* turn before the participant reads it, never a later one.
2. **The participant's words are never rewritten.** The voice still sees exactly what the participant typed — authorship preserved, and the answer must still visibly respond to *their* phrasing. The directive names the asks; it does not replace the message.
3. **Genuine ambiguity gets a clarifying question — from the voice, in-world.** "Do you mean how we worshiped, or whether we were made to?" is what a real conversation partner does, and a fourth-century person can ask it in character. The Facilitator clarifies visibly only when the ambiguity is system-level or modern-framed (its existing threshold role).

Register statement 1 amends to: *the first sentence answers the first ask — and every ask gets answered.* The audit measures ask-coverage per turn (did each named ask receive an answer) — a mechanical check, not a judgment call.

**Is it one review? Yes conceptually, two calls mechanically (RULED with Q16).** The Facilitator's gate is a single pass over each message, but inside it:
- **The safety classifier stays its own sealed call.** Its fail-toward-safe asymmetry, its adversarial validation bar, and the standing rule that any change to it triggers the full live safety rerun (19/20 floor) mean it must never share a prompt with machinery that gets iterated on. A shared prompt is a shared failure.
- **Everything else unifies into one structured call**: asks named, out-of-scope detection *with press-state* (has the participant pushed this before — the session's event log supplies it), modern-term hits, frame questions. Structured output with **every field always filled** — this is what dodges the recorded single-slot failure (a monitor asked for "the one finding" went silent on real defects; a form with a box per dimension cannot lose a finding to a competing one). Each field carries its own fail-open direction.
- The two calls run concurrently: latency of one, cost ≈ $0.002/turn total.

### 4.3 Question queue (order will adapt to answers)
- Q5 (remainder) — participant surface details are drafted as provisional recommendations in §5B; Mark redlines rather than being interviewed item by item.
- Q11 — Bedrock is drafted into §6.1 from the evidence; the only open item is executing the preflight once the AWS account is live.

---

## 5. Module decomposition — PROVISIONAL (first full draft after Q1–Q4, Q6, Q7)

Eight modules. Each owns one thing; interfaces are named so a violation is visible. Detailed interface contracts and the build order follow as the remaining questions resolve.

**M1 — World Store.** *Owns: what's true.* The database of worlds (built for 100+): records as the single source of truth — sources, terms, stories, quotes, gravities, forces, figures, contested claims, demonstrations, voice craft, world core — with the three-axis confidence block, typed relations, and rights/licensing per record. Validation is schema + gates, with the gate-integrity rule (changing a gate is its own reviewed step) and the inertness rule (a gate with nothing to check against reports that loudly). Interface out: validated record-sets per world, plus one world registry that everything else derives from.

**M2 — World Compiler.** *Owns: derivation.* Deterministic builders: records → deployed artifacts (permanent prompt, capsule, retrieval chunks + indexes, quote index, figure registry, browsable repository, facilitator frame data). Same records → byte-identical outputs; regenerate-and-diff is the staleness gate; the builder list is explicit; every artifact set carries a manifest hash **that the runtime verifies at load** (closing the one gap the 70-file drift left open). Register variants (future voice positions, Q3) and table-mode artifacts (O9) are additional compile targets from the same records — never runtime branches.

**M3 — Admission.** *Owns: the door (Q1, Q7).* The per-world validation battery: fresh-context, held-out, blind-graded probes covering register (O2), source-boundedness/fabrication pressure (Q6), distinctness (O4), safety interplay, and refusal honesty — machine-runnable at fleet scale, human-ruled where the instrument is Mark's reading (R2). A world opens when it passes; it re-enters admission when its records materially change.

**M4 — Conversation Runtime.** *Owns: the live turn, and nothing else.* Session state as an append-only event log over a durable shared store (survives restarts and horizontal scaling — the process-local boundary is designed out). Turn loop: safety routing (M5) → retrieval (session-exclusion enforced, Q4) → one generation call with full-session memory, cache-conscious layout → deterministic grounding checks → stream. Worlds load lazily per conversation (Q7). No LLM quality police (Q1). Mode (interview / future table) is an explicit field, a contract at the entrance with a test that fails on a second writer.

**M5 — Facilitator & Safety.** *Owns: everything no world should own (Q14).* The one voice belonging to no world, visible at door, thresholds, and close; the pre-turn gate (pass through / handle alone / frame-then-hand-inward); safety implemented once fleet-wide (acute distress / harmful dynamic, withholding-not-instructing, crisis resources appended by code, R6); the world-agnostic modern-term dictionary; out-of-scope handling for system/later-age/other-tradition questions (never for in-world thinness — honest limits are the voice's own). Per-check fail-open directions stated in the spec; every classifier fails open toward the voice answering. Specified separately from M4 so its diligence bar (live adversarial trials, the 19/20-floor regression discipline, the owed clinician conversation) is auditable on its own.

**M6 — Participant Surface.** *Owns: the encounter's frame.* World selection that scales past a menu (Q7); the participant-type frame (Q3): Facilitator posture, starter questions, apparatus depth; three-level transparency (citations → glosses → full records with sources); the honesty chrome (disclaimers, session persistence truth); transcript copy. Anonymity: sign-in optional, never required (O6).

**M7 — Transcript Store & Audit.** *Owns: quality after the door (Q1, Q6).* Durable transcripts under the retention/anonymity rules (Q9, open); the offline audit pipeline running the full instrument suite at batch rates over every transcript — register instruments (the two-instrument disagreement is a feature), fabrication detection, repetition (Q4), safety review, world-distinctness drift; findings route to world-build fixes (M1) and admission re-runs (M3), never to live patches. Also the learning corpus and any future standard-answer bank (Q8, open).

**M8 — Cost & Observability.** *Owns: the truthful number (Q2).* Usage logging with correct cache accounting (the double-count class is designed out with tests against raw API shapes), every call attributed to session and participant, $/turn as the engineering unit, the declared 12-turns/hour reporting convention, and Bedrock/first-party parity checks (Q11, open).

**Boundary rules that are themselves spec:** one world registry, everything derived (no hand-synced lists); one product per endpoint contract; shared logic extracted, never duplicated ("the fix is not a fourth copy"); every guard fails open toward the pre-guard state with a stated direction; every generated artifact verifiable against its source by regenerate-and-diff plus load-time manifest hash.

---

## 5A. The World Build Process — standalone, plug-and-play — PROVISIONAL

**Requirement (Mark, 2026-08-20):** a standalone Christian tradition/world build process that gets the information in an organized, efficient way and plugs into the conversation system without impacting it — "a step by step process that builds, organizes and delivers every required aspect needed to deliver the ultimate program deliverables."

### 5A.1 The contract

The unit of delivery is the **World Package**: everything the conversation system will ever need from a world, in one validated bundle. The system promises to need *nothing* about a world beyond its package (no code, no config edits, no prompt surgery); the package promises to arrive complete, validated, and admission-tested. Installing a world = placing its package in the World Store (M1); it becomes selectable the moment it passes Admission (M3). Building a world can never break a live world or the system.

### 5A.2 What a World Package contains

1. **The record set** — the world's whole truth, typed: world core (time window, horizon, formation logic) · sources (with rights, verification, provenance) · lexicon terms (plain meaning first, world word second, per R4; false-friend flags) · stories (tiered, with absent-stories: what this world cannot honestly tell) · licensed quotes (including do-not-voice) · figures (with narratability) · gravities, forces, contested claims (what the world holds under challenge, and what it concedes) · voice craft (how this world speaks — the per-world half of the prompt, as data per R3) · demonstrations (worked example exchanges, including foundational questions — the gap that held go-live once).
2. **Coverage floors, per record type** — so no gate can sit inert (the six-worlds lesson: a world with zero quote records passes the quote gate vacuously). A package below floor is incomplete, not "thin but passing."
3. **Compiled artifacts** (produced by M2 from the records, deterministic): permanent prompt, capsule, retrieval chunks + indexes, quote index, figure registry, repository views, facilitator frame data — with the manifest hash.
4. **The validation record**: gate results, admission battery results (blind, held-out, fresh-context), and the human checkpoint sign-offs.

### 5A.3 The build process — PROVISIONAL REDESIGN (question-led, not analysis-led)

**Mark, 2026-08-20: not locked into the nine-step arc — the bar is "depth of a living ecology and transparent sourcing, able to handle general what-was-life-like and serious theological and doctrinal questions as the source material can answer."**

The old arc was organized by analytical category (identify → sources → gravities → forces → lexicon → stories → voice), and its recorded failure is demand-blindness: worlds with deep ecology analysis answered "who was Jesus?" with displaced calling stories; across 52 demonstrations the cross appeared three times obliquely and the resurrection not once; only 34% of authored figures were ever named in live traffic; quotes were policed but never offered. Supply was built without a map of demand. The redesign bookends the ecology work with demand on both sides:

**Step 0 (once, fleet-wide) — the Question Canon.** The versioned corpus of what participants actually ask. Seeded by Mark, vetted by scholarly review, grown permanently from real transcripts (M7 feeds it). The canon is the definition of "complete" for every world — and the source of admission probes (held-out paraphrases).

**The canon is centered, not flat (RULED 2026-08-20).** Mark: "Our heart is to reveal Jesus, so that would be a centric question." No audience's questions outrank another's — the structure isn't a ranking of families but a center with families around it: at the center sit the questions of Jesus himself — who he was, the cross, the resurrection, what it meant to those who followed him — and every family is partly defined by how its questions lead toward or radiate from that center (daily life as it was lived *because of him*; belonging as the way people *came to him*; pain as the place he is *most needed and hardest to see*). Center coverage is the first thing admission tests — the recorded go-live failure (the cross oblique three times, the resurrection never) is the exact defect this geometry exists to prevent. Guardrail carried from the Constitution: revealing is witness, never recruitment (R7) — each world testifies of Christ *from its own sources only* (no shared center record), and the participant's interpretation remains their own.

*Category families: UNDER RESEARCH (2026-08-20) — two tracks running (internal evidence mining; external frameworks: catechetical structures, seeker courses, church-history pedagogy, deconstruction literature, social history of daily life). Candidate schemes to be presented for Mark's ruling; the four-family sketch (life-world / formation / foundations / pressure) is superseded as a candidate, not a decision.*

**Per world:**
1. **Identify & bound** — scope, time window, what the world is *not*; distinctness against built worlds.
2. **Source ecology** — the approved source base with editions, rights, verification; the search record including searches that returned nothing. Emits the **source request manifest** for Mark (Q12): exact texts, editions, URLs, expected rights; rights are verified from each supplied file's own provenance header, never from the request.
3. **Ecology reconstruction** — gravities, forces, contested claims, figures: the world's interior coherence, *the living-ecology depth*. Proportionate to the source base — the canon coverage is the fixed bar; ecology depth is the means, not a quota.
4. **Answer the canon from the sources.** For every canon domain the world produces either substantive records (terms plain-first, tiered stories, licensed quotes, figures, doctrinal-witness records keyed to the foundations family) or an **honest-limit record**: "our sources do not answer this," as data, in-world. No silent holes — "as the source material can answer" becomes a recorded, per-world fact the participant can see.
5. **Voice** — craft record and demonstrations authored *against canon questions* (foundational ones included by construction, not discovered missing at go-live), to the General/Seeker bar.
6. **Compile & gate** — deterministic build; gates include **canon coverage** (every domain: substantive or honest-limit, never blank) alongside referential/rights/readability.
7. **Admission** — blind battery drawn from held-out canon paraphrases; Mark's read where his reading is the instrument.
8. **Open** — registry flips live; changes re-enter at step 6.

**Human checkpoints (Mark's, RULED Q12):** world identity/Representative identity; the living-tradition determination; the freeze; the admission read — plus the operational source-acquisition role (fetching archive texts the build environment cannot reach, against each build's source request manifest). Everything else is executable by AI threads or scripts against this spec.

*Note (prior ruling preserved): Mark rejected a shared theological "center record" — a Representative may never speak outside its own sources. The foundations family is answered per-world, from that world's records only; the canon shares the questions, never the answers.*

**RULED 2026-08-20: the question-led spine is confirmed — with this guardrail: the canon organizes coverage, it does not replace the content.** Mark's words: "we still want the 3 tier transparency, with lexicon (world specific words), stories, quotes and general reference tracking, not just answers." Binding consequences:
- Answering the canon is done **through the record types** — lexicon terms (world-specific words, plain-first), tiered stories, licensed quotes, figures, doctrinal-witness records — never as prose answer blobs keyed to questions. A canon domain is "covered" when the records that serve it exist, are sourced, and reach the voice.
- **Three-tier transparency is per-turn and universal** (Art. 30): every answer, whatever canon family it serves, carries tier 1 (inline citation marks / glossed terms) → tier 2 (plain-language gloss and source summary) → tier 3 (the full record with its sources, editions, confidence axes). A theological answer is as clickable as a daily-life answer.
- **General reference tracking** is fleet infrastructure: every claim traceable to a source record; the source registry, quote index, and figure registry are the per-turn tracking surfaces; the vendored public-domain text corpus is what verification stands on.

### 5A.4 Efficiency requirement — OPEN (see active question)

At 100+ worlds the current bespoke pace (months per world, hand-tailored batteries, per-world code) is disqualifying. The process must state its own cost per world and drive it down the same way the runtime does: shared instruments, record-native authoring, batch validation.

---

## 5B. Conversation quality — who owns it, and how it is defined measurably

**Ownership (Q1):** the Admission module (M3) owns quality before a world opens; the Transcript Audit (M7) owns it after. The runtime owns none of it. A quality problem is always fixed in the world build, never patched live.

**The definition.** A world's conversation is good when, measured over its admission battery and then over its real transcripts:

1. **Register (O2, the Mark exemplar, operationalized — center of gravity per Q15, never per-turn law):** first sentence answers the first ask, every ask answered (Q16's mechanical ask-coverage check); plain-before-term order (R4 lexicon-order instrument); the two-move readability split (plain answer ≤ FK 10 / FRE ≥ 60; sourced grounding ≤ FK 14 / FRE ≥ 40) **plus** the vocabulary instruments (word-list reach, unglossed wall-words) — the *disagreement* between sentence-architecture and word-choice instruments is itself a tracked signal (the "fake-old" signature). All measured as transcript tendencies; the question may override any statement on any turn. Segments under the scoreable floor are reported as unscored, never as clean.
2. **Groundedness (O3, Q6):** zero unmatched quoted-attributed spans against the quote index; citations shown only when the turn's text carries them; figures within attested dates; honest-limit answers delivered as honest limits, in voice.
3. **Coverage (canon):** every canon domain answerable — substantively or as a recorded honest limit — before the door opens; measured again on real traffic (which questions actually arrived, what served them, what fell through).
4. **Distinctness (O4):** cross-world probes — same question to every open world — must converge on accessibility and diverge on content (near-zero phrase overlap between worlds; the measured instrument that already worked).
5. **Continuity (Q4):** no repeated story/quote/term within a session absent an explicit request; no invented callbacks; deepening across the session graded in the audit (human-read sample, not a formula).
6. **Integrity under pressure:** held positions stay held under bare pushback; thin ground concedes plainly; the two rates are never merged (which failure occurred matters).

**Threshold discipline (R2):** numeric bars are set once, from real baselines — never invented to fill a row; report-only instruments stay report-only until data earns them a bar; Mark's read is the instrument for register and identity, sampled, on schedule, not on demand.

---

## 5C. Participant surface — PROVISIONAL (Q5 remainder; Mark redlines)

- **Choosing a world at 100+ (Q7):** curated doorways instead of a menu — a small set of featured worlds, browse by era/place/question ("who can speak to suffering?"), and search. Every world's own thinness statement ("richest in… thinner on…") stays on its doorway; evidentiary honesty starts before the first message.
- **The frame by participant type (Q3):** the optional "what brings you here?" question selects Facilitator posture, starter questions, and default apparatus depth. Everyone can reach everything; the type changes the default, never the ceiling.
- **Starter questions** drawn from the Question Canon per world and frame — which also makes them the future exact-tap surface for vetted answers (Q8).
- **Three-tier transparency everywhere (Art. 30):** inline marks → hover gloss → full record with sources and confidence; one interaction grammar for citations, terms, and figures; drawn-on vs consulted never conflated (the badge number is a promise about the turn's text).
- **Honesty chrome:** what is kept and why (Q9), the session code (resume + deletion, Q5a), prototype status; one quiet status line, priority-ordered, never stacked.
- **Transcript copy** with speaker names and cited sources.
- **Feedback by interview, not form** (Mark's standing preference), correlated via the optional participant type.

---

## 6.1 Bedrock (Q11) — settled posture

The pilot bills through AWS Bedrock (credits through pilot 2). The spec's stance, from the evidence: keep the Messages-API client shape (the `ChatAnthropicBedrock`-style path — same cache_control, same usage fields — chosen precisely because the alternative zeroes cache accounting silently); refuse to guess model IDs (blank fails loudly; IDs carry region/provider prefixes); nothing is trusted until the preflight runs against the live account — (a) caching actually engages, (b) both usage shapes report cache fields, (c) $/token reconciled against the real AWS invoice, not the first-party price table. **Every cost figure in this spec is re-measured on Bedrock before it is quoted onward (M8 owns parity).** Budget controls: an AWS Budget *Action* (deny policy), not alerts alone; the per-tester session cap remains the primary control.

## 6. Cost model — baseline arithmetic

Per Q2: engineered in $/turn, reported in $/participant-hour at the declared 12 turns/hour convention, with per-participant cost attribution built in. The objective is access: lower is better wherever quality and rigor are not the price.

Established baseline (first-party API, to be re-measured on Bedrock):

```
main_response (Sonnet 5):     $0.01360/turn   43.8%   ← the floor
everything else (13–15 Haiku calls): $0.01743/turn   56.2%
                              --------
measured                      $0.03103/turn
× 12 turns/hr (assumed)     = $0.372/hr    (8/hr → $0.25; 20/hr → $0.62)
```

Cache: static prefix ~17.8k tok/world at 0.1× read; 1h TTL write 2×; pooling measured 16×; worst case (no pooling) +10%. Output ≈ 330 tok ≈ 7–10% of generation cost. If Q1 resolves toward build-time quality, the recurring floor approaches `main_response + safety (~$0.0030) + deterministic checks (~$0)` ≈ **$0.017/turn ≈ $0.20/hr at 12 turns/hr**, with offline audit priced separately at batch rates. Arithmetic to be completed once Q1/Q2/Q4 land.

## 7. Safety and retention — SETTLED (Q9, Q10)

**Safety (Q10):** the existing two-track design carries as-is — acute distress acts on the single message, harmful-dynamic/dependency accumulates across the session; the triggering message is withheld from the voice while safety has the floor (Mark's standing routing ruling: the Representative may still offer its world's empathy, but safety is governed by the Facilitator); crisis resources are appended by code (R6); historical-otherness disorientation is never harm; engagement length/depth/turn count never increment the accumulator. Regression discipline carries: any change touching prompts or routing triggers the full live safety script rerun, 19/20 floor, any new failure halts. **Gates before public availability:** live adversarial trials to the ten-of-ten precedent, and the clinician read. Informed pilot testers may precede both (Article 36: deferrals documented, never hidden; no deferral reduces the standard).

**Retention (Q9):** every transcript kept indefinitely, keyed to an anonymous session; personal identifiers stripped from free text before anything enters the shared learning corpus; the participant is told at the start what is kept and why, and receives a session code granting later deletion (and, per Q5a, resumption) without an account. Sign-in is optional forever and buys only the participant's own cross-visit continuity. The transcript corpus feeds the audit (M7), the Question Canon, and the future vetted-answer bank (Q8).

## 8. Build order — PROVISIONAL

Ordering principles: each stage is verified before its dependents start; risky substitutions land last and alone (R5); the first world proves the whole pipeline before any second world begins; nothing ships a guard it doesn't run.

1. **Record schema + world registry + gates (M1).** Verify: schema validates a seeded reference set; every gate passes the clean fixture and fails every seeded-defect fixture (selftest discipline); inertness reporting fires on a world with missing record types.
2. **Compiler (M2).** Verify: determinism (same records → byte-identical artifacts, twice); regenerate-and-diff CI green on the reference set; manifest hash produced and checked by a stub loader.
3. **Question Canon v1 (step 0).** Mark seeds the four families; scholarly-review vet. Verify: every canon domain has held-out paraphrase probes authored and sealed before any world answers it.
4. **Admission harness (M3).** Verify: blind protocol runs end-to-end on the reference world — fresh-context generation, masked grading files, sealed keys; a seeded register/groundedness defect is caught.
5. **Runtime core + safety (M4 + M5).** Verify: event log durable across restart and second instance (session resume by code works, twice, on different processes); mode contract test fails on a second writer; live safety script at the 19/20 floor; crisis append asserted including the empty-stream case; lazy world load/unload measured.
6. **Cost instrumentation (M8) — on Bedrock, first.** Verify: parity against raw API usage shapes; a deliberately lapsed cache window shows up in the numbers; per-session attribution complete (zero unattributed calls).
7. **First World Package end-to-end: Alexandria (Q13).** Through the full 5A process to open — chosen to stress the foundations family with substantive answers. This stage *is* the verification of the process itself; its admission read is Mark's. No second world starts until Alexandria's build cost and defect list are recorded. Recommended second: Desert, to prove the honest-limit machinery on thin material.
8. **Participant surface (M6).** Verify: three-tier transparency reachable from every citation/term/figure; type-frame defaults; honesty chrome; transcript copy; resume + deletion by code.
9. **Transcript audit (M7).** Verify: full instrument suite runs at batch rates over the pilot transcripts; findings route to record fixes; canon growth loop demonstrated (a new real question enters the canon).
10. **Open the doors** (pilot per Article 36; public waits on the two safety gates). Worlds continue opening as they pass (Q7).

The table product, voice-position variants, and any answer-serving bank are *not* stages — they are compile targets and modules this architecture must keep cheap (O9, Q3, Q8), added by their own future specs.

## 9. Unresolved — running list

*Settled since the list began:* the pacing denominator (Q2: declared 12 turns/hour reporting convention); the target's unit (Q2: access objective, $/turn engineering unit); the review-state ladder (subsumed: records advance through the build steps' exit checks, freeze at Mark's checkpoint — Q12).

Still open:
- **Reading-floor calibration** — the FK [8,10] band has never been checked against the exemplars the register actually aims at (BBC ≈ FK 6); to be settled by measurement during Alexandria's build, not by ruling.
- **The Question Canon v1 seeding** — Mark's seeding session for the four families hasn't happened; it is stage 3 of the build order and blocks admission-probe authoring.
- **Bedrock preflight** — blocked on the live AWS account; every cost figure herein is provisional until re-measured there (§6.1).
- **The clinician conversation and live adversarial safety trials** — owed, now formal public-availability gates (Q10); not scheduled.
- **The never-root-caused cross-contamination incident** (unrelated content in a live API response, 2026-07-20) — carried as an ops watch item; the per-request trace-id discipline that was built in response carries into M8.
