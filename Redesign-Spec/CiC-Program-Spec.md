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

**O8 — Participant types.** Four audiences (General/Seeker, Reassessing, Pastor/Teacher, Graduate-level). Whether and where the system adapts to them is an open interview question (Q-queue). Standing prior ruling in tension with it: "voices never know the persona; persona lives in the Facilitator — a witness testifies the same regardless of audience; only an advocate tailors."

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

### 4.2 Active question

**Q2 — What is the budget's unit and number: dollars per hour, or dollars per conversation?**

Three internal documents flag that the project's $/hour figures use pacing denominators that differ 4–5× (6 vs 12 vs 30 turns/hour) and were never reconciled; pacing — how long a person thinks and types — is the single largest unmeasured input. The repo's own observation: "a twelve-turn conversation costs the same at any pace, and this whole uncertainty disappears."

**Recommendation: budget per conversation, not per hour.** The architecture controls the cost of an answer; the participant controls the pace, and a contemplative participant shouldn't read as an expensive one. On the post-Q1 floor, a 20-turn conversation ≈ $0.35 all-in at today's prices.

### 4.3 Question queue (order will adapt to answers)
- Q3 — Participant types: do the four audiences change the *conversation*, and if so where (Facilitator translation layer per R10? depth of follow-up? never)?
- Q4 — Conversational memory: does the voice remember the conversation (deepening, callbacks) at the measured cache/cost price, or stay memoryless?
- Q5 — What must a participant be able to *do* besides talk (see sources, save transcript, resume a session, guided starters)?
- Q6 — Fabrication posture at runtime: is offline detection within hours acceptable, or must a fabricated citation be caught before/immediately after the participant sees it?
- Q7 — Worlds at launch: all six at redesign quality, or fewer worlds deeper first?
- Q8 — Answer bank: keep as designed (exact curriculum taps only), redesign, or drop?
- Q9 — Retention/anonymity mechanics: what exactly is kept, keyed how, told to the participant in what words.
- Q10 — Safety scope: carry the existing two-track design as-is, or re-derive; what "comparable programs" set the bar.
- Q11 — Bedrock: what the migration changes for this spec (all figures re-measured; caching behavior is the whole bet).

---

## 5. Module decomposition — TBD

*Q1 settled the biggest fork: no runtime governance module. Full drafting waits on Q2–Q4.*

Expected shape (subject to interview): world build system (records → derived views → validation batteries; owns quality per Q1) · conversation runtime (generation + safety + deterministic checks only) · offline transcript audit (owns post-launch quality per Q1) · participant surface · transcript/learning store · cost/observability. Interfaces, ownership, and build order to follow.

## 6. Cost model — baseline arithmetic, unit pending Q2

Established baseline (first-party API, to be re-measured on Bedrock):

```
main_response (Sonnet 5):     $0.01360/turn   43.8%   ← the floor
everything else (13–15 Haiku calls): $0.01743/turn   56.2%
                              --------
measured                      $0.03103/turn
× 12 turns/hr (assumed)     = $0.372/hr    (8/hr → $0.25; 20/hr → $0.62)
```

Cache: static prefix ~17.8k tok/world at 0.1× read; 1h TTL write 2×; pooling measured 16×; worst case (no pooling) +10%. Output ≈ 330 tok ≈ 7–10% of generation cost. If Q1 resolves toward build-time quality, the recurring floor approaches `main_response + safety (~$0.0030) + deterministic checks (~$0)` ≈ **$0.017/turn ≈ $0.20/hr at 12 turns/hr**, with offline audit priced separately at batch rates. Arithmetic to be completed once Q1/Q2/Q4 land.

## 7. Safety and retention — TBD (Q9, Q10)

Carries forward as evidence: the two-track design (acute distress / harmful dynamic), the fail-open direction rules, the SB 243-driven resource naming, the "encounter working as designed is not a system failure" distinction, the 19/20-floor live-script regression discipline, and the standing note that a clinician conversation is owed.

## 8. Build order — TBD

Will be stated as: what gets built, what evidence gate it must pass, and what may not start until it does. The archaeology's strongest ordering lesson is R5 generalized: risky substitutions land last and alone.

## 9. Unresolved — running list

- The pacing denominator (three internal documents flag it; never settled).
- The "$0.30/participant-hour" target's provenance (nearest repo figures: $0.25–1.00/hr band; $0.30–0.75 *per table conversation*).
- Whether the review-state ladder (832/832 records at `draft`) gets teeth: what advances a record, and who may.
- The reading-floor calibration question (BBC ≈ FK 6; the [8,10] band may be set too high — "corpus prose has been edited toward it").
- The one confirmed-real, never-root-caused cross-contamination incident (unrelated content in a live API response, 2026-07-20).
